# Imports #
import ctypes
import os
import sys

# Froms #
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QMessageBox
from PyQt5.QtGui import QMouseEvent


class Ui_Manager_Window(QMainWindow):

    def __init__(self, Script_Path, Role):
        super(Ui_Manager_Window, self).__init__()

        # Bring The Width , Height Of The Screen #
        Computer_User = ctypes.windll.user32
        Computer_User.SetProcessDPIAware()
        [Width_Screen, Height_Screen] = [Computer_User.GetSystemMetrics(0), Computer_User.GetSystemMetrics(1)]

        # GUI Attributes #
        self.Manager_Window_Main = None
        self.Manager_Window_Frame = None
        self.Manager_Window_Blue_Frame = None
        self.Prose_Style_Transfer_Label = None
        self.Manager_Window_White_Frame = None
        self.Button_Without_Data_Augmentation = None
        self.Button_With_Data_Augmentation = None
        self.Button_Settings = None
        self.Button_Settings = None
        self.Back_Button = None
        self.Help_Button = None
        self.Project_Logo = None
        self.Label_Created_By = None
        self.Settings_Icon = None
        self.Back_Icon = None
        self.Help_Icon = None
        self.Application_Main = None

        # Other Component #
        self.Select_Versions_Window_Main = None
        self.Select_Versions_Window_Object = None
        self.Settings_Window_Main = None
        self.Settings_Window_Object = None
        self.Start_Window_Main = None
        self.Start_Window_Object = None

        # Program Attributes #
        self.Script_Path = Script_Path
        self.User_Role = Role
        self.Width = Width_Screen
        self.Height = Height_Screen
        pass

    def Init_UI(self, Application_Main, Manager_Window_Main):
        # Explain Of The Function #
        """
        This Function Make The Initialized Of The GUI.
        """

        ##########
        # Window #
        ##########
        self.Application_Main = Application_Main
        self.Manager_Window_Main = Manager_Window_Main
        Manager_Window_Main.setObjectName("Manager_Window")
        Manager_Window_Main.resize(self.Width, self.Height)
        Manager_Window_Main.setMinimumSize(QtCore.QSize(self.Width, self.Height))
        Manager_Window_Main.setMaximumSize(QtCore.QSize(self.Width, self.Height))
        Manager_Window_Main.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))

        ########
        # Icon #
        ########
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../Pictures/Project - Logo.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Manager_Window_Main.setWindowIcon(icon)

        #########
        # Frame #
        #########
        self.Manager_Window_Frame = QtWidgets.QWidget(Manager_Window_Main)
        self.Manager_Window_Frame.setObjectName("Manager_Window_Frame")

        ###############
        # Blue Layout #
        ###############
        self.Manager_Window_Blue_Frame = QtWidgets.QFrame(self.Manager_Window_Frame)
        self.Manager_Window_Blue_Frame.setGeometry(QtCore.QRect(self.Width / 2, 0, self.Width / 2, self.Height))
        self.Manager_Window_Blue_Frame.setStyleSheet("background-color: rgb(0, 170, 255);")
        self.Manager_Window_Blue_Frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Manager_Window_Blue_Frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Manager_Window_Blue_Frame.setObjectName("Manager_Window_Blue_Frame")

        #####################
        # Prose Style Label #
        #####################
        self.Prose_Style_Transfer_Label = QtWidgets.QLabel(self.Manager_Window_Blue_Frame)
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
        self.Manager_Window_White_Frame = QtWidgets.QFrame(self.Manager_Window_Frame)
        self.Manager_Window_White_Frame.setGeometry(QtCore.QRect(0, 0, self.Width / 2, self.Height))
        self.Manager_Window_White_Frame.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Manager_Window_White_Frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Manager_Window_White_Frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Manager_Window_White_Frame.setObjectName("Manager_Window_White_Frame")

        ####################################
        # Button Without Data Augmentation #
        ####################################
        self.Button_Without_Data_Augmentation = QtWidgets.QPushButton(self.Manager_Window_White_Frame)
        self.Button_Without_Data_Augmentation.setGeometry(QtCore.QRect(self.Width / 25,
                                                                       (self.Height / 2.857) - (self.Height / 8.307),
                                                                        self.Width / 2.320, self.Height / 8.791))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.Button_Without_Data_Augmentation.setFont(font)
        self.Button_Without_Data_Augmentation.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Button_Without_Data_Augmentation.setStyleSheet("background-color: rgb(0, 170, 255);\n" +
                                                            "color: rgb(255, 170, 0);\n"
                                                            "border-radius: 10px; padding: 10px;")
        self.Button_Without_Data_Augmentation.setObjectName("Button_Without_Data_Augmentation")
        self.Button_Without_Data_Augmentation.clicked.connect(self.Running_Model_Without_Data_Augmentation)

        #################################
        # Button With Data Augmentation #
        #################################
        self.Button_With_Data_Augmentation = QtWidgets.QPushButton(self.Manager_Window_White_Frame)
        self.Button_With_Data_Augmentation.setGeometry(QtCore.QRect(self.Width / 25,
                                                                    (self.Height / 2.051) - (self.Height / 8.307),
                                                                     self.Width / 2.320, self.Height / 8.791))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.Button_With_Data_Augmentation.setFont(font)
        self.Button_With_Data_Augmentation.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Button_With_Data_Augmentation.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.Button_With_Data_Augmentation.setStyleSheet("background-color: rgb(0, 170, 255);\n" +
                                                         "color: rgb(255, 170, 0);\n"
                                                         "border-radius: 10px; padding: 10px;")
        self.Button_With_Data_Augmentation.setAutoDefault(False)
        self.Button_With_Data_Augmentation.setObjectName("Button_With_Data_Augmentation")
        self.Button_With_Data_Augmentation.clicked.connect(self.Running_Model_With_Data_Augmentation)

        ########################
        # Button With Settings #
        ########################
        self.Button_Settings = QtWidgets.QPushButton(self.Manager_Window_White_Frame)
        self.Button_Settings.setGeometry(QtCore.QRect(self.Width / 25,
                                                      (self.Height / 1.6) - (self.Height / 8.307),
                                                      self.Width / 2.320, self.Height / 8.791))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.Button_Settings.setFont(font)
        self.Button_Settings.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Button_Settings.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.Button_Settings.setStyleSheet("background-color: rgb(0, 170, 255);\n" +
                                           "color: rgb(255, 170, 0);\n"
                                           "border-radius: 10px; padding: 10px;")
        self.Button_Settings.setAutoDefault(False)
        self.Button_Settings.setObjectName("Button_Settings")
        self.Button_Settings.clicked.connect(self.Setting_Button_Function)

        #################
        # Logout Button #
        #################
        self.Back_Button = QtWidgets.QPushButton(self.Manager_Window_White_Frame)
        self.Back_Button.setGeometry(QtCore.QRect(self.Width / 25,
                                                  (self.Height / 1.311) - (self.Height / 8.307),
                                                  self.Width / 4.45, self.Height / 8.791))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(20)
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
        self.Help_Button = QtWidgets.QPushButton(self.Manager_Window_White_Frame)
        self.Help_Button.setGeometry(QtCore.QRect(self.Width / 3.703,
                                                  (self.Height / 1.311) - (self.Height / 8.307),
                                                  self.Width / 4.975, self.Height / 8.791))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.Help_Button.setFont(font)
        self.Help_Button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Help_Button.setStyleSheet("background-color: rgb(0, 170, 255);\n" +
                                       "color: rgb(255, 170, 0); border-radius: 10px; padding: 10px;")
        self.Help_Button.setObjectName("Help_Button")
        self.Help_Button.clicked.connect(self.Show_Help_Window)

        ################
        # Project Logo #
        ################
        self.Project_Logo = QtWidgets.QLabel(self.Manager_Window_White_Frame)
        self.Project_Logo.setGeometry(QtCore.QRect((self.Width / 6.666) + (self.Width / 19.2),
                                                   (self.Height / 20) - (self.Height / 15.428),
                                                   self.Width / 4.975, (self.Height / 3.791) - (self.Height / 36)))
        self.Project_Logo.setStyleSheet("")
        self.Project_Logo.setText("")
        self.Project_Logo.setPixmap(QtGui.QPixmap("../Pictures/Project - Logo.PNG"))
        self.Project_Logo.setObjectName("Project_Logo")

        ######################
        # Label - Created By #
        ######################
        self.Label_Created_By = QtWidgets.QLabel(self.Manager_Window_White_Frame)
        self.Label_Created_By.setGeometry(QtCore.QRect(self.Width / 24,
                                                       (self.Height / 1.126) - (self.Height / 8.307),
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

        #################
        # Settings Icon #
        #################
        self.Settings_Icon = QtWidgets.QLabel(self.Manager_Window_White_Frame)
        self.Settings_Icon.setGeometry(QtCore.QRect(self.Width / 3.076, (self.Height / 1.523) - (self.Height / 8.307),
                                                    self.Width / 24.390, self.Height / 19.512))
        self.Settings_Icon.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Settings_Icon.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.Settings_Icon.setStyleSheet("background-color: rgb(0, 170, 255);")
        self.Settings_Icon.setText("")
        self.Settings_Icon.setPixmap(QtGui.QPixmap("../Pictures/Settings - Icon.ico"))
        self.Settings_Icon.setScaledContents(True)
        self.Settings_Icon.setAlignment(QtCore.Qt.AlignCenter)
        self.Settings_Icon.setObjectName("Settings_Icon")
        self.Settings_Icon.mousePressEvent = self.Setting_Button_Function

        #############
        # Back Icon #
        #############
        self.Back_Icon = QtWidgets.QLabel(self.Manager_Window_White_Frame)
        self.Back_Icon.setGeometry(QtCore.QRect(self.Width / 4.85, (self.Height / 1.259) - (self.Height / 8.307),
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
        self.Help_Icon = QtWidgets.QLabel(self.Manager_Window_White_Frame)
        self.Help_Icon.setGeometry(QtCore.QRect(self.Width / 2.427, (self.Height / 1.259) - (self.Height / 8.307),
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

        ##################
        # Central Widget #
        ##################
        Manager_Window_Main.setCentralWidget(self.Manager_Window_Frame)
        self.Retranslate_UI(Manager_Window_Main)
        QtCore.QMetaObject.connectSlotsByName(Manager_Window_Main)
        self.Application_Main.aboutToQuit.connect(self.Close_Event_By_X_Button)
        pass

    def Retranslate_UI(self, Manager_Window_Main):
        # Explain Of The Function #
        """
        This Function Fill The Components With Content.
        """

        _translate = QtCore.QCoreApplication.translate
        Manager_Window_Main.setWindowTitle(_translate("Manager_Window", "Prose Style Transfer - Manager Window"))
        self.Prose_Style_Transfer_Label.setText(_translate("Manager_Window", "<html><head/><body><p><span "
                                                                             "style=\" font-size:60pt; "
                                                                             "font-style:italic;\">PROSE<br/>"
                                                                             "STYLE <br/>TRANSFER</span>"
                                                                             "</p></body></html>"))
        self.Button_With_Data_Augmentation.setText(_translate("Manager_Window", "Model With Data Augmentation"))
        self.Button_Settings.setText(_translate("Manager_Window", "Settings"))
        self.Button_Without_Data_Augmentation.setText(_translate("Manager_Window", "Model Without Data Augmentation"))
        self.Back_Button.setText(_translate("AManager_Window", "Back"))
        self.Help_Button.setText(_translate("Manager_Window", "Help"))
        self.Label_Created_By.setText(_translate("Manager_Window", "Created By Din Golan & Matan Peer\n" +
                                                 "Supervisor: Dvora Toledano\n" +
                                                 "Advice Supervisor: Zeev Vladimir Volkovich\n" +
                                                 "Date: 27/01/2020"))
        pass

    def Running_Model_Without_Data_Augmentation(self):
        # Explain Of The Function #
        """
        With This Function We Can Running The Model That We Create Or Already Exist.
        This Model Is Without Data Augmentation.
        """

        # Create New Form #
        self.Select_Versions_Window_Main = QtWidgets.QMainWindow()

        # From #
        from Classes.Select_Versions_Window import Ui_Source_And_Target_Window
        self.Select_Versions_Window_Object = Ui_Source_And_Target_Window(self.Script_Path, self.User_Role, '1')
        self.Select_Versions_Window_Object.Init_UI(self.Application_Main, self.Select_Versions_Window_Main)

        # Close Current Window #
        self.Manager_Window_Main.close()

        # Show Next Window #
        self.Select_Versions_Window_Main.show()
        pass

    def Running_Model_With_Data_Augmentation(self):
        # Explain Of The Function #
        """
        With This Function We Can Running The Model That We Create Or Already Exist.
        This Model Is With Data Augmentation.
        """

        # Create New Form #
        self.Select_Versions_Window_Main = QtWidgets.QMainWindow()

        # From #
        from Classes.Select_Versions_Window import Ui_Source_And_Target_Window
        self.Select_Versions_Window_Object = Ui_Source_And_Target_Window(self.Script_Path, self.User_Role, '2')
        self.Select_Versions_Window_Object.Init_UI(self.Application_Main, self.Select_Versions_Window_Main)

        # Close Current Window #
        self.Manager_Window_Main.close()

        # Show Next Window #
        self.Select_Versions_Window_Main.show()
        pass

    def Setting_Button_Function(self, Event=None):
        # Explain Of The Function #
        """
        With This Function We Will See The Settings Window.
        Note - We Have 'Magic' Parameter.
        """

        if type(Event) == QMouseEvent:
            print("===========================================================================")
            print("\t\t\tMouse Event On - Settings Icon !")
            print("===========================================================================")

        # Create New Form #
        self.Settings_Window_Main = QtWidgets.QMainWindow()

        # From #
        from Classes.Settings_Window import Ui_Settings_Window
        self.Settings_Window_Object = Ui_Settings_Window(self.Script_Path, self.User_Role)
        self.Settings_Window_Object.Init_UI(self.Application_Main, self.Settings_Window_Main)

        # Close Current Window #
        self.Manager_Window_Main.close()

        # Show Settings Window #
        self.Settings_Window_Main.show()
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

    def Back_Button_Function(self, Event=None):
        # Explain Of The Function #
        """
        This Function Back To The Start Window.
        Note - We Have 'Magic' Parameter.
        """

        if type(Event) == QMouseEvent:
            print("===========================================================================")
            print("\t\t\tMouse Event On - Back Icon !")
            print("===========================================================================")

        # Create New Form #
        self.Start_Window_Main = QtWidgets.QMainWindow()

        # From #
        from Classes.Start_Window import Ui_Start_Window
        self.Start_Window_Object = Ui_Start_Window(self.Script_Path)
        self.Start_Window_Object.Init_UI(self.Application_Main, self.Start_Window_Main)

        # Close Current Window #
        self.Manager_Window_Main.close()

        # Show Previous Window #
        self.Start_Window_Main.show()
        pass

    @staticmethod
    def Close_Event_By_X_Button():
        # Explain Of The Function #
        """
        This Function Close The GUI By 'X' Button.
        """

        print("===========================================================================")
        print("\t\t\tThe User Press On - 'X' / 'Close' Button !")
        print("===========================================================================")

        sys.exit(0)
        pass

    pass
