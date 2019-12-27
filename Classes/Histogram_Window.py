# Imports #
import ctypes
import os
import sys

# Froms #
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QMessageBox
from PyQt5.QtGui import QMouseEvent


class Ui_Histogram_Window(QMainWindow):

    def __init__(self, Script_Path, User_Role, Choice_Number, Source_Prose_Pick,
                 Target_Prose_Pick, Accuracy, Max_Values, All_Prediction_List):
        super(Ui_Histogram_Window, self).__init__()

        # Bring The Width , Height Of The Screen #
        Computer_User = ctypes.windll.user32
        Computer_User.SetProcessDPIAware()
        [Width_Screen, Height_Screen] = [Computer_User.GetSystemMetrics(0), Computer_User.GetSystemMetrics(1)]

        # GUI Attributes #
        self.Histogram_Window_Main = None
        self.Histogram_Window_Frame = None
        self.Histogram_Window_Frame_Blue = None
        self.Prose_Style_Transfer_Label = None
        self.Histogram_Window_Frame_White = None
        self.Back_Button = None
        self.Back_Button = None
        self.Label_Created_By = None
        self.Project_Logo = None
        self.Help_Button = None
        self.Help_Icon = None
        self.Back_Icon = None
        self.Histogram_Picture = None
        self.Application_Main = None

        # Other Component #
        self.Results_Window_Main = None
        self.Results_Window_Object = None

        # Program Attributes #
        self.Script_Path = Script_Path
        self.User_Role = User_Role
        self.Choice_Number = Choice_Number
        self.Source_Prose_Pick = Source_Prose_Pick
        self.Target_Prose_Pick = Target_Prose_Pick
        self.Accuracy = Accuracy
        self.Max_Values = Max_Values
        self.All_Prediction_List = All_Prediction_List
        self.Width = Width_Screen
        self.Height = Height_Screen
        pass

    def Init_UI(self, Application_Main, Histogram_Window_Main):
        # Explain Of The Function #
        """
        This Function Make The Initialized Of The GUI.
        """

        ##########
        # Window #
        ##########
        self.Application_Main = Application_Main
        self.Histogram_Window_Main = Histogram_Window_Main
        Histogram_Window_Main.setObjectName("Histogram_Window")
        Histogram_Window_Main.resize(self.Width, self.Height)
        Histogram_Window_Main.setMinimumSize(QtCore.QSize(self.Width, self.Height))
        Histogram_Window_Main.setMaximumSize(QtCore.QSize(self.Width, self.Height))
        Histogram_Window_Main.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        Histogram_Window_Main.setWindowTitle("Prose Style Transfer - Histogram Window")

        ########
        # Icon #
        ########
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../Pictures/Project - Logo.ico"),
                       QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Histogram_Window_Main.setWindowIcon(icon)

        #########
        # Frame #
        #########
        self.Histogram_Window_Frame = QtWidgets.QWidget(Histogram_Window_Main)
        self.Histogram_Window_Frame.setObjectName("Histogram_Window_Frame")

        ###############
        # Blue Layout #
        ###############
        self.Histogram_Window_Frame_Blue = QtWidgets.QFrame(self.Histogram_Window_Frame)
        self.Histogram_Window_Frame_Blue.setGeometry(QtCore.QRect(self.Width / 2, 0,
                                                                  self.Width / 2, self.Height))
        self.Histogram_Window_Frame_Blue.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.Histogram_Window_Frame_Blue.setStyleSheet("background-color: rgb(0, 170, 255);")
        self.Histogram_Window_Frame_Blue.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Histogram_Window_Frame_Blue.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Histogram_Window_Frame_Blue.setObjectName("Histogram_Window_Frame_Blue")

        #####################
        # Prose Style Label #
        #####################
        self.Prose_Style_Transfer_Label = QtWidgets.QLabel(self.Histogram_Window_Frame_Blue)
        self.Prose_Style_Transfer_Label.setGeometry(QtCore.QRect(self.Width / 12.5, self.Height / 5,
                                                                 self.Width / 2.849, self.Height / 1.900))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Prose_Style_Transfer_Label.sizePolicy().hasHeightForWidth())
        self.Prose_Style_Transfer_Label.setSizePolicy(sizePolicy)
        self.Prose_Style_Transfer_Label.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.Prose_Style_Transfer_Label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.Prose_Style_Transfer_Label.setStyleSheet("color: rgb(255, 170, 0);\n"
                                                      "font: 87 8pt \"Segoe UI Black\";")
        self.Prose_Style_Transfer_Label.setAlignment(QtCore.Qt.AlignCenter)
        self.Prose_Style_Transfer_Label.setObjectName("Prose_Style_Transfer_Label")

        ################
        # White Layout #
        ################
        self.Histogram_Window_Frame_White = QtWidgets.QFrame(self.Histogram_Window_Frame)
        self.Histogram_Window_Frame_White.setGeometry(QtCore.QRect(0, 0, self.Width / 2, self.Height))
        self.Histogram_Window_Frame_White.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.Histogram_Window_Frame_White.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Histogram_Window_Frame_White.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Histogram_Window_Frame_White.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Histogram_Window_Frame_White.setObjectName("Histogram_Window_Frame_White")

        ###############
        # Back Button #
        ###############
        self.Back_Button = QtWidgets.QPushButton(self.Histogram_Window_Frame_White)
        self.Back_Button.setGeometry(QtCore.QRect(self.Width / 28.571, (self.Height / 1.333) - (self.Height / 10),
                                                  self.Width / 4.5, self.Height / 8.791))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.Back_Button.setFont(font)
        self.Back_Button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Back_Button.setStyleSheet("background-color: rgb(0, 170, 255);\n"
                                       "color: rgb(255, 170, 0); border-radius: 10px; padding: 10px;")
        self.Back_Button.setObjectName("Back_Button")
        self.Back_Button.clicked.connect(self.Back_Button_Function)

        ####################
        # Label Created By #
        ####################
        self.Label_Created_By = QtWidgets.QLabel(self.Histogram_Window_Frame_White)
        self.Label_Created_By.setGeometry(QtCore.QRect(self.Width / 24, (self.Height / 1.126) - (self.Height / 8.307),
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
        self.Project_Logo = QtWidgets.QLabel(self.Histogram_Window_Frame_White)
        self.Project_Logo.setGeometry(QtCore.QRect((self.Width / 6.451) + (self.Width / 19.7),
                                                   (self.Height / 20) - (self.Height / 10),
                                                    self.Width / 4.975, self.Height / 4.210))
        self.Project_Logo.setStyleSheet("")
        self.Project_Logo.setText("")
        self.Project_Logo.setPixmap(QtGui.QPixmap("../Pictures/Project - Logo.PNG"))
        self.Project_Logo.setObjectName("Project_Logo")

        ###############
        # Help Button #
        ###############
        self.Help_Button = QtWidgets.QPushButton(self.Histogram_Window_Frame_White)
        self.Help_Button.setGeometry(QtCore.QRect(self.Width / 3.773, (self.Height / 1.333) - (self.Height / 10),
                                                  self.Width / 4.878, self.Height / 8.791))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.Help_Button.setFont(font)
        self.Help_Button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Help_Button.setStyleSheet("background-color: rgb(0, 170, 255);\n"
                                       "color: rgb(255, 170, 0); border-radius: 10px; padding: 10px;")
        self.Help_Button.setObjectName("Help_Button")
        self.Help_Button.clicked.connect(self.Show_Help_Window)

        #####################
        # Histogram Picture #
        #####################
        self.Histogram_Picture = QtWidgets.QLabel(self.Histogram_Window_Frame_White)
        self.Histogram_Picture.setGeometry(QtCore.QRect(self.Width / 25, (self.Height / 6),
                                                        self.Width / 2.298, self.Height / 2.11))
        self.Histogram_Picture.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.Histogram_Picture.setPixmap(QtGui.QPixmap("../Pictures/Histogram Result - Picture.png"))
        self.Histogram_Picture.setScaledContents(True)
        self.Histogram_Picture.setObjectName("Histogram_Picture")

        #############
        # Help Icon #
        #############
        self.Help_Icon = QtWidgets.QLabel(self.Histogram_Window_Frame_White)
        self.Help_Icon.setGeometry(QtCore.QRect(self.Width / 2.409, (self.Height / 1.28) - (self.Height / 10),
                                                self.Width / 24.390, self.Height / 19.512))
        self.Help_Icon.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Help_Icon.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.Help_Icon.setStyleSheet("background-color: rgb(0, 170, 255);")
        self.Help_Icon.setPixmap(QtGui.QPixmap("../Pictures/Help - Icon.ico"))
        self.Help_Icon.setScaledContents(True)
        self.Help_Icon.setAlignment(QtCore.Qt.AlignCenter)
        self.Help_Icon.setObjectName("Help_Icon")
        self.Help_Icon.mousePressEvent = self.Show_Help_Window

        #############
        # Back Icon #
        #############
        self.Back_Icon = QtWidgets.QLabel(self.Histogram_Window_Frame_White)
        self.Back_Icon.setGeometry(QtCore.QRect(self.Width / 5, (self.Height / 1.28) - (self.Height / 10),
                                                self.Width / 24.390, self.Height / 19.512))
        self.Back_Icon.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Back_Icon.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.Back_Icon.setStyleSheet("background-color: rgb(0, 170, 255);")
        self.Back_Icon.setPixmap(QtGui.QPixmap("../Pictures/Back - Icon.ico"))
        self.Back_Icon.setScaledContents(True)
        self.Back_Icon.setAlignment(QtCore.Qt.AlignCenter)
        self.Back_Icon.setObjectName("Back_Icon")
        self.Back_Icon.mousePressEvent = self.Back_Button_Function

        ##################
        # Central Widget #
        ##################
        Histogram_Window_Main.setCentralWidget(self.Histogram_Window_Frame)
        self.Retranslate_UI()
        QtCore.QMetaObject.connectSlotsByName(Histogram_Window_Main)
        self.Application_Main.aboutToQuit.connect(self.Close_Event_By_X_Button)
        pass

    def Retranslate_UI(self):
        # Explain Of The Function #
        """
        This Function Fill The Components With Content.
        """

        _translate = QtCore.QCoreApplication.translate
        self.Prose_Style_Transfer_Label.setText(_translate("Histogram_Window",
                                                           "<html><head/><body><p><span "
                                                           "style=\" font-size:60pt; "
                                                           "font-style:italic;\">PROSE<br/>STYLE "
                                                           "<br/>TRANSFER</span></p></body></html>"))
        self.Back_Button.setText(_translate("Histogram_Window", "Back"))
        self.Label_Created_By.setText(_translate("Histogram_Window", "Created By Din Golan & Matan Peer\n"
                                                                     "Supervisor: Dvora Toledano\n"
                                                                     "Advice Supervisor: Zeev Vladimir Volkovich\n"
                                                                     "Date: 27/01/2020"))
        self.Help_Button.setText(_translate("Histogram_Window", "Help"))
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
        self.Results_Window_Main = QtWidgets.QMainWindow()

        # From #
        from Classes.Results_Window import Ui_Results_Window
        self.Results_Window_Object = Ui_Results_Window(self.Script_Path, self.User_Role,
                                                       self.Choice_Number, self.Source_Prose_Pick,
                                                       self.Target_Prose_Pick, self.Accuracy,
                                                       self.Max_Values, self.All_Prediction_List)
        self.Results_Window_Object.Init_UI(self.Application_Main, self.Results_Window_Main)

        # Close Current Window #
        self.Histogram_Window_Main.close()

        # Show Previous Window #
        self.Results_Window_Main.show()
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
