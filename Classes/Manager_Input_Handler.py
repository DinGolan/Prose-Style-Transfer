# Imports #
import gc
import numpy as np

# Froms #
from gensim.models import Word2Vec
from keras.preprocessing.sequence import pad_sequences
from keras.preprocessing.text import Tokenizer


class Manager_Input_Handler_Class(object):

    def __init__(self):
        pass

    def Word_Embedding_Meta_Data(self, Documents, Embedding_dimension):
        # Explain Of The Function #
        """
        Load tokenizer object for given vocabs list.
        Args:
            Documents (list): list of document , Its consist the sentences from the chapters that the users pick.
            Embedding_dimension (int): embedding dimension.
        """

        '''
        Documents Its List Of Sentences.
        For each sentence , we Lower the characters , and we split the sentence according to his words.
        '''
        Documents = [Value.split() for Value in Documents]
        Tokenizer_Object = Tokenizer()

        '''
        Updates internal vocabulary based on a list of texts. 
        This method creates the vocabulary index based on word frequency. 
        So if you give it something like, "The cat sat on the mat." 
        It will create a dictionary i.e word_index["The"] = 1; word_index["cat"] = 2. 
        It is word -> index dictionary so every word gets a unique integer value.
        '''
        Tokenizer_Object.fit_on_texts(Documents)

        print("===========================================================================")
        print("\t\t\tTrain Word To Vector !")
        print("===========================================================================")
        print()

        '''
        Word Embedding is a language modeling technique used for mapping words to vectors of real numbers. 
        It represents words or phrases in vector space with several dimensions. 
        Word embeddings can be generated using various methods like neural networks. 
        Word2Vec consists of models for generating word embedding. 
        These models are shallow two layer neural networks having one input layer, one hidden layer and one output layer. 
        Word2Vec utilizes two architectures : 
        1. CBOW (Continuous Bag of Words) : CBOW model predicts the current word given context words within specific window. 
        The input layer contains the context words and the output layer contains the current word. 
        The hidden layer contains the number of dimensions in which we want to represent current 
        word present at the output layer. 
        2. Skip Gram : Skip gram predicts the surrounding context words within specific window given current word. 
        The input layer contains the current word and the output layer contains the context words. 
        The hidden layer contains the number of dimensions in which we want to represent current word present at 
        the input layer. 
        '''
        Word_Vector = self.Train_Word2Vec(Documents, Embedding_dimension)

        print("===========================================================================")
        print("\t\t\tCreate Embedding Matrix !")
        print("===========================================================================")
        print()

        '''
        A word embedding is a class of approaches for representing words and documents 
        using a dense vector representation.
        It is an improvement over more the traditional bag-of-word model encoding 
        schemes where large sparse vectors were
        used to represent each word or to score each word within a vector to represent an entire vocabulary. 
        These representations were sparse because the vocabularies were vast and a given word or document would be 
        represented by a large vector comprised mostly of zero values.
        Instead, in an embedding, words are represented by dense vectors where a vector represents the projection
        of the word into a continuous vector space.
        The position of a word within the vector space is learned from text and is based on the words that 
        surround the word when it is used.
        The position of a word in the learned vector space is referred to as its embedding.
        Keras offers an Embedding layer that can be used for neural networks on text data. 
        It requires that the input data be integer encoded, so that each word is represented by a unique integer. 
        This data preparation step can be performed using the Tokenizer API also provided with Keras. 
        The Embedding layer is initialized with random weights and will learn an embedding for 
        all of the words in the training dataset. 
        It is a flexible layer that can be used in a variety of ways, such as: It can be used alone to learn a word 
        embedding that can be saved and used in another model later. 
        It can be used as part of a deep learning model where the embedding is learned along with the model itself. 
        It can be used to load a pre-trained word embedding model, a type of transfer learning. 
        The Embedding layer is defined as the first hidden layer of a network. 
        '''
        Embedding_Matrix = self.Create_Embedding_Matrix(Tokenizer_Object, Word_Vector, Embedding_dimension)
        del Word_Vector

        '''
        Forces an immediate garbage collection of all generations.
        '''
        gc.collect()
        return Tokenizer_Object, Embedding_Matrix

    @staticmethod
    def Train_Word2Vec(Documents, Embedding_Dimension):
        # Explain Of The Function #
        """
        train word2vector over training documents.
        Args:
            Documents (list): list of document.
            Embedding_Dimension (int): output word vector size.
        """

        '''
        Word Embedding is a language modeling technique used for mapping words to vectors of real numbers. 
        It represents words or phrases in vector space with several dimensions. 
        Word embeddings can be generated using various methods like neural networks. 
        Word2Vec consists of models for generating word embedding. These models are shallow two layer neural networks 
        having one input layer, one hidden layer and one output layer. Word2Vec utilizes two architectures : 
        1. CBOW (Continuous Bag of Words) : CBOW model predicts the current word given 
        context words within specific window. 
        The input layer contains the context words and the output layer contains the current word. 
        The hidden layer contains the number of dimensions in which we want to represent current word 
        present at the output layer. 
        2. Skip Gram : Skip gram predicts the surrounding context words within specific window given current word. 
        The input layer contains the current word and the output layer contains the context words. 
        The hidden layer contains the number of dimensions in which we want to 
        represent current word present at the input layer. 
        Arguments -
                  min_count = int - Ignores all words with total absolute frequency lower than this - (2, 100)
                  window = int - The maximum distance between the current and predicted word within a sentence. 
                                 E.g. window words on the left and window words on the left of our target - (2, 10)
                  size = int - Dimensionality of the feature vectors. - (50, 300)
                  sample = float - The threshold for configuring which higher-frequency words are randomly downsampled. 
                  alpha = float - The initial learning rate - (0.01, 0.05)
                  min_alpha = float - Learning rate will linearly drop to min_alpha as training progresses. To set it: 
                              alpha - (min_alpha * epochs) ~ 0.00
                  negative = int - If > 0, negative sampling will be used, the int for negative 
                             specifies how many "noise words" should be drown. 
                             If set to 0, no negative sampling is used. - (5, 20)
                  workers = int - Use these many worker threads to train the model 
                  (=faster training with multicore machines)
        '''
        Model_Object = Word2Vec(Documents, min_count=1, size=Embedding_Dimension)

        '''
        We can perform various NLP word tasks with a trained model.
        If we are finished training a model (i.e. no more updates, only querying), 
        we can switch to the KeyedVectors instance, its mean to convert the model.wv to Dictionary.
        '''
        Word_Vectors = Model_Object.wv
        del Model_Object
        return Word_Vectors

    @staticmethod
    def Create_Embedding_Matrix(Tokenizer_Object, Word_Vectors, Embedding_Dimension):
        # Explain Of The Function #
        """
        Create embedding matrix containing word indexes and respective vectors from word vectors.
        Args:
            Tokenizer_Object (keras.preprocessing.text.Tokenizer): keras tokenizer object containing word indexes.
            Word_Vectors (dict): dict containing word and their respective vectors.
            Embedding_Dimension (int): dimension of word vector.
        Returns:
        """

        # Integer #
        Count_Word_Without_Vector = 0

        '''
        Take the Number Of Words From Tokenizer.Word_Index.
        '''
        Number_Of_Words = len(Tokenizer_Object.word_index) + 1

        '''
        The Type of Word_Index Is Dictionary.
        '''
        Word_Index = Tokenizer_Object.word_index

        '''
        Zeros all the cells for Embedding Matrix.
        '''
        Embedding_Matrix = np.zeros((Number_Of_Words, Embedding_Dimension))
        print("===========================================================================")
        print("\t\tEmbedding matrix shape: %s" % str(Embedding_Matrix.shape))
        print("===========================================================================\n")

        '''
        We build an embedding matrix that we can load into an Embedding layer. 
        It must be a matrix of shape (max_words, embedding_dim), where each entry i contains 
        the embedding_dim-dimensional vector for the word of index i in our 
        reference word index (built during tokenization). 
        Note that the index 0 isn’t supposed to stand for any word or token—it’s a placeholder.
        '''
        for Word, Index in Word_Index.items():
            try:
                Embedding_Vector = Word_Vectors[Word]
                if Embedding_Vector is not None:
                    Embedding_Matrix[Index] = Embedding_Vector
                    pass
                pass
            except KeyError:
                Count_Word_Without_Vector += 1
                pass
        print("===========================================================================")
        print("\t\tNumber Of Words Without Vector Is - %d !" % Count_Word_Without_Vector)
        print("===========================================================================\n")
        return Embedding_Matrix

    @staticmethod
    def Create_Train_Development_Settings(Tokenizer_Object, Train_Sentences_Pair,
                                          Train_Labels_List, Max_Sequence_Length,
                                          Validation_Size):
        # Explain Of The Function #
        """
        Create training and validation dataset.
        Args:
            Tokenizer_Object (keras.preprocessing.text.Tokenizer): keras tokenizer object.
            Train_Sentences_Pair (list): list of tuple of sentences pairs.
            Train_Labels_List (list): list containing labels if respective sentences in Sentence_One and Sentence_Two
                                      are same or not (1 if same else 0).
            Max_Sequence_Length (int): max sequence length of sentences to apply padding.
            Validation_Size (float): contain ratio to split training data into validation data.
        """

        '''
        Iterate on dictionary, and take the 'Key' and 'Value'.
        '''
        Train_All_Sentences_List = [x[0] for x in Train_Sentences_Pair]
        Train_Specific_Sentences_List = [x[1] for x in Train_Sentences_Pair]

        '''
        Transform each text in texts in a sequence of integers.
        Only top "num_words" most frequent words will be taken into account. Only words known
        by the tokenizer will be taken into account.
        Arguments -
                  texts = list of texts to turn to sequences.
                  Return = list of sequences (one per text input).
        '''
        Train_All_Sentences_List_Sequences = Tokenizer_Object.texts_to_sequences(Train_All_Sentences_List)
        Train_Specific_Sentences_List_Sequences = Tokenizer_Object.texts_to_sequences(Train_Specific_Sentences_List)
        Train_Leaks = [[len(set(Value_One)), len(set(Value_Two)), len(set(Value_One).intersection(Value_Two))]
                       for Value_One, Value_Two in
                       zip(Train_All_Sentences_List_Sequences, Train_Specific_Sentences_List_Sequences)]

        '''
        This function transforms a list of num_samples sequences (lists of integers) into 
        a 2D Numpy array of shape (num_samples, num_timesteps). 
        num_timesteps is either the maxlen argument if provided, or the length of the longest sequence otherwise. 
        Sequences that are shorter than num_timesteps are padded with value at the end. 
        Sequences longer than num_timesteps are truncated so that they fit the desired length. 
        The position where padding or truncation happens is determined by the 
        arguments padding and truncating, respectively. 
        '''
        Train_Padded_All_Sentences_List = pad_sequences(Train_All_Sentences_List_Sequences,
                                                        maxlen=Max_Sequence_Length,
                                                        padding='post', truncating='post')
        Train_Padded_Specific_Sentences_List = pad_sequences(Train_Specific_Sentences_List_Sequences,
                                                             maxlen=Max_Sequence_Length,
                                                             padding='post', truncating='post')

        '''
        This function [np.array] convert from List to Array.
        '''
        Train_Labels_List = np.array(Train_Labels_List)
        Train_Leaks = np.array(Train_Leaks)

        '''
        Randomly permute a sequence, or return a permuted range.
        If x is a multi-dimensional array, it is only shuffled along its first index.
        Arguments - 
                  x = int or array_like. If x is an integer, randomly permute np.arange(x). 
                      If x is an array, make a copy and shuffle the elements randomly.
                  Returns = ndarray, Permuted sequence or array range.
        '''
        Train_Shuffle_Indices = np.random.permutation(np.arange(len(Train_Labels_List)))
        Train_All_Sentences_List_Shuffled = Train_Padded_All_Sentences_List[Train_Shuffle_Indices]
        Train_Specific_Sentences_List_Shuffled = Train_Padded_Specific_Sentences_List[Train_Shuffle_Indices]
        Train_Labels_Shuffled = Train_Labels_List[Train_Shuffle_Indices]
        Train_Leaks_Shuffled = Train_Leaks[Train_Shuffle_Indices]

        '''
        Divide Index Is Parameter That Divide Between The Training And Testing. 
        '''
        Divide_Index = max(1, int(len(Train_Labels_Shuffled) * Validation_Size))
        Train_All_Sentences_Data, Valid_All_Sentences_Data = Train_All_Sentences_List_Shuffled[:-Divide_Index], \
                                                             Train_All_Sentences_List_Shuffled[-Divide_Index:]
        Train_Specific_Sentences_Data, Valid_Specific_Sentences_Data = \
            Train_Specific_Sentences_List_Shuffled[:-Divide_Index], Train_Specific_Sentences_List_Shuffled[
                                                                    -Divide_Index:]
        Train_Labels, Valid_Labels = Train_Labels_Shuffled[:-Divide_Index], Train_Labels_Shuffled[-Divide_Index:]
        Train_Leaks, Valid_Leaks = Train_Leaks_Shuffled[:-Divide_Index], Train_Leaks_Shuffled[-Divide_Index:]

        # Garbage Collector #
        del Train_Padded_All_Sentences_List
        del Train_Padded_Specific_Sentences_List
        gc.collect()

        return Train_All_Sentences_Data, Train_Specific_Sentences_Data, Train_Labels, Train_Leaks, \
               Valid_All_Sentences_Data, Valid_Specific_Sentences_Data, Valid_Labels, Valid_Leaks

    @staticmethod
    def Create_Test_Data_Big(Tokenizer_Object, Sentences_Pair_Test, Max_Sequence_Length):
        # Explain Of The Function #
        """
        Create training and validation dataset.
        Args:
            Tokenizer_Object (keras.preprocessing.text.Tokenizer): keras tokenizer object.
            Sentences_Pair_Test (list): list of tuple of sentences pairs.
            Max_Sequence_Length (int): max sequence length of sentences to apply padding.
        """

        # Divide The Test Data To Lists #
        Test_All_Sentences_List = [x[0] for x in Sentences_Pair_Test]
        Test_Specific_Sentences_List = [x[1] for x in Sentences_Pair_Test]

        '''
        Transform each text in texts in a sequence of integers.
        Only top "num_words" most frequent words will be taken into account. 
        Only words known by the tokenizer will be taken into account.
        Arguments -
                  texts = list of texts to turn to sequences.
                  Return = list of sequences (one per text input).

        '''
        Test_All_Sentences_List_Sequences = Tokenizer_Object.texts_to_sequences(Test_All_Sentences_List)
        Test_Specific_Sentences_List_Sequences = Tokenizer_Object.texts_to_sequences(Test_Specific_Sentences_List)
        Test_Leaks = [[len(set(Value_One)), len(set(Value_Two)), len(set(Value_One).intersection(Value_Two))]
                      for Value_One, Value_Two in zip(Test_All_Sentences_List_Sequences,
                                                      Test_Specific_Sentences_List_Sequences)]

        '''
        This function [np.array] convert from List to Array.
        '''
        Test_Leaks = np.array(Test_Leaks)

        '''
        This function transforms a list of num_samples sequences (lists of integers) into 
        a 2D Numpy array of shape (num_samples, num_timesteps). 
        num_timesteps is either the maxlen argument if provided, or the length of the longest sequence otherwise. 
        Sequences that are shorter than num_timesteps are padded with value at the end. 
        Sequences longer than num_timesteps are truncated so that they fit the desired length. 
        The position where padding or truncation happens is determined by the 
        arguments padding and truncating, respectively. 
        '''
        Test_Padded_All_Sentences_List = pad_sequences(Test_All_Sentences_List_Sequences,
                                                       maxlen=Max_Sequence_Length,
                                                       padding='post', truncating='post')
        Test_Padded_Specific_Sentences_List = pad_sequences(Test_Specific_Sentences_List_Sequences,
                                                            maxlen=Max_Sequence_Length,
                                                            padding='post', truncating='post')

        return Test_Padded_All_Sentences_List, Test_Padded_Specific_Sentences_List, Test_Leaks

    pass


# Created In Class / Used For Extreme Case #
def Create_Train_Development_Settings(Tokenizer_Object, Train_Sentences_Pair,
                                      Train_Labels_List, Max_Sequence_Length,
                                      Validation_Size):
    # Explain Of The Function #
    """
    Create training and validation dataset.
    Args:
        Tokenizer_Object (keras.preprocessing.text.Tokenizer): keras tokenizer object.
        Train_Sentences_Pair (list): list of tuple of sentences pairs.
        Train_Labels_List (list): list containing labels if respective sentences in Sentence_One and Sentence_Two
                                  are same or not (1 if same else 0).
        Max_Sequence_Length (int): max sequence length of sentences to apply padding.
        Validation_Size (float): contain ratio to split training data into validation data.
    """

    '''
    Iterate on dictionary, and take the 'Key' and 'Value'.
    '''
    Train_All_Sentences_List = [x[0] for x in Train_Sentences_Pair]
    Train_Specific_Sentences_List = [x[1] for x in Train_Sentences_Pair]

    '''
    Transform each text in texts in a sequence of integers.
    Only top "num_words" most frequent words will be taken into account. Only words known
    by the tokenizer will be taken into account.
    Arguments -
              texts = list of texts to turn to sequences.
              Return = list of sequences (one per text input).
    '''
    Train_All_Sentences_List_Sequences = Tokenizer_Object.texts_to_sequences(Train_All_Sentences_List)
    Train_Specific_Sentences_List_Sequences = Tokenizer_Object.texts_to_sequences(Train_Specific_Sentences_List)
    Train_Leaks = [[len(set(Value_One)), len(set(Value_Two)), len(set(Value_One).intersection(Value_Two))]
                   for Value_One, Value_Two in
                   zip(Train_All_Sentences_List_Sequences, Train_Specific_Sentences_List_Sequences)]

    '''
    This function transforms a list of num_samples sequences (lists of integers) into 
    a 2D Numpy array of shape (num_samples, num_timesteps). 
    num_timesteps is either the maxlen argument if provided, or the length of the longest sequence otherwise. 
    Sequences that are shorter than num_timesteps are padded with value at the end. 
    Sequences longer than num_timesteps are truncated so that they fit the desired length. 
    The position where padding or truncation happens is determined by the 
    arguments padding and truncating, respectively. 
    '''
    Train_Padded_All_Sentences_List = pad_sequences(Train_All_Sentences_List_Sequences,
                                                    maxlen=Max_Sequence_Length,
                                                    padding='post', truncating='post')
    Train_Padded_Specific_Sentences_List = pad_sequences(Train_Specific_Sentences_List_Sequences,
                                                         maxlen=Max_Sequence_Length,
                                                         padding='post', truncating='post')

    '''
    This function [np.array] convert from List to Array.
    '''
    Train_Labels_List = np.array(Train_Labels_List)
    Train_Leaks = np.array(Train_Leaks)

    '''
    Randomly permute a sequence, or return a permuted range.
    If x is a multi-dimensional array, it is only shuffled along its first index.
    Parameters - 
               x = int or array_like. If x is an integer, randomly permute np.arange(x). 
                   If x is an array, make a copy and shuffle the elements randomly.
               Returns = ndarray, Permuted sequence or array range.
    '''
    Train_Shuffle_Indices = np.random.permutation(np.arange(len(Train_Labels_List)))
    Train_All_Sentences_List_Shuffled = Train_Padded_All_Sentences_List[Train_Shuffle_Indices]
    Train_Specific_Sentences_List_Shuffled = Train_Padded_Specific_Sentences_List[Train_Shuffle_Indices]
    Train_Labels_Shuffled = Train_Labels_List[Train_Shuffle_Indices]
    Train_Leaks_Shuffled = Train_Leaks[Train_Shuffle_Indices]

    '''
    Divide Index Is Parameter That Divide Between The Training And Testing. 
    '''
    Divide_Index = max(1, int(len(Train_Labels_Shuffled) * Validation_Size))
    Train_All_Sentences_Data, Valid_All_Sentences_Data = Train_All_Sentences_List_Shuffled[:-Divide_Index], \
                                                         Train_All_Sentences_List_Shuffled[-Divide_Index:]
    Train_Specific_Sentences_Data, Valid_Specific_Sentences_Data = \
        Train_Specific_Sentences_List_Shuffled[:-Divide_Index], Train_Specific_Sentences_List_Shuffled[-Divide_Index:]
    Train_Labels, Valid_Labels = Train_Labels_Shuffled[:-Divide_Index], Train_Labels_Shuffled[-Divide_Index:]
    Train_Leaks, Valid_Leaks = Train_Leaks_Shuffled[:-Divide_Index], Train_Leaks_Shuffled[-Divide_Index:]

    # Garbage Collector #
    del Train_Padded_All_Sentences_List
    del Train_Padded_Specific_Sentences_List
    gc.collect()

    return Train_All_Sentences_Data, Train_Specific_Sentences_Data, Train_Labels, Train_Leaks, \
           Valid_All_Sentences_Data, Valid_Specific_Sentences_Data, Valid_Labels, Valid_Leaks
