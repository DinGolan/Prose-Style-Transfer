# Imports #
import os
import re
import pandas
import xlwt
import sys
import nlpaug.augmenter.word as Augmenter_Word

# Froms #
from xlwt import Workbook
from nltk.corpus import stopwords


class Manager_Build_Data_Set_Class(object):

    def __init__(self, Choice_Number):
        self.Choice_Number = Choice_Number
        pass

    def Create_Data_Set(self, Data_Set_Update_Path, Data_Set_Not_Update_Path):
        # Explain Of The Function #
        """
        Main Function Of This Python File.
        """

        print("===========================================================================")
        print("\t\t\tCreate Data Set !")
        print("===========================================================================")
        print()

        # Integer #
        Main_Index = 1

        # Boolean #
        Exit_Loop = False

        # List #
        Sentences_File_One = []
        Sentences_File_Two = []
        Sentences_File_Three = []
        Sentences_File_Four = []

        # Files #
        New_Destination_Path = None
        New_Destination_Directory = None

        # Book's Name #
        Book_One = "בראשית"
        Book_Two = "שמות"
        Book_Three = "ויקרא"
        Book_Four = "במדבר"
        Book_Five = "דברים"

        '''
        'not Exit_Loop' === False
        '''
        while not Exit_Loop:
            # Bring Details #
            Path_One, Path_Two, Path_Three, Path_Four, Name_Of_Sheet, Name_Of_New_File = \
                self.Bring_Details_According_To_Turn(Main_Index, Data_Set_Not_Update_Path)

            # Details From CSV Files #
            if Path_One != "":
                File_One = pandas.read_csv(Path_One, encoding='utf-8', error_bad_lines=False)
                Sentences_File_One = list(File_One['Sentences'])
                pass
            if Path_Two != "":
                File_Two = pandas.read_csv(Path_Two, encoding='utf-8', error_bad_lines=False)
                Sentences_File_Two = list(File_Two['Sentences'])
                pass
            if Path_Three != "":
                File_Three = pandas.read_csv(Path_Three, encoding='utf-8', error_bad_lines=False)
                Sentences_File_Three = list(File_Three['Sentences'])
                pass
            if Path_Four != "":
                File_Four = pandas.read_csv(Path_Three, encoding='utf-8', error_bad_lines=False)
                Sentences_File_Four = list(File_Four['Sentences'])
                pass

            # Create Excel File #
            if 1 <= Main_Index <= 18:
                New_Destination_Directory = Data_Set_Update_Path + Book_One
                New_Destination_Path = Data_Set_Update_Path + Book_One + "\\" + Name_Of_New_File
                pass
            elif 19 <= Main_Index <= 41:
                New_Destination_Directory = Data_Set_Update_Path + Book_Two
                New_Destination_Path = Data_Set_Update_Path + Book_Two + "\\" + Name_Of_New_File
                pass
            elif 42 <= Main_Index <= 56:
                New_Destination_Directory = Data_Set_Update_Path + Book_Three
                New_Destination_Path = Data_Set_Update_Path + Book_Three + "\\" + Name_Of_New_File
                pass
            elif 57 <= Main_Index <= 75:
                New_Destination_Directory = Data_Set_Update_Path + Book_Four
                New_Destination_Path = Data_Set_Update_Path + Book_Four + "\\" + Name_Of_New_File
                pass
            elif 76 <= Main_Index <= 91:
                New_Destination_Directory = Data_Set_Update_Path + Book_Five
                New_Destination_Path = Data_Set_Update_Path + Book_Five + "\\" + Name_Of_New_File
                pass

            self.Create_New_Excel_File(Sentences_File_One,
                                       Sentences_File_Two,
                                       Sentences_File_Three,
                                       Sentences_File_Four,
                                       Name_Of_Sheet,
                                       New_Destination_Directory,
                                       New_Destination_Path)

            print("===========================================================================")
            print("\t\t\tFinish To Create => " + Name_Of_New_File)
            print("===========================================================================")
            print()

            # Update The Counter #
            Main_Index += 1

            # Check If We Are In The Last Chapter #
            # 91 === The Last Chapter #
            if Main_Index == 91:
                Exit_Loop = True

            New_Destination_Path = None
            Sentences_File_One = []
            Sentences_File_Two = []
            Sentences_File_Three = []
            Sentences_File_Four = []
            pass

        print("===========================================================================")
        print("\t\t\t Finish To Create The Data Set !")
        print("===========================================================================")
        print()
        pass

    @staticmethod
    def Bring_Details_According_To_Turn(Main_Index, Data_Set_Not_Update_Path):
        # Explain Of The Function #
        """
        Check The Number Of Turn , And Bring Details According To It.
        """

        # Path's #
        Path_One = ""
        Path_Two = ""
        Path_Three = ""
        Path_Four = ""

        # Excel Parameter's #
        Name_Of_Sheet = ""
        Name_Of_New_File = ""

        # Version's Name #
        Version_One = "ברויאר"
        Version_Two = "לנינגרד"
        Version_Three = "קורן"
        Version_Four = "תלמוד"

        # Book's Name #
        Book_One = "בראשית"
        Book_Two = "שמות"
        Book_Three = "ויקרא"
        Book_Four = "במדבר"
        Book_Five = "דברים"

        # Chapter - בראשית #
        if Main_Index == 1:
            # Path #
            Path_One = Data_Set_Not_Update_Path + Version_One + "\\" + Book_One + "\\" + "בראשית ד, יג - ברויאר.csv"
            Path_Two = Data_Set_Not_Update_Path + Version_Two + "\\" + Book_One + "\\" + "בראשית ד, יג - לנינגרד.csv"
            Path_Three = Data_Set_Not_Update_Path + Version_Three + "\\" + Book_One + "\\" + "בראשית ד, יג - קורן.csv"
            Path_Four = ""

            # Sheet #
            Name_Of_Sheet = "בראשית ד, יג"

            # Excel File #
            Name_Of_New_File = "בראשית ד, יג.xls"
            pass

        elif Main_Index == 2:
            # Path #
            Path_One = Data_Set_Not_Update_Path + Version_One + "\\" + Book_One + "\\" + "בראשית ז, יא - ברויאר.csv"
            Path_Two = Data_Set_Not_Update_Path + Version_Two + "\\" + Book_One + "\\" + "בראשית ז, יא - לנינגרד.csv"
            Path_Three = Data_Set_Not_Update_Path + Version_Three + "\\" + Book_One + \
                         "\\" + "בראשית ז, פסוקים - ח , יא - קורן.csv"
            Path_Four = Data_Set_Not_Update_Path + Version_Four + "\\" + Book_One + \
                        "\\" + "בראשית ז, פסוקים - ח , יא - תלמוד.csv"

            # Sheet #
            Name_Of_Sheet = "בראשית ז, פס' - ח, יא"

            # Excel File #
            Name_Of_New_File = "בראשית ז, פסוקים - ח, יא.xls"
            pass

        elif Main_Index == 3:
            # Path #
            Path_One = Data_Set_Not_Update_Path + Version_One + "\\" + Book_One + "\\" + "בראשית ח, כ - ברויאר.csv"
            Path_Two = Data_Set_Not_Update_Path + Version_Two + "\\" + Book_One + "\\" + "בראשית ח, כ - לנינגרד.csv"
            Path_Three = Data_Set_Not_Update_Path + Version_Three + "\\" + Book_One + "\\" + "בראשית ח, כ - קורן.csv"
            Path_Four = ""

            # Sheet #
            Name_Of_Sheet = "בראשית ח, כ"

            # Excel File #
            Name_Of_New_File = "בראשית ח, כ.xls"
            pass

        elif Main_Index == 4:
            # Path #
            Path_One = Data_Set_Not_Update_Path + Version_One + "\\" + Book_One + "\\" + "בראשית ט, כט - ברויאר.csv"
            Path_Two = Data_Set_Not_Update_Path + Version_Two + "\\" + Book_One + "\\" + "בראשית ט, כט - לנינגרד.csv"
            Path_Three = Data_Set_Not_Update_Path + Version_Three + "\\" + Book_One + "\\" + "בראשית ט, כט - קורן.csv"
            Path_Four = ""

            # Sheet #
            Name_Of_Sheet = "בראשית ט, כט"

            # Excel File #
            Name_Of_New_File = "בראשית ט, כט.xls"
            pass

        elif Main_Index == 5:
            # Path #
            Path_One = Data_Set_Not_Update_Path + Version_One + "\\" + Book_One + "\\" + "בראשית יג, ח - ברויאר.csv"
            Path_Two = Data_Set_Not_Update_Path + Version_Two + "\\" + Book_One + "\\" + "בראשית יג, ח - לנינגרד.csv"
            Path_Three = Data_Set_Not_Update_Path + Version_Three + "\\" + Book_One + \
                         "\\" + "בראשית יג, פסוקים - ג, ז, ח - קורן.csv"
            Path_Four = Data_Set_Not_Update_Path + Version_Four + "\\" + Book_One + \
                        "\\" + "בראשית יג, פסוקים - ג, ז, ח - תלמוד.csv"

            # Sheet #
            Name_Of_Sheet = "בראשית יג, פס' - ג, ז, ח"

            # Excel File #
            Name_Of_New_File = "בראשית יג, פסוקים - ג, ז, ח.xls"
            pass

        elif Main_Index == 6:
            # Path #
            Path_One = Data_Set_Not_Update_Path + Version_One + "\\" + Book_One + "\\" + "בראשית יד, כב - ברויאר.csv"
            Path_Two = Data_Set_Not_Update_Path + Version_Two + "\\" + Book_One + "\\" + "בראשית יד, כב - לנינגרד.csv"
            Path_Three = Data_Set_Not_Update_Path + Version_Three + "\\" + Book_One + "\\" + "בראשית יד, כב - קורן.csv"
            Path_Four = ""

            # Sheet #
            Name_Of_Sheet = "בראשית יד, כב"

            # Excel File #
            Name_Of_New_File = "בראשית יד, כב.xls"
            pass

        elif Main_Index == 7:
            # Path #
            Path_One = Data_Set_Not_Update_Path + Version_One + "\\" + Book_One + "\\" + "בראשית יט, טז - ברויאר.csv"
            Path_Two = Data_Set_Not_Update_Path + Version_Two + "\\" + Book_One + "\\" + "בראשית יט, טז - לנינגרד.csv"
            Path_Three = Data_Set_Not_Update_Path + Version_Three + "\\" + Book_One + "\\" + "בראשית יט, טז - קורן.csv"
            Path_Four = ""

            # Sheet #
            Name_Of_Sheet = "בראשית יט, טז"

            # Excel File #
            Name_Of_New_File = "בראשית יט, טז.xls"
            pass

        elif Main_Index == 8:
            # Path #
            Path_One = Data_Set_Not_Update_Path + Version_One + "\\" + Book_One + "\\" + "בראשית כה, ג - ברויאר.csv"
            Path_Two = Data_Set_Not_Update_Path + Version_Two + "\\" + Book_One + "\\" + "בראשית כה, ג - לנינגרד.csv"
            Path_Three = Data_Set_Not_Update_Path + Version_Three + "\\" + Book_One + \
                         "\\" + "בראשית כה, פסוקים - ג, ו, כג - קורן.csv"
            Path_Four = Data_Set_Not_Update_Path + Version_Four + "\\" + Book_One + \
                        "\\" + "בראשית כה, פסוקים - ג, ו, כג - תלמוד.csv"

            # Sheet #
            Name_Of_Sheet = "בראשית כה, פס' - ג, ו, כג"

            # Excel File #
            Name_Of_New_File = "בראשית כה, פסוקים - ג, ו, כג.xls"
            pass

        elif Main_Index == 9:
            # Path #
            Path_One = Data_Set_Not_Update_Path + Version_One + "\\" + Book_One + "\\" + "בראשית כו, ז - ברויאר.csv"
            Path_Two = Data_Set_Not_Update_Path + Version_Two + "\\" + Book_One + "\\" + "בראשית כו, ז - לנינגרד.csv"
            Path_Three = Data_Set_Not_Update_Path + Version_Three + "\\" + Book_One + "\\" + "בראשית כו, ז - קורן.csv"
            Path_Four = ""

            # Sheet #
            Name_Of_Sheet = "בראשית כו, ז"

            # Excel File #
            Name_Of_New_File = "בראשית כו, ז.xls"
            pass

        elif Main_Index == 10:
            # Path #
            Path_One = Data_Set_Not_Update_Path + Version_One + "\\" + Book_One + "\\" + "בראשית כז, לא - ברויאר.csv"
            Path_Two = Data_Set_Not_Update_Path + Version_Two + "\\" + Book_One + "\\" + "בראשית כז, לא - לנינגרד.csv"
            Path_Three = Data_Set_Not_Update_Path + Version_Three + "\\" + Book_One + "\\" + "בראשית כז, לא - קורן.csv"
            Path_Four = ""

            # Sheet #
            Name_Of_Sheet = "בראשית כז, לא"

            # Excel File #
            Name_Of_New_File = "בראשית כז, לא.xls"
            pass

        elif Main_Index == 11:
            # Path #
            Path_One = Data_Set_Not_Update_Path + Version_One + "\\" + Book_One + \
                       "\\" + "בראשית לה, פסוקים - ה, כג - ברויאר.csv"
            Path_Two = Data_Set_Not_Update_Path + Version_Two + "\\" + Book_One + \
                       "\\" + "בראשית לה, פסוקים - ה, כג - לנינגרד.csv"
            Path_Three = Data_Set_Not_Update_Path + Version_Three + "\\" + Book_One + \
                         "\\" + "בראשית לה, פסוקים - ה, כג - קורן.csv"
            Path_Four = ""

            # Sheet #
            Name_Of_Sheet = "בראשית לה, פס' - ה, כג"

            # Excel File #
            Name_Of_New_File = "בראשית לה, פסוקים - ה, כג.xls"
            pass

        elif Main_Index == 12:
            # Path #
            Path_One = Data_Set_Not_Update_Path + Version_One + "\\" + Book_One + "\\" + "בראשית מ, י - ברויאר.csv"
            Path_Two = Data_Set_Not_Update_Path + Version_Two + "\\" + Book_One + "\\" + "בראשית מ, י - לנינגרד.csv"
            Path_Three = Data_Set_Not_Update_Path + Version_Three + "\\" + Book_One + "\\" + "בראשית מ, י - קורן.csv"
            Path_Four = ""

            # Sheet #
            Name_Of_Sheet = "בראשית מ, י"

            # Excel File #
            Name_Of_New_File = "בראשית מ, י.xls"
            pass

        elif Main_Index == 13:
            # Path #
            Path_One = Data_Set_Not_Update_Path + Version_One + "\\" + Book_One + "\\" + "בראשית מא, לה - ברויאר.csv"
            Path_Two = Data_Set_Not_Update_Path + Version_Two + "\\" + Book_One + "\\" + "בראשית מא, לה - לנינגרד.csv"
            Path_Three = Data_Set_Not_Update_Path + Version_Three + "\\" + Book_One + "\\" + "בראשית מא, לה - קורן.csv"
            Path_Four = ""

            # Sheet #
            Name_Of_Sheet = "בראשית מא, לה"

            # Excel File #
            Name_Of_New_File = "בראשית מא, לה.xls"
            pass

        elif Main_Index == 14:
            # Path #
            Path_One = Data_Set_Not_Update_Path + Version_One + "\\" + Book_One + "\\" + "בראשית מב, ד - ברויאר.csv"
            Path_Two = Data_Set_Not_Update_Path + Version_Two + "\\" + Book_One + "\\" + "בראשית מב, ד - לנינגרד.csv"
            Path_Three = Data_Set_Not_Update_Path + Version_Three + "\\" + Book_One + "\\" + "בראשית מב, ד - קורן.csv"
            Path_Four = Data_Set_Not_Update_Path + Version_Four + "\\" + Book_One + "\\" + "בראשית מב, ד - תלמוד.csv"

            # Sheet #
            Name_Of_Sheet = "בראשית מב, ד"

            # Excel File #
            Name_Of_New_File = "בראשית מב, ד.xls"
            pass

        elif Main_Index == 15:
            # Path #
            Path_One = Data_Set_Not_Update_Path + Version_One + "\\" + Book_One + \
                       "\\" + "בראשית מג, פסוקים - יד, טז, כט - ברויאר.csv"
            Path_Two = Data_Set_Not_Update_Path + Version_Two + "\\" + Book_One + \
                       "\\" + "בראשית מג, פסוקים - יד, טז, כט - לנינגרד.csv"
            Path_Three = Data_Set_Not_Update_Path + Version_Three + "\\" + Book_One + \
                         "\\" + "בראשית מג, פסוקים - יד, טז, כט - קורן.csv"
            Path_Four = Data_Set_Not_Update_Path + Version_Four + "\\" + Book_One + \
                        "\\" + "בראשית מג, פסוקים - יד, טז, כט - תלמוד.csv"

            # Sheet #
            Name_Of_Sheet = "בראשית מג, פס' - יד, טז, כט"

            # Excel File #
            Name_Of_New_File = "בראשית מג, פסוקים - יד, טז, כט.xls"
            pass

        elif Main_Index == 16:
            # Path #
            Path_One = Data_Set_Not_Update_Path + Version_One + "\\" + Book_One + "\\" + "בראשית מה, טו - ברויאר.csv"
            Path_Two = Data_Set_Not_Update_Path + Version_Two + "\\" + Book_One + "\\" + "בראשית מה, טו - לנינגרד.csv"
            Path_Three = Data_Set_Not_Update_Path + Version_Three + "\\" + Book_One + \
                         "\\" + "בראשית מה, פסוקים - יב, טו - קורן.csv"
            Path_Four = Data_Set_Not_Update_Path + Version_Four + "\\" + Book_One + \
                        "\\" + "בראשית מה, פסוקים - יב, טו - תלמוד.csv"

            # Sheet #
            Name_Of_Sheet = "בראשית מה, פס' - יב, טו"

            # Excel File #
            Name_Of_New_File = "בראשית מה, פסוקים - יב, טו.xls"
            pass

        elif Main_Index == 17:
            # Path #
            Path_One = Data_Set_Not_Update_Path + Version_One + "\\" + Book_One + \
                       "\\" + "בראשית מו, פסוקים - ט, יב, יג, יד - ברויאר.csv"
            Path_Two = Data_Set_Not_Update_Path + Version_Two + "\\" + Book_One + \
                       "\\" + "בראשית מו, פסוקים - ט, יב, יג, יד - לנינגרד.csv"
            Path_Three = Data_Set_Not_Update_Path + Version_Three + "\\" + Book_One + \
                         "\\" + "בראשית מו, פסוקים - ט, יב, יג, יד - קורן.csv"
            Path_Four = ""

            # Sheet #
            Name_Of_Sheet = "בראשית מו, פס' - ט, יב, יג, יד"

            # Excel File #
            Name_Of_New_File = "בראשית מו, פסוקים - ט, יב, יג, יד.xls"
            pass

        elif Main_Index == 18:
            # Path #
            Path_One = Data_Set_Not_Update_Path + Version_One + "\\" + Book_One + "\\" + "בראשית מט, יג - ברויאר.csv"
            Path_Two = Data_Set_Not_Update_Path + Version_Two + "\\" + Book_One + "\\" + "בראשית מט, יג - לנינגרד.csv"
            Path_Three = Data_Set_Not_Update_Path + Version_Three + "\\" + Book_One + \
                         "\\" + "בראשית מט, פסוקים - יא, יג, כז - קורן.csv"
            Path_Four = Data_Set_Not_Update_Path + Version_Four + "\\" + Book_One + \
                        "\\" + "בראשית מט, פסוקים - יא, יג, כז - תלמוד.csv"

            # Sheet #
            Name_Of_Sheet = "בראשית מט, פס' - יא, יג, כז"

            # Excel File #
            Name_Of_New_File = "בראשית מט, פסוקים - יא, יג, כז.xls"
            pass

        # Chapter - שמות #
        elif Main_Index == 19:
            # Path #
            Path_One = Data_Set_Not_Update_Path + Version_One + "\\" + Book_Two + "\\" + "שמות א, טז - ברויאר.csv"
            Path_Two = Data_Set_Not_Update_Path + Version_Two + "\\" + Book_Two + "\\" + "שמות א, טז - לנינגרד.csv"
            Path_Three = Data_Set_Not_Update_Path + Version_Three + "\\" + Book_Two + "\\" + "שמות א, טז - קורן.csv"
            Path_Four = ""

            # Sheet #
            Name_Of_Sheet = "שמות א, טז"

            # Excel File #
            Name_Of_New_File = "שמות א, טז.xls"
            pass

        elif Main_Index == 20:
            # Path #
            Path_One = Data_Set_Not_Update_Path + Version_One + "\\" + Book_Two + "\\" + "שמות ד, ג - ברויאר.csv"
            Path_Two = Data_Set_Not_Update_Path + Version_Two + "\\" + Book_Two + "\\" + "שמות ד, ג - לנינגרד.csv"
            Path_Three = Data_Set_Not_Update_Path + Version_Three + "\\" + Book_Two + "\\" + "שמות ד, ג - קורן.csv"
            Path_Four = ""

            # Sheet #
            Name_Of_Sheet = "שמות ד, ג"

            # Excel File #
            Name_Of_New_File = "שמות ד, ג.xls"
            pass

        elif Main_Index == 21:
            # Path #
            Path_One = Data_Set_Not_Update_Path + Version_One + "\\" + Book_Two + "\\" + "שמות ו, יד - ברויאר.csv"
            Path_Two = Data_Set_Not_Update_Path + Version_Two + "\\" + Book_Two + "\\" + "שמות ו, יד - לנינגרד.csv"
            Path_Three = Data_Set_Not_Update_Path + Version_Three + "\\" + Book_Two + \
                         "\\" + "שמות ו, פסוקים - יד , כה - קורן.csv"
            Path_Four = Data_Set_Not_Update_Path + Version_Four + "\\" + Book_Two + \
                        "\\" + "שמות ו, פסוקים - יד , כה - תלמוד.csv"

            # Sheet #
            Name_Of_Sheet = "שמות ו, פס' - יד, כה"

            # Excel File #
            Name_Of_New_File = "שמות ו, פסוקים - יד, כה.xls"
            pass

        elif Main_Index == 22:
            # Path #
            Path_One = Data_Set_Not_Update_Path + Version_One + "\\" + Book_Two + "\\" + "שמות ח, טו - ברויאר.csv"
            Path_Two = Data_Set_Not_Update_Path + Version_Two + "\\" + Book_Two + "\\" + "שמות ח, טו - לנינגרד.csv"
            Path_Three = Data_Set_Not_Update_Path + Version_Three + "\\" + Book_Two + "\\" + "שמות ח, טו - קורן.csv"
            Path_Four = ""

            # Sheet #
            Name_Of_Sheet = "שמות ח, טו"

            # Excel File #
            Name_Of_New_File = "שמות ח, טו.xls"
            pass

        elif Main_Index == 23:
            # Path #
            Path_One = Data_Set_Not_Update_Path + Version_One + "\\" + Book_Two + "\\" + "שמות טו, יא - ברויאר.csv"
            Path_Two = Data_Set_Not_Update_Path + Version_Two + "\\" + Book_Two + "\\" + "שמות טו, יא - לנינגרד.csv"
            Path_Three = Data_Set_Not_Update_Path + Version_Three + "\\" + Book_Two + "\\" + "שמות טו, יא - קורן.csv"
            Path_Four = Data_Set_Not_Update_Path + Version_Four + "\\" + Book_Two + "\\" + "שמות טו, יא - תלמוד.csv"

            # Sheet #
            Name_Of_Sheet = "שמות טו, יא"

            # Excel File #
            Name_Of_New_File = "שמות טו, יא.xls"
            pass

        elif Main_Index == 24:
            # Path #
            Path_One = Data_Set_Not_Update_Path + Version_One + "\\" + Book_Two + "\\" + "שמות י, כה - ברויאר.csv"
            Path_Two = Data_Set_Not_Update_Path + Version_Two + "\\" + Book_Two + "\\" + "שמות י, כה - לנינגרד.csv"
            Path_Three = Data_Set_Not_Update_Path + Version_Three + "\\" + Book_Two + "\\" + "שמות י, כה - קורן.csv"
            Path_Four = ""

            # Sheet #
            Name_Of_Sheet = "שמות י, כה"

            # Excel File #
            Name_Of_New_File = "שמות י, כה.xls"
            pass

        elif Main_Index == 25:
            # Path #
            Path_One = Data_Set_Not_Update_Path + Version_One + "\\" + Book_Two + "\\" + "שמות יב, ד - ברויאר.csv"
            Path_Two = Data_Set_Not_Update_Path + Version_Two + "\\" + Book_Two + "\\" + "שמות יב, ד - לנינגרד.csv"
            Path_Three = Data_Set_Not_Update_Path + Version_Three + "\\" + Book_Two + "\\" + "שמות יב, ד - קורן.csv"
            Path_Four = ""

            # Sheet #
            Name_Of_Sheet = "שמות יב, ד"

            # Excel File #
            Name_Of_New_File = "שמות יב, ד.xls"
            pass

        elif Main_Index == 26:
            # Path #
            Path_One = Data_Set_Not_Update_Path + Version_One + "\\" + Book_Two + \
                       "\\" + "שמות יד, פסוקים - יג , יד , כב - ברויאר.csv"
            Path_Two = Data_Set_Not_Update_Path + Version_Two + "\\" + Book_Two + \
                       "\\" + "שמות יד, פסוקים - יג , יד , כב - לנינגרד.csv"
            Path_Three = Data_Set_Not_Update_Path + Version_Three + "\\" + Book_Two + \
                         "\\" + "שמות יד, פסוקים - ז , יג , יד , כב - קורן.csv"
            Path_Four = Data_Set_Not_Update_Path + Version_Four + "\\" + Book_Two + \
                        "\\" + "שמות יד, פסוקים - ז , יג , יד , כב - תלמוד.csv"

            # Sheet #
            Name_Of_Sheet = "שמות יד, פס' - ז, יג, יד, כב"

            # Excel File #
            Name_Of_New_File = "שמות יד, פסוקים - ז, יג, יד, כב.xls"
            pass

        elif Main_Index == 27:
            # Path #
            Path_One = Data_Set_Not_Update_Path + Version_One + "\\" + Book_Two + \
                       "\\" + "שמות יט, פסוקים - יא , יט - ברויאר.csv"
            Path_Two = Data_Set_Not_Update_Path + Version_Two + "\\" + Book_Two + \
                       "\\" + "שמות יט, פסוקים - יא , יט - לנינגרד.csv"
            Path_Three = Data_Set_Not_Update_Path + Version_Three + "\\" + Book_Two + \
                         "\\" + "שמות יט, פסוקים - יא , יט - קורן.csv"
            Path_Four = ""

            # Sheet #
            Name_Of_Sheet = "שמות יט, פס' - יא, יט"

            # Excel File #
            Name_Of_New_File = "שמות יט, פסוקים - יא , יט.xls"
            pass

        elif Main_Index == 28:
            # Path #
            Path_One = Data_Set_Not_Update_Path + Version_One + "\\" + Book_Two + "\\" + "שמות כ, ב - ברויאר.csv"
            Path_Two = Data_Set_Not_Update_Path + Version_Two + "\\" + Book_Two + "\\" + "שמות כ, ב - לנינגרד.csv"
            Path_Three = Data_Set_Not_Update_Path + Version_Three + "\\" + Book_Two + "\\" + "שמות כ, ב - קורן.csv"
            Path_Four = Data_Set_Not_Update_Path + Version_Four + "\\" + Book_Two + "\\" + "שמות כ, ב - תלמוד.csv"

            # Sheet #
            Name_Of_Sheet = "שמות כ, ב"

            # Excel File #
            Name_Of_New_File = "שמות כ, ב.xls"
            pass

        elif Main_Index == 29:
            # Path #
            Path_One = Data_Set_Not_Update_Path + Version_One + "\\" + Book_Two + "\\" + "שמות כג, כב - ברויאר.csv"
            Path_Two = Data_Set_Not_Update_Path + Version_Two + "\\" + Book_Two + "\\" + "שמות כג, כב - לנינגרד.csv"
            Path_Three = Data_Set_Not_Update_Path + Version_Three + "\\" + Book_Two + \
                         "\\" + "שמות כג, פסוקים - טו , כב - קורן.csv"
            Path_Four = Data_Set_Not_Update_Path + Version_Four + "\\" + Book_Two + \
                        "\\" + "שמות כג, פסוקים - טו , כב - תלמוד.csv"

            # Sheet #
            Name_Of_Sheet = "שמות כג, פס' - טו, כב"

            # Excel File #
            Name_Of_New_File = "שמות כג, פסוקים - טו, כב.xls"
            pass

        elif Main_Index == 30:
            # Path #
            Path_One = Data_Set_Not_Update_Path + Version_One + "\\" + Book_Two + \
                       "\\" + "שמות כה, פסוקים - כב , לא - ברויאר.csv"
            Path_Two = Data_Set_Not_Update_Path + Version_Two + "\\" + Book_Two + \
                       "\\" + "שמות כה, פסוקים - כב , לא - לנינגרד.csv"
            Path_Three = Data_Set_Not_Update_Path + Version_Three + "\\" + Book_Two + \
                         "\\" + "שמות כה, פסוקים - כב , לא - קורן.csv"
            Path_Four = Data_Set_Not_Update_Path + Version_Four + "\\" + Book_Two + "\\" + "שמות כה, כב - תלמוד.csv"

            # Sheet #
            Name_Of_Sheet = "שמות כה, פס' - כב, לא"

            # Excel File #
            Name_Of_New_File = "שמות כה, פסוקים - כב, לא.xls"
            pass

        elif Main_Index == 31:
            # Path #
            Path_One = Data_Set_Not_Update_Path + Version_One + "\\" + Book_Two + "\\" + "שמות כו, כד - ברויאר.csv"
            Path_Two = Data_Set_Not_Update_Path + Version_Two + "\\" + Book_Two + "\\" + "שמות כו, כד - לנינגרד.csv"
            Path_Three = Data_Set_Not_Update_Path + Version_Three + "\\" + Book_Two + \
                         "\\" + "שמות כו, פסוקים - כד , לג , לד - קורן.csv"
            Path_Four = Data_Set_Not_Update_Path + Version_Four + "\\" + Book_Two + \
                        "\\" + "שמות כו, פסוקים - כד , לג , לד - תלמוד.csv"

            # Sheet #
            Name_Of_Sheet = "שמות כו, פס' - כד, לג, לד"

            # Excel File #
            Name_Of_New_File = "שמות כו, פסוקים - כד, לג, לד.xls"
            pass

        elif Main_Index == 32:
            # Path #
            Path_One = Data_Set_Not_Update_Path + Version_One + "\\" + Book_Two + \
                       "\\" + "שמות כח, פסוקים - כו , כח - ברויאר.csv"
            Path_Two = Data_Set_Not_Update_Path + Version_Two + "\\" + Book_Two + \
                       "\\" + "שמות כח, פסוקים - כו , כח - לנינגרד.csv"
            Path_Three = Data_Set_Not_Update_Path + Version_Three + "\\" + Book_Two + \
                         "\\" + "שמות כח, פסוקים - כו , כח - קורן.csv"
            Path_Four = ""

            # Sheet #
            Name_Of_Sheet = "שמות כח, פס' - כו, כח"

            # Excel File #
            Name_Of_New_File = "שמות כח, פסוקים - כו, כח.xls"
            pass

        elif Main_Index == 33:
            # Path #
            Path_One = Data_Set_Not_Update_Path + Version_One + "\\" + Book_Two + \
                       "\\" + "שמות כט, פסוקים - כב , מ - ברויאר.csv"
            Path_Two = Data_Set_Not_Update_Path + Version_Two + "\\" + Book_Two + \
                       "\\" + "שמות כט, פסוקים - כב , מ - לנינגרד.csv"
            Path_Three = Data_Set_Not_Update_Path + Version_Three + "\\" + Book_Two + \
                         "\\" + "שמות כט, פסוקים - כב , מ - קורן.csv"
            Path_Four = ""

            # Sheet #
            Name_Of_Sheet = "שמות כט, פס' - כב, מ"

            # Excel File #
            Name_Of_New_File = "שמות כט, פסוקים - כב, מ.xls"
            pass

        elif Main_Index == 34:
            # Path #
            Path_One = Data_Set_Not_Update_Path + Version_One + "\\" + Book_Two + "\\" + "שמות ל, כו - ברויאר.csv"
            Path_Two = Data_Set_Not_Update_Path + Version_Two + "\\" + Book_Two + "\\" + "שמות ל, כו - לנינגרד.csv"
            Path_Three = Data_Set_Not_Update_Path + Version_Three + "\\" + Book_Two + "\\" + "שמות ל, כו - קורן.csv"
            Path_Four = Data_Set_Not_Update_Path + Version_Four + "\\" + Book_Two + "\\" + "שמות ל, כו - תלמוד.csv"

            # Sheet #
            Name_Of_Sheet = "שמות ל, כו"

            # Excel File #
            Name_Of_New_File = "שמות ל, כו.xls"
            pass

        elif Main_Index == 35:
            # Path #
            Path_One = Data_Set_Not_Update_Path + Version_One + "\\" + Book_Two + "\\" + "שמות לב, לד - ברויאר.csv"
            Path_Two = Data_Set_Not_Update_Path + Version_Two + "\\" + Book_Two + "\\" + "שמות לב, לד - לנינגרד.csv"
            Path_Three = Data_Set_Not_Update_Path + Version_Three + "\\" + Book_Two + "\\" + "שמות לב, לד - קורן.csv"
            Path_Four = ""

            # Sheet #
            Name_Of_Sheet = "שמות לב, לד"

            # Excel File #
            Name_Of_New_File = "שמות לב, לד.xls"
            pass

        elif Main_Index == 36:
            # Path #
            Path_One = Data_Set_Not_Update_Path + Version_One + "\\" + Book_Two + "\\" + "שמות לד, כד - ברויאר.csv"
            Path_Two = Data_Set_Not_Update_Path + Version_Two + "\\" + Book_Two + "\\" + "שמות לד, כד - לנינגרד.csv"
            Path_Three = Data_Set_Not_Update_Path + Version_Three + "\\" + Book_Two + "\\" + "שמות לד, כד - קורן.csv"
            Path_Four = ""

            # Sheet #
            Name_Of_Sheet = "שמות לד, כד"

            # Excel File #
            Name_Of_New_File = "שמות לד, כד.xls"
            pass

        elif Main_Index == 37:
            # Path #
            Path_One = Data_Set_Not_Update_Path + Version_One + "\\" + Book_Two + "\\" + "שמות לו, יג - ברויאר.csv"
            Path_Two = Data_Set_Not_Update_Path + Version_Two + "\\" + Book_Two + "\\" + "שמות לו, יג - לנינגרד.csv"
            Path_Three = Data_Set_Not_Update_Path + Version_Three + "\\" + Book_Two + "\\" + "שמות לו, יג - קורן.csv"
            Path_Four = ""

            # Sheet #
            Name_Of_Sheet = "שמות לו, יג"

            # Excel File #
            Name_Of_New_File = "שמות לו, יג.xls"
            pass

        elif Main_Index == 38:
            # Path #
            Path_One = Data_Set_Not_Update_Path + Version_One + "\\" + Book_Two + "\\" + "שמות לז, ג - ברויאר.csv"
            Path_Two = Data_Set_Not_Update_Path + Version_Two + "\\" + Book_Two + "\\" + "שמות לז, ג - לנינגרד.csv"
            Path_Three = Data_Set_Not_Update_Path + Version_Three + "\\" + Book_Two + "\\" + "שמות לז, ג - קורן.csv"
            Path_Four = ""

            # Sheet #
            Name_Of_Sheet = "שמות לז, ג"

            # Excel File #
            Name_Of_New_File = "שמות לז, ג.xls"
            pass

        elif Main_Index == 39:
            # Path #
            Path_One = Data_Set_Not_Update_Path + Version_One + "\\" + Book_Two + "\\" + "שמות לח, י - ברויאר.csv"
            Path_Two = Data_Set_Not_Update_Path + Version_Two + "\\" + Book_Two + "\\" + "שמות לח, י - לנינגרד.csv"
            Path_Three = Data_Set_Not_Update_Path + Version_Three + "\\" + Book_Two + "\\" + "שמות לח, י - קורן.csv"
            Path_Four = ""

            # Sheet #
            Name_Of_Sheet = "שמות לח, י"

            # Excel File #
            Name_Of_New_File = "שמות לח, י.xls"
            pass

        elif Main_Index == 40:
            # Path #
            Path_One = Data_Set_Not_Update_Path + Version_One + "\\" + Book_Two + \
                       "\\" + "שמות לט, פסוקים - יג , לה - ברויאר.csv"
            Path_Two = Data_Set_Not_Update_Path + Version_Two + "\\" + Book_Two + \
                       "\\" + "שמות לט, פסוקים - יג , לה - לנינגרד.csv"
            Path_Three = Data_Set_Not_Update_Path + Version_Three + "\\" + Book_Two + \
                         "\\" + "שמות לט, פסוקים - יג , לה - קורן.csv"
            Path_Four = ""

            # Sheet #
            Name_Of_Sheet = "שמות לט, פס' - יג, לה"

            # Excel File #
            Name_Of_New_File = "שמות לט, פסוקים - יג, לה.xls"
            pass

        elif Main_Index == 41:
            # Path #
            Path_One = Data_Set_Not_Update_Path + Version_One + "\\" + Book_Two + \
                       "\\" + "שמות מ, פסוקים - ג , ה , כא - ברויאר.csv"
            Path_Two = Data_Set_Not_Update_Path + Version_Two + "\\" + Book_Two + \
                       "\\" + "שמות מ, פסוקים - ג , ה , כא - לנינגרד.csv"
            Path_Three = Data_Set_Not_Update_Path + Version_Three + "\\" + Book_Two + \
                         "\\" + "שמות מ, פסוקים - ג , ה , כא - קורן.csv"
            Path_Four = Data_Set_Not_Update_Path + Version_Four + "\\" + Book_Two + \
                        "\\" + "שמות מ, פסוקים - ג , ה , כא - תלמוד.csv"

            # Sheet #
            Name_Of_Sheet = "שמות מ, פס' - ג, ה, כא"

            # Excel File #
            Name_Of_New_File = "שמות מ, פסוקים - ג, ה, כא.xls"
            pass

        # Chapter - ויקרא #
        elif Main_Index == 42:
            # Path #
            Path_One = Data_Set_Not_Update_Path + Version_One + "\\" + Book_Three + "\\" + "ויקרא ד, לד - ברויאר.csv"
            Path_Two = Data_Set_Not_Update_Path + Version_Two + "\\" + Book_Three + "\\" + "ויקרא ד, לד - לנינגרד.csv"
            Path_Three = Data_Set_Not_Update_Path + Version_Three + "\\" + Book_Three + "\\" + "ויקרא ד, לד - קורן.csv"
            Path_Four = Data_Set_Not_Update_Path + Version_Four + "\\" + Book_Three + "\\" + "ויקרא ד, לד - תלמוד.csv"

            # Sheet #
            Name_Of_Sheet = "ויקרא ד, לד"

            # Excel File #
            Name_Of_New_File = "ויקרא ד, לד.xls"
            pass

        elif Main_Index == 43:
            # Path #
            Path_One = Data_Set_Not_Update_Path + Version_One + "\\" + Book_Three + "\\" + "ויקרא ה, יא - ברויאר.csv"
            Path_Two = Data_Set_Not_Update_Path + Version_Two + "\\" + Book_Three + "\\" + "ויקרא ה, יא - לנינגרד.csv"
            Path_Three = Data_Set_Not_Update_Path + Version_Three + "\\" + Book_Three + "\\" + "ויקרא ה, יא - קורן.csv"
            Path_Four = ""

            # Sheet #
            Name_Of_Sheet = "ויקרא ה, יא"

            # Excel File #
            Name_Of_New_File = "ויקרא ה, יא.xls"
            pass

        elif Main_Index == 44:
            # Path #
            Path_One = Data_Set_Not_Update_Path + Version_One + "\\" + Book_Three + "\\" + "ויקרא ז, יב - ברויאר.csv"
            Path_Two = Data_Set_Not_Update_Path + Version_Two + "\\" + Book_Three + "\\" + "ויקרא ז, יב - לנינגרד.csv"
            Path_Three = Data_Set_Not_Update_Path + Version_Three + "\\" + Book_Three + "\\" + "ויקרא ז, יב - קורן.csv"
            Path_Four = Data_Set_Not_Update_Path + Version_Four + "\\" + Book_Three + "\\" + "ויקרא ז, יב - תלמוד.csv"

            # Sheet #
            Name_Of_Sheet = "ויקרא ז, יב"

            # Excel File #
            Name_Of_New_File = "ויקרא ז, יב.xls"
            pass

        elif Main_Index == 45:
            # Path #
            Path_One = Data_Set_Not_Update_Path + Version_One + "\\" + Book_Three + "\\" + "ויקרא טו, י - ברויאר.csv"
            Path_Two = Data_Set_Not_Update_Path + Version_Two + "\\" + Book_Three + "\\" + "ויקרא טו, י - לנינגרד.csv"
            Path_Three = Data_Set_Not_Update_Path + Version_Three + "\\" + Book_Three + "\\" + "ויקרא טו, י - קורן.csv"
            Path_Four = Data_Set_Not_Update_Path + Version_Four + "\\" + Book_Three + "\\" + "ויקרא טו, י - תלמוד.csv"

            # Sheet #
            Name_Of_Sheet = "ויקרא טו, י"

            # Excel File #
            Name_Of_New_File = "ויקרא טו, י.xls"
            pass

        elif Main_Index == 46:
            # Path #
            Path_One = Data_Set_Not_Update_Path + Version_One + "\\" + Book_Three + "\\" + "ויקרא טז, ח - ברויאר.csv"
            Path_Two = Data_Set_Not_Update_Path + Version_Two + "\\" + Book_Three + "\\" + "ויקרא טז, ח - לנינגרד.csv"
            Path_Three = Data_Set_Not_Update_Path + Version_Three + "\\" + Book_Three + "\\" + "ויקרא טז, ח - קורן.csv"
            Path_Four = ""

            # Sheet #
            Name_Of_Sheet = "ויקרא טז, ח"

            # Excel File #
            Name_Of_New_File = "ויקרא טז, ח.xls"
            pass

        elif Main_Index == 47:
            # Path #
            Path_One = Data_Set_Not_Update_Path + Version_One + "\\" + Book_Three + \
                       "\\" + "ויקרא י, פסוקים - א , יג - ברויאר.csv"
            Path_Two = Data_Set_Not_Update_Path + Version_Two + "\\" + Book_Three + \
                       "\\" + "ויקרא י, פסוקים - א , יג - לנינגרד.csv"
            Path_Three = Data_Set_Not_Update_Path + Version_Three + "\\" + Book_Three + \
                         "\\" + "ויקרא י, פסוקים - א , יג - קורן.csv"
            Path_Four = ""

            # Sheet #
            Name_Of_Sheet = "ויקרא י, פס' - א, יג"

            # Excel File #
            Name_Of_New_File = "ויקרא י, פסוקים - א, יג.xls"
            pass

        elif Main_Index == 48:
            # Path #
            Path_One = Data_Set_Not_Update_Path + Version_One + "\\" + Book_Three + "\\" + "ויקרא יא, ד - ברויאר.csv"
            Path_Two = Data_Set_Not_Update_Path + Version_Two + "\\" + Book_Three + "\\" + "ויקרא יא, ד - לנינגרד.csv"
            Path_Three = Data_Set_Not_Update_Path + Version_Three + "\\" + Book_Three + "\\" + "ויקרא יא, ד - קורן.csv"
            Path_Four = ""

            # Sheet #
            Name_Of_Sheet = "ויקרא יא, ד"

            # Excel File #
            Name_Of_New_File = "ויקרא יא, ד.xls"
            pass

        elif Main_Index == 49:
            # Path #
            Path_One = Data_Set_Not_Update_Path + Version_One + "\\" + Book_Three + "\\" + "ויקרא יג, ו - ברויאר.csv"
            Path_Two = Data_Set_Not_Update_Path + Version_Two + "\\" + Book_Three + "\\" + "ויקרא יג, ו - לנינגרד.csv"
            Path_Three = Data_Set_Not_Update_Path + Version_Three + "\\" + Book_Three + "\\" + "ויקרא יג, ו - קורן.csv"
            Path_Four = ""

            # Sheet #
            Name_Of_Sheet = "ויקרא יג, ו"

            # Excel File #
            Name_Of_New_File = "ויקרא יג, ו.xls"
            pass

        elif Main_Index == 50:
            # Path #
            Path_One = Data_Set_Not_Update_Path + Version_One + "\\" + Book_Three + "\\" + "ויקרא יד, י - ברויאר.csv"
            Path_Two = Data_Set_Not_Update_Path + Version_Two + "\\" + Book_Three + "\\" + "ויקרא יד, י - לנינגרד.csv"
            Path_Three = Data_Set_Not_Update_Path + Version_Three + "\\" + Book_Three + "\\" + "ויקרא יד, י - קורן.csv"
            Path_Four = ""

            # Sheet #
            Name_Of_Sheet = "ויקרא יד, י"

            # Excel File #
            Name_Of_New_File = "ויקרא יד, י.xls"
            pass

        elif Main_Index == 51:
            # Path #
            Path_One = Data_Set_Not_Update_Path + Version_One + "\\" + Book_Three + "\\" + "ויקרא יח, כט - ברויאר.csv"
            Path_Two = Data_Set_Not_Update_Path + Version_Two + "\\" + Book_Three + "\\" + "ויקרא יח, כט - לנינגרד.csv"
            Path_Three = Data_Set_Not_Update_Path + Version_Three + "\\" + Book_Three + "\\" + "ויקרא יח, כט - קורן.csv"
            Path_Four = ""

            # Sheet #
            Name_Of_Sheet = "ויקרא יח, כט"

            # Excel File #
            Name_Of_New_File = "ויקרא יח, כט.xls"
            pass

        elif Main_Index == 52:
            # Path #
            Path_One = Data_Set_Not_Update_Path + Version_One + "\\" + Book_Three + "\\" + "ויקרא יט, ד - ברויאר.csv"
            Path_Two = Data_Set_Not_Update_Path + Version_Two + "\\" + Book_Three + "\\" + "ויקרא יט, ד - לנינגרד.csv"
            Path_Three = Data_Set_Not_Update_Path + Version_Three + "\\" + Book_Three + "\\" + "ויקרא יט, ד - קורן.csv"
            Path_Four = ""

            # Sheet #
            Name_Of_Sheet = "ויקרא יט, ד"

            # Excel File #
            Name_Of_New_File = "ויקרא יט, ד.xls"
            pass

        elif Main_Index == 53:
            # Path #
            Path_One = Data_Set_Not_Update_Path + Version_One + "\\" + Book_Three + "\\" + "ויקרא כ, יח - ברויאר.csv"
            Path_Two = Data_Set_Not_Update_Path + Version_Two + "\\" + Book_Three + "\\" + "ויקרא כ, יח - לנינגרד.csv"
            Path_Three = Data_Set_Not_Update_Path + Version_Three + "\\" + Book_Three + "\\" + "ויקרא כ, יח - קורן.csv"
            Path_Four = ""

            # Sheet #
            Name_Of_Sheet = "ויקרא כ, יח"

            # Excel File #
            Name_Of_New_File = "ויקרא כ, יח.xls"
            pass

        elif Main_Index == 54:
            # Path #
            Path_One = Data_Set_Not_Update_Path + Version_One + "\\" + Book_Three + \
                       "\\" + "ויקרא כג, פסוקים - כ , לח - ברויאר.csv"
            Path_Two = Data_Set_Not_Update_Path + Version_Two + "\\" + Book_Three + \
                       "\\" + "ויקרא כג, פסוקים - כ , לח - לנינגרד.csv"
            Path_Three = Data_Set_Not_Update_Path + Version_Three + "\\" + Book_Three + \
                         "\\" + "ויקרא כג, פסוקים - כ , לח - קורן.csv"
            Path_Four = ""

            # Sheet #
            Name_Of_Sheet = "ויקרא כג, פס' - כ, לח"

            # Excel File #
            Name_Of_New_File = "ויקרא כג, פסוקים - כ, לח.xls"
            pass

        elif Main_Index == 55:
            # Path #
            Path_One = Data_Set_Not_Update_Path + Version_One + "\\" + Book_Three + "\\" + "ויקרא כה, ל - ברויאר.csv"
            Path_Two = Data_Set_Not_Update_Path + Version_Two + "\\" + Book_Three + "\\" + "ויקרא כה, ל - לנינגרד.csv"
            Path_Three = Data_Set_Not_Update_Path + Version_Three + "\\" + Book_Three + "\\" + "ויקרא כה, ל - קורן.csv"
            Path_Four = Data_Set_Not_Update_Path + Version_Four + "\\" + Book_Three + "\\" + "ויקרא כה, ל - תלמוד.csv"

            # Sheet #
            Name_Of_Sheet = "ויקרא כה, ל"

            # Excel File #
            Name_Of_New_File = "ויקרא כה, ל.xls"
            pass

        elif Main_Index == 56:
            # Path #
            Path_One = Data_Set_Not_Update_Path + Version_One + "\\" + Book_Three + "\\" + "ויקרא כו, מה - ברויאר.csv"
            Path_Two = Data_Set_Not_Update_Path + Version_Two + "\\" + Book_Three + "\\" + "ויקרא כו, מה - לנינגרד.csv"
            Path_Three = Data_Set_Not_Update_Path + Version_Three + "\\" + Book_Three + "\\" + "ויקרא כו, מה - קורן.csv"
            Path_Four = ""

            # Sheet #
            Name_Of_Sheet = "ויקרא כו, מה"

            # Excel File #
            Name_Of_New_File = "ויקרא כו, מה.xls"
            pass

        # Chapter - במדבר #
        elif Main_Index == 57:
            # Path #
            Path_One = Data_Set_Not_Update_Path + Version_One + "\\" + Book_Four + "\\" + "במדבר א, יז - ברויאר.csv"
            Path_Two = Data_Set_Not_Update_Path + Version_Two + "\\" + Book_Four + "\\" + "במדבר א, יז - לנינגרד.csv"
            Path_Three = Data_Set_Not_Update_Path + Version_Three + "\\" + Book_Four + "\\" + "במדבר א, יז - קורן.csv"
            Path_Four = ""

            # Sheet #
            Name_Of_Sheet = "במדבר א, יז"

            # Excel File #
            Name_Of_New_File = "במדבר א, יז.xls"
            pass

        elif Main_Index == 58:
            # Path #
            Path_One = Data_Set_Not_Update_Path + Version_One + "\\" + Book_Four + \
                       "\\" + "במדבר ג, פסוקים - ב , מב , מג - ברויאר.csv"
            Path_Two = Data_Set_Not_Update_Path + Version_Two + "\\" + Book_Four + \
                       "\\" + "במדבר ג, פסוקים - ב , מב , מג - לנינגרד.csv"
            Path_Three = Data_Set_Not_Update_Path + Version_Three + "\\" + Book_Four + \
                         "\\" + "במדבר ג, פסוקים - ב , מב , מג - קורן.csv"
            Path_Four = ""

            # Sheet #
            Name_Of_Sheet = "במדבר ג, פס' - ב, מב, מג"

            # Excel File #
            Name_Of_New_File = "במדבר ג, פסוקים - ב, מב, מג.xls"
            pass

        elif Main_Index == 59:
            # Path #
            Path_One = Data_Set_Not_Update_Path + Version_One + "\\" + Book_Four + \
                       "\\" + "במדבר ז, פסוקים - ז , כג - ברויאר.csv"
            Path_Two = Data_Set_Not_Update_Path + Version_Two + "\\" + Book_Four + \
                       "\\" + "במדבר ז, פסוקים - ז , כג - לנינגרד.csv"
            Path_Three = Data_Set_Not_Update_Path + Version_Three + "\\" + Book_Four + \
                         "\\" + "במדבר ז, פסוקים - א , ז , כג - קורן.csv"
            Path_Four = Data_Set_Not_Update_Path + Version_Four + "\\" + Book_Four + \
                        "\\" + "במדבר ז, פסוקים - א , ז , כג - תלמוד.csv"

            # Sheet #
            Name_Of_Sheet = "במדבר ז, פס' - א, ז, כג"

            # Excel File #
            Name_Of_New_File = "במדבר ז, פסוקים - א, ז, כג.xls"
            pass

        elif Main_Index == 60:
            # Path #
            Path_One = Data_Set_Not_Update_Path + Version_One + "\\" + Book_Four + \
                       "\\" + "במדבר ט, פסוקים - ג , ז , יז - ברויאר.csv"
            Path_Two = Data_Set_Not_Update_Path + Version_Two + "\\" + Book_Four + \
                       "\\" + "במדבר ט, פסוקים - ג , ז , יז - לנינגרד.csv"
            Path_Three = Data_Set_Not_Update_Path + Version_Three + "\\" + Book_Four + \
                         "\\" + "במדבר ט, פסוקים - ג , ז , יא , יז - קורן.csv"
            Path_Four = Data_Set_Not_Update_Path + Version_Four + "\\" + Book_Four + \
                        "\\" + "במדבר ט, פסוקים - ג , ז , יא , יז - תלמוד.csv"

            # Sheet #
            Name_Of_Sheet = "במדבר ט, פס' - ג, ז, יא, יז"

            # Excel File #
            Name_Of_New_File = "במדבר ט, פסוקים - ג, ז, יא, יז.xls"
            pass

        elif Main_Index == 61:
            # Path #
            Path_One = Data_Set_Not_Update_Path + Version_One + "\\" + Book_Four + "\\" + "במדבר טו, לט - ברויאר.csv"
            Path_Two = Data_Set_Not_Update_Path + Version_Two + "\\" + Book_Four + "\\" + "במדבר טו, לט - לנינגרד.csv"
            Path_Three = Data_Set_Not_Update_Path + Version_Three + "\\" + Book_Four + \
                         "\\" + "במדבר טו, פסוקים - לח , לט - קורן.csv"
            Path_Four = Data_Set_Not_Update_Path + Version_Four + "\\" + Book_Four + \
                        "\\" + "במדבר טו, פסוקים - לח , לט - תלמוד.csv"

            # Sheet #
            Name_Of_Sheet = "במדבר טו, פס' - לח, לט"

            # Excel File #
            Name_Of_New_File = "במדבר טו, פסוקים - לח, לט.xls"
            pass

        elif Main_Index == 62:
            # Path #
            Path_One = Data_Set_Not_Update_Path + Version_One + "\\" + Book_Four + \
                       "\\" + "במדבר י, פסוקים - ט , י , טז - ברויאר.csv"
            Path_Two = Data_Set_Not_Update_Path + Version_Two + "\\" + Book_Four + \
                       "\\" + "במדבר י, פסוקים - ט , י , טז - לנינגרד.csv"
            Path_Three = Data_Set_Not_Update_Path + Version_Three + "\\" + Book_Four + \
                         "\\" + "במדבר י, פסוקים - ט , י , טז - קורן.csv"
            Path_Four = ""

            # Sheet #
            Name_Of_Sheet = "במדבר י, פס' - ט, י, טז"

            # Excel File #
            Name_Of_New_File = "במדבר י, פסוקים - ט, י, טז.xls"
            pass

        elif Main_Index == 63:
            # Path #
            Path_One = Data_Set_Not_Update_Path + Version_One + "\\" + Book_Four + "\\" + "במדבר יא, כו - ברויאר.csv"
            Path_Two = Data_Set_Not_Update_Path + Version_Two + "\\" + Book_Four + "\\" + "במדבר יא, כו - לנינגרד.csv"
            Path_Three = Data_Set_Not_Update_Path + Version_Three + "\\" + Book_Four + "\\" + "במדבר יא, כו - קורן.csv"
            Path_Four = ""

            # Sheet #
            Name_Of_Sheet = "במדבר יא, כו"

            # Excel File #
            Name_Of_New_File = "במדבר יא, כו.xls"
            pass

        elif Main_Index == 64:
            # Path #
            Path_One = Data_Set_Not_Update_Path + Version_One + "\\" + Book_Four + \
                       "\\" + "במדבר יג, פסוקים - כו , כט , לב - ברויאר.csv"
            Path_Two = Data_Set_Not_Update_Path + Version_Two + "\\" + Book_Four + \
                       "\\" + "במדבר יג, פסוקים - כו , כט , לב - לנינגרד.csv"
            Path_Three = Data_Set_Not_Update_Path + Version_Three + "\\" + Book_Four + \
                         "\\" + "במדבר יג, פסוקים - כו , כט , לב - קורן.csv"
            Path_Four = ""

            # Sheet #
            Name_Of_Sheet = "במדבר יג, פס' - כו, כט, לב"

            # Excel File #
            Name_Of_New_File = "במדבר יג, פסוקים - כו, כט, לב.xls"
            pass

        elif Main_Index == 65:
            # Path #
            Path_One = Data_Set_Not_Update_Path + Version_One + "\\" + Book_Four + "\\" + "במדבר יט, ז - ברויאר.csv"
            Path_Two = Data_Set_Not_Update_Path + Version_Two + "\\" + Book_Four + "\\" + "במדבר יט, ז - לנינגרד.csv"
            Path_Three = Data_Set_Not_Update_Path + Version_Three + "\\" + Book_Four + \
                         "\\" + "במדבר יט, ז - קורן.csv"
            Path_Four = ""

            # Sheet #
            Name_Of_Sheet = "במדבר יט, ז"

            # Excel File #
            Name_Of_New_File = "במדבר יט, ז.xls"
            pass

        elif Main_Index == 66:
            # Path #
            Path_One = Data_Set_Not_Update_Path + Version_One + "\\" + Book_Four + "\\" + "במדבר כ, יז - ברויאר.csv"
            Path_Two = Data_Set_Not_Update_Path + Version_Two + "\\" + Book_Four + "\\" + "במדבר כ, יז - לנינגרד.csv"
            Path_Three = Data_Set_Not_Update_Path + Version_Three + "\\" + Book_Four + "\\" + "במדבר כ, יז - קורן.csv"
            Path_Four = ""

            # Sheet #
            Name_Of_Sheet = "במדבר כ, יז"

            # Excel File #
            Name_Of_New_File = "במדבר כ, יז.xls"
            pass

        elif Main_Index == 67:
            # Path #
            Path_One = Data_Set_Not_Update_Path + Version_One + "\\" + Book_Four + "\\" + "במדבר כא, ל - ברויאר.csv"
            Path_Two = Data_Set_Not_Update_Path + Version_Two + "\\" + Book_Four + "\\" + "במדבר כא, ל - לנינגרד.csv"
            Path_Three = Data_Set_Not_Update_Path + Version_Three + "\\" + Book_Four + \
                         "\\" + "במדבר כא, פסוקים - ל , לד , לה - קורן.csv"
            Path_Four = Data_Set_Not_Update_Path + Version_Four + "\\" + Book_Four + \
                        "\\" + "במדבר כא, פסוקים - ל , לד , לה - תלמוד.csv"

            # Sheet #
            Name_Of_Sheet = "במדבר כא, פס' - ל, לד, לה"

            # Excel File #
            Name_Of_New_File = "במדבר כא, פסוקים - ל, לד, לה.xls"
            pass

        elif Main_Index == 68:
            # Path #
            Path_One = Data_Set_Not_Update_Path + Version_One + "\\" + Book_Four + \
                       "\\" + "במדבר כב, פסוקים - ה , לח - ברויאר.csv"
            Path_Two = Data_Set_Not_Update_Path + Version_Two + "\\" + Book_Four + \
                       "\\" + "במדבר כב, פסוקים - ה , לח - לנינגרד.csv"
            Path_Three = Data_Set_Not_Update_Path + Version_Three + "\\" + Book_Four + \
                         "\\" + "במדבר כב, פסוקים - ה , לח - קורן.csv"
            Path_Four = ""

            # Sheet #
            Name_Of_Sheet = "במדבר כב, פס' - ה, לח"

            # Excel File #
            Name_Of_New_File = "במדבר כב, פסוקים - ה, לח.xls"
            pass

        elif Main_Index == 69:
            # Path #
            Path_One = Data_Set_Not_Update_Path + Version_One + "\\" + Book_Four + "\\" + "במדבר כג, כט - ברויאר.csv"
            Path_Two = Data_Set_Not_Update_Path + Version_Two + "\\" + Book_Four + "\\" + "במדבר כג, כט - לנינגרד.csv"
            Path_Three = Data_Set_Not_Update_Path + Version_Three + "\\" + Book_Four + "\\" + "במדבר כג, כט - קורן.csv"
            Path_Four = ""

            # Sheet #
            Name_Of_Sheet = "במדבר כג, כט"

            # Excel File #
            Name_Of_New_File = "במדבר כג, כט.xls"
            pass

        elif Main_Index == 70:
            # Path #
            Path_One = Data_Set_Not_Update_Path + Version_One + "\\" + Book_Four + "\\" + "במדבר כד, ב - ברויאר.csv"
            Path_Two = Data_Set_Not_Update_Path + Version_Two + "\\" + Book_Four + "\\" + "במדבר כד, ב - לנינגרד.csv"
            Path_Three = Data_Set_Not_Update_Path + Version_Three + "\\" + Book_Four + "\\" + "במדבר כד, ב - קורן.csv"
            Path_Four = Data_Set_Not_Update_Path + Version_Four + "\\" + Book_Four + "\\" + "במדבר כד, ב - תלמוד.csv"

            # Sheet #
            Name_Of_Sheet = "במדבר כד, ב"

            # Excel File #
            Name_Of_New_File = "במדבר כד, ב.xls"
            pass

        elif Main_Index == 71:
            # Path #
            Path_One = Data_Set_Not_Update_Path + Version_One + "\\" + Book_Four + "\\" + "במדבר כו, כד - ברויאר.csv"
            Path_Two = Data_Set_Not_Update_Path + Version_Two + "\\" + Book_Four + "\\" + "במדבר כו, כד - לנינגרד.csv"
            Path_Three = Data_Set_Not_Update_Path + Version_Three + "\\" + Book_Four + "\\" + "במדבר כו, כד - קורן.csv"
            Path_Four = ""

            # Sheet #
            Name_Of_Sheet = "במדבר כו, כד"

            # Excel File #
            Name_Of_New_File = "במדבר כו, כד.xls"
            pass

        elif Main_Index == 72:
            # Path #
            Path_One = Data_Set_Not_Update_Path + Version_One + "\\" + Book_Four + "\\" + "במדבר לב, כב - ברויאר.csv"
            Path_Two = Data_Set_Not_Update_Path + Version_Two + "\\" + Book_Four + "\\" + "במדבר לב, כב - לנינגרד.csv"
            Path_Three = Data_Set_Not_Update_Path + Version_Three + "\\" + Book_Four + "\\" + "במדבר לב, כב - קורן.csv"
            Path_Four = ""

            # Sheet #
            Name_Of_Sheet = "במדבר לב, כב"

            # Excel File #
            Name_Of_New_File = "במדבר לב, כב.xls"
            pass

        elif Main_Index == 73:
            # Path #
            Path_One = Data_Set_Not_Update_Path + Version_One + "\\" + Book_Four + \
                       "\\" + "במדבר לג, פסוקים - לה , לו , נב - ברויאר.csv"
            Path_Two = Data_Set_Not_Update_Path + Version_Two + "\\" + Book_Four + \
                       "\\" + "במדבר לג, פסוקים - לה , לו , נב - לנינגרד.csv"
            Path_Three = Data_Set_Not_Update_Path + Version_Three + "\\" + Book_Four + \
                         "\\" + "במדבר לג, פסוקים - לה , לו , נב - קורן.csv"
            Path_Four = ""

            # Sheet #
            Name_Of_Sheet = "במדבר לג, פס' - לה, לו, נב"

            # Excel File #
            Name_Of_New_File = "במדבר לג, פסוקים - לה, לו, נב.xls"
            pass

        elif Main_Index == 74:
            # Path #
            Path_One = Data_Set_Not_Update_Path + Version_One + "\\" + Book_Four + "\\" + "במדבר לד, יא - ברויאר.csv"
            Path_Two = Data_Set_Not_Update_Path + Version_Two + "\\" + Book_Four + "\\" + "במדבר לד, יא - לנינגרד.csv"
            Path_Three = Data_Set_Not_Update_Path + Version_Three + "\\" + Book_Four + "\\" + "במדבר לד, יא - קורן.csv"
            Path_Four = ""

            # Sheet #
            Name_Of_Sheet = "במדבר לד, יא"

            # Excel File #
            Name_Of_New_File = "במדבר לד, יא.xls"
            pass

        elif Main_Index == 75:
            # Path #
            Path_One = Data_Set_Not_Update_Path + Version_One + "\\" + Book_Four + "\\" + "במדבר לה, יט - ברויאר.csv"
            Path_Two = Data_Set_Not_Update_Path + Version_Two + "\\" + Book_Four + "\\" + "במדבר לה, יט - לנינגרד.csv"
            Path_Three = Data_Set_Not_Update_Path + Version_Three + "\\" + Book_Four + "\\" + "במדבר לה, יט - קורן.csv"
            Path_Four = ""

            # Sheet #
            Name_Of_Sheet = "במדבר לה, יט"

            # Excel File #
            Name_Of_New_File = "במדבר לה, יט.xls"
            pass

        # Chapter - דברים #
        elif Main_Index == 76:
            # Path #
            Path_One = Data_Set_Not_Update_Path + Version_One + "\\" + Book_Five + \
                       "\\" + "דברים א, פסוקים - טו , לח - ברויאר.csv"
            Path_Two = Data_Set_Not_Update_Path + Version_Two + "\\" + Book_Five + \
                       "\\" + "דברים א, פסוקים - טו , לח - לנינגרד.csv"
            Path_Three = Data_Set_Not_Update_Path + Version_Three + "\\" + Book_Five + \
                         "\\" + "דברים א, פסוקים - יג , טו , לח - קורן.csv"
            Path_Four = Data_Set_Not_Update_Path + Version_Four + "\\" + Book_Five + \
                        "\\" + "דברים א, פסוקים - יג , טו , לח - תלמוד.csv"

            # Sheet #
            Name_Of_Sheet = "דברים א, פס' - יג, טו, לח"

            # Excel File #
            Name_Of_New_File = "דברים א, פסוקים - יג, טו, לח.xls"
            pass

        elif Main_Index == 77:
            # Path #
            Path_One = Data_Set_Not_Update_Path + Version_One + "\\" + Book_Five + "\\" + "דברים ב, כג - ברויאר.csv"
            Path_Two = Data_Set_Not_Update_Path + Version_Two + "\\" + Book_Five + "\\" + "דברים ב, כג - לנינגרד.csv"
            Path_Three = Data_Set_Not_Update_Path + Version_Three + "\\" + Book_Five + "\\" + "דברים ב, כג - קורן.csv"
            Path_Four = ""

            # Sheet #
            Name_Of_Sheet = "דברים ב, כג"

            # Excel File #
            Name_Of_New_File = "דברים ב, כג.xls"
            pass

        elif Main_Index == 78:
            # Path #
            Path_One = Data_Set_Not_Update_Path + Version_One + "\\" + Book_Five + "\\" + "דברים ד, ג - ברויאר.csv"
            Path_Two = Data_Set_Not_Update_Path + Version_Two + "\\" + Book_Five + "\\" + "דברים ד, ג - לנינגרד.csv"
            Path_Three = Data_Set_Not_Update_Path + Version_Three + "\\" + Book_Five + "\\" + "דברים ד, ג - קורן.csv"
            Path_Four = ""

            # Sheet #
            Name_Of_Sheet = "דברים ד, ג"

            # Excel File #
            Name_Of_New_File = "דברים ד, ג.xls"
            pass

        elif Main_Index == 79:
            # Path #
            Path_One = Data_Set_Not_Update_Path + Version_One + "\\" + Book_Five + \
                       "\\" + "דברים ו, פסוקים - ט , כא - ברויאר.csv"
            Path_Two = Data_Set_Not_Update_Path + Version_Two + "\\" + Book_Five + \
                       "\\" + "דברים ו, פסוקים - ט , כא - לנינגרד.csv"
            Path_Three = Data_Set_Not_Update_Path + Version_Three + "\\" + Book_Five + \
                         "\\" + "דברים ו, פסוקים - ח , כ , ט , כא - קורן.csv"
            Path_Four = Data_Set_Not_Update_Path + Version_Four + "\\" + Book_Five + \
                        "\\" + "דברים ו, פסוקים - ח , כ - תלמוד.csv"

            # Sheet #
            Name_Of_Sheet = "דברים ו, פס' - ח, כ, ט, כא"

            # Excel File #
            Name_Of_New_File = "דברים ו, פסוקים - ח, כ, ט, כא.xls"
            pass

        elif Main_Index == 80:
            # Path #
            Path_One = Data_Set_Not_Update_Path + Version_One + "\\" + Book_Five + "\\" + "דברים ט, טו - ברויאר.csv"
            Path_Two = Data_Set_Not_Update_Path + Version_Two + "\\" + Book_Five + "\\" + "דברים ט, טו - לנינגרד.csv"
            Path_Three = Data_Set_Not_Update_Path + Version_Three + "\\" + Book_Five + "\\" + "דברים ט, טו - קורן.csv"
            Path_Four = ""

            # Sheet #
            Name_Of_Sheet = "דברים ט, טו"

            # Excel File #
            Name_Of_New_File = "דברים ט, טו.xls"
            pass

        elif Main_Index == 81:
            # Path #
            Path_One = Data_Set_Not_Update_Path + Version_One + "\\" + Book_Five + "\\" + "דברים י, ח - ברויאר.csv"
            Path_Two = Data_Set_Not_Update_Path + Version_Two + "\\" + Book_Five + "\\" + "דברים י, ח - לנינגרד.csv"
            Path_Three = Data_Set_Not_Update_Path + Version_Three + "\\" + Book_Five + "\\" + "דברים י, ח - קורן.csv"
            Path_Four = Data_Set_Not_Update_Path + Version_Four + "\\" + Book_Five + "\\" + "דברים י, ח - תלמוד.csv"

            # Sheet #
            Name_Of_Sheet = "דברים י, ח"

            # Excel File #
            Name_Of_New_File = "דברים י, ח.xls"
            pass

        elif Main_Index == 82:
            # Path #
            Path_One = Data_Set_Not_Update_Path + Version_One + "\\" + Book_Five + "\\" + "דברים יא, יח - ברויאר.csv"
            Path_Two = Data_Set_Not_Update_Path + Version_Two + "\\" + Book_Five + "\\" + "דברים יא, יח - לנינגרד.csv"
            Path_Three = Data_Set_Not_Update_Path + Version_Three + "\\" + Book_Five + "\\" + "דברים יא, יח - קורן.csv"
            Path_Four = Data_Set_Not_Update_Path + Version_Four + "\\" + Book_Five + "\\" + "דברים יא, יח - תלמוד.csv"

            # Sheet #
            Name_Of_Sheet = "דברים יא, יח"

            # Excel File #
            Name_Of_New_File = "דברים יא, יח.xls"
            pass

        elif Main_Index == 83:
            # Path #
            Path_One = Data_Set_Not_Update_Path + Version_One + "\\" + Book_Five + "\\" + "דברים יב, כ - ברויאר.csv"
            Path_Two = Data_Set_Not_Update_Path + Version_Two + "\\" + Book_Five + "\\" + "דברים יב, כ - לנינגרד.csv"
            Path_Three = Data_Set_Not_Update_Path + Version_Three + "\\" + Book_Five + "\\" + "דברים יב, כ - קורן.csv"
            Path_Four = ""

            # Sheet #
            Name_Of_Sheet = "דברים יב, כ"

            # Excel File #
            Name_Of_New_File = "דברים יב, כ.xls"
            pass

        elif Main_Index == 84:
            # Path #
            Path_One = Data_Set_Not_Update_Path + Version_One + "\\" + Book_Five + "\\" + "דברים יח, כב - ברויאר.csv"
            Path_Two = Data_Set_Not_Update_Path + Version_Two + "\\" + Book_Five + "\\" + "דברים יח, כב - לנינגרד.csv"
            Path_Three = Data_Set_Not_Update_Path + Version_Three + "\\" + Book_Five + "\\" + "דברים יח, כב - קורן.csv"
            Path_Four = ""

            # Sheet #
            Name_Of_Sheet = "דברים יח, כב"

            # Excel File #
            Name_Of_New_File = "דברים יח, כב.xls"
            pass

        elif Main_Index == 85:
            # Path #
            Path_One = Data_Set_Not_Update_Path + Version_One + "\\" + Book_Five + \
                       "\\" + "דברים כב, פסוקים - ב , טו - ברויאר.csv"
            Path_Two = Data_Set_Not_Update_Path + Version_Two + "\\" + Book_Five + \
                       "\\" + "דברים כב, פסוקים - ב , טו - לנינגרד.csv"
            Path_Three = Data_Set_Not_Update_Path + Version_Three + "\\" + Book_Five + \
                         "\\" + "דברים כב, פסוקים - ב , טו - קורן.csv"
            Path_Four = Data_Set_Not_Update_Path + Version_Four + "\\" + Book_Five + \
                        "\\" + "דברים כב, פסוקים - ב , טו - תלמוד.csv"

            # Sheet #
            Name_Of_Sheet = "דברים כב, פס' - ב, טו"

            # Excel File #
            Name_Of_New_File = "דברים כב, פסוקים - ב, טו.xls"
            pass

        elif Main_Index == 86:
            # Path #
            Path_One = Data_Set_Not_Update_Path + Version_One + "\\" + Book_Five + "\\" + "דברים כג, ב - ברויאר.csv"
            Path_Two = Data_Set_Not_Update_Path + Version_Two + "\\" + Book_Five + "\\" + "דברים כג, ב - לנינגרד.csv"
            Path_Three = Data_Set_Not_Update_Path + Version_Three + "\\" + Book_Five + \
                         "\\" + "דברים כג, פסוקים - ב , כו - קורן.csv"
            Path_Four = Data_Set_Not_Update_Path + Version_Four + "\\" + Book_Five + \
                        "\\" + "דברים כג, פסוקים - ב , כו - תלמוד.csv"

            # Sheet #
            Name_Of_Sheet = "דברים כג, פס' - ב, כו"

            # Excel File #
            Name_Of_New_File = "דברים כג, פסוקים - ב, כו.xls"
            pass

        elif Main_Index == 87:
            # Path #
            Path_One = Data_Set_Not_Update_Path + Version_One + "\\" + Book_Five + "\\" + "דברים כח, נט - ברויאר.csv"
            Path_Two = Data_Set_Not_Update_Path + Version_Two + "\\" + Book_Five + "\\" + "דברים כח, נט - לנינגרד.csv"
            Path_Three = Data_Set_Not_Update_Path + Version_Three + "\\" + Book_Five + "\\" + "דברים כח, נט - קורן.csv"
            Path_Four = ""

            # Sheet #
            Name_Of_Sheet = "דברים כח, נט"

            # Excel File #
            Name_Of_New_File = "דברים כח, נט.xls"
            pass

        elif Main_Index == 88:
            # Path #
            Path_One = Data_Set_Not_Update_Path + Version_One + "\\" + Book_Five + \
                       "\\" + "דברים ל, פסוקים - יח , יט - ברויאר.csv"
            Path_Two = Data_Set_Not_Update_Path + Version_Two + "\\" + Book_Five + \
                       "\\" + "דברים ל, פסוקים - יח , יט - לנינגרד.csv"
            Path_Three = Data_Set_Not_Update_Path + Version_Three + "\\" + Book_Five + \
                         "\\" + "דברים ל, פסוקים - יח , יט - קורן.csv"
            Path_Four = ""

            # Sheet #
            Name_Of_Sheet = "דברים ל, פס' - יח, יט"

            # Excel File #
            Name_Of_New_File = "דברים ל, פסוקים - יח, יט.xls"
            pass

        elif Main_Index == 89:
            # Path #
            Path_One = Data_Set_Not_Update_Path + Version_One + "\\" + Book_Five + \
                       "\\" + "דברים לא, פסוקים - ט , כה , כו - ברויאר.csv"
            Path_Two = Data_Set_Not_Update_Path + Version_Two + "\\" + Book_Five + \
                       "\\" + "דברים לא, פסוקים - ט , כה , כו - לנינגרד.csv"
            Path_Three = Data_Set_Not_Update_Path + Version_Three + "\\" + Book_Five + \
                         "\\" + "דברים לא, פסוקים - ט , כה , כו - קורן.csv"
            Path_Four = Data_Set_Not_Update_Path + Version_Four + "\\" + Book_Five + \
                        "\\" + "דברים לא, פסוקים - ט , כה , כו - תלמוד.csv"

            # Sheet #
            Name_Of_Sheet = "דברים לא, פס' - ט, כה, כו"

            # Excel File #
            Name_Of_New_File = "דברים לא, פסוקים - ט, כה, כו.xls"
            pass

        elif Main_Index == 90:
            # Path #
            Path_One = Data_Set_Not_Update_Path + Version_One + "\\" + Book_Five + "\\" + "דברים לב, לד - ברויאר.csv"
            Path_Two = Data_Set_Not_Update_Path + Version_Two + "\\" + Book_Five + "\\" + "דברים לב, לד - לנינגרד.csv"
            Path_Three = Data_Set_Not_Update_Path + Version_Three + "\\" + Book_Five + "\\" + "דברים לב, לד - קורן.csv"
            Path_Four = ""

            # Sheet #
            Name_Of_Sheet = "דברים לב, לד"

            # Excel File #
            Name_Of_New_File = "דברים לב, לד.xls"
            pass

        elif Main_Index == 91:
            # Path #
            Path_One = Data_Set_Not_Update_Path + Version_One + "\\" + Book_Five + "\\" + "דברים לד, יא - ברויאר.csv"
            Path_Two = Data_Set_Not_Update_Path + Version_Two + "\\" + Book_Five + "\\" + "דברים לד, יא - לנינגרד.csv"
            Path_Three = Data_Set_Not_Update_Path + Version_Three + "\\" + Book_Five + "\\" + "דברים לד, יא - קורן.csv"
            Path_Four = ""

            # Sheet #
            Name_Of_Sheet = "דברים לד, יא"

            # Excel File #
            Name_Of_New_File = "דברים לד, יא.xls"
            pass

        return Path_One, Path_Two, Path_Three, Path_Four, Name_Of_Sheet, Name_Of_New_File

    def Create_New_Excel_File(self, Sentences_File_One, Sentences_File_Two, Sentences_File_Three,
                              Sentences_File_Four, Name_Of_Sheet, New_Destination_Directory,
                              New_Destination_Path):
        # Explain Of The Function #
        """
        Create Excel File.
        """

        # Integer #
        Index_One = 0
        Index_Two = 0
        Index_Three = 0
        Index_Four = 0
        Index_Excel = 1

        # Boolean #
        Flag_Remove_Last_Char_One = False
        Flag_Remove_Last_Char_Two = False
        Flag_Remove_Last_Char_Three = False
        Flag_Remove_Last_Char_Four = False

        # Styles #
        Style_One = None
        Style_Two = None
        Style_Three = None
        Style_Four = None

        # Check If Directory Exist #
        if not os.path.exists(New_Destination_Directory):
            os.makedirs(New_Destination_Directory)

        # Check If File Exist #
        if os.path.isfile(New_Destination_Path) is True:
            os.remove(New_Destination_Path)

        # For Hebrew Version #
        if self.Choice_Number == '1':

            # Stop Words #
            Hebrew_Stop_Words = self.Get_Hebrew_Stop_Words()

            # Remove Unnecessary Chars #
            while Index_One < len(Sentences_File_One):

                # All Sentences #
                # 1 #
                Sentences_File_One[Index_One] = re.sub('[\t]', '', Sentences_File_One[Index_One])
                if '\t' in Sentences_File_One[Index_One]:
                    Sentences_File_One[Index_One].replace('\t', '')
                # 2 #
                Sentences_File_One[Index_One] = re.sub('[־]', ' ', Sentences_File_One[Index_One])
                if '־' in Sentences_File_One[Index_One]:
                    Sentences_File_One[Index_One].replace('־', ' ')
                # 3 #
                Sentences_File_One[Index_One] = re.sub('[׀]', '', Sentences_File_One[Index_One])
                if '׀' in Sentences_File_One[Index_One]:
                    Sentences_File_One[Index_One].replace('׀', ' ')
                Sentences_File_One[Index_One] = Sentences_File_One[Index_One][1:]

                # Specific Sentences #
                # 1 #
                Sentences_File_Two[Index_One] = re.sub('[\t]', '', Sentences_File_Two[Index_One])
                if '\t' in Sentences_File_Two[Index_One]:
                    Sentences_File_Two[Index_One].replace('\t', '')
                # 2 #
                Sentences_File_Two[Index_One] = re.sub('[־]', ' ', Sentences_File_Two[Index_One])
                if '־' in Sentences_File_Two[Index_One]:
                    Sentences_File_Two[Index_One].replace('־', ' ')
                # 3 #
                Sentences_File_Two[Index_One] = re.sub('[׀]', ' ', Sentences_File_Two[Index_One])
                if '׀' in Sentences_File_Two[Index_One]:
                    Sentences_File_Two[Index_One].replace('׀', ' ')
                Sentences_File_Two[Index_One] = Sentences_File_Two[Index_One][1:]

                # Labels #
                # 1 #
                Sentences_File_Three[Index_One] = re.sub('[\t]', '', Sentences_File_Three[Index_One])
                if '\t' in Sentences_File_Three[Index_One]:
                    Sentences_File_Three[Index_One].replace('\t', '')
                # 2 #
                Sentences_File_Three[Index_One] = re.sub('[־]', ' ', Sentences_File_Three[Index_One])
                if '־' in Sentences_File_Three[Index_One]:
                    Sentences_File_Three[Index_One].replace('־', ' ')
                # 3 #
                Sentences_File_Three[Index_One] = re.sub('[׀]', ' ', Sentences_File_Three[Index_One])
                if '׀' in Sentences_File_Three[Index_One]:
                    Sentences_File_Three[Index_One].replace('׀', ' ')
                Sentences_File_Three[Index_One] = Sentences_File_Three[Index_One][1:]

                Char = Sentences_File_One[Index_One][len(Sentences_File_One[Index_One]) - 1]
                if Char == 'פ' or Char == 'ס':
                    '''
                    '[:-3]' Because We Have 'פ :'
                    '[:-3]' Because We Have 'ס :'
                    '''
                    Sentences_File_One[Index_One] = Sentences_File_One[Index_One][:-3]
                    Flag_Remove_Last_Char_One = True
                    pass

                Char = Sentences_File_Two[Index_One][len(Sentences_File_Two[Index_One]) - 1]
                if Char == 'פ' or Char == 'ס':
                    '''
                    '[:-3]' Because We Have 'פ :'
                    '[:-3]' Because We Have 'ס :'
                    '''
                    Sentences_File_Two[Index_One] = Sentences_File_Two[Index_One][:-3]
                    Flag_Remove_Last_Char_Two = True
                    pass

                Char = Sentences_File_Three[Index_One][len(Sentences_File_Three[Index_One]) - 1]
                if Char == 'פ' or Char == 'ס':
                    '''
                    '[:-3]' Because We Have 'פ :'
                    '[:-3]' Because We Have 'ס :'
                    '''
                    Sentences_File_Three[Index_One] = Sentences_File_Three[Index_One][:-3]
                    Flag_Remove_Last_Char_Three = True
                    pass

                # If Not === False #
                if not Flag_Remove_Last_Char_One:
                    Char = Sentences_File_One[Index_One][len(Sentences_File_One[Index_One]) - 1]
                    if Char != ')':
                        Sentences_File_One[Index_One] = Sentences_File_One[Index_One][:-1]
                        pass
                    pass
                if not Flag_Remove_Last_Char_Two:
                    Char = Sentences_File_Two[Index_One][len(Sentences_File_Two[Index_One]) - 1]
                    if Char != ')':
                        Sentences_File_Two[Index_One] = Sentences_File_Two[Index_One][:-1]
                        pass
                    pass
                if not Flag_Remove_Last_Char_Three:
                    Char = Sentences_File_Three[Index_One][len(Sentences_File_Three[Index_One]) - 1]
                    if Char != ')':
                        Sentences_File_Three[Index_One] = Sentences_File_Three[Index_One][:-1]
                        pass
                    pass

                # Extreme Case #
                if Name_Of_Sheet == "במדבר יט, ז":
                    if Sentences_File_One[Index_One] == "וידבר יהוה אל משה ואל אהרן לאמר׃":
                        Sentences_File_One[Index_One] = Sentences_File_One[Index_One][:-1]
                        Sentences_File_Two[Index_One] = Sentences_File_Two[Index_One][:-1]
                        Sentences_File_Three[Index_One] = Sentences_File_Three[Index_One][:-1]
                        pass
                    pass

                # Default Values #
                Flag_Remove_Last_Char_One = False
                Flag_Remove_Last_Char_Two = False
                Flag_Remove_Last_Char_Three = False

                # Remove Stop Words #
                # Integer #
                Local_Index = 0

                # Split List #
                Sentences_File_One_Split = Sentences_File_One[Index_One].split()
                Sentences_File_Two_Split = Sentences_File_Two[Index_One].split()
                Sentences_File_Three_Split = Sentences_File_Three[Index_One].split()

                # Iterate On List.Split() #
                while Local_Index < len(Sentences_File_One_Split):
                    if Sentences_File_One_Split[Local_Index] in Hebrew_Stop_Words:
                        Sentences_File_One_Split.pop(Local_Index)
                        pass
                    else:
                        Local_Index += 1
                    pass

                # Default Value #
                Local_Index = 0

                while Local_Index < len(Sentences_File_Two_Split):
                    if Sentences_File_Two_Split[Local_Index] in Hebrew_Stop_Words:
                        Sentences_File_Two_Split.pop(Local_Index)
                        pass
                    else:
                        Local_Index += 1
                    pass

                # Default Value #
                Local_Index = 0

                while Local_Index < len(Sentences_File_Three_Split):
                    if Sentences_File_Three_Split[Local_Index] in Hebrew_Stop_Words:
                        Sentences_File_Three_Split.pop(Local_Index)
                        pass
                    else:
                        Local_Index += 1
                    pass

                # Update Sentence  #
                Sentences_File_One[Index_One] = None
                Sentences_File_Two[Index_One] = None
                Sentences_File_Three[Index_One] = None
                Sentences_File_One[Index_One] = ' '.join(Specific_Word for Specific_Word in Sentences_File_One_Split)
                Sentences_File_Two[Index_One] = ' '.join(Specific_Word for Specific_Word in Sentences_File_Two_Split)
                Sentences_File_Three[Index_One] = ' '.join(
                    Specific_Word for Specific_Word in Sentences_File_Three_Split)

                # Update Count #
                Index_One += 1
                pass

            # Default Value #
            Index_One = 0

            # For Sentences File Four - תלמוד #
            if len(Sentences_File_Four) > 0:
                while Index_One < len(Sentences_File_Four):
                    # 1 #
                    Sentences_File_Four[Index_One] = re.sub('[\t]', '', Sentences_File_Four[Index_One])
                    if '\t' in Sentences_File_Four[Index_One]:
                        Sentences_File_Four[Index_One].replace('\t', '')
                    # 2 #
                    Sentences_File_Four[Index_One] = re.sub('[־]', ' ', Sentences_File_Four[Index_One])
                    if '־' in Sentences_File_Four[Index_One]:
                        Sentences_File_Four[Index_One].replace('־', ' ')
                    # 3 #
                    Sentences_File_Four[Index_One] = re.sub('[׀]', ' ', Sentences_File_Four[Index_One])
                    if '׀' in Sentences_File_Four[Index_One]:
                        Sentences_File_Four[Index_One].replace('׀', ' ')
                    Sentences_File_Four[Index_One] = Sentences_File_Four[Index_One][1:]

                    Char = Sentences_File_Four[Index_One][len(Sentences_File_Four[Index_One]) - 1]
                    if Char == 'פ' or Char == 'ס':
                        '''
                        '[:-3]' Because We Have 'פ :'
                        '[:-3]' Because We Have 'ס :'
                        '''
                        Sentences_File_Four[Index_One] = Sentences_File_Four[Index_One][:-3]
                        Flag_Remove_Last_Char_Four = True
                        pass
                    pass

                    # If Not === False #
                    if not Flag_Remove_Last_Char_Four:
                        if Char != ')':
                            Sentences_File_Four[Index_One] = Sentences_File_Four[Index_One][:-1]
                            pass
                        pass

                    # Default Values #
                    Flag_Remove_Last_Char_Four = False

                    # Remove Stop Words #
                    # Integer #
                    Local_Index = 0

                    # Split List #
                    Sentences_File_Four_Split = Sentences_File_Four[Index_One].split()

                    # Iterate On List.Split() #
                    while Local_Index < len(Sentences_File_Four_Split):
                        if Sentences_File_Four_Split[Local_Index] in Hebrew_Stop_Words:
                            Sentences_File_Four_Split.pop(Local_Index)
                            pass
                        Local_Index += 1
                        pass

                    # Update Sentence  #
                    Sentences_File_Four[Index_One] = None
                    Sentences_File_Four[Index_One] = ' '.join(
                        Specific_Word for Specific_Word in Sentences_File_Four_Split)

                    # Update Count #
                    Index_One += 1
                pass
            pass

        # For English Version #
        elif self.Choice_Number == '2':

            # 1 #
            Sentences_File_One = self.Augment_English_File(Sentences_File_One)

            # 2 #
            Sentences_File_Two = self.Augment_English_File(Sentences_File_Two)

            # 3 #
            Sentences_File_Three = self.Augment_English_File(Sentences_File_Three)

            # 4 #
            if len(Sentences_File_Four) > 0:
                Sentences_File_Four = self.Augment_English_File(Sentences_File_Four)
                pass
            pass

        # Default Value #
        Index_One = 0

        # Versions #
        Version_One = "Version - ברויאר"
        Version_Two = "Version - לנינגרד"
        Version_Three = "Version - קורן"
        Version_Four = "Version - תלמוד"

        # Workbook is created
        Workbook_Object = Workbook()

        # 'add_sheet' is used to create sheet.
        Sheet_One = Workbook_Object.add_sheet(Name_Of_Sheet)

        # For Hebrew Version #
        if self.Choice_Number == '1':

            # Style #
            Style_One = xlwt.easyxf('font: bold off, color black;\
                                     borders: top_color black, bottom_color black, right_color black, left_color black,\
                                              left thin, right thin, top thin, bottom thin;\
                                     pattern: pattern solid, fore_color Yellow;\
                                     align: horiz center')
            Style_Two = xlwt.easyxf('font: bold off, color black;\
                                     borders: top_color black, bottom_color black, right_color black, left_color black,\
                                              left thin, right thin, top thin, bottom thin;\
                                     pattern: pattern solid, fore_color red;\
                                     align: horiz center')
            Style_Three = xlwt.easyxf('font: bold off, color black;\
                                       borders: top_color black, bottom_color black, right_color black, left_color black,\
                                                left thin, right thin, top thin, bottom thin;\
                                       pattern: pattern solid, fore_color white;\
                                       align: horiz center')
            Style_Four = xlwt.easyxf('font: bold off, color black;\
                                      borders: top_color black, bottom_color black, right_color black, left_color black,\
                                               left thin, right thin, top thin, bottom thin;\
                                      pattern: pattern solid, fore_color white;\
                                      align: horiz right')

            # Width #
            Sheet_One.col(0).width = int(100 * 260)
            Sheet_One.col(1).width = int(100 * 260)
            Sheet_One.col(2).width = int(30 * 260)

            pass

        # For English Version #
        elif self.Choice_Number == '2':

            # Style #
            Style_One = xlwt.easyxf('font: bold off, color black;\
                                     borders: top_color black, bottom_color black, right_color black, left_color black,\
                                              left thin, right thin, top thin, bottom thin;\
                                     pattern: pattern solid, fore_color Yellow;\
                                     align: horiz center')
            Style_Two = xlwt.easyxf('font: bold off, color black;\
                                     borders: top_color black, bottom_color black, right_color black, left_color black,\
                                              left thin, right thin, top thin, bottom thin;\
                                     pattern: pattern solid, fore_color red;\
                                     align: horiz center')
            Style_Three = xlwt.easyxf('font: bold off, color black;\
                                       borders: top_color black, bottom_color black, right_color black, left_color black,\
                                                left thin, right thin, top thin, bottom thin;\
                                       pattern: pattern solid, fore_color white;\
                                       align: horiz center')
            Style_Four = xlwt.easyxf('font: bold off, color black;\
                                      borders: top_color black, bottom_color black, right_color black, left_color black,\
                                               left thin, right thin, top thin, bottom thin;\
                                      pattern: pattern solid, fore_color white;\
                                      align: horiz center')

            # Width #
            Sheet_One.col(0).width = int(130 * 260)
            Sheet_One.col(1).width = int(130 * 260)
            Sheet_One.col(2).width = int(30 * 260)

            pass

        # HeadLines #
        Sheet_One.write(0, 0, 'All Sentences', Style_One)
        Sheet_One.write(0, 1, 'Specific Sentence', Style_One)
        Sheet_One.write(0, 2, 'Labels', Style_One)

        if len(Sentences_File_Four) == 0:
            # The Books - ברויאר , לנינגרד , קורן #
            while Index_One < len(Sentences_File_One):
                # HeadLines #
                Sheet_One.write(Index_Excel, 0, Version_Two, Style_Two)
                Sheet_One.write(Index_Excel, 1, Version_One, Style_Two)
                Sheet_One.write(Index_Excel, 2, Version_One, Style_Two)
                Index_Excel += 1

                # First Version = ברויאר #
                # Second Version = לנינגרד #
                while Index_Two < len(Sentences_File_Two):
                    Sheet_One.write(Index_Excel, 0, Sentences_File_Two[Index_Two], Style_Four)
                    Sheet_One.write(Index_Excel, 1, Sentences_File_One[Index_One], Style_Three)
                    if self.Choice_Number == '1':
                        if Sentences_File_One[Index_One] == Sentences_File_Two[Index_Two]:
                            Sheet_One.write(Index_Excel, 2, 1, Style_Three)
                        else:
                            Sheet_One.write(Index_Excel, 2, 0, Style_Three)
                        pass
                    elif self.Choice_Number == '2':
                        Temp_Sentences_File_One = set(Sentences_File_One[Index_One].split())
                        Temp_Sentences_File_Two = set(Sentences_File_Two[Index_Two].split())
                        Threshold = len(Temp_Sentences_File_One & Temp_Sentences_File_Two) * 2
                        Threshold = Threshold / (len(Temp_Sentences_File_One) + len(Temp_Sentences_File_Two))
                        if Threshold >= 0.5:
                            Sheet_One.write(Index_Excel, 2, 1, Style_Three)
                        else:
                            Sheet_One.write(Index_Excel, 2, 0, Style_Three)
                        pass
                    Index_Two += 1
                    Index_Excel += 1
                    pass

                # HeadLines #
                Sheet_One.write(Index_Excel, 0, Version_Three, Style_Two)
                Sheet_One.write(Index_Excel, 1, Version_One, Style_Two)
                Sheet_One.write(Index_Excel, 2, Version_One, Style_Two)
                Index_Excel += 1

                # First Version = ברויאר #
                # Third Version = קורן #
                while Index_Three < len(Sentences_File_Three):
                    Sheet_One.write(Index_Excel, 0, Sentences_File_Three[Index_Three], Style_Four)
                    Sheet_One.write(Index_Excel, 1, Sentences_File_One[Index_One], Style_Three)
                    if self.Choice_Number == '1':
                        if Sentences_File_One[Index_One] == Sentences_File_Three[Index_Three]:
                            Sheet_One.write(Index_Excel, 2, 1, Style_Three)
                        else:
                            Sheet_One.write(Index_Excel, 2, 0, Style_Three)
                        pass
                    elif self.Choice_Number == '2':
                        Temp_Sentences_File_One = set(Sentences_File_One[Index_One].split())
                        Temp_Sentences_File_Three = set(Sentences_File_Three[Index_Three].split())
                        Threshold = len(Temp_Sentences_File_One & Temp_Sentences_File_Three) * 2
                        Threshold = Threshold / (len(Temp_Sentences_File_One) + len(Temp_Sentences_File_Three))
                        if Threshold >= 0.5:
                            Sheet_One.write(Index_Excel, 2, 1, Style_Three)
                        else:
                            Sheet_One.write(Index_Excel, 2, 0, Style_Three)
                        pass
                    Index_Three += 1
                    Index_Excel += 1
                    pass

                Index_One += 1
                Index_Two = 0
                Index_Three = 0
                pass

            # Default Values #
            Index_Two = 0
            Index_Three = 0

            # The Books - לנינגרד , קורן #
            while Index_Two < len(Sentences_File_Two):

                # HeadLines #
                Sheet_One.write(Index_Excel, 0, Version_Three, Style_Two)
                Sheet_One.write(Index_Excel, 1, Version_Two, Style_Two)
                Sheet_One.write(Index_Excel, 2, Version_Two, Style_Two)
                Index_Excel += 1

                while Index_Three < len(Sentences_File_Three):
                    Sheet_One.write(Index_Excel, 0, Sentences_File_Three[Index_Three], Style_Four)
                    Sheet_One.write(Index_Excel, 1, Sentences_File_Two[Index_Two], Style_Three)
                    if self.Choice_Number == '1':
                        if Sentences_File_Two[Index_Two] == Sentences_File_Three[Index_Three]:
                            Sheet_One.write(Index_Excel, 2, 1, Style_Three)
                        else:
                            Sheet_One.write(Index_Excel, 2, 0, Style_Three)
                        pass
                    elif self.Choice_Number == '2':
                        Temp_Sentences_File_Two = set(Sentences_File_Two[Index_Two].split())
                        Temp_Sentences_File_Three = set(Sentences_File_Three[Index_Three].split())
                        Threshold = len(Temp_Sentences_File_Two & Temp_Sentences_File_Three) * 2
                        Threshold = Threshold / (len(Temp_Sentences_File_Two) + len(Temp_Sentences_File_Three))
                        if Threshold >= 0.5:
                            Sheet_One.write(Index_Excel, 2, 1, Style_Three)
                        else:
                            Sheet_One.write(Index_Excel, 2, 0, Style_Three)
                        pass
                    Index_Three += 1
                    Index_Excel += 1
                    pass

                Index_Two += 1
                Index_Three = 0
                pass
            pass

        else:
            # The Books - ברויאר , לנינגרד , קורן , תלמוד #
            while Index_One < len(Sentences_File_One):
                # HeadLines #
                Sheet_One.write(Index_Excel, 0, Version_Two, Style_Two)
                Sheet_One.write(Index_Excel, 1, Version_One, Style_Two)
                Sheet_One.write(Index_Excel, 2, Version_One, Style_Two)
                Index_Excel += 1

                # First Version = ברויאר #
                # Second Version = לנינגרד #
                while Index_Two < len(Sentences_File_Two):
                    Sheet_One.write(Index_Excel, 0, Sentences_File_Two[Index_Two], Style_Four)
                    Sheet_One.write(Index_Excel, 1, Sentences_File_One[Index_One], Style_Three)
                    if self.Choice_Number == '1':
                        if Sentences_File_One[Index_One] == Sentences_File_Two[Index_Two]:
                            Sheet_One.write(Index_Excel, 2, 1, Style_Three)
                        else:
                            Sheet_One.write(Index_Excel, 2, 0, Style_Three)
                        pass
                    elif self.Choice_Number == '2':
                        Temp_Sentences_File_One = set(Sentences_File_One[Index_One].split())
                        Temp_Sentences_File_Two = set(Sentences_File_Two[Index_Two].split())
                        Threshold = len(Temp_Sentences_File_One & Temp_Sentences_File_Two) * 2
                        Threshold = Threshold / (len(Temp_Sentences_File_One) + len(Temp_Sentences_File_Two))
                        if Threshold >= 0.5:
                            Sheet_One.write(Index_Excel, 2, 1, Style_Three)
                        else:
                            Sheet_One.write(Index_Excel, 2, 0, Style_Three)
                        pass
                    Index_Two += 1
                    Index_Excel += 1
                    pass

                # HeadLines #
                Sheet_One.write(Index_Excel, 0, Version_Three, Style_Two)
                Sheet_One.write(Index_Excel, 1, Version_One, Style_Two)
                Sheet_One.write(Index_Excel, 2, Version_One, Style_Two)
                Index_Excel += 1

                # First Version = ברויאר #
                # Third Version = קורן #
                while Index_Three < len(Sentences_File_Three):
                    Sheet_One.write(Index_Excel, 0, Sentences_File_Three[Index_Three], Style_Four)
                    Sheet_One.write(Index_Excel, 1, Sentences_File_One[Index_One], Style_Three)
                    if self.Choice_Number == '1':
                        if Sentences_File_One[Index_One] == Sentences_File_Three[Index_Three]:
                            Sheet_One.write(Index_Excel, 2, 1, Style_Three)
                        else:
                            Sheet_One.write(Index_Excel, 2, 0, Style_Three)
                        pass
                    elif self.Choice_Number == '2':
                        Temp_Sentences_File_One = set(Sentences_File_One[Index_One].split())
                        Temp_Sentences_File_Three = set(Sentences_File_Three[Index_Three].split())
                        Threshold = len(Temp_Sentences_File_One & Temp_Sentences_File_Three) * 2
                        Threshold = Threshold / (len(Temp_Sentences_File_One) + len(Temp_Sentences_File_Three))
                        if Threshold >= 0.5:
                            Sheet_One.write(Index_Excel, 2, 1, Style_Three)
                        else:
                            Sheet_One.write(Index_Excel, 2, 0, Style_Three)
                        pass
                    Index_Three += 1
                    Index_Excel += 1
                    pass

                # HeadLines #
                Sheet_One.write(Index_Excel, 0, Version_Four, Style_Two)
                Sheet_One.write(Index_Excel, 1, Version_One, Style_Two)
                Sheet_One.write(Index_Excel, 2, Version_One, Style_Two)
                Index_Excel += 1

                # First Version = ברויאר #
                # Four Version = תלמוד #
                while Index_Four < len(Sentences_File_Four):
                    Sheet_One.write(Index_Excel, 0, Sentences_File_Four[Index_Four], Style_Four)
                    Sheet_One.write(Index_Excel, 1, Sentences_File_One[Index_One], Style_Three)
                    if self.Choice_Number == '1':
                        if Sentences_File_One[Index_One] == Sentences_File_Four[Index_Four]:
                            Sheet_One.write(Index_Excel, 2, 1, Style_Three)
                        else:
                            Sheet_One.write(Index_Excel, 2, 0, Style_Three)
                        pass
                    elif self.Choice_Number == '2':
                        Temp_Sentences_File_One = set(Sentences_File_One[Index_One].split())
                        Temp_Sentences_File_Four = set(Sentences_File_Four[Index_Four].split())
                        Threshold = len(Temp_Sentences_File_One & Temp_Sentences_File_Four) * 2
                        Threshold = Threshold / (len(Temp_Sentences_File_One) + len(Temp_Sentences_File_Four))
                        if Threshold >= 0.5:
                            Sheet_One.write(Index_Excel, 2, 1, Style_Three)
                        else:
                            Sheet_One.write(Index_Excel, 2, 0, Style_Three)
                        pass
                    Index_Four += 1
                    Index_Excel += 1
                    pass

                Index_One += 1
                Index_Two = 0
                Index_Three = 0
                Index_Four = 0
                pass

            # Default Values #
            Index_Two = 0
            Index_Three = 0
            Index_Four = 0

            # The Books - לנינגרד , קורן , תלמוד #
            while Index_Two < len(Sentences_File_Two):

                # HeadLines #
                Sheet_One.write(Index_Excel, 0, Version_Three, Style_Two)
                Sheet_One.write(Index_Excel, 1, Version_Two, Style_Two)
                Sheet_One.write(Index_Excel, 2, Version_Two, Style_Two)
                Index_Excel += 1

                # Second Version = לנינגרד #
                # Third Version = קורן #
                while Index_Three < len(Sentences_File_Three):
                    Sheet_One.write(Index_Excel, 0, Sentences_File_Three[Index_Three], Style_Four)
                    Sheet_One.write(Index_Excel, 1, Sentences_File_Two[Index_Two], Style_Three)
                    if self.Choice_Number == '1':
                        if Sentences_File_Two[Index_Two] == Sentences_File_Three[Index_Three]:
                            Sheet_One.write(Index_Excel, 2, 1, Style_Three)
                        else:
                            Sheet_One.write(Index_Excel, 2, 0, Style_Three)
                        pass
                    elif self.Choice_Number == '2':
                        Temp_Sentences_File_Two = set(Sentences_File_Two[Index_Two].split())
                        Temp_Sentences_File_Three = set(Sentences_File_Three[Index_Three].split())
                        Threshold = len(Temp_Sentences_File_Two & Temp_Sentences_File_Three) * 2
                        Threshold = Threshold / (len(Temp_Sentences_File_Two) + len(Temp_Sentences_File_Three))
                        if Threshold >= 0.5:
                            Sheet_One.write(Index_Excel, 2, 1, Style_Three)
                        else:
                            Sheet_One.write(Index_Excel, 2, 0, Style_Three)
                        pass
                    Index_Three += 1
                    Index_Excel += 1
                    pass

                # HeadLines #
                Sheet_One.write(Index_Excel, 0, Version_Four, Style_Two)
                Sheet_One.write(Index_Excel, 1, Version_Two, Style_Two)
                Sheet_One.write(Index_Excel, 2, Version_Two, Style_Two)
                Index_Excel += 1

                # Second Version = לנינגרד #
                # Four Version = תלמוד #
                while Index_Four < len(Sentences_File_Four):
                    Sheet_One.write(Index_Excel, 0, Sentences_File_Four[Index_Four], Style_Four)
                    Sheet_One.write(Index_Excel, 1, Sentences_File_Two[Index_Two], Style_Three)
                    if self.Choice_Number == '1':
                        if Sentences_File_Two[Index_Two] == Sentences_File_Four[Index_Four]:
                            Sheet_One.write(Index_Excel, 2, 1, Style_Three)
                        else:
                            Sheet_One.write(Index_Excel, 2, 0, Style_Three)
                        pass
                    elif self.Choice_Number == '2':
                        Temp_Sentences_File_Two = set(Sentences_File_Two[Index_Two].split())
                        Temp_Sentences_File_Four = set(Sentences_File_Four[Index_Four].split())
                        Threshold = len(Temp_Sentences_File_Two & Temp_Sentences_File_Four) * 2
                        Threshold = Threshold / (len(Temp_Sentences_File_Two) + len(Temp_Sentences_File_Four))
                        if Threshold >= 0.5:
                            Sheet_One.write(Index_Excel, 2, 1, Style_Three)
                        else:
                            Sheet_One.write(Index_Excel, 2, 0, Style_Three)
                        pass
                    Index_Four += 1
                    Index_Excel += 1
                    pass

                Index_Two += 1
                Index_Three = 0
                Index_Four = 0
                pass

            # Default Values #
            Index_Three = 0
            Index_Four = 0

            # The Books - קורן , תלמוד #
            while Index_Three < len(Sentences_File_Three):

                # HeadLines #
                Sheet_One.write(Index_Excel, 0, Version_Four, Style_Two)
                Sheet_One.write(Index_Excel, 1, Version_Three, Style_Two)
                Sheet_One.write(Index_Excel, 2, Version_Three, Style_Two)
                Index_Excel += 1

                # Third Version = קורן #
                # Four Version = תלמוד #
                while Index_Four < len(Sentences_File_Three):
                    Sheet_One.write(Index_Excel, 0, Sentences_File_Four[Index_Four], Style_Four)
                    Sheet_One.write(Index_Excel, 1, Sentences_File_Three[Index_Three], Style_Three)
                    if self.Choice_Number == '1':
                        if Sentences_File_Three[Index_Three] == Sentences_File_Four[Index_Four]:
                            Sheet_One.write(Index_Excel, 2, 1, Style_Three)
                        else:
                            Sheet_One.write(Index_Excel, 2, 0, Style_Three)
                        pass
                    elif self.Choice_Number == '2':
                        Temp_Sentences_File_Three = set(Sentences_File_Three[Index_Three].split())
                        Temp_Sentences_File_Four = set(Sentences_File_Four[Index_Four].split())
                        Threshold = len(Temp_Sentences_File_Three & Temp_Sentences_File_Four) * 2
                        Threshold = Threshold / (len(Temp_Sentences_File_Three) + len(Temp_Sentences_File_Four))
                        if Threshold >= 0.5:
                            Sheet_One.write(Index_Excel, 2, 1, Style_Three)
                        else:
                            Sheet_One.write(Index_Excel, 2, 0, Style_Three)
                        pass
                    Index_Four += 1
                    Index_Excel += 1
                    pass
                pass

                Index_Three += 1
                Index_Four = 0
            pass

        # Save The Excel File #
        Workbook_Object.save(New_Destination_Path)
        pass

    @staticmethod
    def Get_Hebrew_Stop_Words():
        # Explain Of The Function #
        """
        Function That Contains All the Stop Words.
        """

        return ['אני', 'את', 'אתה', 'אנחנו', 'אתן', 'אתם', 'הם', 'הן', 'היא', 'הוא', 'שלי', 'שלו', 'שלך', 'שלה', 'שלנו',
                'שלכם', 'שלכן', 'שלהם', 'עד', 'אשר', 'במידה', 'שוב', 'יותר',
                'שלהן', 'לי', 'לו', 'לה', 'לנו', 'לכם', 'לכן', 'להם', 'להן', 'אותה', 'אותו', 'זה', 'זאת', 'אלה', 'אלו',
                'תחת', 'מתחת', 'מעל', 'בין', 'מכיוון', 'יכולה', 'יכולים', 'יכולות',
                'עם', 'עד', 'נגר', 'על', 'אל', 'מול', 'של', 'אצל', 'כמו', 'אחר', 'אותו', 'בלי', 'לפני', 'אחרי',
                'מאחורי', 'עלי', 'עליו', 'עליה', 'הסיבה שבגללה', 'למה', 'אלו', 'אף', 'על', 'מעל',
                'עליך', 'עלינו', 'עליכם', 'לעיכן', 'עליהם', 'עליהן', 'כל', 'כולם', 'כולן', 'כך', 'ככה', 'כזה', 'זה',
                'זאת', 'אותי', 'אותה', 'אותם', 'איתן', 'איתנו', 'עצמן', 'עצמנו', 'מהיכן', 'מן', 'לעבר', 'מכאן',
                'אותך', 'אותו', 'אותן', 'אותנו', 'ואת', 'את', 'אתכם', 'אתכן', 'איתי', 'איתו', 'איתך', 'איתה', 'איתם',
                'איתכם', 'איתכן', 'יהיה', 'תהיה', 'היתי', 'היתה', 'היה', 'להיות', 'עצמי', 'עצמו', 'עצמה', 'עצמם',
                'עצמהם', 'עצמהן', 'מי', 'מה', 'איפה', 'היכן', 'במקום שבו', 'אם', 'לאן', 'למקום שבו', 'מקום בו', 'איזה',
                'איך', 'כיצד', 'באיזו מידה', 'מתי', 'בשעה ש', 'כאשר', 'כש', 'למרות', 'לפני', 'אחרי', 'מאיזו סיבה',
                'מדוע', 'לאיזו תכלית', 'כי', 'יש', 'אין', 'אך', 'מנין', 'מאין', 'מאיפה', 'יכל', 'יכלה', 'יכלו', 'יכול',
                'יוכלו', 'יוכל', 'מסוגל', 'לא', 'רק', 'אולי', 'אין', 'לאו', 'אי', 'כלל', 'נגד', 'אם', 'עם', 'אל', 'אלה',
                'מתחת', 'מצד', 'בשביל', 'לבין', 'באמצע', 'בתוך', 'דרך', 'מבעד', 'באמצעות', 'למעלה', 'למטה', 'מחוץ',
                'כאן', 'הנה', 'הרי', 'פה', 'שם', 'אך', 'ברם', 'שוב', 'אבל', 'מבלי', 'בלי', 'מלבד', 'רק', 'בגלל',
                'ואילו', 'למרות', 'אס', 'כמו', 'כפי', 'אז', 'אחרי', 'כן', 'לכן', 'לפיכך', 'מאד', 'עז', 'מעט', 'מעטים',
                'מדי', 'גם', 'כן', 'נו', 'אחר', 'אחרת', 'אחרים', 'אחרות', 'אשר', 'או']
        pass

    def Augment_English_File(self, Sentences_File):
        # Explain Of The Function #
        """
        This Function Translate From Hebrew To English.
        """

        # Integer #
        Index = 0

        # Stop Words #
        English_Stop_Words = set(stopwords.words('english'))

        try:
            # Remove Unnecessary Chars #
            while Index < len(Sentences_File):
                # 1 #
                Sentences_File[Index] = re.sub('[\t]', '', Sentences_File[Index])
                if '\t' in Sentences_File[Index]:
                    Sentences_File[Index].replace('\t', '')
                # 2 #
                Sentences_File[Index] = re.sub('[,]', ' ', Sentences_File[Index])
                if ',' in Sentences_File[Index]:
                    Sentences_File[Index].replace(',', ' ')
                # 3 #
                Sentences_File[Index] = re.sub('[:]', '', Sentences_File[Index])
                if ':' in Sentences_File[Index]:
                    Sentences_File[Index].replace(':', ' ')
                # 4 #
                Sentences_File[Index] = re.sub('[.]', '', Sentences_File[Index])
                if '.' in Sentences_File[Index]:
                    Sentences_File[Index].replace('.', ' ')
                # 5 #
                Sentences_File[Index] = re.sub('[\']', '', Sentences_File[Index])
                if '\'' in Sentences_File[Index]:
                    Sentences_File[Index].replace('\'', ' ')
                # 6 #
                Sentences_File[Index] = re.sub('[`]', '', Sentences_File[Index])
                if '`' in Sentences_File[Index]:
                    Sentences_File[Index].replace('`', ' ')

                # 7 #
                Sentences_File[Index] = re.sub('[?]', '', Sentences_File[Index])
                if '?' in Sentences_File[Index]:
                    Sentences_File[Index].replace('?', ' ')

                # 8 #
                Sentences_File[Index] = re.sub('[;]', '', Sentences_File[Index])
                if ';' in Sentences_File[Index]:
                    Sentences_File[Index].replace(';', ' ')

                # Split The Sentence To Words #
                Sentences_File_Split = Sentences_File[Index].split()

                # Integer #
                Local_Index = 0

                # Iterate On List.Split() , And Remove Stop Words #
                while Local_Index < len(Sentences_File_Split):
                    if Sentences_File_Split[Local_Index].lower() in English_Stop_Words:
                        Sentences_File_Split.pop(Local_Index)
                        pass
                    else:
                        Local_Index += 1
                    pass

                # Clear Sentence After All The Change's #
                Sentences_File[Index] = None
                Sentences_File[Index] = ' '.join(Specific_Word for Specific_Word in Sentences_File_Split)

                # Update The Index For Next Sentence #
                Index += 1
                pass

            # Make Data Augmentation #
            Index = 0
            while Index < len(Sentences_File):
                New_Sentence_After_Augmentation = self.Make_Data_Augmentation_To_Sentence(Sentences_File[Index])
                Sentences_File[Index] = New_Sentence_After_Augmentation
                Index += 1
                pass

            return Sentences_File

        except Exception as Object_Exception:
            # Write Exception To Console #
            print()
            print("===========================================================================")
            print("\tThere Have Exception In Function - " + "Augment_English_File !")
            print("\tBecause - " + str(Object_Exception))
            print("===========================================================================")
            print()

            return None
        pass

    @staticmethod
    def Make_Data_Augmentation_To_Sentence(Sentence_From_File):
        # Explain Of The Function #
        """
        This Function Making The Data Augmentation To The Data Set After We Make The Translation.
        """

        try:
            Augmentation_Data = Augmenter_Word.SynonymAug(aug_src='wordnet')
            Augmented_Text = Augmentation_Data.augment(Sentence_From_File)
            return Augmented_Text
            pass
        except Exception as Object_Exception:
            # Write Exception To Console #
            print()
            print("===========================================================================")
            print("\tThere Have Exception In Function - " + "Make_Data_Augmentation_To_Sentence !")
            print("\tBecause - " + str(Object_Exception))
            print("===========================================================================")
            print()
            pass
        pass

    @staticmethod
    def Read_From_Data_Set(Data_Set_Update_Path):
        # Explain Of The Function #
        """
        This Function Read The Data Set.
        """

        # Integer #
        Index = 0

        # List #
        Sentence_Column_One = []
        Sentence_Column_Two = []
        Sentence_Column_Three = []

        for Path, Sub_Folders, Files in os.walk(Data_Set_Update_Path, topdown=True):
            if len(Files) > 0:
                for Specific_File in Files:
                    Result_From_Pandas = pandas.read_excel(Path + "\\" + Specific_File, encoding='utf-8',
                                                           error_bad_lines=False)
                    Sentence_Column_One.extend(list(Result_From_Pandas["All Sentences"]))
                    Sentence_Column_Two.extend(list(Result_From_Pandas["Specific Sentence"]))
                    Sentence_Column_Three.extend(list(Result_From_Pandas["Labels"]))

                    print("===========================================================================")
                    print("\t\t\tFinish To Read => " + str(Specific_File) + " !")
                    print("===========================================================================")
                    print()

                    # Delete , For Next Iteration #
                    del Result_From_Pandas
                    pass
                pass
            pass

        print("===========================================================================")
        print("\t\t\tRemove Unnecessary Lines - Part One !")
        print("===========================================================================")
        print()

        # Check The Max Length #
        Max_Length = -sys.maxsize - 1
        Max_Sentence = None

        # Remove The Lines With 'Version' String #
        while Index < len(Sentence_Column_One):
            if "Version" in Sentence_Column_One[Index]:
                Sentence_Column_One.pop(Index)
                continue
            else:
                if Max_Length < len(Sentence_Column_One[Index]):
                    Max_Length = len(Sentence_Column_One[Index])
                    Max_Sentence = Sentence_Column_One[Index]
                Index += 1
            pass

        # Default Value #
        Index = 0

        print("===========================================================================")
        print("\t\t\tRemove Unnecessary Lines - Part Two !")
        print("===========================================================================")
        print()

        # Remove The Lines With 'Version' String #
        while Index < len(Sentence_Column_Two):
            if "Version" in Sentence_Column_Two[Index]:
                Sentence_Column_Two.pop(Index)
            else:
                if Max_Length < len(Sentence_Column_Two[Index]):
                    Max_Length = len(Sentence_Column_Two[Index])
                    Max_Sentence = Sentence_Column_Two[Index]
                Index += 1
            pass

        # Default Value #
        Index = 0

        print("===========================================================================")
        print("\t\t\tRemove Unnecessary Lines - Part Three !")
        print("===========================================================================")
        print()

        # Remove The Lines With 'Version' String #
        while Index < len(Sentence_Column_Three):
            if Sentence_Column_Three[Index] == 1 or \
                    Sentence_Column_Three[Index] == 0:
                Index += 1
            else:
                if Max_Length < len(Sentence_Column_Three[Index]):
                    Max_Length = len(Sentence_Column_Three[Index])
                    Max_Sentence = Sentence_Column_Three[Index]
                Sentence_Column_Three.pop(Index)
            pass

        print("===========================================================================")
        print("\t\t\tThe Max Length For Line Is - " + str(Max_Length))
        print("===========================================================================")
        print()

        # For Printing #
        Max_Length += 35
        for Local_Index in range(0, Max_Length):
            print("=", end='')
        print("\nThe Max Sentence Is - " + str(Max_Sentence))
        for Local_Index in range(0, Max_Length):
            print("=", end='')
        print("\n")

        return Sentence_Column_One, Sentence_Column_Two, Sentence_Column_Three

    pass
