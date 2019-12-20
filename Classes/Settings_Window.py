# Imports #
import shelve
import ctypes
import os

# Froms #
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QMessageBox
from PyQt5.QtGui import QMouseEvent


class Ui_Settings_Window(QMainWindow):

    def __init__(self, Script_Path, User_Role):
        super(Ui_Settings_Window, self).__init__()

        # Bring The Width , Height Of The Screen #
        Computer_User = ctypes.windll.user32
        Computer_User.SetProcessDPIAware()
        [Width_Screen, Height_Screen] = [Computer_User.GetSystemMetrics(0), Computer_User.GetSystemMetrics(1)]

        # GUI Attributes #
        self.Settings_Window_Main = None
        self.Settings_Window_Frame = None
        self.Settings_Window_Blue_Frame = None
        self.Prose_Style_Transfer_Label = None
        self.Settings_Window_White_Frame = None
        self.Epoch_Number_Label = None
        self.Epoch_Number_Text = None
        self.Batch_Size_Label = None
        self.Batch_Size_Text = None
        self.Training_Split_Label = None
        self.Training_Split_Text = None
        self.Back_Button = None
        self.Help_Button = None
        self.Apply_Button = None
        self.Project_Logo = None
        self.Label_Created_By = None
        self.Back_Icon = None
        self.Help_Icon = None
        self.Apply_Icon = None

        # Other Component #
        self.Manager_Window_Main = None
        self.Manager_Window_Object = None

        # Program Attributes #
        self.Script_Path = Script_Path
        self.User_Role = User_Role
        self.Width = Width_Screen
        self.Height = Height_Screen
        pass

    def Init_UI(self, Settings_Window_Main):
        # Explain Of The Function #
        """
        This Function Make The Initialized Of The GUI.
        """

        ##########
        # Window #
        ##########
        self.Settings_Window_Main = Settings_Window_Main
        Settings_Window_Main.setObjectName("Settings_Window")
        Settings_Window_Main.resize(self.Width, self.Height)
        Settings_Window_Main.setMinimumSize(QtCore.QSize(self.Width, self.Height))
        Settings_Window_Main.setMaximumSize(QtCore.QSize(self.Width, self.Height))

        ########
        # Icon #
        ########
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../Pictures/Project - Logo.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Settings_Window_Main.setWindowIcon(icon)

        #########
        # Frame #
        #########
        self.Settings_Window_Frame = QtWidgets.QWidget(Settings_Window_Main)
        self.Settings_Window_Frame.setObjectName("Settings_Window_Frame")

        ###############
        # Blue Layout #
        ###############
        self.Settings_Window_Blue_Frame = QtWidgets.QFrame(self.Settings_Window_Frame)
        self.Settings_Window_Blue_Frame.setGeometry(QtCore.QRect(self.Width / 2, 0, self.Width / 2, self.Height))
        self.Settings_Window_Blue_Frame.setStyleSheet("background-color: rgb(0, 170, 255);")
        self.Settings_Window_Blue_Frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Settings_Window_Blue_Frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Settings_Window_Blue_Frame.setObjectName("Settings_Window_Blue_Frame")

        #####################
        # Prose Style Label #
        #####################
        self.Prose_Style_Transfer_Label = QtWidgets.QLabel(self.Settings_Window_Blue_Frame)
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
        self.Settings_Window_White_Frame = QtWidgets.QFrame(self.Settings_Window_Frame)
        self.Settings_Window_White_Frame.setGeometry(QtCore.QRect(0, 0, self.Width / 2, self.Height))
        self.Settings_Window_White_Frame.setWhatsThis("")
        self.Settings_Window_White_Frame.setAccessibleName("")
        self.Settings_Window_White_Frame.setAccessibleDescription("")
        self.Settings_Window_White_Frame.setAutoFillBackground(False)
        self.Settings_Window_White_Frame.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Settings_Window_White_Frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Settings_Window_White_Frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Settings_Window_White_Frame.setLineWidth(0)
        self.Settings_Window_White_Frame.setObjectName("Settings_Window_White_Frame")

        ###############
        # Epoch Label #
        ###############
        self.Epoch_Number_Label = QtWidgets.QLabel(self.Settings_Window_White_Frame)
        self.Epoch_Number_Label.setGeometry(QtCore.QRect(self.Width / 33.333, (self.Height / 3.2) - (self.Height / 8),
                                                         self.Width / 7.092, self.Height / 26.666))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(23)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.Epoch_Number_Label.setFont(font)
        self.Epoch_Number_Label.setStyleSheet("color: rgb(255, 170, 0);")
        self.Epoch_Number_Label.setObjectName("Epoch_Number_Label")

        ##############
        # Epoch Text #
        ##############
        self.Epoch_Number_Text = QtWidgets.QLineEdit(self.Settings_Window_White_Frame)
        self.Epoch_Number_Text.setGeometry(QtCore.QRect(self.Width / 5.555, (self.Height / 3.2) - (self.Height / 8.307),
                                                        self.Width / 3.322, self.Height / 25.806))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.Epoch_Number_Text.setFont(font)
        self.Epoch_Number_Text.setInputMethodHints(QtCore.Qt.ImhNone)
        self.Epoch_Number_Text.setText("")
        self.Epoch_Number_Text.setFrame(True)
        self.Epoch_Number_Text.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.Epoch_Number_Text.setAlignment(QtCore.Qt.AlignCenter)
        self.Epoch_Number_Text.setCursorMoveStyle(QtCore.Qt.LogicalMoveStyle)
        self.Epoch_Number_Text.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.Epoch_Number_Text.setObjectName("Epoch_Number_Text")

        ###############
        # Back Button #
        ###############
        self.Back_Button = QtWidgets.QPushButton(self.Settings_Window_White_Frame)
        self.Back_Button.setGeometry(QtCore.QRect(self.Width / 33.333, (self.Height / 1.739) - (self.Height / 8.307),
                                                  self.Width / 4.587, self.Height / 8.791))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(25)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.Back_Button.setFont(font)
        self.Back_Button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Back_Button.setStyleSheet("background-color: rgb(0, 170, 255);\n" +
                                       "color: rgb(255, 170, 0); border-radius: 10px; padding: 10px;")
        self.Back_Button.setObjectName("Back_Button")
        self.Back_Button.clicked.connect(self.Back_Button_Function)

        ###############
        # Help Button #
        ###############
        self.Help_Button = QtWidgets.QPushButton(self.Settings_Window_White_Frame)
        self.Help_Button.setGeometry(QtCore.QRect(self.Width / 3.703, (self.Height / 1.739) - (self.Height / 8.307),
                                                  self.Width / 4.739, self.Height / 8.791))
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

        ##################
        # Project - Logo #
        ##################
        self.Project_Logo = QtWidgets.QLabel(self.Settings_Window_White_Frame)
        self.Project_Logo.setGeometry(QtCore.QRect((self.Width / 6.666) + (self.Width / 19.2),
                                                   (self.Height / 80) - (self.Height / 15.428),
                                                   self.Width / 4.975, (self.Height / 3.791) - (self.Height / 36)))
        self.Project_Logo.setStyleSheet("")
        self.Project_Logo.setText("")
        self.Project_Logo.setPixmap(QtGui.QPixmap("../Pictures/Project - Logo.PNG"))
        self.Project_Logo.setObjectName("Project_Logo")

        ################
        # Apply Button #
        ################
        self.Apply_Button = QtWidgets.QPushButton(self.Settings_Window_White_Frame)
        self.Apply_Button.setGeometry(QtCore.QRect(self.Width / 33.333, (self.Height / 1.403) - (self.Height / 8.307),
                                                   self.Width / 2.217, self.Height / 8.791))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(25)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.Apply_Button.setFont(font)
        self.Apply_Button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Apply_Button.setStyleSheet("background-color: rgb(0, 170, 255);\n" +
                                        "color: rgb(255, 170, 0); border-radius: 10px; padding: 10px;")
        self.Apply_Button.setObjectName("Apply_Button")
        self.Apply_Button.clicked.connect(self.Save_Details_From_Texts_In_Settings)

        ####################
        # Batch Size Label #
        ####################
        self.Batch_Size_Label = QtWidgets.QLabel(self.Settings_Window_White_Frame)
        self.Batch_Size_Label.setGeometry(QtCore.QRect(self.Width / 33.333, (self.Height / 2.580) - (self.Height / 8),
                                                       self.Width / 3.322, self.Height / 26.666))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(23)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.Batch_Size_Label.setFont(font)
        self.Batch_Size_Label.setStyleSheet("color: rgb(255, 170, 0);")
        self.Batch_Size_Label.setObjectName("Batch_Size_Label")

        ###################
        # Batch Size Text #
        ###################
        self.Batch_Size_Text = QtWidgets.QLineEdit(self.Settings_Window_White_Frame)
        self.Batch_Size_Text.setGeometry(QtCore.QRect(self.Width / 5.555, (self.Height / 2.580) - (self.Height / 8.307),
                                                      self.Width / 3.322, self.Height / 25.806))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.Batch_Size_Text.setFont(font)
        self.Batch_Size_Text.setInputMethodHints(QtCore.Qt.ImhNone)
        self.Batch_Size_Text.setText("")
        self.Batch_Size_Text.setFrame(True)
        self.Batch_Size_Text.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.Batch_Size_Text.setAlignment(QtCore.Qt.AlignCenter)
        self.Batch_Size_Text.setCursorMoveStyle(QtCore.Qt.LogicalMoveStyle)
        self.Batch_Size_Text.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.Batch_Size_Text.setObjectName("Batch_Size_Text")

        ########################
        # Training Split Label #
        ########################
        self.Training_Split_Label = QtWidgets.QLabel(self.Settings_Window_White_Frame)
        self.Training_Split_Label.setGeometry(QtCore.QRect(self.Width / 33.333, (self.Height / 2.162) - (self.Height / 8.3),
                                                           self.Width / 7.092, self.Height / 26.666))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(23)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.Training_Split_Label.setFont(font)
        self.Training_Split_Label.setStyleSheet("color: rgb(255, 170, 0);")
        self.Training_Split_Label.setObjectName("Training_Split_Label")

        #######################
        # Training Split Text #
        #######################
        self.Training_Split_Text = QtWidgets.QLineEdit(self.Settings_Window_White_Frame)
        self.Training_Split_Text.setGeometry(QtCore.QRect(self.Width / 5.555, (self.Height / 2.162) - (self.Height / 8.307),
                                                          self.Width / 3.322, self.Height / 25.806))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.Training_Split_Text.setFont(font)
        self.Training_Split_Text.setInputMethodHints(QtCore.Qt.ImhNone)
        self.Training_Split_Text.setText("")
        self.Training_Split_Text.setFrame(True)
        self.Training_Split_Text.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.Training_Split_Text.setAlignment(QtCore.Qt.AlignCenter)
        self.Training_Split_Text.setCursorMoveStyle(QtCore.Qt.LogicalMoveStyle)
        self.Training_Split_Text.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.Training_Split_Text.setObjectName("Training_Split_Text")

        ######################
        # Label - Created By #
        ######################
        self.Label_Created_By = QtWidgets.QLabel(self.Settings_Window_White_Frame)
        self.Label_Created_By.setGeometry(QtCore.QRect(self.Width / 22, (self.Height / 1.159) - (self.Height / 8.307),
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

        #############
        # Back Icon #
        #############
        self.Back_Icon = QtWidgets.QLabel(self.Settings_Window_White_Frame)
        self.Back_Icon.setGeometry(QtCore.QRect(self.Width / 5.405, (self.Height / 1.649) - (self.Height / 8.307),
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

        #############
        # Help Icon #
        #############
        self.Help_Icon = QtWidgets.QLabel(self.Settings_Window_White_Frame)
        self.Help_Icon.setGeometry(QtCore.QRect(self.Width / 2.380, (self.Height / 1.649) - (self.Height / 8.307),
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

        ##############
        # Apply Icon #
        ##############
        self.Apply_Icon = QtWidgets.QLabel(self.Settings_Window_White_Frame)
        self.Apply_Icon.setGeometry(QtCore.QRect(self.Width / 3.174, (self.Height / 1.344) - (self.Height / 8.307),
                                                 self.Width / 24.390, self.Height / 19.512))
        self.Apply_Icon.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Apply_Icon.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.Apply_Icon.setStyleSheet("background-color: rgb(0, 170, 255);")
        self.Apply_Icon.setText("")
        self.Apply_Icon.setPixmap(QtGui.QPixmap("../Pictures/Apply - Icon.ico"))
        self.Apply_Icon.setScaledContents(True)
        self.Apply_Icon.setAlignment(QtCore.Qt.AlignCenter)
        self.Apply_Icon.setObjectName("Apply_Icon")
        self.Apply_Icon.mousePressEvent = self.Save_Details_From_Texts_In_Settings

        ##################
        # Central Widget #
        ##################
        Settings_Window_Main.setCentralWidget(self.Settings_Window_Frame)
        self.Retranslate_UI(Settings_Window_Main)
        QtCore.QMetaObject.connectSlotsByName(Settings_Window_Main)
        pass

    def Retranslate_UI(self, Settings_Window_Main):
        # Explain Of The Function #
        """
        This Function Fill The Components With Content.
        """

        _translate = QtCore.QCoreApplication.translate
        Settings_Window_Main.setWindowTitle(_translate("Settings_Window", "Prose Style Transfer - Settings Window"))
        self.Prose_Style_Transfer_Label.setText(_translate("Settings_Window",
                                                           "<html><head/><body><p><span style=\" font-size:70pt; "
                                                           "font-style:italic;\">PROSE<br/>STYLE "
                                                           "<br/>TRANSFER</span></p></body></html>"))
        self.Epoch_Number_Label.setText(_translate("Settings_Window", "Epoch Number :"))
        self.Epoch_Number_Text.setPlaceholderText(_translate("Settings_Window", "1 <= Epoch Number <= 50"))
        self.Back_Button.setText(_translate("Settings_Window", "Back"))
        self.Help_Button.setText(_translate("Settings_Window", "Help"))
        self.Apply_Button.setText(_translate("Settings_Window", "Apply"))
        self.Batch_Size_Label.setText(_translate("Settings_Window", "Batch Size :"))
        self.Batch_Size_Text.setPlaceholderText(_translate("Settings_Window", "32 <= Batch Size <= 64"))
        self.Training_Split_Label.setText(_translate("Settings_Window", "Training Split :"))
        self.Training_Split_Text.setPlaceholderText(_translate("Settings_Window", "0.5 <= Training Split <= 0.9"))
        self.Label_Created_By.setText(_translate("Settings_Window", "Created By Din Golan & Matan Peer\n" +
                                                 "Supervisor: Dvora Toledano\n" +
                                                 "Advice Supervisor: Zeev Vladimir Volkovich\n" +
                                                 "Date: 27/01/2020"))
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
        self.Manager_Window_Main = QtWidgets.QMainWindow()

        # From #
        from Classes.Manager_Window import Ui_Manager_Window
        self.Manager_Window_Object = Ui_Manager_Window(self.Script_Path, self.User_Role)
        self.Manager_Window_Object.Init_UI(self.Manager_Window_Main)

        # Close Current Window #
        self.Settings_Window_Main.close()

        # Show Previous Window #
        self.Manager_Window_Main.show()
        pass

    def Save_Details_From_Texts_In_Settings(self, Event=None):
        # Explain Of The Function #
        """
        This Function Save The Details That The Manager Fill In The Texts Box.
        Note - We Have 'Magic' Parameter.
        """

        try:
            if type(Event) == QMouseEvent:
                print("===========================================================================")
                print("\t\t\tMouse Event On - Apply Icon !")
                print("===========================================================================")

            # String #
            Missing_Values_String = ""

            # Dictionary #
            Setting_Dictionary = dict()

            # 1 #
            Epoch_Number_Text = self.Epoch_Number_Text.text()
            try:
                if 1 <= int(Epoch_Number_Text) <= 50:
                    Setting_Dictionary["Epoch_Number_Text"] = Epoch_Number_Text
            except ValueError:
                # Explain #
                """
                # If The User Input Is Different Than 'Integer' #
                """
                pass

            # 2 #
            Batch_Size_Text = self.Batch_Size_Text.text()
            try:
                if 32 <= int(Batch_Size_Text) <= 64:
                    Setting_Dictionary["Batch_Size_Text"] = Batch_Size_Text
            except ValueError:
                # Explain #
                """
                # If The User Input Is Different Than 'Integer' #
                """
                pass

            # 3 #
            Training_Split_Text = self.Training_Split_Text.text()
            try:
                if 0.5 <= float(Training_Split_Text) <= 0.9:
                    Setting_Dictionary["Training_Split_Text"] = Training_Split_Text
            except ValueError:
                # Explain #
                """
                # If The User Input Is Different Than 'Float' #
                """
                pass

            # Check If We Have Missing Values #
            if "Epoch_Number_Text" not in Setting_Dictionary.keys():
                Missing_Values_String += "You Type Wrong Values For - Epoch Number !<br><br>"
            if "Batch_Size_Text" not in Setting_Dictionary.keys():
                Missing_Values_String += "You Type Wrong Values For - Batch Size !<br><br>"
            if "Training_Split_Text" not in Setting_Dictionary.keys():
                Missing_Values_String += "You Type Wrong Values For - Training Split !<br><br>"

            if len(Missing_Values_String) > 0:
                Missing_Values_String += "Do You Want To Use With The Default Values ?"

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
                Button_Reply = QMessageBox.question(self, "Warning - Settings", "<p><font color='#ffaa00'>" +
                                                    Missing_Values_String + "</font></p>",
                                                    QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
                if Button_Reply == QMessageBox.Yes:
                    # Save In Shelve The Default Values #
                    """
                    Explain - 
                    Flag 'c' : Open Database For Reading and Writing, Creating It If It Doesnt Exist.
                    """
                    Shelve_File = shelve.open(self.Script_Path + "Pickle , Shelve Files" + "\\" +
                                              "Shelve_Settings.shelve", flag='c')
                    Shelve_File['Settings'] = {"Epoch_Number_Text": 10, "Batch_Size_Text": 64,
                                               "Training_Split_Text": 0.7}
                    Shelve_File.close()

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
                    QMessageBox.information(self, "Correct - Settings",
                                            "<p><font color='#ffaa00'>The Settings You Type Save Successfully !</font></p>")

                    self.Back_To_The_Manager_Window_After_Details_Saved()

                elif Button_Reply == QMessageBox.No:
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
                    QMessageBox.information(self, "Incorrect - Settings",
                                            "<p><font color='#ffaa00'>Please Try Again To Insert Correct Settings !</font></p>")
            else:
                # Save In Shelve The Correct Values #
                """
                Explain - 
                Flag 'c' : Open Database For Reading and Writing, Creating It If It Doesnt Exist.
                """
                Shelve_File = shelve.open(self.Script_Path + "Pickle , Shelve Files" + "\\" +
                                          "Shelve_Settings.shelve", flag='c')
                Shelve_File['Settings'] = {"Epoch_Number_Text": int(Setting_Dictionary["Epoch_Number_Text"]),
                                           "Batch_Size_Text": int(Setting_Dictionary["Batch_Size_Text"]),
                                           "Training_Split_Text": float(Setting_Dictionary["Training_Split_Text"])}
                Shelve_File.close()

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
                QMessageBox.information(self, "Correct - Settings",
                                        "<p><font color='#ffaa00'>The Settings You Type Save Successfully !</font></p>")

                self.Back_To_The_Manager_Window_After_Details_Saved()

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
            QMessageBox.critical(self, "Error - Exception",
                                 "<p><font color='#ffaa00'>The Exception Is - <br>" +
                                 str(Object_Exception) + " !</font></p>")
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

    def Back_To_The_Manager_Window_After_Details_Saved(self):
        # Explain Of The Function #
        """
        This Function Going Back To The Main Window.
        """

        # Create New Form #
        self.Manager_Window_Main = QtWidgets.QMainWindow()

        # From #
        from Classes.Manager_Window import Ui_Manager_Window
        self.Manager_Window_Object = Ui_Manager_Window(self.Script_Path, self.User_Role)
        self.Manager_Window_Object.Init_UI(self.Manager_Window_Main)

        # Close Current Window #
        self.Settings_Window_Main.close()

        # Show Previous Window #
        self.Manager_Window_Main.show()
        pass

    pass
