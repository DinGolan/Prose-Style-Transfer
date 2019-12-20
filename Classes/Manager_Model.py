# Imports #
import os
import shutil

# Froms #
from keras.callbacks import EarlyStopping, ModelCheckpoint
from keras.callbacks import TensorBoard
from keras.layers import Bidirectional, Dense, Dropout, Input, LSTM
from keras.layers.embeddings import Embedding
from keras.layers.merge import concatenate
from keras.layers.normalization import BatchNormalization
from keras.models import Model


class SiameseBiLSTM(object):

    def __init__(self, Embedding_Dimension, Max_Sequence_Length_Without_Aug,
                 Max_Sequence_Length_With_Aug, Validation_Size, Number_LSTM_Units,
                 Rate_Drop_LSTM, Number_Dense_Units, Rate_Drop_Dense, Activation_Function):
        self.Embedding_Dimension = Embedding_Dimension
        self.Max_Sequence_Length_Without_Aug = Max_Sequence_Length_Without_Aug
        self.Max_Sequence_Length_With_Aug = Max_Sequence_Length_With_Aug
        self.Validation_Size = Validation_Size
        self.Number_LSTM_Units = Number_LSTM_Units
        self.Rate_Drop_LSTM = Rate_Drop_LSTM
        self.Number_Dense_Units = Number_Dense_Units
        self.Rate_Drop_Dense = Rate_Drop_Dense
        self.Activation_Function = Activation_Function
        self.Max_Sequence_Length = None
        pass

    def Train_And_Valid_Model(self, Train_Sentences_Pair, Train_Labels_List,
                              Embedding_Meta_Data, Model_Save_Directory, Validation_Size, Case_Number,
                              Shelve_Settings_Dictionary, Manager_Input_Handler_Object=None):
        # Explain Of The Function #
        """
        Train Siamese network to find similarity between sentences in `Train_Sentences_Pair`.
            Steps Involved:
                1. Pass each from sentences_pairs  to bidirectional LSTM encoder.
                2. Merge the vectors from LSTM encodes and passed to dense layer.
                3. Pass the  dense layer vectors to sigmoid output layer.
                4. Use cross entropy loss to train weights.
        Args:
            Train_Sentences_Pair (list): list of tuple of sentence pairs.
            Train_Labels_List (list): target value 1 if same sentences pair are similar otherwise 0.
            Embedding_Meta_Data (dict): dict containing tokenizer and word embedding matrix.
            Model_Save_Directory (str): working directory for where to save models.
            Validation_Size (float): The Size Of The Validation In The Training.
            Case_Number (Char): We Have Two Types Of Choice, According To The Model.
            Shelve_Settings_Dictionary (dict): Dictionary That Contains Parameters To Model.fit().
            Manager_Input_Handler_Object (object): Object of class.
                                                   Note - It Can Be 'Magic' Parameter.
        """

        # String #
        Best_Model_Path = None

        Tokenizer, Embedding_Matrix = Embedding_Meta_Data['Tokenizer'], Embedding_Meta_Data['Embedding_Matrix']

        # Check Which Max Sequence Length We Need According To The Model #
        if Case_Number == '1':
            self.Max_Sequence_Length = self.Max_Sequence_Length_Without_Aug
        elif Case_Number == '2':
            self.Max_Sequence_Length = self.Max_Sequence_Length_With_Aug

        '''
        Create training and validation dataset.
        Arguments -
                  Tokenizer (keras.preprocessing.text.Tokenizer): keras tokenizer object.
                  Train_Sentences_Pair (list): list of tuple of sentences pairs.
                  Train_Labels_List (list): list containing labels if respective sentences in sentence1 and sentence2
                                            are same or not (1 if same else 0).
                  Max_Sequence_Length (int): max sequence length of sentences to apply padding.
                  Validation_Size (float): contain ratio to split training data into validation data.
        '''
        # Use With Object #
        if Manager_Input_Handler_Object is not None:
            Train_All_Sentences_Data, Train_Specific_Sentences_Data, Train_Labels, Train_Leaks, \
            Valid_All_Sentences_Data, Valid_Specific_Sentences_Data, Valid_Labels, Valid_Leaks = \
                Manager_Input_Handler_Object.Create_Train_Development_Settings(Tokenizer, Train_Sentences_Pair,
                                                                               Train_Labels_List,
                                                                               self.Max_Sequence_Length,
                                                                               Validation_Size)
        # Not Use With Object #
        else:
            from Classes.Manager_Input_Handler import Create_Train_Development_Settings
            Train_All_Sentences_Data, Train_Specific_Sentences_Data, Train_Labels, Train_Leaks, \
            Valid_All_Sentences_Data, Valid_Specific_Sentences_Data, Valid_Labels, Valid_Leaks = \
                Create_Train_Development_Settings(Tokenizer, Train_Sentences_Pair,
                                                  Train_Labels_List,
                                                  self.Max_Sequence_Length,
                                                  Validation_Size)

        # Check Extreme Case #
        if Train_All_Sentences_Data is None:
            print("===========================================================================")
            print("\t\t\tFailure: Unable To Train Model !")
            print("===========================================================================")
            print()
            return None

        Number_Of_Words = len(Tokenizer.word_index) + 1

        # Creating word embedding layer #
        """
        Arguments - 
                  input_dim: int > 0. Size of the vocabulary, i.e. maximum integer index + 1.
                  output_dim: int >= 0. Dimension of the dense embedding.
                  embeddings_initializer: Initializer for the embeddings matrix (see initializers).
                  embeddings_regularizer: Regularizer function applied to the embeddings matrix (see regularizer).
                  activity_regularizer: Regularizer function applied to the output of the layer (its "activation").
                  embeddings_constraint: Constraint function applied to the embeddings matrix.
                  mask_zero: Whether or not the input value 0 is a special "padding" value that should be masked out. 
                             This is useful when using recurrent layers which may take variable length input. 
                             If this is True then all subsequent layers in the model need to support 
                             masking or an exception will be raised. 
                             If mask_zero is set to True, as a consequence, index 0 cannot be used in the vocabulary 
                             (input_dim should equal size of vocabulary + 1).
                  input_length: Length of input sequences, when it is constant. 
                                This argument is required if you are going to connect Flatten then Dense layers upstream 
                                (without it, the shape of the dense outputs cannot be computed).
        """
        Embedding_Layer = Embedding(Number_Of_Words, self.Embedding_Dimension, weights=[Embedding_Matrix],
                                    input_length=self.Max_Sequence_Length, trainable=False)

        # Creating LSTM Encoder #
        """
        Arguments - 
                  layer: Recurrent instance. merge_mode: Mode by which outputs of the forward and backward RNNs 
                         will be combined. One of {'sum', 'mul', 'concat', 'ave', None}. 
                         If None, the outputs will not be combined, they will be returned as a list. 
                  backward_layer: Optional Recurrent instance to be used to handle backwards input processing. 
                                  If backward_layer is not provided, the layer instance passed as the layer argument
                                  will be used to generate the backward layer automatically. 
                                  Note that the provided backward_layer layer should have properties matching 
                                  those of the layer argument, in particular it should have the same values for 
                                  stateful, return_states, return_sequence, etc. 
                                  In addition, backward_layer and layer should have different go_backwards 
                                  argument values. A ValueError will be raised if these requirements are not met. 
                  Call arguments: The call arguments for this layer are the same as those of the wrapped RNN layer. 
                  Raises: ValueError: 1. If layer or backward_layer is not a Layer instance. 
                                         In case of invalid merge_mode argument. If backward_layer has mismatched 
                                         properties compared to layer. 
        """
        Lstm_Layer = Bidirectional(LSTM(self.Number_LSTM_Units, dropout=self.Rate_Drop_LSTM,
                                        recurrent_dropout=self.Rate_Drop_LSTM))

        # Creating LSTM Encoder layer for First Sentence #
        """
        Input() is used to instantiate a Keras tensor. 
        A Keras tensor is a tensor object from the underlying backend (Theano, TensorFlow or CNTK), 
        which we augment with certain attributes that allow us to build a Keras model just by knowing the inputs and 
        outputs of the model. 
        For instance, if a, b and c are Keras tensors, it becomes possible to do: model = Model(input=[a, b], output=c) 
        Arguments - 
                  _keras_shape: Integer shape tuple propagated via Keras-side shape inference. 
                  keras_history: Last layer applied to the tensor. 
                                 the entire layer graph is retrievable from that layer, recursively. 
                  Arguments shape: A shape tuple (integer), not including the batch size. For instance, shape=(32,) 
                                   indicates that the expected input will be batches of 32-dimensional vectors. 
                  batch_shape: A shape tuple (integer), including the batch size. 
                               For instance, batch_shape=(10, 32) indicates that the expected input will be batches 
                               of 10 32-dim vectors. batch_shape=(None, 32) indicates batches of an 
                               arbitrary number of 32-dimensional 
                  vectors. name: An optional name string for the layer. 
                                 Should be unique in a model (do not reuse the same name twice). 
                                 It will be autogenerated if it isn't provided. 
                  dtype: The data type expected by the input, as a string (float32, float64, int32...). 
                  sparse: A boolean specifying whether the placeholder to be created is sparse. 
                  tensor: Optional existing tensor to wrap into the Input layer. If set, the layer will 
                          not create a placeholder tensor. 
        """
        Sequence_One_Input = Input(shape=(self.Max_Sequence_Length,), dtype='int32')

        """
        The embedding layer in Keras can be used when we want to create the embeddings to embed higher dimensional data 
        into lower dimensional vector space.
        The Keras Embedding layer requires all individual documents to be of same length. 
        Hence we wil pad the shorter documents with 0 for now. 
        Therefore now in Keras Embedding layer the 'input_length' will be equal to the length (ie no of words) 
        of the document with maximum length or maximum number of words.
        """
        Embedded_Sequences_1 = Embedding_Layer(Sequence_One_Input)

        """
        Based on available runtime hardware and constraints, this layer will choose different implementations 
        (cuDNN-based or pure-TensorFlow) to maximize the performance. 
        If a GPU is available and all the arguments to the layer meet the requirement of the CuDNN 
        kernel (see below for details), the layer will use a fast cuDNN implementation.
        Arguments - 
                  activation == 'tanh'
                  recurrent_activation == 'sigmoid'
                  recurrent_dropout == 0
                  unroll = False
                  use_bias = True
                  Inputs = Are not masked or strictly right padded.
        """
        X_1 = Lstm_Layer(Embedded_Sequences_1)

        # Creating LSTM Encoder layer for Second Sentence #
        """
        Input() is used to instantiate a Keras tensor. 
        A Keras tensor is a tensor object from the underlying backend (Theano, TensorFlow or CNTK), 
        which we augment with certain attributes that allow us to build a Keras model just by knowing the inputs and 
        outputs of the model. 
        For instance, if a, b and c are Keras tensors, it becomes possible to do: model = Model(input=[a, b], output=c) 
        Arguments - 
                  _keras_shape: Integer shape tuple propagated via Keras-side shape inference. 
                  keras_history: Last layer applied to the tensor. 
                                 the entire layer graph is retrievable from that layer, recursively. 
                  Arguments shape: A shape tuple (integer), not including the batch size. For instance, shape=(32,) 
                                   indicates that the expected input will be batches of 32-dimensional vectors. 
                  batch_shape: A shape tuple (integer), including the batch size. 
                               For instance, batch_shape=(10, 32) indicates that the expected input will be batches 
                               of 10 32-dim vectors. batch_shape=(None, 32) indicates batches of an 
                               arbitrary number of 32-dimensional 
                  vectors. name: An optional name string for the layer. 
                                 Should be unique in a model (do not reuse the same name twice). 
                                 It will be autogenerated if it isn't provided. 
                  dtype: The data type expected by the input, as a string (float32, float64, int32...). 
                  sparse: A boolean specifying whether the placeholder to be created is sparse. 
                  tensor: Optional existing tensor to wrap into the Input layer. If set, the layer will 
                          not create a placeholder tensor. 
        """
        Sequence_Two_Input = Input(shape=(self.Max_Sequence_Length,), dtype='int32')

        """
        The embedding layer in Keras can be used when we want to create the embeddings to embed higher dimensional data 
        into lower dimensional vector space.
        The Keras Embedding layer requires all individual documents to be of same length. 
        Hence we wil pad the shorter documents with 0 for now. 
        Therefore now in Keras Embedding layer the 'input_length' will be equal to the length (ie no of words) 
        of the document with maximum length or maximum number of words.
        """
        Embedded_Sequences_2 = Embedding_Layer(Sequence_Two_Input)

        """
        Based on available runtime hardware and constraints, this layer will choose different implementations 
        (cuDNN-based or pure-TensorFlow) to maximize the performance. 
        If a GPU is available and all the arguments to the layer meet the requirement of the CuDNN 
        kernel (see below for details), the layer will use a fast cuDNN implementation.
        Arguments - 
                  activation == 'tanh'
                  recurrent_activation == 'sigmoid'
                  recurrent_dropout == 0
                  unroll = False
                  use_bias = True
                  Inputs = Are not masked or strictly right padded.
        """
        X_2 = Lstm_Layer(Embedded_Sequences_2)

        # Creating leaks input #
        """
        Input() is used to instantiate a Keras tensor. 
        A Keras tensor is a tensor object from the underlying backend (Theano, TensorFlow or CNTK), 
        which we augment with certain attributes that allow us to build a Keras model just by knowing the inputs and 
        outputs of the model. 
        For instance, if a, b and c are Keras tensors, it becomes possible to do: model = Model(input=[a, b], output=c) 
        Arguments - 
                  _keras_shape: Integer shape tuple propagated via Keras-side shape inference. 
                  keras_history: Last layer applied to the tensor. 
                                 the entire layer graph is retrievable from that layer, recursively. 
                  Arguments shape: A shape tuple (integer), not including the batch size. For instance, shape=(32,) 
                                   indicates that the expected input will be batches of 32-dimensional vectors. 
                  batch_shape: A shape tuple (integer), including the batch size. 
                               For instance, batch_shape=(10, 32) indicates that the expected input will be batches 
                               of 10 32-dim vectors. batch_shape=(None, 32) indicates batches of an 
                               arbitrary number of 32-dimensional 
                  vectors. name: An optional name string for the layer. 
                                 Should be unique in a model (do not reuse the same name twice). 
                                 It will be autogenerated if it isn't provided. 
                  dtype: The data type expected by the input, as a string (float32, float64, int32...). 
                  sparse: A boolean specifying whether the placeholder to be created is sparse. 
                  tensor: Optional existing tensor to wrap into the Input layer. If set, the layer will 
                          not create a placeholder tensor. 
        """
        Leaks_Input = Input(shape=(Train_Leaks.shape[1],))

        """
        Dense implements the operation: 
        output = activation(dot(input, kernel) + bias) where activation is the element-wise activation function passed 
        as the activation argument, kernel is a weights matrix created by the layer, and bias is a bias vector created 
        by the layer (only applicable if use_bias is True).
        Note: if the input to the layer has a rank greater than 2, then it is flattened prior to the initial
              dot product with kernel.
        """
        Leaks_Dense = Dense(int(self.Number_Dense_Units / 2), activation=self.Activation_Function)(Leaks_Input)

        """
        Merging two LSTM encodes vectors from sentences to pass it to dense layer applying dropout 
        and batch normalisation.
        """
        Merged = concatenate([X_1, X_2, Leaks_Dense])

        """
        Normalize the activations of the previous layer at each batch, i.e. 
        applies a transformation that maintains the mean activation close to 0 and the activation 
        standard deviation close to 1. 
        """
        Merged = BatchNormalization()(Merged)

        """
        Applies Dropout to the input. Dropout consists in randomly setting a fraction rate of input units to 0 at 
        each update during training time, which helps prevent overfitting. 
        Arguments - 
                  rate: float between 0 and 1. Fraction of the input units to drop. 
                  noise_shape: 1D integer tensor representing the shape of the binary dropout mask that
                  will be multiplied with the input. For instance, if your inputs have shape 
                  (batch_size, timesteps, features) and you want the dropout mask to be the same for all 
                  timesteps, you can use noise_shape=(batch_size, 1, features).        
                  seed: A Python integer to use as random seed. 
        """
        Merged = Dropout(self.Rate_Drop_Dense)(Merged)

        """
        Dense implements the operation: 
        output = activation(dot(input, kernel) + bias) where activation is the element-wise activation function passed 
        as the activation argument, kernel is a weights matrix created by the layer, and bias is a bias vector created 
        by the layer (only applicable if use_bias is True).
        Note: if the input to the layer has a rank greater than 2, then it is flattened prior to the initial
              dot product with kernel.
        """
        Merged = Dense(self.Number_Dense_Units, activation=self.Activation_Function)(Merged)

        """
        Normalize the activations of the previous layer at each batch, i.e. 
        applies a transformation that maintains the mean activation close to 0 and the activation 
        standard deviation close to 1. 
        """
        Merged = BatchNormalization()(Merged)

        """
        Applies Dropout to the input. Dropout consists in randomly setting a fraction rate of input units to 0 at 
        each update during training time, which helps prevent overfitting. 
        Arguments - 
                  rate: float between 0 and 1. Fraction of the input units to drop. 
                  noise_shape: 1D integer tensor representing the shape of the binary dropout mask that
                  will be multiplied with the input. For instance, if your inputs have shape 
                  (batch_size, timesteps, features) and you want the dropout mask to be the same for all 
                  timesteps, you can use noise_shape=(batch_size, 1, features).        
                  seed: A Python integer to use as random seed. 
        """
        Merged = Dropout(self.Rate_Drop_Dense)(Merged)

        """
        Dense implements the operation: output = activation(dot(input, kernel) + bias) where 
        activation is the element-wise activation function passed as the activation argument, 
        kernel is a weights matrix created by the layer, and bias is a bias vector created by the layer 
        (only applicable if use_bias is True).
        Note: if the input to the layer has a rank greater than 2, then it is flattened prior to the initial
              dot product with kernel.
        """
        Preds = Dense(1, activation='sigmoid')(Merged)

        """
        Configures the model for training.
        """
        Model_Object = Model(inputs=[Sequence_One_Input, Sequence_Two_Input, Leaks_Input], outputs=Preds)

        """
        Configures the model for training.  
        """
        Model_Object.compile(loss='binary_crossentropy', optimizer='nadam', metrics=['acc'])

        """
        Stop training when a monitored quantity has stopped improving.
        """
        Early_Stopping = EarlyStopping(monitor='val_loss', patience=3)

        Checkpoint_Directory = Model_Save_Directory

        # If Directory Exist - Remove #
        if os.path.exists(Checkpoint_Directory):
            shutil.rmtree(Checkpoint_Directory)
            pass

        # Create New Directory #
        os.makedirs(Checkpoint_Directory)

        if Case_Number == '1':
            Best_Model_Path = Checkpoint_Directory + "\\" + "Model_Without_Augmentation" + '.h5'
        elif Case_Number == '2':
            Best_Model_Path = Checkpoint_Directory + "\\" + "Model_With_Augmentation" + '.h5'

        """
        Save the model after every epoch.
        `filepath` can contain named formatting options, which will be filled with the values of `epoch` and
        keys in `logs` (passed in `on_epoch_end`).
        For example: if `filepath` is `weights.{epoch:02d}-{val_loss:.2f}.hdf5`, then the model checkpoints will 
        be saved with the epoch number and the validation loss in the filename.
        """
        Model_Checkpoint = ModelCheckpoint(Best_Model_Path, save_best_only=True, save_weights_only=False)

        Tensorboard_Object = TensorBoard(log_dir=Checkpoint_Directory + "\\" + "Logs" + "\\")

        """
        Trains the model for a fixed number of epochs (iterations on a dataset).
        """
        Model_Object.fit([Train_All_Sentences_Data, Train_Specific_Sentences_Data, Train_Leaks], Train_Labels,
                         validation_data=([Valid_All_Sentences_Data, Valid_Specific_Sentences_Data, Valid_Leaks],
                                          Valid_Labels),
                         epochs=Shelve_Settings_Dictionary["Settings"]["Epoch_Number_Text"],
                         batch_size=Shelve_Settings_Dictionary["Settings"]["Batch_Size_Text"], shuffle=True,
                         callbacks=[Early_Stopping, Model_Checkpoint, Tensorboard_Object])

        return Best_Model_Path

    pass
