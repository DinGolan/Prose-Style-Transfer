# Imports #
import os
import pickle
import sys
import shelve
import ctypes

# Froms #
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QFileDialog, QMessageBox, QApplication
from PyQt5.QtGui import QMouseEvent


class Ui_Source_And_Target_Window(QMainWindow):

    def __init__(self, Script_Path, User_Role, Choice_Number,
                 Source_Prose_Pick=None, Source_Prose_Path=None,
                 Target_Prose_Pick=None, Target_Prose_Path=None):
        # Explain Of The Function #
        """
        In This Constructor I Have 'Magic' Parameter.
        The 'Magic' Parameter Is - Default Model.
        """

        super(Ui_Source_And_Target_Window, self).__init__()

        # Bring The Width , Height Of The Screen #
        Computer_User = ctypes.windll.user32
        Computer_User.SetProcessDPIAware()
        [Width_Screen, Height_Screen] = [Computer_User.GetSystemMetrics(0), Computer_User.GetSystemMetrics(1)]

        # GUI Attributes #
        self.Source_And_Target_Window_Main = None
        self.Source_And_Target_Frame = None
        self.Source_And_Target_Window_Frame_Blue = None
        self.Prose_Style_Transfer_Label = None
        self.Source_And_Target_Window_Frame_White = None
        self.Back_Button = None
        self.Project_Logo = None
        self.Help_Button = None
        self.Label_Created_By = None
        self.Label_Source_Prose = None
        self.Label_Target_Prose = None
        self.Run_Model_Button = None
        self.Text_Source_Prose = None
        self.Tool_Button_Source_Prose = None
        self.Text_Target_Prose = None
        self.Tool_Button_Target_Prose = None
        self.Run_Model_Icon = None
        self.Back_Icon = None
        self.Help_Icon = None
        self.Application_Main = None

        # Other Component #
        self.User_Window_Main = None
        self.User_Window_Object = None
        self.Manager_Window_Main = None
        self.Manager_Window_Object = None
        self.Progress_Window_Main = None
        self.Progress_Window_Object = None
        self.Create_Model_Window_Main = None
        self.Create_Model_Window_Object = None

        # Program Attributes #
        self.Script_Path = Script_Path
        self.User_Role = User_Role
        self.Choice_Number = Choice_Number
        self.Source_Prose_Pick = Source_Prose_Pick
        self.Source_Prose_Pick_Path = Source_Prose_Path
        self.Target_Prose_Pick = Target_Prose_Pick
        self.Target_Prose_Pick_Path = Target_Prose_Path
        self.Default_Model_Path = None
        self.Width = Width_Screen
        self.Height = Height_Screen
        self.Shelve_Settings_Dictionary = None
        pass

    def Init_UI(self, Application_Main, Select_Versions_Window_Main):
        # Explain Of The Function #
        """
        This Function Make The Initialized Of The GUI.
        """

        ##########
        # Window #
        ##########
        self.Application_Main = Application_Main
        self.Source_And_Target_Window_Main = Select_Versions_Window_Main
        Select_Versions_Window_Main.setObjectName("Source_And_Target_Window")
        Select_Versions_Window_Main.resize(self.Width, self.Height)
        Select_Versions_Window_Main.setMinimumSize(QtCore.QSize(self.Width, self.Height))
        Select_Versions_Window_Main.setMaximumSize(QtCore.QSize(self.Width, self.Height))
        Select_Versions_Window_Main.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        QApplication.restoreOverrideCursor()
        Select_Versions_Window_Main.setWindowTitle("Prose Style Transfer - Select Source & Target Window")

        ########
        # Icon #
        ########
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../Pictures/Project - Logo.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Select_Versions_Window_Main.setWindowIcon(icon)

        #########
        # Frame #
        #########
        self.Source_And_Target_Frame = QtWidgets.QWidget(self)
        self.setObjectName("Source_And_Target_Frame")

        ###############
        # Blue Layout #
        ###############
        self.Source_And_Target_Window_Frame_Blue = QtWidgets.QFrame(self.Source_And_Target_Frame)
        self.Source_And_Target_Window_Frame_Blue.setGeometry(QtCore.QRect(self.Width / 2, 0,
                                                                          self.Width / 2, self.Height))
        self.Source_And_Target_Window_Frame_Blue.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.Source_And_Target_Window_Frame_Blue.setStyleSheet("background-color: rgb(0, 170, 255);")
        self.Source_And_Target_Window_Frame_Blue.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Source_And_Target_Window_Frame_Blue.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Source_And_Target_Window_Frame_Blue.setObjectName("Source_And_Target_Window_Frame_Blue")

        #####################
        # Prose Style Label #
        #####################
        self.Prose_Style_Transfer_Label = QtWidgets.QLabel(self.Source_And_Target_Window_Frame_Blue)
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
        self.Source_And_Target_Window_Frame_White = QtWidgets.QFrame(self.Source_And_Target_Frame)
        self.Source_And_Target_Window_Frame_White.setGeometry(QtCore.QRect(0, 0, self.Width / 2, self.Height))
        self.Source_And_Target_Window_Frame_White.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.Source_And_Target_Window_Frame_White.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Source_And_Target_Window_Frame_White.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Source_And_Target_Window_Frame_White.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Source_And_Target_Window_Frame_White.setObjectName("Source_And_Target_Window_Frame_White")

        ###############
        # Back Button #
        ###############
        self.Back_Button = QtWidgets.QPushButton(self.Source_And_Target_Window_Frame_White)
        self.Back_Button.setGeometry(QtCore.QRect(self.Width / 20,
                                                  (self.Height / 1.702) - (self.Height / 8.307),
                                                  self.Width / 4.7, self.Height / 8.791))
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

        ################
        # Project Logo #
        ################
        self.Project_Logo = QtWidgets.QLabel(self.Source_And_Target_Window_Frame_White)
        self.Project_Logo.setGeometry(QtCore.QRect((self.Width / 6.666) + (self.Width / 17),
                                                   (self.Height / 20) - (self.Height / 11),
                                                   self.Width / 4.975, self.Height / 3.791))
        self.Project_Logo.setStyleSheet("")
        self.Project_Logo.setText("")
        self.Project_Logo.setPixmap(QtGui.QPixmap("../Pictures/Project - Logo.PNG"))
        self.Project_Logo.setObjectName("Project_Logo")

        ###############
        # Help Button #
        ###############
        self.Help_Button = QtWidgets.QPushButton(self.Source_And_Target_Window_Frame_White)
        self.Help_Button.setGeometry(QtCore.QRect(self.Width / 3.703,
                                                  (self.Height / 1.702) - (self.Height / 8.307),
                                                  self.Width / 5.235, self.Height / 8.791))
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

        ######################
        # Label - Created By #
        ######################
        self.Label_Created_By = QtWidgets.QLabel(self.Source_And_Target_Window_Frame_White)
        self.Label_Created_By.setGeometry(QtCore.QRect(self.Width / 21,
                                                       (self.Height / 1.142) - (self.Height / 8.307),
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

        ########################
        # Label - Source Prose #
        ########################
        self.Label_Source_Prose = QtWidgets.QLabel(self.Source_And_Target_Window_Frame_White)
        self.Label_Source_Prose.setGeometry(QtCore.QRect((self.Width / 7) + (self.Width / 17),
                                                         (self.Height / 3.076) - (self.Height / 8.307),
                                                         self.Width / 5.235, self.Height / 19.512))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(17)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.Label_Source_Prose.setFont(font)
        self.Label_Source_Prose.setStyleSheet("color: rgb(255, 170, 0);")
        self.Label_Source_Prose.setObjectName("Label_Source_Prose")

        ########################
        # Label - Target Prose #
        ########################
        self.Label_Target_Prose = QtWidgets.QLabel(self.Source_And_Target_Window_Frame_White)
        self.Label_Target_Prose.setGeometry(QtCore.QRect((self.Width / 7.2) + (self.Width / 17),
                                                         (self.Height / 2.285) - (self.Height / 8.307),
                                                         self.Width / 4.739, self.Height / 19.512))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(17)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.Label_Target_Prose.setFont(font)
        self.Label_Target_Prose.setStyleSheet("color: rgb(255, 170, 0);")
        self.Label_Target_Prose.setObjectName("Label_Target_Prose")

        ######################
        # Button - Run Model #
        ######################
        self.Run_Model_Button = QtWidgets.QPushButton(self.Source_And_Target_Window_Frame_White)
        self.Run_Model_Button.setGeometry(QtCore.QRect(self.Width / 20, (self.Height / 1.333) - (self.Height / 7),
                                                       self.Width / 2.433, self.Height / 8.791))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.Run_Model_Button.setFont(font)
        self.Run_Model_Button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Run_Model_Button.setStyleSheet("background-color: rgb(0, 170, 255);\n"
                                            "color: rgb(255, 170, 0); border-radius: 10px; padding: 10px;")
        self.Run_Model_Button.setObjectName("Run_Model_Button")
        self.Run_Model_Button.clicked.connect(self.Running_The_Model_By_User_OR_Manager)

        #######################
        # Text - Source Prose #
        #######################
        self.Text_Source_Prose = QtWidgets.QTextEdit(self.Source_And_Target_Window_Frame_White)
        self.Text_Source_Prose.setGeometry(QtCore.QRect(self.Width / 6.25, (self.Height / 2.666) - (self.Height / 8.307),
                                                        self.Width / 3.703, self.Height / 21))
        self.Text_Source_Prose.setObjectName("Text_Source_Prose")
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.Text_Source_Prose.setFont(font)
        self.Text_Source_Prose.viewport().setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.Text_Source_Prose.setReadOnly(True)
        # Explain #
        """
        In Case That The User Press On Help Button , And We Want To Remain His Prose Selection ... 
        After He Come Back To The Current Window 
        """
        if self.Source_Prose_Pick is not None:
            self.Text_Source_Prose.setText(self.Source_Prose_Pick)

        ##############################
        # Tool Button - Source Prose #
        ##############################
        self.Tool_Button_Source_Prose = QtWidgets.QToolButton(self.Source_And_Target_Window_Frame_White)
        self.Tool_Button_Source_Prose.setGeometry(QtCore.QRect(self.Width / 11.111, (self.Height / 2.666) - (self.Height / 8.307),
                                                               self.Width / 14.084, self.Height / 21))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.Tool_Button_Source_Prose.setFont(font)
        self.Tool_Button_Source_Prose.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Tool_Button_Source_Prose.setStyleSheet("color: rgb(255, 170, 0); background-color: rgb(0, 170, 255);\n"
                                                    "border-radius: 10px; padding: 10px;")
        self.Tool_Button_Source_Prose.setObjectName("Tool_Button_Source_Prose")
        self.Tool_Button_Source_Prose.clicked.connect(self.Open_File_Dialog_Source_Prose)

        #######################
        # Text - Target Prose #
        #######################
        self.Text_Target_Prose = QtWidgets.QTextEdit(self.Source_And_Target_Window_Frame_White)
        self.Text_Target_Prose.setGeometry(QtCore.QRect(self.Width / 6.25, (self.Height / 2.051) - (self.Height / 8.307),
                                                        self.Width / 3.703, self.Height / 21))
        self.Text_Target_Prose.setObjectName("Text_Target_Prose")
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.Text_Target_Prose.setFont(font)
        self.Text_Target_Prose.viewport().setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.Text_Target_Prose.setReadOnly(True)
        # Explain #
        """
        In Case That The User Press On Help Button , And We Want To Remain His Prose Selection ... 
        After He Come Back To The Current Window 
        """
        if self.Target_Prose_Pick is not None:
            self.Text_Target_Prose.setText(self.Target_Prose_Pick)

        ##############################
        # Tool Button - Target Prose #
        ##############################
        self.Tool_Button_Target_Prose = QtWidgets.QToolButton(self.Source_And_Target_Window_Frame_White)
        self.Tool_Button_Target_Prose.setGeometry(QtCore.QRect(self.Width / 11.111, (self.Height / 2.051) - (self.Height / 8.307),
                                                               self.Width / 14.084, self.Height / 21))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.Tool_Button_Target_Prose.setFont(font)
        self.Tool_Button_Target_Prose.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Tool_Button_Target_Prose.setStyleSheet("color: rgb(255, 170, 0); background-color: rgb(0, 170, 255);\n"
                                                    "border-radius: 10px; padding: 10px;")
        self.Tool_Button_Target_Prose.setObjectName("Tool_Button_Target_Prose")
        self.Tool_Button_Target_Prose.clicked.connect(self.Open_File_Dialog_Target_Prose)

        #############
        # Back Icon #
        #############
        self.Back_Icon = QtWidgets.QLabel(self.Source_And_Target_Window_Frame_White)
        self.Back_Icon.setGeometry(QtCore.QRect(self.Width / 4.85, (self.Height / 1.616) - (self.Height / 8.307),
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
        self.Help_Icon = QtWidgets.QLabel(self.Source_And_Target_Window_Frame_White)
        self.Help_Icon.setGeometry(QtCore.QRect(self.Width / 2.469, (self.Height / 1.616) - (self.Height / 8.307),
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
        # Run Model Icon #
        ##################
        self.Run_Model_Icon = QtWidgets.QLabel(self.Source_And_Target_Window_Frame_White)
        self.Run_Model_Icon.setGeometry(QtCore.QRect(self.Width / 2.941, (self.Height / 1.28) - (self.Height / 7),
                                                     self.Width / 24.390, self.Height / 19.512))
        self.Run_Model_Icon.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Run_Model_Icon.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.Run_Model_Icon.setStyleSheet("background-color: rgb(0, 170, 255);")
        self.Run_Model_Icon.setText("")
        self.Run_Model_Icon.setPixmap(QtGui.QPixmap("../Pictures/Run Model - Icon.ico"))
        self.Run_Model_Icon.setScaledContents(True)
        self.Run_Model_Icon.setAlignment(QtCore.Qt.AlignCenter)
        self.Run_Model_Icon.setObjectName("Run_Model_Icon")
        self.Run_Model_Icon.mousePressEvent = self.Running_The_Model_By_User_OR_Manager

        ##################
        # Central Widget #
        ##################
        Select_Versions_Window_Main.setCentralWidget(self.Source_And_Target_Frame)
        self.Retranslate_UI()
        QtCore.QMetaObject.connectSlotsByName(self.Source_And_Target_Frame)
        self.Application_Main.aboutToQuit.connect(self.Close_Event_By_X_Button)
        pass

    def Retranslate_UI(self):
        # Explain Of The Function #
        """
        This Function Fill The Components With Content.
        """

        _translate = QtCore.QCoreApplication.translate
        self.Prose_Style_Transfer_Label.setText(_translate("Source_And_Target_Window", "<html><head/><body><p><span "
                                                                                       "style=\" font-size:60pt; "
                                                                                       "font-style:italic;\">PROSE<br/>"
                                                                                       "STYLE <br/>TRANSFER</span></p>"
                                                                                       "</body></html>"))
        self.Back_Button.setText(_translate("Source_And_Target_Window", "Back"))
        self.Help_Button.setText(_translate("Source_And_Target_Window", "Help"))
        self.Label_Created_By.setText(_translate("Source_And_Target_Window", "Created By Din Golan & Matan Peer\n" +
                                                 "Supervisor: Dvora Toledano\n" +
                                                 "Advice Supervisor: Zeev Vladimir Volkovich\n" +
                                                 "Date: 27/01/2020"))
        self.Label_Source_Prose.setText(_translate("Source_And_Target_Window", "Select First Version"))
        self.Label_Target_Prose.setText(_translate("Source_And_Target_Window", "Select Second Version"))
        self.Run_Model_Button.setText(_translate("Source_And_Target_Window", "Run Model"))
        self.Tool_Button_Source_Prose.setText(_translate("Source_And_Target_Window", "Browse ..."))
        self.Tool_Button_Target_Prose.setText(_translate("Source_And_Target_Window", "Browse ..."))
        pass

    def Open_File_Dialog_Source_Prose(self):
        # Explain Of The Function #
        """
        This Function Open File Dialog.
        With This Function We Pick The Source Prose.
        """

        try:
            # String #
            Data_Set_Path = ""

            # Check If We Have The Real Path Of The Code #
            if self.Script_Path is None:
                self.Script_Path = os.path.dirname(os.path.realpath(sys.argv[0]))
                if "Classes" in self.Script_Path:
                    self.Script_Path = self.Script_Path.replace("Classes", "")

            # Check If We Have Directory Of Pickle File #
            if os.path.isfile(self.Script_Path + "Pickle Files" +
                              "\\" + "Pickle_Script_Path.pickle"):
                # Load From Pickle File #
                with open(self.Script_Path + "Pickle Files" + "\\" + "Pickle_Script_Path.pickle", 'rb') as Pickle_File:
                    Script_Path = pickle.load(Pickle_File)
            else:
                Script_Path = self.Script_Path

            # Path Of Data Set Model According To The Choice Of The User #
            if self.Choice_Number == '1':
                Data_Set_Path = Script_Path + "Data - Set" + "\\" + "Without - Augmentation" + \
                                "\\" + "Data Set - Before Change" + "\\"
            elif self.Choice_Number == '2':
                Data_Set_Path = Script_Path + "Data - Set" + "\\" + "With - Augmentation" + \
                                "\\" + "Data Set - Before Change" + "\\"

            # Create QFile Dialog #
            if os.path.isdir(Data_Set_Path):
                if os.listdir(Data_Set_Path):
                    Options = QFileDialog.Options()
                    Source_File_Name = QFileDialog.getOpenFileNames(None, "Select Source Prose", Data_Set_Path,
                                                                    "Excel Files (*.xls *.csv)", options=Options)
                    if len(Source_File_Name[0]) > 0:
                        Excel_Path_Pick = Source_File_Name[0]
                        self.Source_Prose_Pick_Path = Excel_Path_Pick
                        Excel_Path_Pick_String = '/'.join(Excel_Path_Pick)
                        Excel_Path_Pick_List = Excel_Path_Pick_String.split('/')
                        Excel_Name_Pick = Excel_Path_Pick_List[len(Excel_Path_Pick_List) - 1]
                        if Excel_Name_Pick.endswith('.xls') or Excel_Name_Pick.endswith('.csv'):
                            self.Text_Source_Prose.setText(Excel_Name_Pick)
                            self.Source_Prose_Pick = Excel_Name_Pick
                            pass
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
                            QMessageBox.warning(self, "Error - The File Is Not Excel", "<p><font color='#ffaa00'>You Pick Wrong File !<br>" +
                                                "The File Should Be Excel File !</font></p>")
                    else:
                        if self.Text_Source_Prose.toPlainText() is None or self.Text_Source_Prose.toPlainText() == "":
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
                            QMessageBox.warning(self, "Error - Problems With File Dialog",
                                                "<p><font color='#ffaa00'>1 - You Press On 'Cancel' Button !<br><br>" +
                                                "2 - You Press On 'X' Button !<br><br>" +
                                                "Please , Select Excel File !</font></p>")
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
                    QMessageBox.critical(self, "Error - Don't Have Files In Data Set",
                                         "<p><font color='#ffaa00'>We Dont Have Any Data Set Files In Directory !<br>" +
                                         "We Need To Insert Them Into The Directory Of Data Set !</font></p>")
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
                QMessageBox.critical(self, "Error - Don't Have Directory Of Data Set",
                                     "<p><font color='#ffaa00'>We Dont Have Directory Of Data Set !</font></p>")

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

    def Open_File_Dialog_Target_Prose(self):
        # Explain Of The Function #
        """
        This Function Open File Dialog.
        With This Function We Pick The Target Prose.
        """

        try:
            # String #
            Data_Set_Path = ""

            # Check If We Have The Real Path Of The Code #
            if self.Script_Path is None:
                self.Script_Path = os.path.dirname(os.path.realpath(sys.argv[0]))
                if "Classes" in self.Script_Path:
                    self.Script_Path = self.Script_Path.replace("Classes", "")

            # Check If We Have Directory Of Pickle File #
            if os.path.isfile(self.Script_Path + "Pickle Files" +
                              "\\" + "Pickle_Script_Path.pickle"):
                # Load From Pickle File #
                with open(self.Script_Path + "Pickle Files" + "\\" + "Pickle_Script_Path.pickle", 'rb') as Pickle_File:
                    Script_Path = pickle.load(Pickle_File)
            else:
                Script_Path = self.Script_Path

            # Path Of Data Set Model According To The Choice Of The User #
            if self.Choice_Number == '1':
                Data_Set_Path = Script_Path + "Data - Set" + "\\" + "Without - Augmentation" + \
                                "\\" + "Data Set - Before Change" + "\\"
            elif self.Choice_Number == '2':
                Data_Set_Path = Script_Path + "Data - Set" + "\\" + "With - Augmentation" + \
                                "\\" + "Data Set - Before Change" + "\\"

            # Create QFile Dialog #
            if os.path.isdir(Data_Set_Path):
                if os.listdir(Data_Set_Path):
                    Options = QFileDialog.Options()
                    Source_File_Name = QFileDialog.getOpenFileNames(None, "Select Target Prose", Data_Set_Path,
                                                                    "Excel Files (*.xls *.csv)", options=Options)
                    if len(Source_File_Name[0]) > 0:
                        Excel_Path_Pick = Source_File_Name[0]
                        self.Target_Prose_Pick_Path = Excel_Path_Pick
                        Excel_Path_Pick_String = '/'.join(Excel_Path_Pick)
                        Excel_Path_Pick_List = Excel_Path_Pick_String.split('/')
                        Excel_Name_Pick = Excel_Path_Pick_List[len(Excel_Path_Pick_List) - 1]
                        if Excel_Name_Pick.endswith('.xls') or Excel_Name_Pick.endswith('.csv'):
                            self.Text_Target_Prose.setText(Excel_Name_Pick)
                            self.Target_Prose_Pick = Excel_Name_Pick
                            pass
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
                            QMessageBox.warning(self, "Error - The File Is Not Excel", "<p><font color='#ffaa00'>You Pick Wrong File !<br>"
                                                                                       "The File Should Be Excel File !</font></p>")
                    else:
                        if self.Text_Target_Prose.toPlainText() is None or self.Text_Target_Prose.toPlainText() == "":
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
                            QMessageBox.warning(self, "Error - Problems With File Dialog",
                                                "<p><font color='#ffaa00'>1 - You Press On 'Cancel' Button !<br><br>" +
                                                "2 - You Press On 'X' Button !<br><br>" +
                                                "Please , Select Excel File !</font></p>")
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
                    QMessageBox.critical(self, "Error - Don't Have Files In Data Set", "<p><font color='#ffaa00'>We Dont Have Any Data Set Files In Directory !<br>" +
                                         "We Need To Insert Them Into The Directory Of Data Set !</font></p>")
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
                QMessageBox.critical(self, "Error - Don't Have Directory Of Data Set",
                                     "<p><font color='#ffaa00'>We Dont Have Directory Of Data Set !</font></p>")

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

    def Running_The_Model_By_User_OR_Manager(self, Event=None):
        # Explain Of The Function #
        """
        With The Function We Will See The Progress Window (If The Model Exist) Or ...
        We Will See The Create Model Window (If The Model Not Exist).
        Note - We Have 'Magic' Parameter.
        """

        try:
            if type(Event) == QMouseEvent:
                print("===========================================================================")
                print("\t\t\tMouse Event On - Run Model Icon !")
                print("===========================================================================")

            # Wait Cursor #
            QApplication.setOverrideCursor(QtCore.Qt.WaitCursor)

            # Check Extreme Case #
            if self.Source_Prose_Pick is None or self.Target_Prose_Pick is None:
                # Default Cursor #
                QApplication.restoreOverrideCursor()

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
                QMessageBox.critical(self, "Error - Need To Select Source & Target Proses",
                                     "<p><font color='#ffaa00'>You Don't Pick Source Prose Or Target Prose !<br>" +
                                     "Please , Select Source Prose & Target Prose !</font></p>")
            else:

                # Check If We Have The Real Path Of The Code #
                if self.Script_Path is None:
                    self.Script_Path = os.path.dirname(os.path.realpath(sys.argv[0]))
                    if "Classes" in self.Script_Path:
                        self.Script_Path = self.Script_Path.replace("Classes", "")

                # Check If We Have Details From Settings Shelve File #
                if os.path.isfile(self.Script_Path + "Pickle , Shelve Files" +
                                  "\\" + "Shelve_Settings.shelve.dat"):
                    """
                    Explain - 
                    Flag 'c' : Open Database For Reading and Writing, Creating It If It Doesnt Exist.
                    """
                    self.Shelve_Settings_Dictionary = shelve.open(self.Script_Path + "Pickle , Shelve Files" + "\\" +
                                                                  "Shelve_Settings.shelve", flag='c')
                else:
                    # Default Values , If Shelve File Not Exist #
                    Shelve_File = dict()
                    Shelve_File["Settings"] = {"Epoch_Number_Text": 10, "Batch_Size_Text": 64,
                                               "Training_Split_Text": 0.7}
                    self.Shelve_Settings_Dictionary = Shelve_File

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
                                                                         User_Controller_Object,
                                                                         None,
                                                                         self.Shelve_Settings_Dictionary)

                        self.Progress_Window_Object.Init_UI(self.Application_Main, self.Progress_Window_Main)

                        # Close Current Window #
                        self.Source_And_Target_Window_Main.close()

                        # Show Next Window #
                        self.Progress_Window_Main.show()
                    else:
                        # Explain #
                        """
                        # If The Model Not Exist The User Will Run {Default Model} OR {Will Get Error Message} #
                        """

                        # Default Cursor #
                        QApplication.restoreOverrideCursor()

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
                        Button_Reply = QMessageBox.question(self, "Warning - Settings",
                                                            "<p><font color='#ffaa00'>Do You Want To Use With The Default Model ?</font></p>",
                                                            QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
                        if Button_Reply == QMessageBox.Yes:

                            # Take Default Model According To Choice Number #
                            if self.Choice_Number == '1':
                                self.Default_Model_Path = self.Script_Path + "Model" + "\\" + "Default - Model" + \
                                                          "\\" + "Model_Without_Augmentation.h5"
                            elif self.Choice_Number == '2':
                                self.Default_Model_Path = self.Script_Path + "Model" + "\\" + "Default - Model" + \
                                                          "\\" + "Model_With_Augmentation.h5"

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
                                                                             User_Controller_Object,
                                                                             self.Default_Model_Path,
                                                                             self.Shelve_Settings_Dictionary)

                            self.Progress_Window_Object.Init_UI(self.Application_Main, self.Progress_Window_Main)

                            # Close Current Window #
                            self.Source_And_Target_Window_Main.close()

                            # Show Next Window #
                            self.Progress_Window_Main.show()

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
                            QMessageBox.critical(self, "No Have - Model To Run",
                                                 "<p><font color='#ffaa00'>You Can't Running New Model , Because It Not Created !</font></p>")
                ###########
                # Manager #
                ###########
                elif self.User_Role == "Manager":
                    # From #
                    from Classes.Manager_Controller import Manager_Controller_Class
                    Manager_Controller_Object = Manager_Controller_Class(self.Script_Path,
                                                                         self.Choice_Number,
                                                                         self.Shelve_Settings_Dictionary)

                    # Check If Manager Fill New Settings #
                    if self.Shelve_Settings_Dictionary["Settings"]["Epoch_Number_Text"] != 10 or \
                       self.Shelve_Settings_Dictionary["Settings"]["Batch_Size_Text"] != 64 or \
                       self.Shelve_Settings_Dictionary["Settings"]["Training_Split_Text"] != 0.7:

                        # Default Cursor #
                        QApplication.restoreOverrideCursor()

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
                        Button_Reply = QMessageBox.question(self, "Information About - New Settings",
                                                            "<p><font color='#ffaa00'>Do You Want To Create New Model<br>" +
                                                            "With The New Settings That You Fill ?<br><br>" +
                                                            "Yes = Create New Model !<br>" +
                                                            "X / No = Check If Exist Model In The System !</font></p>",
                                                            QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

                        if Button_Reply == QMessageBox.Yes:
                            # Create New Form #
                            self.Create_Model_Window_Main = QtWidgets.QMainWindow()

                            # From #
                            from Classes.Create_Model_Window import Ui_Create_Model_Window
                            self.Create_Model_Window_Object = Ui_Create_Model_Window(self.Script_Path,
                                                                                     self.User_Role,
                                                                                     self.Choice_Number,
                                                                                     self.Source_Prose_Pick,
                                                                                     self.Source_Prose_Pick_Path,
                                                                                     self.Target_Prose_Pick,
                                                                                     self.Target_Prose_Pick_Path,
                                                                                     Manager_Controller_Object,
                                                                                     self.Shelve_Settings_Dictionary)

                            self.Create_Model_Window_Object.Init_UI(self.Application_Main, self.Create_Model_Window_Main)

                            # Close Current Window #
                            self.Source_And_Target_Window_Main.close()

                            # Show Previous Window #
                            self.Create_Model_Window_Main.show()

                            # Return From Function, Because We Build New Model #
                            return

                    if Manager_Controller_Object.Check_If_The_Model_Exist():

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
                                                                         Manager_Controller_Object,
                                                                         None,
                                                                         self.Shelve_Settings_Dictionary)

                        self.Progress_Window_Object.Init_UI(self.Application_Main, self.Progress_Window_Main)

                        # Close Current Window #
                        self.Source_And_Target_Window_Main.close()

                        # Show Next Window #
                        self.Progress_Window_Main.show()
                    else:
                        # Explain #
                        """
                        # If The Model Not Exist The Manager Will Run {Default Model} OR {New Model} #
                        """

                        # Default Cursor #
                        QApplication.restoreOverrideCursor()

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
                        Button_Reply = QMessageBox.question(self, "Warning - Settings",
                                                            "<p><font color='#ffaa00'>Do You Want To Use With The Default Model ?<br><br>" +
                                                            "Yes = You Use With Default Model !<br>" +
                                                            "X / No = You Create New Model !</font></p>",
                                                            QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
                        if Button_Reply == QMessageBox.Yes:

                            # Take Default Model According To Choice Number #
                            if self.Choice_Number == '1':
                                self.Default_Model_Path = self.Script_Path + "Model" + "\\" + "Default - Model" + \
                                                          "\\" + "Model_Without_Augmentation.h5"
                            elif self.Choice_Number == '2':
                                self.Default_Model_Path = self.Script_Path + "Model" + "\\" + "Default - Model" + \
                                                          "\\" + "Model_With_Augmentation.h5"
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
                                                                             Manager_Controller_Object,
                                                                             self.Default_Model_Path,
                                                                             self.Shelve_Settings_Dictionary)

                            self.Progress_Window_Object.Init_UI(self.Application_Main, self.Progress_Window_Main)

                            # Close Current Window #
                            self.Source_And_Target_Window_Main.close()

                            # Show Next Window #
                            self.Progress_Window_Main.show()

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
                            QMessageBox.information(self, "Create - New Model",
                                                    "<p><font color='#ffaa00'>The System Will Create New Model For You !<br>" +
                                                    "The Time It Will Take To Create The New Model<br>" +
                                                    "Is Approximately Between 2 - 4 Hours !</font></p>")
                            if QMessageBox.Ok:
                                # Create New Form #
                                self.Create_Model_Window_Main = QtWidgets.QMainWindow()

                                # From #
                                from Classes.Create_Model_Window import Ui_Create_Model_Window
                                self.Create_Model_Window_Object = Ui_Create_Model_Window(self.Script_Path,
                                                                                         self.User_Role,
                                                                                         self.Choice_Number,
                                                                                         self.Source_Prose_Pick,
                                                                                         self.Source_Prose_Pick_Path,
                                                                                         self.Target_Prose_Pick,
                                                                                         self.Target_Prose_Pick_Path,
                                                                                         Manager_Controller_Object,
                                                                                         self.Shelve_Settings_Dictionary)

                                self.Create_Model_Window_Object.Init_UI(self.Application_Main, self.Create_Model_Window_Main)

                                # Close Current Window #
                                self.Source_And_Target_Window_Main.close()

                                # Show Next Window #
                                self.Create_Model_Window_Main.show()

        except Exception as Object_Exception:
            # Default Cursor #
            QApplication.restoreOverrideCursor()

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
        With This Function We Come Back To The Previous Page.
        Note - We Have 'Magic' Parameter.
        """

        if type(Event) == QMouseEvent:
            print("===========================================================================")
            print("\t\t\tMouse Event On - Back Icon !")
            print("===========================================================================")

        if self.User_Role == "User":

            # Create New Form #
            self.User_Window_Main = QtWidgets.QMainWindow()

            # From #
            from Classes.User_Window import Ui_User_Window
            self.User_Window_Object = Ui_User_Window(self.Script_Path, self.User_Role)
            self.User_Window_Object.Init_UI(self.Application_Main, self.User_Window_Main)

            # Close Current Window #
            self.Source_And_Target_Window_Main.close()

            # Show Previous Window #
            self.User_Window_Main.show()

        elif self.User_Role == "Manager":

            # Create New Form #
            self.Manager_Window_Main = QtWidgets.QMainWindow()

            # From #
            from Classes.Manager_Window import Ui_Manager_Window
            self.Manager_Window_Object = Ui_Manager_Window(self.Script_Path, self.User_Role)
            self.Manager_Window_Object.Init_UI(self.Application_Main, self.Manager_Window_Main)

            # Close Current Window #
            self.Source_And_Target_Window_Main.close()

            # Show Previous Window #
            self.Manager_Window_Main.show()
            pass
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
