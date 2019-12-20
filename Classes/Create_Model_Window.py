# Imports #
import ctypes
import os

# Froms #
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QMessageBox
from PyQt5.QtGui import QMouseEvent


class Ui_Create_Model_Window(QMainWindow):

    def __init__(self, Script_Path, User_Role, Choice_Number, Source_Prose_Pick,
                 Source_Prose_Pick_Path, Target_Prose_Pick, Target_Prose_Pick_Path,
                 Manager_Controller_Object, Shelve_Settings_Dictionary):
        super(Ui_Create_Model_Window, self).__init__()

        # Bring The Width , Height Of The Screen #
        Computer_User = ctypes.windll.user32
        Computer_User.SetProcessDPIAware()
        [Width_Screen, Height_Screen] = [Computer_User.GetSystemMetrics(0), Computer_User.GetSystemMetrics(1)]

        # GUI Attributes #
        self.Create_Model_Window_Main = None
        self.Create_Model_Frame = None
        self.Create_Model_Window_Frame_Blue = None
        self.Prose_Style_Transfer_Label = None
        self.Create_Model_Window_Frame_White = None
        self.Build_Button = None
        self.Help_Button = None
        self.Back_Button = None
        self.Label_Created_By = None
        self.Project_Logo = None
        self.Wait_Label = None
        self.Continue_To_Predict_Button = None
        self.Wait_Picture = None
        self.Build_Model_Picture = None
        self.Help_Icon = None
        self.Back_Icon = None
        self.Build_Model_Icon = None
        self.Continue_To_Predict_Icon = None

        # Other Component #
        self.Progress_Window_Main = None
        self.Progress_Window_Object = None
        self.Manager_Controller_Object = Manager_Controller_Object
        self.Source_And_Target_Window_Main = None
        self.Source_And_Target_Window_Object = None

        # Program Attributes #
        self.Script_Path = Script_Path
        self.User_Role = User_Role
        self.Choice_Number = Choice_Number
        self.Source_Prose_Pick = Source_Prose_Pick
        self.Source_Prose_Pick_Path = Source_Prose_Pick_Path
        self.Target_Prose_Pick = Target_Prose_Pick
        self.Target_Prose_Pick_Path = Target_Prose_Pick_Path
        self.Shelve_Settings_Dictionary = Shelve_Settings_Dictionary
        self.Width = Width_Screen
        self.Height = Height_Screen
        pass

    def Init_UI(self, Create_Model_Window_Main):
        # Explain Of The Function #
        """
        This Function Make The Initialized Of The GUI.
        """

        ##########
        # Window #
        ##########
        self.Create_Model_Window_Main = Create_Model_Window_Main
        Create_Model_Window_Main.setObjectName("Create_Model_Window")
        Create_Model_Window_Main.resize(self.Width, self.Height)
        Create_Model_Window_Main.setMinimumSize(QtCore.QSize(self.Width, self.Height))
        Create_Model_Window_Main.setMaximumSize(QtCore.QSize(self.Width, self.Height))
        Create_Model_Window_Main.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        Create_Model_Window_Main.setWindowTitle("Prose Style Transfer - Create Model Window")

        ########
        # Icon #
        ########
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../Pictures/Project - Logo.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Create_Model_Window_Main.setWindowIcon(icon)

        #########
        # Frame #
        #########
        self.Create_Model_Frame = QtWidgets.QWidget(Create_Model_Window_Main)
        self.Create_Model_Frame.setObjectName("Create_Model_Frame")

        ###############
        # Blue Layout #
        ###############
        self.Create_Model_Window_Frame_Blue = QtWidgets.QFrame(self.Create_Model_Frame)
        self.Create_Model_Window_Frame_Blue.setGeometry(QtCore.QRect(self.Width / 2, 0, self.Width / 2, self.Height))
        self.Create_Model_Window_Frame_Blue.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.Create_Model_Window_Frame_Blue.setStyleSheet("background-color: rgb(0, 170, 255);")
        self.Create_Model_Window_Frame_Blue.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Create_Model_Window_Frame_Blue.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Create_Model_Window_Frame_Blue.setObjectName("Create_Model_Window_Frame_Blue")

        #####################
        # Prose Style Label #
        #####################
        self.Prose_Style_Transfer_Label = QtWidgets.QLabel(self.Create_Model_Window_Frame_Blue)
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
        self.Create_Model_Window_Frame_White = QtWidgets.QFrame(self.Create_Model_Frame)
        self.Create_Model_Window_Frame_White.setEnabled(True)
        self.Create_Model_Window_Frame_White.setGeometry(QtCore.QRect(0, 0, self.Width / 2, self.Height))
        self.Create_Model_Window_Frame_White.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.Create_Model_Window_Frame_White.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Create_Model_Window_Frame_White.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Create_Model_Window_Frame_White.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Create_Model_Window_Frame_White.setObjectName("Create_Model_Window_Frame_White")

        ################
        # Build Button #
        ################
        self.Build_Button = QtWidgets.QPushButton(self.Create_Model_Window_Frame_White)
        self.Build_Button.setEnabled(True)
        self.Build_Button.setGeometry(QtCore.QRect(self.Width / 33.333, (self.Height / 1.6) - (self.Height / 7.7),
                                                   self.Width / 2.222, self.Height / 8.791))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(25)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.Build_Button.setFont(font)
        self.Build_Button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Build_Button.setStyleSheet("background-color: rgb(0, 170, 255);\n" +
                                        "color: rgb(255, 170, 0); border-radius: 10px; padding: 10px;")
        self.Build_Button.setObjectName("Build_Button")
        self.Build_Button.clicked.connect(self.Build_New_Model)

        ###############
        # Help Button #
        ###############
        self.Help_Button = QtWidgets.QPushButton(self.Create_Model_Window_Frame_White)
        self.Help_Button.setEnabled(True)
        self.Help_Button.setGeometry(QtCore.QRect(self.Width / 3.773, (self.Height / 1.333) - (self.Height / 7.7),
                                                  self.Width / 4.651, self.Height / 8.791))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(25)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.Help_Button.setFont(font)
        self.Help_Button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Help_Button.setStyleSheet("background-color: rgb(0, 170, 255);\n" +
                                       "color: rgb(255, 170, 0); border-radius: 10px; padding: 10px;")
        self.Help_Button.setObjectName("Help_Button")
        self.Help_Button.clicked.connect(self.Show_Help_Window)

        ###############
        # Back Button #
        ###############
        self.Back_Button = QtWidgets.QPushButton(self.Create_Model_Window_Frame_White)
        self.Back_Button.setEnabled(True)
        self.Back_Button.setGeometry(QtCore.QRect(self.Width / 33.333, (self.Height / 1.333) - (self.Height / 7.7),
                                                  self.Width / 4.4, self.Height / 8.791))
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
        self.Label_Created_By = QtWidgets.QLabel(self.Create_Model_Window_Frame_White)
        self.Label_Created_By.setGeometry(QtCore.QRect((self.Width / 23),
                                                       (self.Height / 1.118) - (self.Height / 20),
                                                       self.Width / 2.320, self.Height / 9.411))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(11)
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
        self.Project_Logo = QtWidgets.QLabel(self.Create_Model_Window_Frame_White)
        self.Project_Logo.setGeometry(QtCore.QRect((self.Width / 6.666) + (self.Width / 21),
                                                   (self.Height / 53.333) - (self.Height / 15.428),
                                                   self.Width / 4.975, self.Height / 4.968))
        self.Project_Logo.setStyleSheet("")
        self.Project_Logo.setText("")
        self.Project_Logo.setPixmap(QtGui.QPixmap("../Pictures/Project - Logo.PNG"))
        self.Project_Logo.setObjectName("Project_Logo")

        ##############
        # Wait Label #
        ##############
        self.Wait_Label = QtWidgets.QLabel(self.Create_Model_Window_Frame_White)
        self.Wait_Label.setGeometry(QtCore.QRect((self.Width / 25) - (self.Width / 150),
                                                 (self.Height / 4.444) - (self.Height / 10),
                                                 self.Width / 2.320, self.Height / 8.421))
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

        ##############################
        # Continue To Predict Button #
        ##############################
        self.Continue_To_Predict_Button = QtWidgets.QPushButton(self.Create_Model_Window_Frame_White)
        self.Continue_To_Predict_Button.setEnabled(False)
        self.Continue_To_Predict_Button.setGeometry(QtCore.QRect(self.Width / 33.333,
                                                                 (self.Height / 1.142) - (self.Height / 7.7),
                                                                 self.Width / 2.222, self.Height / 8.791))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(25)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.Continue_To_Predict_Button.setFont(font)
        self.Continue_To_Predict_Button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Continue_To_Predict_Button.setStyleSheet("background-color: rgb(0, 170, 255);\n" +
                                                      "color: rgb(255, 170, 0); border-radius: 10px; padding: 10px;")
        self.Continue_To_Predict_Button.setObjectName("Continue_To_Predict_Button")
        self.Continue_To_Predict_Button.clicked.connect(self.Continue_To_Predict_Model)

        ################
        # Wait Picture #
        ################
        self.Wait_Picture = QtWidgets.QLabel(self.Create_Model_Window_Frame_White)
        self.Wait_Picture.setGeometry(QtCore.QRect((self.Width / 15),
                                                   (self.Height / 2.857) - (self.Height / 8.307),
                                                   self.Width / 4.878, self.Height / 3.980))
        self.Wait_Picture.setText("")
        self.Wait_Picture.setPixmap(QtGui.QPixmap("../Pictures/Wait_Image.ico"))
        self.Wait_Picture.setObjectName("Wait_Picture")

        #######################
        # Build Model Picture #
        #######################
        self.Build_Model_Picture = QtWidgets.QLabel(self.Create_Model_Window_Frame_White)
        self.Build_Model_Picture.setGeometry(QtCore.QRect((self.Width / 3.906) + (self.Width / 20),
                                                          (self.Height / 2.857) - (self.Height / 9.25),
                                                          self.Width / 4.878, self.Height / 3.980))
        self.Build_Model_Picture.setText("")
        self.Build_Model_Picture.setPixmap(QtGui.QPixmap("../Pictures/Build_Model.ico"))
        self.Build_Model_Picture.setObjectName("Build_Model_Picture")

        #############
        # Help Icon #
        #############
        self.Help_Icon = QtWidgets.QLabel(self.Create_Model_Window_Frame_White)
        self.Help_Icon.setGeometry(QtCore.QRect(self.Width / 2.380, (self.Height / 1.28) - (self.Height / 7.7),
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

        #############
        # Back Icon #
        #############
        self.Back_Icon = QtWidgets.QLabel(self.Create_Model_Window_Frame_White)
        self.Back_Icon.setGeometry(QtCore.QRect(self.Width / 5.07, (self.Height / 1.28) - (self.Height / 7.7),
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

        ####################
        # Build Model Icon #
        ####################
        self.Build_Model_Icon = QtWidgets.QLabel(self.Create_Model_Window_Frame_White)
        self.Build_Model_Icon.setGeometry(QtCore.QRect(self.Width / 2.9,
                                                       (self.Height / 1.523) - (self.Height / 7.7),
                                                       self.Width / 24.390, self.Height / 19.512))
        self.Build_Model_Icon.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Build_Model_Icon.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.Build_Model_Icon.setStyleSheet("background-color: rgb(0, 170, 255);")
        self.Build_Model_Icon.setText("")
        self.Build_Model_Icon.setPixmap(QtGui.QPixmap("../Pictures/Build Model - Icon.ico"))
        self.Build_Model_Icon.setScaledContents(True)
        self.Build_Model_Icon.setAlignment(QtCore.Qt.AlignCenter)
        self.Build_Model_Icon.setObjectName("Build_Model_Icon")
        self.Build_Model_Icon.mousePressEvent = self.Build_New_Model

        ############################
        # Continue To Predict Icon #
        ############################
        self.Continue_To_Predict_Icon = QtWidgets.QLabel(self.Create_Model_Window_Frame_White)
        self.Continue_To_Predict_Icon.setGeometry(QtCore.QRect(self.Width / 2.631, (self.Height / 1.103) - (self.Height / 7.7),
                                                               self.Width / 24.390, self.Height / 19.512))
        self.Continue_To_Predict_Icon.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Continue_To_Predict_Icon.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.Continue_To_Predict_Icon.setStyleSheet("background-color: rgb(0, 170, 255);")
        self.Continue_To_Predict_Icon.setText("")
        self.Continue_To_Predict_Icon.setPixmap(QtGui.QPixmap("../Pictures/Predict - Icon.ico"))
        self.Continue_To_Predict_Icon.setScaledContents(True)
        self.Continue_To_Predict_Icon.setAlignment(QtCore.Qt.AlignCenter)
        self.Continue_To_Predict_Icon.setObjectName("Continue_To_Predict_Icon")
        self.Continue_To_Predict_Icon.mousePressEvent = self.Continue_To_Predict_Model

        ##################
        # Central Widget #
        ##################
        Create_Model_Window_Main.setCentralWidget(self.Create_Model_Frame)
        self.Retranslate_UI()
        QtCore.QMetaObject.connectSlotsByName(Create_Model_Window_Main)
        pass

    def Retranslate_UI(self):
        # Explain Of The Function #
        """
        This Function Fill The Components With Content.
        """

        _translate = QtCore.QCoreApplication.translate
        self.Prose_Style_Transfer_Label.setText(_translate("Create_Model_Window", "<html><head/><body><p><span "
                                                                                  "style=\" font-size:70pt; "
                                                                                  "font-style:italic;\">"
                                                                                  "PROSE<br/>STYLE <br/>"
                                                                                  "TRANSFER</span></p></body></html>"))
        self.Help_Button.setText(_translate("Create_Model_Window", "Help"))
        self.Back_Button.setText(_translate("Create_Model_Window", "Back"))
        self.Build_Button.setText(_translate("Create_Model_Window", "Build Model"))
        self.Label_Created_By.setText(_translate("Create_Model_Window", "Created By Din Golan & Matan Peer\n" +
                                                 "Supervisor: Dvora Toledano\n" +
                                                 "Advice Supervisor: Zeev Vladimir Volkovich\n" +
                                                 "Date: 27/01/2020"))
        self.Wait_Label.setText(_translate("Create_Model_Window", "Press On 'Build Model' Button !\n" +
                                           "Approximately Time Of Creating\n" +
                                           "The Model Is Between 2 - 4 Hours !"))
        self.Continue_To_Predict_Button.setText(_translate("Create_Model_Window", "Continue To Predict"))
        pass

    def Build_New_Model(self, Event=None):
        # Explain Of The Function #
        """
        This Function Start With Creation Of New Model.
        Note - We Have 'Magic' Parameter.
        """

        try:
            if type(Event) == QMouseEvent:
                print("===========================================================================")
                print("\t\t\tMouse Event On - Build New Model Icon !")
                print("===========================================================================")

            # Explain #
            """
            # Disable Pressing Twice On 'Build Model' Button #
            # Disable Pressing On Help Button #
            # Disable Pressing On Back Button #
            """
            self.Build_Button.setEnabled(False)
            self.Help_Button.setEnabled(False)
            self.Back_Button.setEnabled(False)

            ###################
            # Build New Model #
            ###################
            if self.Manager_Controller_Object.Manager_Main_Function(self.Choice_Number,
                                                                    self.Shelve_Settings_Dictionary) == "True":
                # Explain #
                """
                # After We Finish To Create The Model We Can Continue To Predict The Model #
                # We Make Enable To Back , Help Button's #
                """
                self.Continue_To_Predict_Button.setEnabled(True)
                self.Help_Button.setEnabled(True)
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
                QMessageBox.information(self, "Success - Create New Model",
                                        "<p><font color='#ffaa00'>The New Model Created Successfully !<br><br>" +
                                        "Now, You Can Make Prediction To The Model !</font></p>")
            else:
                # Return 'Build Model' Button To Enable , Because There Have Error #
                self.Build_Button.setEnabled(True)

                # Return 'Help' Button To Enable , Because There Have Error #
                self.Help_Button.setEnabled(True)

                # Return 'Back' Button To Enable , Because There Have Error #
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
                QMessageBox.critical(self, "Error -  Create New Model",
                                     "<p><font color='#ffaa00'>We Cant Build New Model , Because We Have Exception During The Building !</font></p>")

        except Exception as Object_Exception:
            # Return 'Build Model' Button To Enable , Because There Have Exception #
            self.Build_Button.setEnabled(True)

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
            QMessageBox.critical(self, "Error - Exception",
                                 "<p><font color='#ffaa00'>We Cant Build New Model !<br>" +
                                 "The Exception Is - <br>" + str(Object_Exception) + " !</font></p>")
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

    def Continue_To_Predict_Model(self, Event=None):
        # Explain Of The Function #
        """
        With This Function We Will See The Progress Window.
        Furthermore, This Function Will Give Us The Option Of Predict The Model.
        Note - We Have 'Magic' Parameter.
        """

        if type(Event) == QMouseEvent:
            print("===========================================================================")
            print("\t\t\tMouse Event On - Continue To Predict Icon !")
            print("===========================================================================")

        # Create New Form #
        self.Progress_Window_Main = QtWidgets.QMainWindow()

        # From #
        from Classes.Progress_Window import Ui_Progress_Window
        self.Progress_Window_Object = Ui_Progress_Window(self.Script_Path,
                                                         self.User_Role,
                                                         self.Choice_Number,
                                                         self.Source_Prose_Pick,
                                                         self.Source_Prose_Pick_Path,
                                                         self.Target_Prose_Pick,
                                                         self.Target_Prose_Pick_Path,
                                                         self.Manager_Controller_Object)

        self.Progress_Window_Object.Init_UI(self.Progress_Window_Main)

        # Close Current Window #
        self.Create_Model_Window_Main.close()

        # Show Previous Window #
        self.Progress_Window_Main.show()
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
                                                                           self.Source_Prose_Pick_Path, self.Target_Prose_Pick,
                                                                           self.Target_Prose_Pick_Path)
        self.Source_And_Target_Window_Object.Init_UI(self.Source_And_Target_Window_Main)

        # Close Current Window #
        self.Create_Model_Window_Main.close()

        # Show Previous Window #
        self.Source_And_Target_Window_Main.show()
        pass

    pass
