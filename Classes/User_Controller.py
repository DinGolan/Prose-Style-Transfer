# Imports #
import os
import numpy


class User_Controller_Class(object):

    # Constructor #
    def __init__(self, Script_Path, Choice_Number):
        self.Script_Path = Script_Path
        self.Choice_Number = Choice_Number
        pass

    def Check_If_The_Model_Exist(self):
        # Explain Of The Function #
        """
        This Function Check If The Model Exist.
        """

        if self.Choice_Number == '1':
            if not os.path.exists(self.Script_Path + "Model" + "\\" + "Without - Augmentation" + "\\" +
                                  "Model_Without_Augmentation.h5"):
                return False
            else:
                return True

        elif self.Choice_Number == '2':
            if not os.path.exists(self.Script_Path + "Model" + "\\" + "With - Augmentation" + "\\" +
                                  "Model_With_Augmentation.h5"):
                return False
            else:
                return True
        pass

    def Create_Test_Data_Small(self, Tokenizer_Object, Small_Sentences_Pair_Test, Max_Sequence_Length):
        # Explain Of The Function #
        """
        Create training and validation dataset.
        Args:
            Tokenizer_Object (keras.preprocessing.text.Tokenizer): keras tokenizer object.
            Small_Sentences_Pair_Test (list): list of tuple of sentences pairs.
            Max_Sequence_Length (int): max sequence length of sentences to apply padding.
        """

        # Froms #
        from keras.preprocessing.sequence import pad_sequences

        # List #
        Test_Sentences_1 = []
        Test_Sentences_2 = []

        # Divide The Test Data To Lists #
        if self.Choice_Number == '1':
            Test_Sentences_1 = [Pair[0] for Pair in Small_Sentences_Pair_Test]
            Test_Sentences_2 = [Pair[1] for Pair in Small_Sentences_Pair_Test]
        elif self.Choice_Number == '2':
            Test_Sentences_1 = [Pair[0].lower() for Pair in Small_Sentences_Pair_Test]
            Test_Sentences_2 = [Pair[1].lower() for Pair in Small_Sentences_Pair_Test]

        '''
        Transform each text in texts in a sequence of integers.
        Only top "num_words" most frequent words will be taken into account. 
        Only words known by the tokenizer will be taken into account.
        Arguments --->
        texts: list of texts to turn to sequences.
        Return: list of sequences (one per text input).
        texts_to_sequences_generator(texts): generator version of the above.
        '''
        Test_Sequences_1 = Tokenizer_Object.texts_to_sequences(Test_Sentences_1)
        Test_Sequences_2 = Tokenizer_Object.texts_to_sequences(Test_Sentences_2)
        Test_Leaks = [[len(set(Value_One)), len(set(Value_Two)), len(set(Value_One).intersection(Value_Two))]
                      for Value_One, Value_Two in zip(Test_Sequences_1, Test_Sequences_2)]

        '''
        This function [np.array] convert from List to Array.
        '''
        Test_Leaks = numpy.array(Test_Leaks)

        '''
        This function transforms a list of num_samples sequences (lists of integers) into a 2D Numpy array of shape 
        (num_samples, num_timesteps). 
        num_timesteps is either the maxlen argument if provided, or the length of the longest sequence otherwise. 
        Sequences that are shorter than num_timesteps are padded with value at the end. 
        Sequences longer than num_timesteps are truncated so that they fit the desired length. 
        The position where padding or truncation happens is determined by the arguments padding and truncating, 
        respectively. 
        '''
        Test_Data_1 = pad_sequences(Test_Sequences_1, maxlen=Max_Sequence_Length, padding='post', truncating='post')
        Test_Data_2 = pad_sequences(Test_Sequences_2, maxlen=Max_Sequence_Length, padding='post', truncating='post')

        return Test_Data_1, Test_Data_2, Test_Leaks

    pass
