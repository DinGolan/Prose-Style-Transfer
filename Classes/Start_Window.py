# Imports #
import pickle
import sys
import os
import ctypes

# Froms #
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QMessageBox
from PyQt5.QtGui import QMouseEvent


class Ui_Start_Window(QMainWindow):

    def __init__(self, Script_Path):
        super(Ui_Start_Window, self).__init__()

        # Bring The Width , Height Of The Screen #
        Computer_User = ctypes.windll.user32
        Computer_User.SetProcessDPIAware()
        [Width_Screen, Height_Screen] = [Computer_User.GetSystemMetrics(0), Computer_User.GetSystemMetrics(1)]

        # GUI Attributes #
        self.Start_Window_Main = None
        self.Start_Window_Frame = None
        self.Start_Window_Frame_Blue = None
        self.Prose_Style_Transfer_Label = None
        self.Start_Window_Frame_White = None
        self.Help_Button = None
        self.Label_Created_By = None
        self.Project_Logo = None
        self.Description_Label = None
        self.Start_Button = None
        self.Exit_Button = None
        self.Start_Combo_Box = None
        self.Start_Icon = None
        self.Exit_Icon = None
        self.Help_Icon = None
        self.Message_Box_Icon = None

        # Other Component #
        self.User_Window_Main = None
        self.User_Window_Object = None
        self.Manager_Window_Main = None
        self.Manager_Window_Object = None

        # Program Attributes #
        self.Role = None
        self.Script_Path = Script_Path
        self.Width = Width_Screen
        self.Height = Height_Screen
        pass

    def Init_UI(self, Start_Window_Main):
        # Explain Of The Function #
        """
        This Function Make The Initialized Of The GUI.
        """

        ##########
        # Window #
        ##########
        self.Start_Window_Main = Start_Window_Main
        Start_Window_Main.setObjectName("Start_Window")
        Start_Window_Main.resize(self.Width, self.Height)
        Start_Window_Main.setMinimumSize(QtCore.QSize(self.Width, self.Height))
        Start_Window_Main.setMaximumSize(QtCore.QSize(self.Width, self.Height))
        Start_Window_Main.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        Start_Window_Main.setWindowTitle("Prose Style Transfer - Start Window")

        ########
        # Icon #
        ########
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../Pictures/Project - Logo.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Start_Window_Main.setWindowIcon(icon)
        self.Message_Box_Icon = icon

        #########
        # Frame #
        #########
        self.Start_Window_Frame = QtWidgets.QWidget(Start_Window_Main)
        self.Start_Window_Frame.setObjectName("Start_Window_Frame")

        ###############
        # Blue Layout #
        ###############
        self.Start_Window_Frame_Blue = QtWidgets.QFrame(self.Start_Window_Frame)
        self.Start_Window_Frame_Blue.setGeometry(QtCore.QRect(self.Width / 2, 0,
                                                              self.Width / 2, self.Height))
        self.Start_Window_Frame_Blue.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.Start_Window_Frame_Blue.setStyleSheet("background-color: rgb(0, 170, 255);")
        self.Start_Window_Frame_Blue.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Start_Window_Frame_Blue.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Start_Window_Frame_Blue.setObjectName("Start_Window_Frame_Blue")

        #####################
        # Prose Style Label #
        #####################
        self.Prose_Style_Transfer_Label = QtWidgets.QLabel(self.Start_Window_Frame_Blue)
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
        self.Start_Window_Frame_White = QtWidgets.QFrame(self.Start_Window_Frame)
        self.Start_Window_Frame_White.setGeometry(QtCore.QRect(0, 0, self.Width / 2, self.Height))
        self.Start_Window_Frame_White.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.Start_Window_Frame_White.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Start_Window_Frame_White.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Start_Window_Frame_White.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Start_Window_Frame_White.setObjectName("Start_Window_Frame_White")

        ###############
        # Help Button #
        ###############
        self.Help_Button = QtWidgets.QPushButton(self.Start_Window_Frame_White)
        self.Help_Button.setGeometry(QtCore.QRect(self.Width / 28.571, (self.Height / 1.333) - (self.Height / 8.307),
                                                  self.Width / 4.5, self.Height / 8.791))
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

        ######################
        # Label - Created By #
        ######################
        self.Label_Created_By = QtWidgets.QLabel(self.Start_Window_Frame_White)
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
        self.Project_Logo = QtWidgets.QLabel(self.Start_Window_Frame_White)
        self.Project_Logo.setGeometry(QtCore.QRect((self.Width / 6.451) + (self.Width / 19.7),
                                                   (self.Height / 20) - (self.Height / 15.428),
                                                   self.Width / 4.975, self.Height / 4.210))
        self.Project_Logo.setStyleSheet("")
        self.Project_Logo.setText("")
        self.Project_Logo.setPixmap(QtGui.QPixmap("../Pictures/Project - Logo.PNG"))
        self.Project_Logo.setObjectName("Project_Logo")

        #####################
        # Description Label #
        #####################
        self.Description_Label = QtWidgets.QLabel(self.Start_Window_Frame_White)
        self.Description_Label.setGeometry(QtCore.QRect(self.Width / 25, (self.Height / 4) - (self.Height / 15.428),
                                                        self.Width / 2.320, self.Height / 9.876))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.Description_Label.setFont(font)
        self.Description_Label.setStyleSheet("color: rgb(255, 170, 0);")
        self.Description_Label.setAlignment(QtCore.Qt.AlignCenter)
        self.Description_Label.setObjectName("Description_Label")

        ################
        # Start Button #
        ################
        self.Start_Button = QtWidgets.QPushButton(self.Start_Window_Frame_White)
        self.Start_Button.setGeometry(QtCore.QRect(self.Width / 28.571, (self.Height / 1.632) - (self.Height / 8.307),
                                                   self.Width / 2.298, self.Height / 8.791))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(25)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.Start_Button.setFont(font)
        self.Start_Button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Start_Button.setStyleSheet("background-color: rgb(0, 170, 255);\n" +
                                        "color: rgb(255, 170, 0); border-radius: 10px; padding: 10px;")
        self.Start_Button.setObjectName("Start_Button")
        self.Start_Button.clicked.connect(self.Start_Program)

        ###############
        # Exit Button #
        ###############
        self.Exit_Button = QtWidgets.QPushButton(self.Start_Window_Frame_White)
        self.Exit_Button.setGeometry(QtCore.QRect(self.Width / 3.773, (self.Height / 1.333) - (self.Height / 8.307),
                                                  self.Width / 4.878, self.Height / 8.791))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(25)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.Exit_Button.setFont(font)
        self.Exit_Button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Exit_Button.setStyleSheet("background-color: rgb(0, 170, 255);\n" +
                                       "color: rgb(255, 170, 0); border-radius: 10px; padding: 10px;")
        self.Exit_Button.setObjectName("Exit_Button")
        self.Exit_Button.clicked.connect(self.Exit_Button_Function)

        ###################
        # Start Combo Box #
        ###################
        self.Start_Combo_Box = QtWidgets.QComboBox(self.Start_Window_Frame_White)
        self.Start_Combo_Box.setGeometry(QtCore.QRect(self.Width / 7.142, (self.Height / 2.285) - (self.Height / 8.307),
                                                      self.Width / 4.347, self.Height / 26.666))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(10)
        self.Start_Combo_Box.setFont(font)
        self.Start_Combo_Box.setEditable(False)
        self.Start_Combo_Box.setStyleSheet("color:white; background-color: rgb(255, 170, 0);"
                                           "selection-background-color: rgb(255, 170, 0);"
                                           "border: 3px solid rgb(0, 170, 255);")
        self.Start_Combo_Box.setObjectName("Start_Combo_Box")
        self.Start_Combo_Box.addItems(["", "User", "Manager"])
        self.Start_Combo_Box.view().setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Start_Combo_Box.view().setStyleSheet("color: white; background-color: rgb(255, 170, 0);"
                                                  "border: 3px solid rgb(0, 170, 255);"
                                                  "outline: 1px solid rgb(0, 170, 255);")
        self.Start_Combo_Box.view().setRowHidden(0, True)
        self.Start_Combo_Box.activated[str].connect(self.Pick_The_Role)

        ##############
        # Start Icon #
        ##############
        self.Start_Icon = QtWidgets.QLabel(self.Start_Window_Frame_White)
        self.Start_Icon.setGeometry(QtCore.QRect(self.Width / 3.278, (self.Height / 1.553) - (self.Height / 8.307),
                                                 self.Width / 24.390, self.Height / 19.512))
        self.Start_Icon.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Start_Icon.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.Start_Icon.setStyleSheet("background-color: rgb(0, 170, 255);")
        self.Start_Icon.setText("")
        self.Start_Icon.setPixmap(QtGui.QPixmap("../Pictures/Start.ico"))
        self.Start_Icon.setScaledContents(True)
        self.Start_Icon.setAlignment(QtCore.Qt.AlignCenter)
        self.Start_Icon.setObjectName("Start_Icon")
        self.Start_Icon.mousePressEvent = self.Start_Program

        #############
        # Exit Icon #
        #############
        self.Exit_Icon = QtWidgets.QLabel(self.Start_Window_Frame_White)
        self.Exit_Icon.setGeometry(QtCore.QRect(self.Width / 2.409, (self.Height / 1.28) - (self.Height / 8.307),
                                                self.Width / 24.390, self.Height / 19.512))
        self.Exit_Icon.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Exit_Icon.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.Exit_Icon.setStyleSheet("background-color: rgb(0, 170, 255);")
        self.Exit_Icon.setText("")
        self.Exit_Icon.setPixmap(QtGui.QPixmap("../Pictures/Exit.ico"))
        self.Exit_Icon.setScaledContents(True)
        self.Exit_Icon.setAlignment(QtCore.Qt.AlignCenter)
        self.Exit_Icon.setObjectName("Exit_Icon")
        self.Exit_Icon.mousePressEvent = self.Exit_Button_Function

        #############
        # Help Icon #
        #############
        self.Help_Icon = QtWidgets.QLabel(self.Start_Window_Frame_White)
        self.Help_Icon.setGeometry(QtCore.QRect(self.Width / 5, (self.Height / 1.28) - (self.Height / 8.307),
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
        Start_Window_Main.setCentralWidget(self.Start_Window_Frame)
        self.Retranslate_UI()
        QtCore.QMetaObject.connectSlotsByName(Start_Window_Main)
        pass

    def Retranslate_UI(self):
        # Explain Of The Function #
        """
        This Function Fill The Components With Content.
        """

        _translate = QtCore.QCoreApplication.translate
        self.Prose_Style_Transfer_Label.setText(_translate("Start_Window", "<html><head/><body><p><span "
                                                                           "style=\" font-size:70pt; "
                                                                           "font-style:italic;\">PROSE<br/>"
                                                                           "STYLE <br/>TRANSFER</span>"
                                                                           "</p></body></html>"))
        self.Help_Button.setText(_translate("Start_Window", "Help"))
        self.Label_Created_By.setText(_translate("Start_Window", "Created By Din Golan & Matan Peer\n" +
                                                 "Supervisor: Dvora Toledano\n" +
                                                 "Advice Supervisor: Zeev Vladimir Volkovich\n" +
                                                 "Date: 27/01/2020"))
        self.Description_Label.setText(_translate("Start_Window", "Please , Select Which Role\n" +
                                                  "You Want To Be ?"))
        self.Start_Button.setText(_translate("Start_Window", "Start"))
        self.Exit_Button.setText(_translate("Start_Window", "Exit"))
        pass

    def Pick_The_Role(self, Combo_Box_Text):
        # Explain Of The Function #
        """
        This Function Give For Us The Picking Of The User.
        The Picking Of The User Is Which Role He Want To Run The Program.
        """

        self.Role = Combo_Box_Text
        pass

    def Start_Program(self, Event=None):
        # Explain Of The Function #
        """
        This Function Start The Program According To The User Pick.
        Note - We Have 'Magic' Parameter.
        """

        if type(Event) == QMouseEvent:
            print("===========================================================================")
            print("\t\t\tMouse Event On - Start Icon !")
            print("===========================================================================")

        if self.Role is None:
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
            QMessageBox.critical(self, "Not Picked - Role",
                                 "<p><font color='#ffaa00'>You Not Pick Any Role !<br>" +
                                 "Please , Select Which Role You Want !</font></p>")
        else:
            if self.Role == "User":
                # Create New Form #
                self.User_Window_Main = QtWidgets.QMainWindow()

                # From #
                from Classes.User_Window import Ui_User_Window
                self.User_Window_Object = Ui_User_Window(self.Script_Path, self.Role)
                self.User_Window_Object.Init_UI(self.User_Window_Main)

                # Close Current Window #
                self.Start_Window_Main.close()

                # Show Next Window #
                self.User_Window_Main.show()

            elif self.Role == "Manager":
                # Create New Form #
                self.Manager_Window_Main = QtWidgets.QMainWindow()

                # From #
                from Classes.Manager_Window import Ui_Manager_Window
                self.Manager_Window_Object = Ui_Manager_Window(self.Script_Path, self.Role)
                self.Manager_Window_Object.Init_UI(self.Manager_Window_Main)

                # Close Current Window #
                self.Start_Window_Main.close()

                # Show Next Window #
                self.Manager_Window_Main.show()
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

    def Exit_Button_Function(self, Event=None):
        # Explain Of The Function #
        """
        This Function Close The GUI.
        Note - We Have 'Magic' Parameter.
        """

        if type(Event) == QMouseEvent:
            print("===========================================================================")
            print("\t\t\tMouse Event On - Exit Icon !")
            print("===========================================================================")

        self.Start_Window_Main.close()
        pass

    def Add_Paths_To_System(self):
        # Adding Path's Of Folders To System #
        Temp_Script_Path_Main = self.Script_Path[:-1]

        # Explain #
        """
        1. Final - Project. 
            - Scripts.
        2. Classes.
        3. Model. 
            - Model With Augmentation.
            - Model Without Augmentation.
            - Default Model.
        4. Pictures.
        5. Pickle , Shelve Files.
        6. Data Set.
            - Data Set Without Augmentation.
                - Data Set Before Change.
                    - Version One.
                        - Book One
                        - Book Two.
                        - Book Three.
                        - Book Four.
                        - Book Five.
                    - Version Two.
                        - Book One
                        - Book Two.
                        - Book Three.
                        - Book Four.
                        - Book Five.
                    - Version Three.
                        - Book One
                        - Book Two.
                        - Book Three.
                        - Book Four.
                        - Book Five.
                    - Version Four.
                        - Book One
                        - Book Two.
                        - Book Three.
                        - Book Four.
                        - Book Five.
                - Data Set After Change.
                    - Book One
                    - Book Two.
                    - Book Three.
                    - Book Four.
                    - Book Five.
            - Data Set Without Augmentation.
                - Data Set Before Change.
                    - Version One.
                        - Book One
                        - Book Two.
                        - Book Three.
                        - Book Four.
                        - Book Five.
                    - Version Two.
                        - Book One
                        - Book Two.
                        - Book Three.
                        - Book Four.
                        - Book Five.
                    - Version Three.
                        - Book One
                        - Book Two.
                        - Book Three.
                        - Book Four.
                        - Book Five.
                    - Version Four.
                        - Book One
                        - Book Two.
                        - Book Three.
                        - Book Four.
                        - Book Five.
                - Data Set After Change. 
                    - Book One
                    - Book Two.
                    - Book Three.
                    - Book Four.
                    - Book Five.
        7. Output.
        8. Help.
        """
        sys.path.append(Temp_Script_Path_Main)
        sys.path.append(Script_Path_Main + "venv")
        sys.path.append(Script_Path_Main + "venv" + "\\" + "Include")
        sys.path.append(Script_Path_Main + "venv" + "\\" + "Lib")
        sys.path.append(Script_Path_Main + "venv" + "\\" + "Scripts")
        sys.path.append(Script_Path_Main + "Classes")
        sys.path.append(Script_Path_Main + "Model")
        sys.path.append(Script_Path_Main + "Model" + "\\" + "With - Augmentation")
        sys.path.append(Script_Path_Main + "Model" + "\\" + "Without - Augmentation")
        sys.path.append(Script_Path_Main + "Model" + "\\" + "Default - Model")
        sys.path.append(Script_Path_Main + "Pictures")
        sys.path.append(Script_Path_Main + "Pickle , Shelve Files")

        # Data Set - 1 #
        sys.path.append(Script_Path_Main + "Data - Set")

        # Data Set - 1.1 #
        sys.path.append(Script_Path_Main + "Data - Set" + "\\" + "Without - Augmentation")

        # Data Set - 1.1.1 #
        sys.path.append(Script_Path_Main + "Data - Set" + "\\" + "Without - Augmentation" + "\\" + "Data Set - Before Change")

        # Data Set - 1.1.1.1 #
        sys.path.append(Script_Path_Main + "Data - Set" + "\\" + "Without - Augmentation" +
                        "\\" + "Data Set - Before Change" + "\\" + "ברויאר")

        # Data Set - 1.1.1.1.1 #
        sys.path.append(Script_Path_Main + "Data - Set" + "\\" + "Without - Augmentation" +
                        "\\" + "Data Set - Before Change" + "\\" + "ברויאר" + "\\" + "בראשית")
        # Data Set - 1.1.1.1.2 #
        sys.path.append(Script_Path_Main + "Data - Set" + "\\" + "Without - Augmentation" +
                        "\\" + "Data Set - Before Change" + "\\" + "ברויאר" + "\\" + "שמות")
        # Data Set - 1.1.1.1.3 #
        sys.path.append(Script_Path_Main + "Data - Set" + "\\" + "Without - Augmentation" +
                        "\\" + "Data Set - Before Change" + "\\" + "ברויאר" + "\\" + "ויקרא")
        # Data Set - 1.1.1.1.4 #
        sys.path.append(Script_Path_Main + "Data - Set" + "\\" + "Without - Augmentation" +
                        "\\" + "Data Set - Before Change" + "\\" + "ברויאר" + "\\" + "במדבר")
        # Data Set - 1.1.1.1.5 #
        sys.path.append(Script_Path_Main + "Data - Set" + "\\" + "Without - Augmentation" +
                        "\\" + "Data Set - Before Change" + "\\" + "ברויאר" + "\\" + "דברים")

        # Data Set - 1.1.1.2 #
        sys.path.append(Script_Path_Main + "Data - Set" + "\\" + "Without - Augmentation" +
                        "\\" + "Data Set - Before Change" + "\\" + "לנינגרד")

        # Data Set - 1.1.1.2.1 #
        sys.path.append(Script_Path_Main + "Data - Set" + "\\" + "Without - Augmentation" +
                        "\\" + "Data Set - Before Change" + "\\" + "לנינגרד" + "\\" + "בראשית")
        # Data Set - 1.1.1.2.2 #
        sys.path.append(Script_Path_Main + "Data - Set" + "\\" + "Without - Augmentation" +
                        "\\" + "Data Set - Before Change" + "\\" + "לנינגרד" + "\\" + "שמות")
        # Data Set - 1.1.1.2.3 #
        sys.path.append(Script_Path_Main + "Data - Set" + "\\" + "Without - Augmentation" +
                        "\\" + "Data Set - Before Change" + "\\" + "לנינגרד" + "\\" + "ויקרא")
        # Data Set - 1.1.1.2.4 #
        sys.path.append(Script_Path_Main + "Data - Set" + "\\" + "Without - Augmentation" +
                        "\\" + "Data Set - Before Change" + "\\" + "לנינגרד" + "\\" + "במדבר")
        # Data Set - 1.1.1.2.5 #
        sys.path.append(Script_Path_Main + "Data - Set" + "\\" + "Without - Augmentation" +
                        "\\" + "Data Set - Before Change" + "\\" + "לנינגרד" + "\\" + "דברים")

        # Data Set - 1.1.1.3 #
        sys.path.append(Script_Path_Main + "Data - Set" + "\\" + "Without - Augmentation" +
                        "\\" + "Data Set - Before Change" + "\\" + "קורן")

        # Data Set - 1.1.1.3.1 #
        sys.path.append(Script_Path_Main + "Data - Set" + "\\" + "Without - Augmentation" +
                        "\\" + "Data Set - Before Change" + "\\" + "קורן" + "\\" + "בראשית")
        # Data Set - 1.1.1.3.2 #
        sys.path.append(Script_Path_Main + "Data - Set" + "\\" + "Without - Augmentation" +
                        "\\" + "Data Set - Before Change" + "\\" + "קורן" + "\\" + "שמות")
        # Data Set - 1.1.1.3.3 #
        sys.path.append(Script_Path_Main + "Data - Set" + "\\" + "Without - Augmentation" +
                        "\\" + "Data Set - Before Change" + "\\" + "קורן" + "\\" + "ויקרא")
        # Data Set - 1.1.1.3.4 #
        sys.path.append(Script_Path_Main + "Data - Set" + "\\" + "Without - Augmentation" +
                        "\\" + "Data Set - Before Change" + "\\" + "קורן" + "\\" + "במדבר")
        # Data Set - 1.1.1.3.5 #
        sys.path.append(Script_Path_Main + "Data - Set" + "\\" + "Without - Augmentation" +
                        "\\" + "Data Set - Before Change" + "\\" + "קורן" + "\\" + "דברים")

        # Data Set - 1.1.1.4 #
        sys.path.append(Script_Path_Main + "Data - Set" + "\\" + "Without - Augmentation" +
                        "\\" + "Data Set - Before Change" + "\\" + "תלמוד")

        # Data Set - 1.1.1.4.1 #
        sys.path.append(Script_Path_Main + "Data - Set" + "\\" + "Without - Augmentation" +
                        "\\" + "Data Set - Before Change" + "\\" + "תלמוד" + "\\" + "בראשית")
        # Data Set - 1.1.1.4.2 #
        sys.path.append(Script_Path_Main + "Data - Set" + "\\" + "Without - Augmentation" +
                        "\\" + "Data Set - Before Change" + "\\" + "תלמוד" + "\\" + "שמות")
        # Data Set - 1.1.1.4.3 #
        sys.path.append(Script_Path_Main + "Data - Set" + "\\" + "Without - Augmentation" +
                        "\\" + "Data Set - Before Change" + "\\" + "תלמוד" + "\\" + "ויקרא")
        # Data Set - 1.1.1.4.4 #
        sys.path.append(Script_Path_Main + "Data - Set" + "\\" + "Without - Augmentation" +
                        "\\" + "Data Set - Before Change" + "\\" + "תלמוד" + "\\" + "במדבר")
        # Data Set - 1.1.1.4.5 #
        sys.path.append(Script_Path_Main + "Data - Set" + "\\" + "Without - Augmentation" +
                        "\\" + "Data Set - Before Change" + "\\" + "תלמוד" + "\\" + "דברים")

        # Data Set - 1.1.2 #
        sys.path.append(Script_Path_Main + "Data - Set" + "\\" + "Without - Augmentation" + "\\" + "Data Set - After Change")

        # Data Set - 1.1.2.1 #
        sys.path.append(Script_Path_Main + "Data - Set" + "\\" + "Without - Augmentation" +
                        "\\" + "Data Set - After Change" + "\\" + "בראשית")
        # Data Set - 1.1.2.2 #
        sys.path.append(Script_Path_Main + "Data - Set" + "\\" + "Without - Augmentation" +
                        "\\" + "Data Set - After Change" + "\\" + "שמות")
        # Data Set - 1.1.2.3 #
        sys.path.append(Script_Path_Main + "Data - Set" + "\\" + "Without - Augmentation" +
                        "\\" + "Data Set - After Change" + "\\" + "ויקרא")
        # Data Set - 1.1.2.4 #
        sys.path.append(Script_Path_Main + "Data - Set" + "\\" + "Without - Augmentation" +
                        "\\" + "Data Set - After Change" + "\\" + "במדבר")
        # Data Set - 1.1.2.5 #
        sys.path.append(Script_Path_Main + "Data - Set" + "\\" + "Without - Augmentation" +
                        "\\" + "Data Set - After Change" + "\\" + "דברים")

        # Data Set - 1.2 #
        sys.path.append(Script_Path_Main + "Data - Set" + "\\" + "With - Augmentation")

        # Data Set - 1.2.1 #
        sys.path.append(Script_Path_Main + "Data - Set" + "\\" + "With - Augmentation" + "\\" + "Data Set - Before Change")

        # Data Set - 1.2.1.1 #
        sys.path.append(Script_Path_Main + "Data - Set" + "\\" + "With - Augmentation" +
                        "\\" + "Data Set - Before Change" + "\\" + "ברויאר")

        # Data Set - 1.2.1.1.1 #
        sys.path.append(Script_Path_Main + "Data - Set" + "\\" + "With - Augmentation" +
                        "\\" + "Data Set - Before Change" + "\\" + "ברויאר" + "\\" + "בראשית")
        # Data Set - 1.2.1.1.2 #
        sys.path.append(Script_Path_Main + "Data - Set" + "\\" + "With - Augmentation" +
                        "\\" + "Data Set - Before Change" + "\\" + "ברויאר" + "\\" + "שמות")
        # Data Set - 1.2.1.1.3 #
        sys.path.append(Script_Path_Main + "Data - Set" + "\\" + "With - Augmentation" +
                        "\\" + "Data Set - Before Change" + "\\" + "ברויאר" + "\\" + "ויקרא")
        # Data Set - 1.2.1.1.4 #
        sys.path.append(Script_Path_Main + "Data - Set" + "\\" + "With - Augmentation" +
                        "\\" + "Data Set - Before Change" + "\\" + "ברויאר" + "\\" + "במדבר")
        # Data Set - 1.2.1.1.5 #
        sys.path.append(Script_Path_Main + "Data - Set" + "\\" + "With - Augmentation" +
                        "\\" + "Data Set - Before Change" + "\\" + "ברויאר" + "\\" + "דברים")

        # Data Set - 1.2.1.2 #
        sys.path.append(Script_Path_Main + "Data - Set" + "\\" + "With - Augmentation" +
                        "\\" + "Data Set - Before Change" + "\\" + "לנינגרד")

        # Data Set - 1.2.1.2.1 #
        sys.path.append(Script_Path_Main + "Data - Set" + "\\" + "With - Augmentation" +
                        "\\" + "Data Set - Before Change" + "\\" + "לנינגרד" + "\\" + "בראשית")
        # Data Set - 1.2.1.2.2 #
        sys.path.append(Script_Path_Main + "Data - Set" + "\\" + "With - Augmentation" +
                        "\\" + "Data Set - Before Change" + "\\" + "לנינגרד" + "\\" + "שמות")
        # Data Set - 1.2.1.2.3 #
        sys.path.append(Script_Path_Main + "Data - Set" + "\\" + "With - Augmentation" +
                        "\\" + "Data Set - Before Change" + "\\" + "לנינגרד" + "\\" + "ויקרא")
        # Data Set - 1.2.1.2.4 #
        sys.path.append(Script_Path_Main + "Data - Set" + "\\" + "With - Augmentation" +
                        "\\" + "Data Set - Before Change" + "\\" + "לנינגרד" + "\\" + "במדבר")
        # Data Set - 1.2.1.2.5 #
        sys.path.append(Script_Path_Main + "Data - Set" + "\\" + "With - Augmentation" +
                        "\\" + "Data Set - Before Change" + "\\" + "לנינגרד" + "\\" + "דברים")

        # Data Set - 1.2.1.3 #
        sys.path.append(Script_Path_Main + "Data - Set" + "\\" + "With - Augmentation" +
                        "\\" + "Data Set - Before Change" + "\\" + "קורן")

        # Data Set - 1.2.1.3.1 #
        sys.path.append(Script_Path_Main + "Data - Set" + "\\" + "With - Augmentation" +
                        "\\" + "Data Set - Before Change" + "\\" + "קורן" + "\\" + "בראשית")
        # Data Set - 1.2.1.3.2 #
        sys.path.append(Script_Path_Main + "Data - Set" + "\\" + "With - Augmentation" +
                        "\\" + "Data Set - Before Change" + "\\" + "קורן" + "\\" + "שמות")
        # Data Set - 1.2.1.3.3 #
        sys.path.append(Script_Path_Main + "Data - Set" + "\\" + "With - Augmentation" +
                        "\\" + "Data Set - Before Change" + "\\" + "קורן" + "\\" + "ויקרא")
        # Data Set - 1.2.1.3.4 #
        sys.path.append(Script_Path_Main + "Data - Set" + "\\" + "With - Augmentation" +
                        "\\" + "Data Set - Before Change" + "\\" + "קורן" + "\\" + "במדבר")
        # Data Set - 1.2.1.3.5 #
        sys.path.append(Script_Path_Main + "Data - Set" + "\\" + "With - Augmentation" +
                        "\\" + "Data Set - Before Change" + "\\" + "קורן" + "\\" + "דברים")

        # Data Set - 1.2.1.4 #
        sys.path.append(Script_Path_Main + "Data - Set" + "\\" + "With - Augmentation" +
                        "\\" + "Data Set - Before Change" + "\\" + "תלמוד")

        # Data Set - 1.2.1.4.1 #
        sys.path.append(Script_Path_Main + "Data - Set" + "\\" + "With - Augmentation" +
                        "\\" + "Data Set - Before Change" + "\\" + "תלמוד" + "\\" + "בראשית")
        # Data Set - 1.2.1.4.2 #
        sys.path.append(Script_Path_Main + "Data - Set" + "\\" + "With - Augmentation" +
                        "\\" + "Data Set - Before Change" + "\\" + "תלמוד" + "\\" + "שמות")
        # Data Set - 1.2.1.4.3 #
        sys.path.append(Script_Path_Main + "Data - Set" + "\\" + "With - Augmentation" +
                        "\\" + "Data Set - Before Change" + "\\" + "תלמוד" + "\\" + "ויקרא")
        # Data Set - 1.2.1.4.4 #
        sys.path.append(Script_Path_Main + "Data - Set" + "\\" + "With - Augmentation" +
                        "\\" + "Data Set - Before Change" + "\\" + "תלמוד" + "\\" + "במדבר")
        # Data Set - 1.2.1.4.5 #
        sys.path.append(Script_Path_Main + "Data - Set" + "\\" + "With - Augmentation" +
                        "\\" + "Data Set - Before Change" + "\\" + "תלמוד" + "\\" + "דברים")

        # Data Set - 1.2.2 #
        sys.path.append(Script_Path_Main + "Data - Set" + "\\" + "With - Augmentation" + "\\" + "Data Set - After Change")

        # Data Set - 1.2.2.1 #
        sys.path.append(Script_Path_Main + "Data - Set" + "\\" + "With - Augmentation" +
                        "\\" + "Data Set - After Change" + "\\" + "בראשית")
        # Data Set - 1.2.2.2 #
        sys.path.append(Script_Path_Main + "Data - Set" + "\\" + "With - Augmentation" +
                        "\\" + "Data Set - After Change" + "\\" + "שמות")
        # Data Set - 1.2.2.3 #
        sys.path.append(Script_Path_Main + "Data - Set" + "\\" + "With - Augmentation" +
                        "\\" + "Data Set - After Change" + "\\" + "ויקרא")
        # Data Set - 1.2.2.4 #
        sys.path.append(Script_Path_Main + "Data - Set" + "\\" + "With - Augmentation" +
                        "\\" + "Data Set - After Change" + "\\" + "במדבר")
        # Data Set - 1.2.2.5 #
        sys.path.append(Script_Path_Main + "Data - Set" + "\\" + "With - Augmentation" +
                        "\\" + "Data Set - After Change" + "\\" + "דברים")

        sys.path.append(Script_Path_Main + "Output")
        sys.path.append(Script_Path_Main + "Help")
        pass

    pass


# Not In Used #
"""
# if __name__ == "__main__": #
"""

if __name__.endswith('__main__'):
    # Check If The Folders Of The Project Exist #
    Script_Path_Main = os.path.dirname(os.path.realpath(sys.argv[0]))
    if "Classes" in Script_Path_Main:
        Script_Path_Main = Script_Path_Main.replace("Classes", "")

    # Model Folder #
    if not os.path.exists(Script_Path_Main + "Model"):
        os.mkdir(Script_Path_Main + "Model")
        os.mkdir(Script_Path_Main + "Model" + "\\" + "With - Augmentation")
        os.mkdir(Script_Path_Main + "Model" + "\\" + "Without - Augmentation")
        os.mkdir(Script_Path_Main + "Model" + "\\" + "Default - Model")

    # Pictures Folder #
    if not os.path.exists(Script_Path_Main + "Pictures"):
        os.mkdir(Script_Path_Main + "Pictures")

    # Pickle / Shelve Files Folder #
    if not os.path.exists(Script_Path_Main + "Pickle , Shelve Files"):
        os.mkdir(Script_Path_Main + "Pickle , Shelve Files")
    else:
        if os.path.exists(Script_Path_Main + "Pickle , Shelve Files" + "\\" + "Pickle_Script_Path.pickle"):
            os.remove(Script_Path_Main + "Pickle , Shelve Files" + "\\" + "Pickle_Script_Path.pickle")
        if os.path.exists(Script_Path_Main + "Pickle , Shelve Files" + "\\" + "Shelve_Settings.shelve.bak"):
            os.remove(Script_Path_Main + "Pickle , Shelve Files" + "\\" + "Shelve_Settings.shelve.bak")
        if os.path.exists(Script_Path_Main + "Pickle , Shelve Files" + "\\" + "Shelve_Settings.shelve.dat"):
            os.remove(Script_Path_Main + "Pickle , Shelve Files" + "\\" + "Shelve_Settings.shelve.dat")
        if os.path.exists(Script_Path_Main + "Pickle , Shelve Files" + "\\" + "Shelve_Settings.shelve.dir"):
            os.remove(Script_Path_Main + "Pickle , Shelve Files" + "\\" + "Shelve_Settings.shelve.dir")

    # Data Set Folder #
    if not os.path.exists(Script_Path_Main + "Data - Set"):
        os.mkdir(Script_Path_Main + "Data - Set" + "\\" + "With - Augmentation")
        os.mkdir(Script_Path_Main + "Data - Set" + "\\" + "With - Augmentation" + "\\" + "Data Set - Before Change")
        os.mkdir(Script_Path_Main + "Data - Set" + "\\" + "With - Augmentation" + "\\" + "Data Set - After Change")

        os.mkdir(Script_Path_Main + "Data - Set" + "\\" + "Without - Augmentation")
        os.mkdir(Script_Path_Main + "Data - Set" + "\\" + "Without - Augmentation" + "\\" + "Data Set - Before Change")
        os.mkdir(Script_Path_Main + "Data - Set" + "\\" + "Without - Augmentation" + "\\" + "Data Set - After Change")

    # Output Folder #
    if not os.path.exists(Script_Path_Main + "Output"):
        os.mkdir(Script_Path_Main + "Output")

    # Help Folder #
    if not os.path.exists(Script_Path_Main + "Help"):
        os.mkdir(Script_Path_Main + "Help")

    # Save Variable In Pickle File #
    with open(Script_Path_Main + "\\" + "Pickle , Shelve Files" + "\\" +
              "Pickle_Script_Path.pickle", 'wb') as Pickle_File:
        pickle.dump(Script_Path_Main, Pickle_File)

    # Create Application #
    Application = QtWidgets.QApplication(sys.argv)
    Start_Window = QtWidgets.QMainWindow()
    Start_Window_Object = Ui_Start_Window(Script_Path_Main)
    Start_Window_Object.Add_Paths_To_System()
    Start_Window_Object.Init_UI(Start_Window)
    Start_Window.show()
    sys.exit(Application.exec_())
    pass
