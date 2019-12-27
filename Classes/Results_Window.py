# Imports #
import os
import xlwt
import re
import sys
import ctypes
import numpy
import pandas
import matplotlib
matplotlib.use('Qt5Agg')

# Froms #
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QFileDialog, QMessageBox, QApplication
from PyQt5.QtGui import QMouseEvent
from matplotlib import pyplot, pylab
from xlwt import Workbook


class Ui_Results_Window(QMainWindow):

    def __init__(self, Script_Path, User_Role, Choice_Number, Source_Prose_Pick,
                 Target_Prose_Pick, Accuracy, Max_Values, All_Prediction_List):
        super(Ui_Results_Window, self).__init__()

        # Bring The Width , Height Of The Screen #
        Computer_User = ctypes.windll.user32
        Computer_User.SetProcessDPIAware()
        [Width_Screen, Height_Screen] = [Computer_User.GetSystemMetrics(0), Computer_User.GetSystemMetrics(1)]

        # GUI Attributes #
        self.Results_Window_Main = None
        self.Results_Window_Frame = None
        self.Results_Window_Frame_Blue = None
        self.Prose_Style_Transfer_Label = None
        self.Results_Window_Frame_White = None
        self.Home_Button = None
        self.Label_Created_By = None
        self.Project_Logo = None
        self.Result_Label = None
        self.Result_Excel_Label = None
        self.Help_Button = None
        self.Histogram_Button = None
        self.Excel_Picture = None
        self.Home_Icon = None
        self.Help_Icon = None
        self.Histogram_Icon = None
        self.Application_Main = None

        # Other Component #
        self.User_Window_Main = None
        self.User_Window_Object = None
        self.Manager_Window_Main = None
        self.Manager_Window_Object = None
        self.Histogram_Window_Main = None
        self.Histogram_Window_Object = None

        # Program Attributes #
        self.Script_Path = Script_Path
        self.User_Role = User_Role
        self.Choice_Number = Choice_Number
        self.Accuracy = Accuracy
        self.Max_Values = Max_Values
        self.All_Prediction_List = All_Prediction_List
        self.Source_Prose_Pick = Source_Prose_Pick
        self.Target_Prose_Pick = Target_Prose_Pick
        self.Output_Excel_Name = "Model_Final_Output.xls"
        self.Width = Width_Screen
        self.Height = Height_Screen
        pass

    def Init_UI(self, Application_Main, Results_Window_Main):
        # Explain Of The Function #
        """
        This Function Make The Initialized Of The GUI.
        """

        ##########
        # Window #
        ##########
        self.Application_Main = Application_Main
        self.Results_Window_Main = Results_Window_Main
        Results_Window_Main.setObjectName("Results_Window")
        Results_Window_Main.resize(self.Width, self.Height)
        Results_Window_Main.setMinimumSize(QtCore.QSize(self.Width, self.Height))
        Results_Window_Main.setMaximumSize(QtCore.QSize(self.Width, self.Height))
        Results_Window_Main.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        QApplication.restoreOverrideCursor()
        Results_Window_Main.setWindowTitle("Prose Style Transfer - Results Window")

        ########
        # Icon #
        ########
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../Pictures/Project - Logo.ico"),
                       QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Results_Window_Main.setWindowIcon(icon)

        #########
        # Frame #
        #########
        self.Results_Window_Frame = QtWidgets.QWidget(Results_Window_Main)
        self.Results_Window_Frame.setObjectName("Results_Window_Frame")

        ###############
        # Blue Layout #
        ###############
        self.Results_Window_Frame_Blue = QtWidgets.QFrame(self.Results_Window_Frame)
        self.Results_Window_Frame_Blue.setGeometry(QtCore.QRect(self.Width / 2, 0, self.Width / 2, self.Height))
        self.Results_Window_Frame_Blue.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.Results_Window_Frame_Blue.setStyleSheet("background-color: rgb(0, 170, 255);")
        self.Results_Window_Frame_Blue.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Results_Window_Frame_Blue.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Results_Window_Frame_Blue.setObjectName("Results_Window_Frame_Blue")

        #####################
        # Prose Style Label #
        #####################
        self.Prose_Style_Transfer_Label = QtWidgets.QLabel(self.Results_Window_Frame_Blue)
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
        self.Results_Window_Frame_White = QtWidgets.QFrame(self.Results_Window_Frame)
        self.Results_Window_Frame_White.setGeometry(QtCore.QRect(0, 0, self.Width / 2, self.Height))
        self.Results_Window_Frame_White.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.Results_Window_Frame_White.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Results_Window_Frame_White.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Results_Window_Frame_White.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Results_Window_Frame_White.setObjectName("Results_Window_Frame_White")

        ###############
        # Home Button #
        ###############
        self.Home_Button = QtWidgets.QPushButton(self.Results_Window_Frame_White)
        self.Home_Button.setGeometry(QtCore.QRect(self.Width / 50, (self.Height / 1.777) - (self.Height / 8.307),
                                                  self.Width / 4.3, self.Height / 8.791))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.Home_Button.setFont(font)
        self.Home_Button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Home_Button.setStyleSheet("background-color: rgb(0, 170, 255);\n"
                                       "color: rgb(255, 170, 0); border-radius: 10px; padding: 10px;")
        self.Home_Button.setObjectName("Home_Button")
        self.Home_Button.clicked.connect(self.Home_Button_Function)

        ######################
        # Label - Created By #
        ######################
        self.Label_Created_By = QtWidgets.QLabel(self.Results_Window_Frame_White)
        self.Label_Created_By.setGeometry(QtCore.QRect(self.Width / 25, (self.Height / 1.176) - (self.Height / 8.307),
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
        self.Project_Logo = QtWidgets.QLabel(self.Results_Window_Frame_White)
        self.Project_Logo.setGeometry(QtCore.QRect((self.Width / 6.666) + (self.Width / 19),
                                                   (self.Height / 20) - (self.Height / 16),
                                                   self.Width / 4.975, self.Height / 3.791))
        self.Project_Logo.setStyleSheet("")
        self.Project_Logo.setText("")
        self.Project_Logo.setPixmap(QtGui.QPixmap("../Pictures/Project - Logo.PNG"))
        self.Project_Logo.setObjectName("Project_Logo")

        ################
        # Result Label #
        ################
        self.Result_Label = QtWidgets.QLabel(self.Results_Window_Frame_White)
        self.Result_Label.setGeometry(QtCore.QRect(self.Width / 20, (self.Height / 2.9) - (self.Height / 7),
                                                   self.Width / 2.5, self.Height / 9.876))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(17)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.Result_Label.setFont(font)
        self.Result_Label.setStyleSheet("color: rgb(255, 170, 0);")
        self.Result_Label.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.Result_Label.setObjectName("Result_Label")

        ######################
        # Result Excel Label #
        ######################
        self.Result_Excel_Label = QtWidgets.QLabel(self.Results_Window_Frame_White)
        self.Result_Excel_Label.setGeometry(QtCore.QRect(self.Width / 20, (self.Height / 2.222) - (self.Height / 7),
                                                         self.Width / 5.524, self.Height / 15.686))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(17)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.Result_Excel_Label.setFont(font)
        self.Result_Excel_Label.setStyleSheet("color: rgb(255, 170, 0);")
        self.Result_Excel_Label.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.Result_Excel_Label.setObjectName("Result_Excel_Label")

        ###############
        # Help Button #
        ###############
        self.Help_Button = QtWidgets.QPushButton(self.Results_Window_Frame_White)
        self.Help_Button.setGeometry(QtCore.QRect(self.Width / 3.846, (self.Height / 1.777) - (self.Height / 8.307),
                                                  self.Width / 4.545, self.Height / 8.791))
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

        ####################
        # Histogram Button #
        ####################
        self.Histogram_Button = QtWidgets.QPushButton(self.Results_Window_Frame_White)
        self.Histogram_Button.setGeometry(QtCore.QRect(self.Width / 50, (self.Height / 1.428) - (self.Height / 8.307),
                                                       self.Width / 2.169, self.Height / 8.791))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.Histogram_Button.setFont(font)
        self.Histogram_Button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Histogram_Button.setStyleSheet("background-color: rgb(0, 170, 255);\n"
                                            "color: rgb(255, 170, 0); border-radius: 10px; padding: 10px;")
        self.Histogram_Button.setObjectName("Histogram_Button")
        self.Histogram_Button.clicked.connect(self.Create_Histogram)

        #################
        # Excel Picture #
        #################
        self.Excel_Picture = QtWidgets.QLabel(self.Results_Window_Frame_White)
        self.Excel_Picture.setGeometry(QtCore.QRect(self.Width / 7, (self.Height / 2.222) - (self.Height / 7.7),
                                                    self.Width / 32, self.Height / 22))
        self.Excel_Picture.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Excel_Picture.setPixmap(QtGui.QPixmap("../Pictures/Excel_Picture.ico"))
        self.Excel_Picture.setObjectName("Excel_Picture")
        self.Excel_Picture.mousePressEvent = self.Take_Excel_Model_Output

        #############
        # Home Icon #
        #############
        self.Home_Icon = QtWidgets.QLabel(self.Results_Window_Frame_White)
        self.Home_Icon.setGeometry(QtCore.QRect(self.Width / 5.25, (self.Height / 1.684) - (self.Height / 8.307),
                                                self.Width / 24.390, self.Height / 19.512))
        self.Home_Icon.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Home_Icon.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.Home_Icon.setStyleSheet("background-color: rgb(0, 170, 255);")
        self.Home_Icon.setText("")
        self.Home_Icon.setPixmap(QtGui.QPixmap("../Pictures/Home - Icon.ico"))
        self.Home_Icon.setScaledContents(True)
        self.Home_Icon.setAlignment(QtCore.Qt.AlignCenter)
        self.Home_Icon.setObjectName("Home_Icon")
        self.Home_Icon.mousePressEvent = self.Home_Button_Function

        #############
        # Help Icon #
        #############
        self.Help_Icon = QtWidgets.QLabel(self.Results_Window_Frame_White)
        self.Help_Icon.setGeometry(QtCore.QRect(self.Width / 2.398, (self.Height / 1.684) - (self.Height / 8.307),
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
        # Histogram Icon #
        ##################
        self.Histogram_Icon = QtWidgets.QLabel(self.Results_Window_Frame_White)
        self.Histogram_Icon.setGeometry(QtCore.QRect(self.Width / 2.702, (self.Height / 1.367) - (self.Height / 8.307),
                                        self.Width / 24.390, self.Height / 19.512))
        self.Histogram_Icon.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Histogram_Icon.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.Histogram_Icon.setStyleSheet("background-color: rgb(0, 170, 255);")
        self.Histogram_Icon.setPixmap(QtGui.QPixmap("../Pictures/Histogram - Icon.ico"))
        self.Histogram_Icon.setScaledContents(True)
        self.Histogram_Icon.setAlignment(QtCore.Qt.AlignCenter)
        self.Histogram_Icon.setObjectName("Histogram_Icon")
        self.Histogram_Icon.mousePressEvent = self.Create_Histogram

        ##################
        # Central Widget #
        ##################
        Results_Window_Main.setCentralWidget(self.Results_Window_Frame)
        self.Retranslate_UI()
        QtCore.QMetaObject.connectSlotsByName(Results_Window_Main)
        self.Application_Main.aboutToQuit.connect(self.Close_Event_By_X_Button)

        ##############
        # Excel File #
        ##############
        self.Create_Output_Excel_File()
        pass

    def Retranslate_UI(self):
        # Explain Of The Function #
        """
        This Function Fill The Components With Content.
        """

        _translate = QtCore.QCoreApplication.translate
        self.Prose_Style_Transfer_Label.setText(_translate("Results_Window",
                                                           "<html><head/><body><p><span "
                                                           "style=\" font-size:60pt; "
                                                           "font-style:italic;\">PROSE<br/>"
                                                           "STYLE <br/>TRANSFER</span></p></body></html>"))
        self.Home_Button.setText(_translate("Results_Window", "Home"))
        self.Label_Created_By.setText(_translate("Results_Window", "Created By Din Golan & Matan Peer\n" +
                                                 "Supervisor: Dvora Toledano\n" +
                                                 "Advice Supervisor: Zeev Vladimir Volkovich\n" +
                                                 "Date: 27/01/2020"))
        self.Result_Label.setText(_translate("Results_Window", "Accuracy Between The Versions Is - " +
                                             str(self.Accuracy) + "% !"))
        self.Result_Excel_Label.setText(_translate("Results_Window", "Output Result - "))
        self.Help_Button.setText(_translate("Results_Window", "Help"))
        self.Histogram_Button.setText(_translate("Results_Window", "Show Histogram"))
        pass

    def Home_Button_Function(self, Event=None):
        # Explain Of The Function #
        """
        With This Function We Will See The Home Page.
        We Return From The Current Page (Result Window) To The Home Window.
        Note - We Have 'Magic' Parameter.
        """

        try:
            if type(Event) == QMouseEvent:
                print("===========================================================================")
                print("\t\t\tMouse Event On - Home Icon !")
                print("===========================================================================")

            if self.User_Role == "User":
                # Create New Form #
                self.User_Window_Main = QtWidgets.QMainWindow()

                # From #
                from Classes.User_Window import Ui_User_Window
                self.User_Window_Object = Ui_User_Window(self.Script_Path, self.User_Role)
                self.User_Window_Object.Init_UI(self.Application_Main, self.User_Window_Main)

                # Close Current Window #
                self.Results_Window_Main.close()

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
                self.Results_Window_Main.close()

                # Show Previous Window #
                self.Manager_Window_Main.show()
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
            QMessageBox.critical(self, "Error - Exception", "<p><font color='#ffaa00'>Cant Back To Home Window !<br>" 
                                                            "The Exception Is - <br>" +
                                                            str(Object_Exception) + " !</font></p>")
        pass

    def Create_Output_Excel_File(self):
        # Explain Of The Function #
        """
        This Function Create For Us Output Excel (Part From The Final Results).
        """

        try:
            # Integer #
            Index_Excel = 1

            # Check If Directory Exist #
            if not os.path.exists(self.Script_Path + "Output"):
                os.makedirs(self.Script_Path + "Output")

            # Check If File Exist #
            if os.path.isfile(self.Script_Path + "Output" + "\\" + self.Output_Excel_Name) is True:
                os.remove(self.Script_Path + "Output" + "\\" + self.Output_Excel_Name)

            # Workbook is created
            Workbook_Object = Workbook()

            # 'add_sheet' is used to create sheet.
            Sheet_One = Workbook_Object.add_sheet(self.Output_Excel_Name)

            # Style #
            Style_One = xlwt.easyxf('font: bold off, color black;\
                                     borders: top_color black, bottom_color black, right_color black, left_color black,\
                                              left thin, right thin, top thin, bottom thin;\
                                     pattern: pattern solid, fore_color Yellow;\
                                     align: horiz center')
            Style_Two = xlwt.easyxf('font: bold off, color black;\
                                     borders: top_color black, bottom_color black, right_color black, left_color black,\
                                              left thin, right thin, top thin, bottom thin;\
                                     pattern: pattern solid, fore_color white;\
                                     align: horiz left')
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
            if self.Choice_Number == '1':
                Sheet_One.col(0).width = int(130 * 260)
                Sheet_One.col(1).width = int(130 * 260)
                Sheet_One.col(2).width = int(50 * 260)
            elif self.Choice_Number == '2':
                Sheet_One.col(0).width = int(220 * 260)
                Sheet_One.col(1).width = int(210 * 260)
                Sheet_One.col(2).width = int(50 * 260)

            # Remove '.csv' From Headlines #
            if '.csv' in self.Source_Prose_Pick:
                self.Source_Prose_Pick = re.sub('.csv', '', self.Source_Prose_Pick)
            if '.csv' in self.Target_Prose_Pick:
                self.Target_Prose_Pick = re.sub('.csv', '', self.Target_Prose_Pick)

            # HeadLines #
            Sheet_One.write(0, 0, self.Source_Prose_Pick, Style_One)
            Sheet_One.write(0, 1, self.Target_Prose_Pick, Style_One)
            Sheet_One.write(0, 2, 'Max - Accuracy', Style_One)

            for Tuple in self.Max_Values:
                # For Hebrew #
                if self.Choice_Number == '1':
                    Sheet_One.write(Index_Excel, 0, Tuple[0], Style_Four)
                    Sheet_One.write(Index_Excel, 1, Tuple[1], Style_Four)

                # For English #
                elif self.Choice_Number == '2':
                    Sheet_One.write(Index_Excel, 0, Tuple[0], Style_Two)
                    Sheet_One.write(Index_Excel, 1, Tuple[1], Style_Two)

                Sheet_One.write(Index_Excel, 2, float(Tuple[2]), Style_Three)
                Index_Excel += 1

            # Save The Excel File #
            Workbook_Object.save(self.Script_Path + "Output" + "\\" + self.Output_Excel_Name)
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
            QMessageBox.critical(self, "Error - Exception", "<p><font color='#ffaa00'>Cant Create File !<br>" +
                                                            "The Exception Is - <br>" +
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

    def Take_Excel_Model_Output(self, Event=None):
        """
        This Function Take The Output Excel From Specific Directory.
        Note - We Have 'Magic' Parameter.
        """
        try:
            if type(Event) == QMouseEvent:
                print("===========================================================================")
                print("\t\t\tMouse Event On - Excel Icon !")
                print("===========================================================================")

            # Check If Directory Exist #
            if not os.path.exists(self.Script_Path + "Output"):
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
                QMessageBox.critical(self, "Directory - Not Exist",
                                     "<p><font color='#ffaa00'>Directory Of Model Output Not Exist !</font></p>")
            else:
                # Check If File Exist #
                if not os.path.isfile(self.Script_Path + "Output" + "\\" + self.Output_Excel_Name):
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
                    QMessageBox.critical(self, "File - Not Exist",
                                         "<p><font color='#ffaa00'>File Of Model Output Not Exist !</font></p>")
                else:
                    # Take File #
                    Options = QFileDialog.Options()
                    Output_File = QFileDialog.getOpenFileNames(None, "File - Output Model",
                                                               self.Script_Path + "Output" + "\\",
                                                               "Excel Files (*.xls *.csv)", options=Options)

                    # Explain #
                    """
                    # Output_File[0] = List That Include The Output File Path #
                    # Output_File[0][0] = Output File Path #
                    """
                    if len(Output_File[0]) > 0:
                        os.startfile(Output_File[0][0])

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
            QMessageBox.critical(self, "Error - Exception", "<p><font color='#ffaa00'>No Have Access To Model Output !<br>" +
                                                            "The Exception Is - <br>" +
                                                            str(Object_Exception) + " !</font></p>")
        pass

    def Create_Histogram(self, Event=None):
        # Explain Of The Function #
        """
        This Function Create New Histogram From Our Data.
        """

        try:
            if type(Event) == QMouseEvent:
                print("===========================================================================")
                print("\t\t\tMouse Event On - Histogram Icon !")
                print("===========================================================================")

            # Wait Cursor #
            QApplication.setOverrideCursor(QtCore.Qt.WaitCursor)

            # Take Details From Output Excel #
            List_Of_Accuracy = self.Take_Accuracy_List_From_Excel()

            if List_Of_Accuracy is not None:
                # Set The Range Of X Axis #
                pyplot.xlim([0, 100])

                # In Case Of - 100% Match In Some Compressions #
                Index = 0
                while Index < len(List_Of_Accuracy):
                    if List_Of_Accuracy[Index] == 1.0:
                        List_Of_Accuracy[Index] = 0.95
                    Index += 1

                # Histogram #
                pyplot.hist(list(map(lambda Value: Value * 100, List_Of_Accuracy)),
                            bins='auto', histtype='bar', facecolor='orange')

                # Figure Title & Bar #
                Figure = pylab.gcf()
                Figure.set_size_inches(10, 9)
                Figure.canvas.set_window_title('Histogram - Result')
                Figure.canvas.window().statusBar().setVisible(False)
                pyplot.title('Histogram - Compressions Between Sentences', color='#00aaff', fontsize=25, fontstyle='italic')

                # Not In Used #
                """
                Figure.canvas.manager.window.wm_geometry("+%d+%d" % (self.Width / 4.5, self.Height / 20)) 
                """

                # Color & Size Of Axis , Title #
                Axis = pyplot.gca()
                Title = Axis.title
                Title.set_position([.5, 1.05])
                Axis.xaxis.set_ticks(numpy.arange(0, 110, 10))
                X_Ticks_Labels = ['0%', '10%', '20%', '30%', '40%', '50%', '60%', '70%', '80%', '90%', '100%']
                Axis.set_xticklabels(X_Ticks_Labels)
                Axis.tick_params(axis='x', colors='black', labelsize=16, pad=30)
                Axis.tick_params(axis='y', colors='black', labelsize=16, pad=15)
                Axis.xaxis.label.set_color('#00aaff')
                Axis.yaxis.label.set_color('#00aaff')

                # Labels Of Figure #
                pyplot.xlabel('Accuracy', fontsize=20, fontstyle='italic', labelpad=15)
                pyplot.ylabel('Count Of Compressions', fontsize=20, fontstyle='italic', labelpad=20)

                # Set Fonts #
                self.set_fonts(Axis)

                # Check If Picture Exist #
                if os.path.exists(self.Script_Path + "Pictures" + "\\" + "Histogram Result - Picture.png"):
                    os.remove(self.Script_Path + "Pictures" + "\\" + "Histogram Result - Picture.png")

                # Save Plot #
                pyplot.savefig(self.Script_Path + "Pictures" + "\\" + "Histogram Result - Picture.png", bbox_inches='tight')

                self.Show_Histogram_Window()
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
                QMessageBox.critical(self, "Don't Have Values To Present At - Histogram",
                                     "<p><font color='#ffaa00'>We Don't Have Values To Present At Histogram !</font></p>")
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
                                 "<p><font color='#ffaa00'>We Cant Present Histogram Because Exception !<br>" +
                                 "The Exception Is - <br>" +
                                 str(Object_Exception) + " !</font></p>")
        pass

    @staticmethod
    def set_fonts(Axis):

        Title_Font = {'weight': 'bold',
                      'size': '25'}
        Axes_Font = {'weight': 'bold'}

        Axis.set_title(Axis.get_title(), **Title_Font)
        Axis.set_ylabel(Axis.get_ylabel(), **Axes_Font)
        Axis.set_xlabel(Axis.get_xlabel(), **Axes_Font)
        pyplot.setp(Axis.get_xticklabels(), fontweight='bold', fontstyle='italic')
        pyplot.setp(Axis.get_yticklabels(), fontweight='bold', fontstyle='italic')
        pass

    def Show_Histogram_Window(self):
        # Explain Of The Function #
        """
        With This Function We Present The Histogram Window.
        Note - We Have 'Magic' Parameter.
        """

        # Default Cursor #
        QApplication.restoreOverrideCursor()

        # Create New Form #
        self.Histogram_Window_Main = QtWidgets.QMainWindow()

        # From #
        from Classes.Histogram_Window import Ui_Histogram_Window
        self.Histogram_Window_Object = Ui_Histogram_Window(self.Script_Path, self.User_Role,
                                                           self.Choice_Number, self.Source_Prose_Pick,
                                                           self.Target_Prose_Pick, self.Accuracy,
                                                           self.Max_Values, self.All_Prediction_List)
        self.Histogram_Window_Object.Init_UI(self.Application_Main, self.Histogram_Window_Main)

        # Close Current Window #
        self.Results_Window_Main.close()

        # Show Next Window #
        self.Histogram_Window_Main.show()
        pass

    def Take_Accuracy_List_From_Excel(self):
        # Explain Of The Function #
        """
        This Function Take The Values Of Accuracy From Excel.
        """

        try:
            if not os.path.exists(self.Script_Path + "Output"):

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
                QMessageBox.critical(self, "Output Directory - Not Exist",
                                     "<p><font color='#ffaa00'>The Output Directory Not Exist !<br>" +
                                     "We Cant Show You Histogram Of The Results !</font></p>")
                return None

            elif not os.path.exists(self.Script_Path + "Output" + "\\" + "Model_Final_Output.xls"):

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
                QMessageBox.critical(self, "Output File - Not Exist",
                                     "<p><font color='#ffaa00'>The Output File Not Exist !<br>" +
                                     "We Cant Show You Histogram Of The Results !</font></p>")
                return None

            else:
                Result_From_Pandas = pandas.read_excel(self.Script_Path + "\\" + "Output" + "\\" +
                                                       "Model_Final_Output.xls", encoding='utf-8',
                                                       error_bad_lines=False)
                return list(Result_From_Pandas["Max - Accuracy"])

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
                                 "<p><font color='#ffaa00'>Exception When Trying To Bring Details <br>" +
                                 "From Output Excel File !<br>" +
                                 "The Exception Is - <br>" + str(Object_Exception) + "</font></p>")
            return None
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
