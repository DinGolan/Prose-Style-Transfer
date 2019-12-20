# Imports #
import pandas
import sys
import ctypes
import math
import os

# Froms #
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSignal, QThread, pyqtSlot
from PyQt5.QtWidgets import QMainWindow, QMessageBox, QApplication
from PyQt5.QtGui import QMouseEvent


class Ui_Progress_Window(QMainWindow):

    def __init__(self, Script_Path, User_Role, Choice_Number,
                 Source_Prose_Pick, Source_Prose_Path,
                 Target_Prose_Pick, Target_Prose_Path,
                 Role_Controller_Object, Default_Model_Path=None,
                 Shelve_Settings_Dictionary=None):
        # Explain Of The Function #
        """
        In This Constructor I Have 'Magic' Parameter.
        The 'Magic' Parameter Is - Default Model.
        """

        super(Ui_Progress_Window, self).__init__()

        # Bring The Width , Height Of The Screen #
        Computer_User = ctypes.windll.user32
        Computer_User.SetProcessDPIAware()
        [Width_Screen, Height_Screen] = [Computer_User.GetSystemMetrics(0), Computer_User.GetSystemMetrics(1)]

        # GUI Attributes #
        self.Progress_Window_Main = None
        self.Progress_Bar_Frame = None
        self.Progress_Window_Frame_Blue = None
        self.Prose_Style_Transfer_Label = None
        self.Progress_Window_Frame_White = None
        self.Predict_Button = None
        self.Help_Button = None
        self.Back_Button = None
        self.Label_Created_By = None
        self.Project_Logo = None
        self.Wait_Label = None
        self.Progress_Bar = None
        self.Update_Progress_Bar_Value = None
        self.Predict_Icon = None
        self.Help_Icon = None
        self.Back_Icon = None

        # Other Component #
        self.Results_Window_Main = None
        self.Results_Window_Object = None
        self.User_Window_Main = None
        self.User_Window_Object = None
        self.Manager_Window_Main = None
        self.Manager_Window_Object = None
        self.User_Controller_Object = None
        self.Manager_Controller_Object = None
        self.Source_And_Target_Window_Main = None
        self.Source_And_Target_Window_Object = None

        # Program Attributes #
        self.Script_Path = Script_Path
        self.User_Role = User_Role
        self.Choice_Number = Choice_Number
        self.Source_Prose_Pick = Source_Prose_Pick
        self.Source_Prose_Path = Source_Prose_Path
        self.Target_Prose_Pick = Target_Prose_Pick
        self.Target_Prose_Path = Target_Prose_Path
        self.Model_Path = None
        self.Default_Model_Path = Default_Model_Path
        self.Max_Sequence_Length = None
        self.Role_Controller_Object = Role_Controller_Object
        self.Width = Width_Screen
        self.Height = Height_Screen
        self.Execute_Thread = None
        self.Shelve_Settings_Dictionary = Shelve_Settings_Dictionary

        # Check Which Controller We Need To Use #
        if self.User_Role == "User":
            self.User_Controller_Object = Role_Controller_Object
        elif self.User_Role == "Manager":
            self.Manager_Controller_Object = Role_Controller_Object
        pass

    def Init_UI(self, Progress_Window_Main):
        # Explain Of The Function #
        """
        This Function Make The Initialized Of The GUI.
        """

        ##########
        # Window #
        ##########
        self.Progress_Window_Main = Progress_Window_Main
        Progress_Window_Main.setObjectName("Progress_Window")
        Progress_Window_Main.resize(self.Width, self.Height)
        Progress_Window_Main.setMinimumSize(QtCore.QSize(self.Width, self.Height))
        Progress_Window_Main.setMaximumSize(QtCore.QSize(self.Width, self.Height))
        Progress_Window_Main.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        Progress_Window_Main.setWindowTitle("Prose Style Transfer - Progress Bar Window")

        ########
        # Icon #
        ########
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../Pictures/Project - Logo.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Progress_Window_Main.setWindowIcon(icon)

        #########
        # Frame #
        #########
        self.Progress_Bar_Frame = QtWidgets.QWidget(Progress_Window_Main)
        self.Progress_Bar_Frame.setObjectName("Progress_Bar_Frame")

        ###############
        # Blue Layout #
        ###############
        self.Progress_Window_Frame_Blue = QtWidgets.QFrame(self.Progress_Bar_Frame)
        self.Progress_Window_Frame_Blue.setGeometry(QtCore.QRect(self.Width / 2, 0, self.Width / 2, self.Height))
        self.Progress_Window_Frame_Blue.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.Progress_Window_Frame_Blue.setStyleSheet("background-color: rgb(0, 170, 255);")
        self.Progress_Window_Frame_Blue.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Progress_Window_Frame_Blue.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Progress_Window_Frame_Blue.setObjectName("Progress_Window_Frame_Blue")

        #####################
        # Prose Style Label #
        #####################
        self.Prose_Style_Transfer_Label = QtWidgets.QLabel(self.Progress_Window_Frame_Blue)
        self.Prose_Style_Transfer_Label.setGeometry(QtCore.QRect(self.Width / 12.5, self.Height / 5,
                                                                 self.Width / 2.849, self.Height / 1.900))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Prose_Style_Transfer_Label.sizePolicy().hasHeightForWidth())
        self.Prose_Style_Transfer_Label.setSizePolicy(sizePolicy)
        self.Prose_Style_Transfer_Label.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.Prose_Style_Transfer_Label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.Prose_Style_Transfer_Label.setStyleSheet("color: rgb(255, 170, 0);\n" +
                                                      "font: 87 8pt \"Segoe UI Black\";")
        self.Prose_Style_Transfer_Label.setAlignment(QtCore.Qt.AlignCenter)
        self.Prose_Style_Transfer_Label.setObjectName("Prose_Style_Transfer_Label")

        ################
        # White Layout #
        ################
        self.Progress_Window_Frame_White = QtWidgets.QFrame(self.Progress_Bar_Frame)
        self.Progress_Window_Frame_White.setGeometry(QtCore.QRect(0, 0, self.Width / 2, self.Height))
        self.Progress_Window_Frame_White.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.Progress_Window_Frame_White.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Progress_Window_Frame_White.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Progress_Window_Frame_White.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Progress_Window_Frame_White.setObjectName("Progress_Window_Frame_White")

        ##################
        # Predict Button #
        ##################
        self.Predict_Button = QtWidgets.QPushButton(self.Progress_Window_Frame_White)
        self.Predict_Button.setEnabled(True)
        self.Predict_Button.setGeometry(QtCore.QRect(self.Width / 7.142, (self.Height / 2.352) - (self.Height / 8.307),
                                                     self.Width / 4.739, self.Height / 8.791))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(25)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.Predict_Button.setFont(font)
        self.Predict_Button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Predict_Button.setStyleSheet("background-color: rgb(0, 170, 255);\n"
                                          "color: rgb(255, 170, 0); border-radius: 10px; padding: 10px;")
        self.Predict_Button.setObjectName("Predict_Button")
        self.Predict_Button.clicked.connect(self.Call_To_Predict_Results)

        ###############
        # Help Button #
        ###############
        self.Help_Button = QtWidgets.QPushButton(self.Progress_Window_Frame_White)
        self.Help_Button.setEnabled(True)
        self.Help_Button.setGeometry(QtCore.QRect(self.Width / 3.846, (self.Height / 1.428) - (self.Height / 8.307),
                                                  self.Width / 4.739, self.Height / 8.791))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(25)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.Help_Button.setFont(font)
        self.Help_Button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Help_Button.setStyleSheet("background-color: rgb(0, 170, 255);\n"
                                       "color: rgb(255, 170, 0); border-radius: 10px; padding: 10px;")
        self.Help_Button.setObjectName("Help_Button")
        self.Help_Button.clicked.connect(self.Show_Help_Window)

        ###############
        # Back Button #
        ###############
        self.Back_Button = QtWidgets.QPushButton(self.Progress_Window_Frame_White)
        self.Back_Button.setEnabled(True)
        self.Back_Button.setGeometry(QtCore.QRect(self.Width / 33.333, (self.Height / 1.428) - (self.Height / 8.307),
                                                  self.Width / 4.739, self.Height / 8.791))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(25)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.Back_Button.setFont(font)
        self.Back_Button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Back_Button.setStyleSheet("background-color: rgb(0, 170, 255);\n"
                                       "color: rgb(255, 170, 0); border-radius: 10px; padding: 10px;")
        self.Back_Button.setObjectName("Back_Button")
        self.Back_Button.clicked.connect(self.Back_Button_Function)

        ######################
        # Label - Created By #
        ######################
        self.Label_Created_By = QtWidgets.QLabel(self.Progress_Window_Frame_White)
        self.Label_Created_By.setGeometry(QtCore.QRect(self.Width / 32, (self.Height / 1.176) - (self.Height / 8.307),
                                                       self.Width / 2.320, self.Height / 6))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(17)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.Label_Created_By.setFont(font)
        self.Label_Created_By.setStyleSheet("color: rgb(255, 170, 0);")
        self.Label_Created_By.setAlignment(QtCore.Qt.AlignCenter)
        self.Label_Created_By.setObjectName("Label_Created_By")

        ################
        # Project Logo #
        ################
        self.Project_Logo = QtWidgets.QLabel(self.Progress_Window_Frame_White)
        self.Project_Logo.setGeometry(QtCore.QRect((self.Width / 6.666) + (self.Width / 24),
                                                   (self.Height / 20) - (self.Height / 11),
                                                   self.Width / 4.975, self.Height / 3.791))
        self.Project_Logo.setStyleSheet("")
        self.Project_Logo.setText("")
        self.Project_Logo.setPixmap(QtGui.QPixmap("../Pictures/Project - Logo.PNG"))
        self.Project_Logo.setObjectName("Project_Logo")

        ##############
        # Wait Label #
        ##############
        self.Wait_Label = QtWidgets.QLabel(self.Progress_Window_Frame_White)
        self.Wait_Label.setGeometry(QtCore.QRect((self.Width / 50) - (self.Width / 100),
                                                 (self.Height / 3.333) - (self.Height / 8.307),
                                                 self.Width / 2.127, self.Height / 9.876))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.Wait_Label.setFont(font)
        self.Wait_Label.setStyleSheet("color: rgb(255, 170, 0);")
        self.Wait_Label.setAlignment(QtCore.Qt.AlignCenter)
        self.Wait_Label.setObjectName("Wait_Label")

        ################
        # Progress Bar #
        ################
        self.Progress_Bar = QtWidgets.QProgressBar(self.Progress_Window_Frame_White)
        self.Progress_Bar.setGeometry(QtCore.QRect(self.Width / 16.666, (self.Height / 1.720) - (self.Height / 8.307),
                                                   self.Width / 2.380, self.Height / 13.333))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.Progress_Bar.setFont(font)
        self.Progress_Bar.setStyleSheet("color: rgb(255, 170, 0);")
        self.Progress_Bar.setProperty("value", 0)
        self.Progress_Bar.setMinimum(0)
        self.Progress_Bar.setMaximum(100)
        self.Progress_Bar.setObjectName("Progress_Bar")
        # Not In Used #
        """
        self.Update_Progress_Bar_Value = Progress_Bar_Thread(Count=0)
        self.Update_Progress_Bar_Value.Count_Changed.connect(self.Progress_Bar.setValue)
        """

        #############
        # Help Icon #
        #############
        self.Help_Icon = QtWidgets.QLabel(self.Progress_Window_Frame_White)
        self.Help_Icon.setGeometry(QtCore.QRect(self.Width / 2.439, (self.Height / 1.367) - (self.Height / 8.307),
                                                self.Width / 24.390, self.Height / 19.512))
        self.Help_Icon.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Help_Icon.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.Help_Icon.setStyleSheet("background-color: rgb(0, 170, 255);")
        self.Help_Icon.setText("")
        self.Help_Icon.setPixmap(QtGui.QPixmap("../Pictures/Help - Icon.ico"))
        self.Help_Icon.setScaledContents(True)
        self.Help_Icon.setAlignment(QtCore.Qt.AlignCenter)
        self.Help_Icon.setObjectName("Help_Icon")
        self.Help_Icon.mousePressEvent = self.Show_Help_Window

        ################
        # Predict Icon #
        ################
        self.Predict_Icon = QtWidgets.QLabel(self.Progress_Window_Frame_White)
        self.Predict_Icon.setGeometry(QtCore.QRect(self.Width / 3.389, (self.Height / 2.191) - (self.Height / 8.307),
                                                   self.Width / 24.390, self.Height / 19.512))
        self.Predict_Icon.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Predict_Icon.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.Predict_Icon.setStyleSheet("background-color: rgb(0, 170, 255);")
        self.Predict_Icon.setText("")
        self.Predict_Icon.setPixmap(QtGui.QPixmap("../Pictures/Predict - Icon.ico"))
        self.Predict_Icon.setScaledContents(True)
        self.Predict_Icon.setAlignment(QtCore.Qt.AlignCenter)
        self.Predict_Icon.setObjectName("Predict_Icon")
        self.Predict_Icon.mousePressEvent = self.Call_To_Predict_Results

        #############
        # Back Icon #
        #############
        self.Back_Icon = QtWidgets.QLabel(self.Progress_Window_Frame_White)
        self.Back_Icon.setGeometry(QtCore.QRect(self.Width / 5.555, (self.Height / 1.367) - (self.Height / 8.307),
                                                self.Width / 24.390, self.Height / 19.512))
        self.Back_Icon.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Back_Icon.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.Back_Icon.setStyleSheet("background-color: rgb(0, 170, 255);")
        self.Back_Icon.setText("")
        self.Back_Icon.setPixmap(QtGui.QPixmap("../Pictures/Back - Icon.ico"))
        self.Back_Icon.setScaledContents(True)
        self.Back_Icon.setAlignment(QtCore.Qt.AlignCenter)
        self.Back_Icon.setObjectName("Back_Icon")
        self.Back_Icon.mousePressEvent = self.Back_Button_Function

        ##################
        # Central Widget #
        ##################
        Progress_Window_Main.setCentralWidget(self.Progress_Bar_Frame)
        self.Retranslate_UI()
        QtCore.QMetaObject.connectSlotsByName(Progress_Window_Main)
        pass

    def Retranslate_UI(self):
        # Explain Of The Function #
        """
        This Function Fill The Components With Content.
        """

        _translate = QtCore.QCoreApplication.translate
        self.Prose_Style_Transfer_Label.setText(_translate("Progress_Window",
                                                           "<html><head/><body><p><span "
                                                           "style=\" font-size:70pt; font-style:italic;\">PROSE<br/>"
                                                           "STYLE <br/>TRANSFER</span></p></body></html>"))
        self.Predict_Button.setText(_translate("Progress_Window", "Predict"))
        self.Help_Button.setText(_translate("Progress_Window", "Help"))
        self.Back_Button.setText(_translate("Progress_Window", "Back"))
        self.Label_Created_By.setText(_translate("Progress_Window", "Created By Din Golan & Matan Peer\n" +
                                                 "Supervisor: Dvora Toledano\n" +
                                                 "Advice Supervisor: Zeev Vladimir Volkovich\n" +
                                                 "Date: 27/01/2020"))
        self.Wait_Label.setText(_translate("Progress_Window", "Press On 'Predict' Button , And Wait\n" +
                                           "Until The Model Will Finish His Running !"))
        pass

    def Call_To_Predict_Results(self, Event=None):
        # Explain Of The Function #
        """
        This Function Call To Predict Function.
        The Predict Function Make The Prediction Of The Model.
        Note - We Have 'Magic' Parameter.
        """

        try:
            if type(Event) == QMouseEvent:
                print("===========================================================================")
                print("\t\t\tMouse Event On - Predict Icon !")
                print("===========================================================================")

            # Make Checking Again - If The Model Exist #
            if self.Shelve_Settings_Dictionary is None:
                # Default Values , If Shelve File Not Exist #
                self.Shelve_Settings_Dictionary = {"Epoch_Number_Text": 10, "Batch_Size_Text": 64,
                                                   "Training_Split_Text": 0.7}

            # Flag For - Checking If Model Exist #
            Is_Model_Exist = None

            ########
            # User #
            ########
            if self.User_Role == "User":
                # From #
                from Classes.User_Controller import User_Controller_Class
                User_Controller_Object = User_Controller_Class(self.Script_Path,
                                                               self.Choice_Number)

                # Need To Check If The Model Is Load Or Not #
                if User_Controller_Object.Check_If_The_Model_Exist():
                    Is_Model_Exist = True
                else:
                    Is_Model_Exist = False

            ###########
            # Manager #
            ###########
            elif self.User_Role == "Manager":
                # From #
                from Classes.Manager_Controller import Manager_Controller_Class
                Manager_Controller_Object = Manager_Controller_Class(self.Script_Path,
                                                                     self.Choice_Number,
                                                                     self.Shelve_Settings_Dictionary)

                if Manager_Controller_Object.Check_If_The_Model_Exist():
                    Is_Model_Exist = True
                else:
                    Is_Model_Exist = False

            # If The Model Exist #
            if Is_Model_Exist:
                # Explain #
                """
                # Disable Pressing Twice On 'Predict' Button #
                # Disable Pressing On Help Button #
                # Disable Pressing On Back Button #
                """
                self.Predict_Button.setEnabled(False)
                self.Help_Button.setEnabled(False)
                self.Back_Button.setEnabled(False)

                # Default Model Path #
                if self.Default_Model_Path is not None:
                    self.Model_Path = self.Default_Model_Path

                # Not Default Model Path #
                else:
                    if self.Choice_Number == '1':
                        self.Model_Path = self.Script_Path + "Model" + "\\" + "Without - Augmentation" + "\\" \
                                          "Model_Without_Augmentation.h5"
                    elif self.Choice_Number == '2':
                        self.Model_Path = self.Script_Path + "Model" + "\\" + "With - Augmentation" + "\\" \
                                          "Model_With_Augmentation.h5"

                # Call To Predict Result's #
                Accuracy, Max_Values = self.Predict_Results(self.Source_Prose_Path,
                                                            self.Target_Prose_Path,
                                                            self.Model_Path)

                if Accuracy != -1 and Max_Values is not None:
                    # Enabled The Prediction Button , And Help Button #
                    self.Predict_Button.setEnabled(True)
                    self.Help_Button.setEnabled(True)
                    self.Back_Button.setEnabled(True)

                    print()
                    print("===========================================================================")
                    print("\t\tThe Predict Finished With - Success !")
                    print("===========================================================================")

                    # Style Sheet #
                    Icon = QtGui.QIcon()
                    Icon.addPixmap(QtGui.QPixmap("../Pictures/Project - Logo.ico"),
                                   QtGui.QIcon.Normal,
                                   QtGui.QIcon.Off)
                    QMessageBox.setWindowIcon(self, Icon)
                    QMessageBox.setStyleSheet(self,
                                              'QMessageBox{background-color: #00aaff; font-size: 16px;'
                                              'font-style: italic; font-family: Segoe UI Black;}\n' +
                                              'QPushButton{color: white; font-size: 16px; background-color: #1d1d1d; ' +
                                              'border-radius: 10px; padding: 10px; text-align: center;}\n ' +
                                              'QPushButton:hover{color: #ffaa00;}')
                    QMessageBox.information(self, "Predict - Finished",
                                            "<p><font color='#ffaa00'>The Predict Of The Model Finished , Now You Will See The Results !</font></p>")

                    # Explain #
                    """
                    Show New Window With The Accuracy Result.
                    Show File That Represent The Accuracy Between Each Sentence.
                    """
                    self.Show_Results_Window(Accuracy, Max_Values)
                else:
                    print()
                    print("===========================================================================")
                    print("\t\tThe Predict Finished With - Failure !")
                    print("===========================================================================")

                    # Style Sheet #
                    Icon = QtGui.QIcon()
                    Icon.addPixmap(QtGui.QPixmap("../Pictures/Project - Logo.ico"),
                                   QtGui.QIcon.Normal,
                                   QtGui.QIcon.Off)
                    QMessageBox.setWindowIcon(self, Icon)
                    QMessageBox.setStyleSheet(self,
                                              'QMessageBox{background-color: #00aaff; font-size: 16px;'
                                              'font-style: italic; font-family: Segoe UI Black;}\n' +
                                              'QPushButton{color: white; font-size: 16px; background-color: #1d1d1d; ' +
                                              'border-radius: 10px; padding: 10px; text-align: center;}\n ' +
                                              'QPushButton:hover{color: #ffaa00;}')
                    QMessageBox.critical(self, "Exception In - Predict Model",
                                         "<p><font color='#ffaa00'>There Have Exception In - Predict Function !</font></p>")
                    if QMessageBox.Ok:
                        if self.User_Role == "User":
                            # Create New Form #
                            self.User_Window_Main = QtWidgets.QMainWindow()

                            # From #
                            from Classes.User_Window import Ui_User_Window
                            self.User_Window_Object = Ui_User_Window(self.Script_Path, self.User_Role)
                            self.User_Window_Object.Init_UI(self.User_Window_Main)

                            # Close Current Window #
                            self.Progress_Window_Main.close()

                            # Show Previous Window #
                            self.User_Window_Main.show()

                        elif self.User_Role == "Manager":
                            # Create New Form #
                            self.Manager_Window_Main = QtWidgets.QMainWindow()

                            # From #
                            from Classes.Manager_Window import Ui_Manager_Window
                            self.Manager_Window_Object = Ui_Manager_Window(self.Script_Path, self.User_Role)
                            self.Manager_Window_Object.Init_UI(self.Manager_Window_Main)

                            # Close Current Window #
                            self.Progress_Window_Main.close()

                            # Show Previous Window #
                            self.Manager_Window_Main.show()

            # If The Model Not Exist #
            else:
                # Style Sheet #
                Icon = QtGui.QIcon()
                Icon.addPixmap(QtGui.QPixmap("../Pictures/Project - Logo.ico"),
                               QtGui.QIcon.Normal,
                               QtGui.QIcon.Off)
                QMessageBox.setWindowIcon(self, Icon)
                QMessageBox.setStyleSheet(self,
                                          'QMessageBox{background-color: #00aaff; font-size: 16px;'
                                          'font-style: italic; font-family: Segoe UI Black;}\n' +
                                          'QPushButton{color: white; font-size: 16px; background-color: #1d1d1d; ' +
                                          'border-radius: 10px; padding: 10px; text-align: center;}\n ' +
                                          'QPushButton:hover{color: #ffaa00;}')
                QMessageBox.critical(self, "The Model - Not Exist",
                                     "<p><font color='#ffaa00'>The Model Not Exist !<br>" +
                                     "You Can't Predict The Results Of The Model !</font></p>")

        except Exception as Object_Exception:
            # Return 'Predict' Button To Enable , Because There Have Exception #
            self.Predict_Button.setEnabled(True)

            # Return 'Help' Button To Enable , Because There Have Exception #
            self.Help_Button.setEnabled(True)

            # Return 'Back' Button To Enable , Because There Have Exception #
            self.Back_Button.setEnabled(True)

            # Style Sheet #
            Icon = QtGui.QIcon()
            Icon.addPixmap(QtGui.QPixmap("../Pictures/Project - Logo.ico"),
                           QtGui.QIcon.Normal,
                           QtGui.QIcon.Off)
            QMessageBox.setWindowIcon(self, Icon)
            QMessageBox.setStyleSheet(self,
                                      'QMessageBox{background-color: #00aaff; font-size: 16px;'
                                      'font-style: italic; font-family: Segoe UI Black;}\n' +
                                      'QPushButton{color: white; font-size: 16px; background-color: #1d1d1d; ' +
                                      'border-radius: 10px; padding: 10px; text-align: center;}\n ' +
                                      'QPushButton:hover{color: #ffaa00;}')
            QMessageBox.critical(self, "Error - Exception", "<p><font color='#ffaa00'>The Exception Is - <br>" +
                                 str(Object_Exception) + " !</font></p>")
        pass

    def Predict_Results(self, Source_Prose_Path, Target_Prose_Path, Model_Path):
        # Explain Of The Function #
        """
        This Function Make The Prediction To The Model.
        """

        try:
            # Froms #
            from keras.models import load_model
            from keras.preprocessing.text import Tokenizer
            from Classes.Manager_Config import Siamese_Config

            # Tokenizer #
            Tokenizer_Object = Tokenizer()

            # Style Sheet #
            Icon = QtGui.QIcon()
            Icon.addPixmap(QtGui.QPixmap("../Pictures/Project - Logo.ico"),
                           QtGui.QIcon.Normal,
                           QtGui.QIcon.Off)
            QMessageBox.setWindowIcon(self, Icon)
            QMessageBox.setStyleSheet(self,
                                      'QMessageBox{background-color: #00aaff; font-size: 16px;'
                                      'font-style: italic; font-family: Segoe UI Black;}\n' +
                                      'QPushButton{color: white; font-size: 16px; background-color: #1d1d1d; ' +
                                      'border-radius: 10px; padding: 10px; text-align: center;}\n ' +
                                      'QPushButton:hover{color: #ffaa00;}')
            QMessageBox.information(self, "Load - Model",
                                    "<p><font color='#ffaa00'>The System Loading The Model , Its Will Take Some Seconds !</font></p>")

            # Load The File Of The Module #
            Model_Object = load_model(Model_Path)

            # Integer #
            Index_Source = 0
            Index_Target = 0
            Count_Zero = 0
            Count_One = 0
            Max_Value = -sys.maxsize - 1
            Max_Index_Target = -1

            # List #
            Preds_Label = []
            Max_Values = []

            # Read From Source And Target Proses #
            Source_Prose_Path_String = Source_Prose_Path[0]
            Source_Prose_Path_String = Source_Prose_Path_String.replace('/', '\\')
            Source_File = pandas.read_csv(open(Source_Prose_Path_String, 'r', encoding='utf-8'), error_bad_lines=False)
            Sentences_Source_File = list(Source_File['Sentences'])
            Target_Prose_Path_String = Target_Prose_Path[0]
            Target_Prose_Path_String = Target_Prose_Path_String.replace('/', '\\')
            Target_File = pandas.read_csv(open(Target_Prose_Path_String, 'r', encoding='utf-8'), error_bad_lines=False)
            Sentences_Target_File = list(Target_File['Sentences'])

            # Progress Update #
            Progress_Update = round(100 / len(Sentences_Source_File), 2)

            # Create Thread For Progress Bar #
            self.Execute_Thread = Execute_Session(self.Progress_Bar, Progress_Update)
            self.Execute_Thread.PyQt_Signal.connect(self.Update_Progress_Bar)

            while Index_Source < len(Sentences_Source_File):
                while Index_Target < len(Sentences_Target_File):
                    List_Split_Sentences = []
                    if self.Choice_Number == '1':
                        List_Split_Sentences.append(Sentences_Source_File[Index_Source].split())
                        List_Split_Sentences.append(Sentences_Target_File[Index_Target].split())
                        Tokenizer_Object.fit_on_texts(List_Split_Sentences)
                        self.Max_Sequence_Length = Siamese_Config['MAX_SEQUENCE_LENGTH_WITHOUT_AUG']

                    elif self.Choice_Number == '2':
                        List_Split_Sentences.append(Sentences_Source_File[Index_Source].lower().split())
                        List_Split_Sentences.append(Sentences_Target_File[Index_Target].lower().split())
                        Tokenizer_Object.fit_on_texts(List_Split_Sentences)
                        self.Max_Sequence_Length = Siamese_Config['MAX_SEQUENCE_LENGTH_WITH_AUG']

                    Small_Sentence_Pair_Test = [(Sentences_Source_File[Index_Source],
                                                 Sentences_Target_File[Index_Target])]

                    # Variables #
                    Test_Data_Source_Prose = None
                    Test_Data_Target_Prose = None
                    Leaks_Test = None

                    if self.User_Role == "User":
                        Test_Data_Source_Prose, Test_Data_Target_Prose, Leaks_Test = \
                            self.User_Controller_Object.Create_Test_Data_Small(Tokenizer_Object,
                                                                               Small_Sentence_Pair_Test,
                                                                               self.Max_Sequence_Length)
                    elif self.User_Role == "Manager":
                        Test_Data_Source_Prose, Test_Data_Target_Prose, Leaks_Test = \
                            self.Manager_Controller_Object.Create_Test_Data_Small(Tokenizer_Object,
                                                                                  Small_Sentence_Pair_Test,
                                                                                  self.Max_Sequence_Length)

                    Preds = list(Model_Object.predict([Test_Data_Source_Prose, Test_Data_Target_Prose, Leaks_Test],
                                                      verbose=1).ravel())
                    for Value in Preds:
                        if Value < 0.01:
                            Preds_Label.append(0)
                        else:
                            Preds_Label.append(1)

                        if Max_Value < Value:
                            Max_Value = Value
                            Max_Index_Target = Index_Target

                    # Update The Index #
                    Index_Target += 1
                    pass

                # Start The Thread #
                # QApplication.processEvents()
                self.Execute_Thread.start()
                QApplication.processEvents()

                # Create Tuple #
                Small_Tuple = (Sentences_Source_File[Index_Source],
                               Sentences_Target_File[Max_Index_Target],
                               Max_Value)
                Max_Values.append(Small_Tuple)

                # Default Value's #
                Max_Index_Target = -1
                Max_Value = -sys.maxsize - 1
                Index_Target = 0

                # Update The Index #
                Index_Source += 1
                pass

            # Sort The Value's #
            Preds_Label.sort()
            for Value in Preds_Label:
                if Value == 0:
                    Count_Zero += 1
                else:
                    Count_One += 1

            # Accuracy Between Both Versions Of Prose's #
            Accuracy_Value = round((Count_One / (Count_Zero + Count_One)) * 1000, 2)

            # Return The Results From Function #
            return Accuracy_Value, Max_Values
        except Exception as Object_Exception:

            # Print To Console #
            print()
            print("===========================================================================")
            print("\t\tThe Exception Is - " + str(Object_Exception))
            print("===========================================================================")

            # Exception #
            return -1, None
        pass

    @pyqtSlot(int)
    def Update_Progress_Bar(self, Update_Value):
        self.Progress_Bar.setValue(math.ceil(Update_Value))
        pass

    def Show_Help_Window(self, Event=None):
        # Explain Of The Function #
        """
        This Function Show For Us The Help Window.
        Note - We Have 'Magic' Parameter.
        """

        if type(Event) == QMouseEvent:
            print("===========================================================================")
            print("\t\t\tMouse Event On - Help Icon !")
            print("===========================================================================")

        if os.path.exists(self.Script_Path + "Help"):
            if os.path.exists(self.Script_Path + "Help" + "\\" + "Prose Style Transfer - Help Page.pdf"):
                os.startfile(self.Script_Path + "Help" + "\\" + "Prose Style Transfer - Help Page.pdf")
            else:
                # Style Sheet #
                Icon = QtGui.QIcon()
                Icon.addPixmap(QtGui.QPixmap("../Pictures/Project - Logo.ico"),
                               QtGui.QIcon.Normal,
                               QtGui.QIcon.Off)
                QMessageBox.setWindowIcon(self, Icon)
                QMessageBox.setStyleSheet(self,
                                          'QMessageBox{background-color: #00aaff; font-size: 16px;'
                                          'font-style: italic; font-family: Segoe UI Black;}\n' +
                                          'QPushButton{color: white; font-size: 16px; background-color: #1d1d1d; ' +
                                          'border-radius: 10px; padding: 10px; text-align: center;}\n ' +
                                          'QPushButton:hover{color: #ffaa00;}')
                QMessageBox.critical(self, "Help Page - Not Found",
                                     "<p><font color='#ffaa00'>The Help File Not Exist !<br>" +
                                     "Because Of That, You Can't See <br>" +
                                     "The Help File Of The System !</font></p>")
        else:
            # Style Sheet #
            Icon = QtGui.QIcon()
            Icon.addPixmap(QtGui.QPixmap("../Pictures/Project - Logo.ico"),
                           QtGui.QIcon.Normal,
                           QtGui.QIcon.Off)
            QMessageBox.setWindowIcon(self, Icon)
            QMessageBox.setStyleSheet(self,
                                      'QMessageBox{background-color: #00aaff; font-size: 16px;'
                                      'font-style: italic; font-family: Segoe UI Black;}\n' +
                                      'QPushButton{color: white; font-size: 16px; background-color: #1d1d1d; ' +
                                      'border-radius: 10px; padding: 10px; text-align: center;}\n ' +
                                      'QPushButton:hover{color: #ffaa00;}')
            QMessageBox.critical(self, "Help Directory - Not Found",
                                 "<p><font color='#ffaa00'>The Help Directory Not Exist !<br>" +
                                 "Because Of That, You Can't See <br>" +
                                 "The Help File Of The System !</font></p>")
        pass

    def Show_Results_Window(self, Accuracy, Max_Values):
        # Explain Of The Function #
        """
        With This Function We Will See The Result Window.
        """

        try:
            # Extreme Case - If The Model Without Data Augmentation, And The Versions Is The Same #
            if self.Choice_Number == '1' and \
               self.Source_Prose_Pick == self.Target_Prose_Pick:
                Accuracy = 100

            # Create New Form #
            self.Results_Window_Main = QtWidgets.QMainWindow()

            # From #
            from Classes.Results_Window import Ui_Results_Window
            self.Results_Window_Object = Ui_Results_Window(self.Script_Path, self.User_Role, self.Choice_Number,
                                                           self.Source_Prose_Pick, self.Target_Prose_Pick,
                                                           Accuracy, Max_Values)
            self.Results_Window_Object.Init_UI(self.Results_Window_Main)

            # Close Current Window #
            self.Progress_Window_Main.close()

            # Show Previous Window #
            self.Results_Window_Main.show()

            pass
        except Exception as Object_Exception:
            # Style Sheet #
            Icon = QtGui.QIcon()
            Icon.addPixmap(QtGui.QPixmap("../Pictures/Project - Logo.ico"),
                           QtGui.QIcon.Normal,
                           QtGui.QIcon.Off)
            QMessageBox.setWindowIcon(self, Icon)
            QMessageBox.setStyleSheet(self,
                                      'QMessageBox{background-color: #00aaff; font-size: 16px;'
                                      'font-style: italic; font-family: Segoe UI Black;}\n' +
                                      'QPushButton{color: white; font-size: 16px; background-color: #1d1d1d; ' +
                                      'border-radius: 10px; padding: 10px; text-align: center;}\n ' +
                                      'QPushButton:hover{color: #ffaa00;}')
            QMessageBox.critical(self, "Error - Exception", "<p><font color='#ffaa00'>The Exception Is - <br>" +
                                 str(Object_Exception) + " !</font></p>")
        pass

    def Back_Button_Function(self, Event=None):
        # Explain Of The Function #
        """
        With This Function We Come Back To The Previous Page.
        Note - We Have 'Magic' Parameter.
        """

        if type(Event) == QMouseEvent:
            print("===========================================================================")
            print("\t\t\tMouse Event On - Back Icon !")
            print("===========================================================================")

        # Create New Form #
        self.Source_And_Target_Window_Main = QtWidgets.QMainWindow()

        # From #
        from Classes.Select_Versions_Window import Ui_Source_And_Target_Window
        self.Source_And_Target_Window_Object = Ui_Source_And_Target_Window(self.Script_Path, self.User_Role,
                                                                           self.Choice_Number, self.Source_Prose_Pick,
                                                                           self.Source_Prose_Path,
                                                                           self.Target_Prose_Pick,
                                                                           self.Target_Prose_Path)
        self.Source_And_Target_Window_Object.Init_UI(self.Source_And_Target_Window_Main)

        # Close Current Window #
        self.Progress_Window_Main.close()

        # Show Previous Window #
        self.Source_And_Target_Window_Main.show()
        pass

    pass


class Execute_Session(QThread):
    PyQt_Signal = pyqtSignal(int)

    def __init__(self, Progress_Bar, Progress_Update):
        QThread.__init__(self)
        self.Progress_Bar = Progress_Bar
        self.Progress_Update = Progress_Update
        pass

    def run(self):
        # Update The Progress Bar #
        self.PyQt_Signal.emit(self.Progress_Bar.value() + math.ceil(self.Progress_Update))
        pass

    pass
