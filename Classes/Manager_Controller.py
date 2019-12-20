# Imports #
import os
import numpy

# Froms #
from keras.models import load_model
from sklearn import metrics
from sklearn.model_selection import train_test_split


class Manager_Controller_Class(object):

    def __init__(self, Script_Path, Choice_Number, Shelve_Settings_Dictionary):
        self.Script_Path = Script_Path
        self.Choice_Number = Choice_Number
        self.Shelve_Settings_Dictionary = Shelve_Settings_Dictionary
        pass

    def Check_If_The_Model_Exist(self):
        # Explain Of The Function #
        """
        This Function Check If The Model Exist.
        This Function Belong Called By Select Versions Window Class.
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
        Arguments -
                  texts = list of texts to turn to sequences.
                  Return = list of sequences (one per text input).
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

    def Manager_Main_Function(self, Choice_Number, Shelve_Settings_Dictionary):
        # Explain Of The Function #
        """
        Main Function Of This Python File.
        """

        try:
            ###########################################################################################################
            ######################################## Data Preparation #################################################
            ###########################################################################################################

            # Bring Choice Number If It None #
            if self.Choice_Number is None:
                self.Choice_Number = Choice_Number

            # Bring Source Path If It None #
            if self.Script_Path is None:
                self.Script_Path = self.Bring_Source_Code_Path()

            # Bring Shelve Settings Dictionary If It None #
            if self.Shelve_Settings_Dictionary is None:
                self.Shelve_Settings_Dictionary = Shelve_Settings_Dictionary

            if self.Script_Path is not None:
                # Bring Data Set , Model Paths #
                Data_Set_Yes_Update_Path_No_Augmentation, Data_Set_Not_Update_Path_No_Augmentation, \
                Data_Set_Yes_Update_Path_Yes_Augmentation, Data_Set_Not_Update_Path_Yes_Augmentation, \
                Best_Model_Path = self.Bring_Data_Set_And_Model_Paths()

                # According The Choice Of The User ---> Data Augmentation , Not Data Augmentation #
                All_Sentence_List, Specific_Sentence_List, Labels_List = \
                    self.Check_The_Model_According_To_The_User_Choice(Data_Set_Yes_Update_Path_No_Augmentation,
                                                                      Data_Set_Not_Update_Path_No_Augmentation,
                                                                      Data_Set_Yes_Update_Path_Yes_Augmentation,
                                                                      Data_Set_Not_Update_Path_Yes_Augmentation)

                #######################################################################################################
                ######################################## Word Embedding ###############################################
                #######################################################################################################

                # From #
                from Classes.Manager_Input_Handler import Manager_Input_Handler_Class
                from Classes.Manager_Config import Siamese_Config

                # Creating word embedding meta data for word embedding #
                Manager_Input_Handler_Object = Manager_Input_Handler_Class()
                Tokenizer_Object, Embedding_Matrix = \
                    Manager_Input_Handler_Object.Word_Embedding_Meta_Data(All_Sentence_List + Specific_Sentence_List,
                                                                          Siamese_Config['EMBEDDING_DIM'])

                # Embedding Meta Data Dictionary #
                Embedding_Meta_Data = {
                    'Tokenizer': Tokenizer_Object,
                    'Embedding_Matrix': Embedding_Matrix
                }

                print("===========================================================================")
                print("\t\t\tDivide To Training And Testing !")
                print("===========================================================================")
                print()

                '''
                # Need Here To Split The Data To Training = 60% , Validation = 10% , Testing = 30% #
                # Note - Random State = 1 ===> The Divide Is The Same At Each Iteration #
                '''
                Train_All_Sentence_List, Test_All_Sentence_List, Train_Specific_Sentence_List, \
                Test_Specific_Sentence_List, Train_Labels_List, Test_Labels_List = \
                    train_test_split(All_Sentence_List, Specific_Sentence_List, Labels_List,
                                     test_size=1 - self.Shelve_Settings_Dictionary["Settings"]["Training_Split_Text"],
                                     train_size=self.Shelve_Settings_Dictionary["Settings"]["Training_Split_Text"])

                # Creating Train Sentence Pairs #
                Train_Sentences_Pair = [(Value_One, Value_Two) for Value_One, Value_Two in
                                        zip(Train_All_Sentence_List, Train_Specific_Sentence_List)]

                #######################################################################################################
                ######################################## Training #####################################################
                #######################################################################################################

                # From #
                from Classes.Manager_Model import SiameseBiLSTM

                # Create Siamese Bidirectional LSTM Object #
                Siamese = SiameseBiLSTM(Siamese_Config['EMBEDDING_DIM'],
                                        Siamese_Config['MAX_SEQUENCE_LENGTH_WITHOUT_AUG'],
                                        Siamese_Config['MAX_SEQUENCE_LENGTH_WITH_AUG'],
                                        Siamese_Config['VALIDATION_SIZE'], Siamese_Config['NUMBER_LSTM_UNITS'],
                                        Siamese_Config['RATE_DROP_LSTM'], Siamese_Config['NUMBER_DENSE_UNITS'],
                                        Siamese_Config['RATE_DROP_DENSE'], Siamese_Config['ACTIVATION_FUNCTION'])

                # Check If Model Exist , If Not (It's Mean Return False From Function) Train The Model #
                if not self.Check_If_Model_Exist(Best_Model_Path):
                    print("===========================================================================")
                    print("\t\t\tTrain The Model !")
                    print("===========================================================================")
                    print()

                    # Divide The Data To Training And Testing #
                    Model_Directory_Path = ""
                    if self.Choice_Number == '1':
                        Model_Directory_Path = self.Script_Path + "Model" + "\\" + "Without - Augmentation"
                    elif self.Choice_Number == '2':
                        Model_Directory_Path = self.Script_Path + "Model" + "\\" + "With - Augmentation"

                    Best_Model_Path = Siamese.Train_And_Valid_Model(Train_Sentences_Pair,
                                                                    Train_Labels_List, Embedding_Meta_Data,
                                                                    Model_Directory_Path, Siamese.Validation_Size,
                                                                    self.Choice_Number, self.Shelve_Settings_Dictionary,
                                                                    Manager_Input_Handler_Object)
                    # For - Console #
                    print()
                    pass

                #######################################################################################################
                ######################################## Testing ######################################################
                #######################################################################################################

                print("===========================================================================")
                print("\t\t\tLoad The Model !")
                print("===========================================================================")
                print()

                # Load The File Of The Module #
                if Best_Model_Path is not None:
                    Model_Object = load_model(Best_Model_Path)

                    # Creating Test Sentence Pairs #
                    Test_Sentences_Pair = [(Val_One, Val_Two) for Val_One, Val_Two in
                                           zip(Test_All_Sentence_List, Test_Specific_Sentence_List)]

                    # Check If The Length Of The Test Lists Is Even Or Odd #
                    Test_Sentences_Pair, Test_Labels_List = \
                        self.Check_The_Length_Of_The_Test_Lists(Test_Sentences_Pair, Test_Labels_List)

                    print("===========================================================================")
                    print("\t\t\tTest The Model !")
                    print("===========================================================================")

                    # Manipulate On The Testing Data #
                    Test_All_Sentences_List_Data = []
                    Test_Specific_Sentences_List_Data = []
                    Test_Leaks_Data = []

                    if self.Choice_Number == '1':
                        Test_All_Sentences_List_Data, Test_Specific_Sentences_List_Data, Test_Leaks_Data = \
                            Manager_Input_Handler_Object.Create_Test_Data_Big(Tokenizer_Object,
                                                                              Test_Sentences_Pair,
                                                                              Siamese_Config[
                                                                                  'MAX_SEQUENCE_LENGTH_WITHOUT_AUG'])
                    elif self.Choice_Number == '2':
                        Test_All_Sentences_List_Data, Test_Specific_Sentences_List_Data, Test_Leaks_Data = \
                            Manager_Input_Handler_Object.Create_Test_Data_Big(Tokenizer_Object,
                                                                              Test_Sentences_Pair,
                                                                              Siamese_Config[
                                                                                  'MAX_SEQUENCE_LENGTH_WITH_AUG'])

                    # Create Prediction For The Model #
                    Preds = list(Model_Object.predict([Test_All_Sentences_List_Data, Test_Specific_Sentences_List_Data,
                                                       Test_Leaks_Data], verbose=1).ravel())

                    # Create Prediction Label #
                    Preds_Label = self.Create_Prediction_Labels(Preds)

                    # Use With Confusion Matrix To Estimate The Result #
                    Confusion_Matrix = metrics.confusion_matrix(Test_Labels_List, Preds_Label).ravel()

                    # Print Confusion Results #
                    self.Print_Confusion_Results(Confusion_Matrix)

                    print("===========================================================================")
                    print("\t\t\tFinish To Build The Model !")
                    print("===========================================================================")

                    return "True"
                else:
                    return "Best Model Path = None"
            else:
                # Write Exception To Console #
                print()
                print("===========================================================================")
                print("\tThere Have Exception In Function - " + "Manager_Main_Function !")
                print("\tBecause - We Cant Find The Path Of The Script !")
                print("===========================================================================")
                print()

                return "Script Path = None"

        except Exception as Object_Exception:
            # Write To The Console The Exception #
            print()
            print("===========================================================================")
            print("\tThere Have Exception In Function - " + "Manager_Main_Function !")
            print("\tBecause - " + str(Object_Exception))
            print("===========================================================================")
            print()

            return "Exception"
        pass

    @staticmethod
    def Bring_Source_Code_Path():
        # Explain Of The Function #
        """
        This Function Bring For Us The Real Path Of The Script.
        """

        try:
            Path_Of_Script = os.path.realpath(__file__)

            # Manipulate On The Path Of The Exe Application ---> We Need To Make It Only One Time #
            Temp_List = []
            Global_Index = len(Path_Of_Script) - 1
            while Path_Of_Script[Global_Index] != "\\":
                Temp_List.append(Path_Of_Script[Global_Index])
                Global_Index -= 1
            Temp_List.reverse()
            Temp_String = ''.join(Temp_List)
            New_Path_Of_Script = Path_Of_Script.replace(Temp_String, '')
            New_Path_Of_Script = New_Path_Of_Script.replace("Classes\\", '')
            return New_Path_Of_Script

        except Exception as Object_Exception:
            # Write Exception To Console #
            print()
            print("===========================================================================")
            print("\tThere Have Exception In Function - " + "Bring_Source_Code_Path !")
            print("\tBecause - " + str(Object_Exception))
            print("===========================================================================")
            print()
            return None
            pass
        pass

    def Bring_Data_Set_And_Model_Paths(self):
        # Explain Of The Function #
        """
        This Function Bring For Us The Paths Of The Data Set And The Model.
        """

        # String #
        Best_Model_Path = ""

        # Path Of The Data Set - After Change Without Augmentation #
        Data_Set_Yes_Update_Path_No_Augmentation = self.Script_Path + "Data - Set\\Without - Augmentation\\" \
                                                                      "Data Set - After Change\\"

        # Path Of The Data Set - Before Change Without Augmentation #
        Data_Set_Not_Update_Path_No_Augmentation = self.Script_Path + "Data - Set\\Without - Augmentation\\" \
                                                                      "Data Set - Before Change\\"

        Data_Set_Yes_Update_Path_Yes_Augmentation = self.Script_Path + "Data - Set\\With - Augmentation\\" \
                                                                       "Data Set - After Change\\"

        Data_Set_Not_Update_Path_Yes_Augmentation = self.Script_Path + "Data - Set\\With - Augmentation\\" \
                                                                       "Data Set - Before Change\\"

        # Path Of The Model #
        if self.Choice_Number == '1':
            Best_Model_Path = self.Script_Path + "Model" + "\\" + "Without - Augmentation" + "\\" + \
                              "Model_Without_Augmentation.h5"
        elif self.Choice_Number == '2':
            Best_Model_Path = self.Script_Path + "Model" + "\\" + "With - Augmentation" + "\\" + \
                              "Model_With_Augmentation.h5"

        return Data_Set_Yes_Update_Path_No_Augmentation, Data_Set_Not_Update_Path_No_Augmentation, \
               Data_Set_Yes_Update_Path_Yes_Augmentation, Data_Set_Not_Update_Path_Yes_Augmentation, Best_Model_Path
        pass

    def Check_The_Model_According_To_The_User_Choice(self, Data_Set_Yes_Update_Path_No_Augmentation,
                                                     Data_Set_Not_Update_Path_No_Augmentation,
                                                     Data_Set_Yes_Update_Path_Yes_Augmentation,
                                                     Data_Set_Not_Update_Path_Yes_Augmentation):
        # Explain Of The Function #
        """
        This Function Check Which Model We Need To Run.
        """

        # Froms #
        from Classes.Manager_Build_Data_Set import Manager_Build_Data_Set_Class

        # Manager Build Data Set #
        Manager_Build_Data_Set_Object = Manager_Build_Data_Set_Class(self.Choice_Number)

        # List #
        All_Sentence_List = []
        Specific_Sentence_List = []
        Labels_List = []

        # According The Choice Of The User ---> Not Data Augmentation #
        if self.Choice_Number == '1':

            # Check If Directory Exist #
            There_Have_Files_In_Sub_Directory = self.Check_If_Directory_Exist(Data_Set_Yes_Update_Path_No_Augmentation)

            # If The Data Set Not Perfect , Create New Data Set #
            if There_Have_Files_In_Sub_Directory < 5:
                # Create New Data Set Without - Data Augmentation #
                Manager_Build_Data_Set_Object.Create_Data_Set(Data_Set_Yes_Update_Path_No_Augmentation,
                                                              Data_Set_Not_Update_Path_No_Augmentation)
                pass

            # Read From Data Set #
            All_Sentence_List, Specific_Sentence_List, Labels_List = \
                Manager_Build_Data_Set_Object.Read_From_Data_Set(Data_Set_Yes_Update_Path_No_Augmentation)

            pass

        # According The Choice Of The User ---> Data Augmentation #
        elif self.Choice_Number == '2':

            # Check If Directory Exist #
            There_Have_Files_In_Sub_Directory = self.Check_If_Directory_Exist(Data_Set_Yes_Update_Path_Yes_Augmentation)

            # If The Data Set Not Perfect , Create New Data Set #
            if There_Have_Files_In_Sub_Directory < 5:
                # Create New Data Set With - Data Augmentation #
                Manager_Build_Data_Set_Object.Create_Data_Set(Data_Set_Yes_Update_Path_Yes_Augmentation,
                                                              Data_Set_Not_Update_Path_Yes_Augmentation)
                pass

            # Read From Data Set #
            All_Sentence_List, Specific_Sentence_List, Labels_List = \
                Manager_Build_Data_Set_Object.Read_From_Data_Set(Data_Set_Yes_Update_Path_Yes_Augmentation)

            pass

        return All_Sentence_List, Specific_Sentence_List, Labels_List

    @staticmethod
    def Check_If_Directory_Exist(Data_Set_Update_Path):
        # Explain Of The Function #
        """
        Check If Directory Exist.
        """

        # Integer #
        There_Have_Files_In_Sub_Directory = 0

        if not os.path.exists(Data_Set_Update_Path):
            os.makedirs(Data_Set_Update_Path)
        else:
            """
            Check If Data Set Exist.
            If It's Exist , We Continue , Other Wise We Create Data Set. 
            """
            for Path, Sub_Folders, Files in os.walk(Data_Set_Update_Path, topdown=True):
                if not Files:
                    continue
                    pass
                else:
                    There_Have_Files_In_Sub_Directory += 1
        return There_Have_Files_In_Sub_Directory
        pass

    @staticmethod
    def Check_If_Model_Exist(Best_Model_Path):
        # Explain Of The Function #
        """
        This Function Check If The Model Exist.
        This Function Belong Called By Manager Controller Class.
        """

        if not os.path.exists(Best_Model_Path):
            return False
        else:
            return True
        pass

    @staticmethod
    def Check_The_Length_Of_The_Test_Lists(Test_Sentences_Pair, Test_Labels_List):
        # Explain Of The Function #
        """
        This Function Check If We Have Even Or Odd Length In The Test Lists.
        """

        # If We Have Odd Number In The List #
        if len(Test_Sentences_Pair) % 2 == 1:
            Test_Sentences_Pair.pop(len(Test_Sentences_Pair) - 1)
            pass

        # If We Have Odd Number In The List #
        if len(Test_Labels_List) % 2 == 1:
            Test_Labels_List.pop(len(Test_Labels_List) - 1)
            pass

        return Test_Sentences_Pair, Test_Labels_List
        pass

    @staticmethod
    def Create_Prediction_Labels(Preds):
        # Explain Of The Function #
        """
        This Function Create Prediction Labels.
        If The Prediction > 0.5 ===> We Will Get ---> 1.
        Else The Prediction < 0.5 ===> We Will Get ---> 0.
        """

        # Note ---> The Threshold = 0.01 #
        Preds_Label = []
        for Value in Preds:
            if Value < 0.01:
                Preds_Label.append(0)
                pass
            else:
                Preds_Label.append(1)
                pass
            pass

        return Preds_Label
        pass

    @staticmethod
    def Print_Confusion_Results(Confusion_Matrix):
        # Explain Of The Function #
        """
        This Function Print The Confusion Matrix Results.
        """

        print()
        print("===========================================================================")
        print("\t\tThe Confusion Matrix Is ===> " + str(Confusion_Matrix))
        print("===========================================================================")
        print()

        # Error Rate = (FP + FN) / (FP + TP + FN + TN) #
        Error_Rate = (Confusion_Matrix[1] + Confusion_Matrix[2]) / sum(Confusion_Matrix)
        print("===========================================================================")
        print("\t\tThe Error Rate Is ===> " + str(Error_Rate))
        print("===========================================================================")
        print()

        # Accuracy = (TP + TN) / (FP + TP + FN + TN) #
        Accuracy = (Confusion_Matrix[0] + Confusion_Matrix[3]) / sum(Confusion_Matrix)
        print("===========================================================================")
        print("\t\tThe Accuracy Is ===> " + str(Accuracy))
        print("===========================================================================")
        print()
        pass

    pass
