# Imports #
import os
import sys

# From #
from cx_Freeze import Executable, setup

# Real Path Of File #
Exe_Directory = os.path.dirname(__file__)
Exe_Directory = Exe_Directory.replace("/","\\")
Project_Directory = Exe_Directory.replace("Executable","")

# Packages #
Packages = ["pickle", "sys", "os", "ctypes", "shelve", "pandas", "math", "xlwt", "re",
            "nlpaug", "numpy", "keras", "sklearn", "gc", "gensim", "shutil", "PyQt5",
            "PyQt5.QtWidgets", "PyQt5.QtGui", "PyQt5.QtCore"]

# Include Files #
Include_Files = [

    # DLL #
    (os.path.join(Project_Directory + "venv" + "\\" + "Lib" + "\\" + "tcl8.6", "init.tcl"), "init.tcl"),

    # Py Classes #
    (Project_Directory + "Classes" + "\\" + "Create_Model_Window.py", "Create_Model_Window.py"),
    (Project_Directory + "Classes" + "\\" + "Manager_Build_Data_Set.py","Manager_Build_Data_Set.py"),
    (Project_Directory + "Classes" + "\\" + "Manager_Config.py","Manager_Config.py"),
    (Project_Directory + "Classes" + "\\" + "Manager_Controller.py","Manager_Controller.py"),
    (Project_Directory + "Classes" + "\\" + "Manager_Input_Handler.py","Manager_Input_Handler.py"),
    (Project_Directory + "Classes" + "\\" + "Manager_Model.py","Manager_Model.py"),
    (Project_Directory + "Classes" + "\\" + "Manager_Window.py","Manager_Window.py"),
    (Project_Directory + "Classes" + "\\" + "Progress_Window.py","Progress_Window.py"),
    (Project_Directory + "Classes" + "\\" + "Results_Window.py","Results_Window.py"),
    (Project_Directory + "Classes" + "\\" + "Select_Versions_Window.py","Select_Versions_Window.py"),
    (Project_Directory + "Classes" + "\\" + "Settings_Window.py","Settings_Window.py"),
    (Project_Directory + "Classes" + "\\" + "User_Controller.py","User_Controller.py"),
    (Project_Directory + "Classes" + "\\" + "User_Window.py","User_Window.py"),

    # Help #
    (Project_Directory + "Help" + "\\" + "Prose Style Transfer - Help Page.docx","Prose Style Transfer - Help Page.docx"),
    (Project_Directory + "Help" + "\\" + "Prose Style Transfer - Help Page.pdf","Prose Style Transfer - Help Page.pdf"),

    # Model #
    (Project_Directory + "Model" + "\\" + "Default - Model" + "\\" + "Model_With_Augmentation.h5","Model_With_Augmentation.h5"),
    (Project_Directory + "Model" + "\\" + "Default - Model" + "\\" + "Model_Without_Augmentation.h5","Model_Without_Augmentation.h5"),
    (Project_Directory + "Model" + "\\" + "With - Augmentation" + "\\" + "Model_With_Augmentation.h5","Model_With_Augmentation.h5"),
    (Project_Directory + "Model" + "\\" + "Without - Augmentation" + "\\" + "Model_Without_Augmentation.h5","Model_Without_Augmentation.h5"),

    # Pictures #
    (Project_Directory + "Pictures" + "\\" + "Apply - Icon.ico","Apply - Icon.ico"),
    (Project_Directory + "Pictures" + "\\" + "Back - Icon.ico","Back - Icon.ico"),
    (Project_Directory + "Pictures" + "\\" + "Build Model - Icon.ico","Build Model - Icon.ico"),
    (Project_Directory + "Pictures" + "\\" + "Build_Model.ico","Build_Model.ico"),
    (Project_Directory + "Pictures" + "\\" + "Close - Icon.ico","Close - Icon.ico"),
    (Project_Directory + "Pictures" + "\\" + "Excel_Picture.ico","Excel_Picture.ico"),
    (Project_Directory + "Pictures" + "\\" + "Exit.ico","Exit.ico"),
    (Project_Directory + "Pictures" + "\\" + "Help - Icon.ico","Help - Icon.ico"),
    (Project_Directory + "Pictures" + "\\" + "Home - Icon.ico","Home - Icon.ico"),
    (Project_Directory + "Pictures" + "\\" + "Predict - Icon.ico","Predict - Icon.ico"),
    (Project_Directory + "Pictures" + "\\" + "Project - Logo.ico","Project - Logo.ico"),
    (Project_Directory + "Pictures" + "\\" + "Project - Logo.PNG","Project - Logo.PNG"),
    (Project_Directory + "Pictures" + "\\" + "Run Model - Icon.ico","Run Model - Icon.ico"),
    (Project_Directory + "Pictures" + "\\" + "Settings - Icon.ico","Settings - Icon.ico"),
    (Project_Directory + "Pictures" + "\\" + "Start.ico","Start.ico"),
    (Project_Directory + "Pictures" + "\\" + "Wait_Image.ico","Wait_Image.ico"),
]

# Executable Constructor #
Base = 'Win32GUI' if sys.platform == "win32" else None

GUI_To_Exe = Executable(script=Project_Directory + "Classes" + "\\" + "Start_Window.py",
                        base=Base,
                        targetName="Prose Style Transfer.exe",
                        icon=Project_Directory + "Pictures" + "\\" + "Project - Logo.ico")

# Set Up Constructor #
setup(name='Prose Style Transfer - Project',
      version='6.0',
      description='Prose Style Transfer',
      author="Din Golan & Matan Peer",
      options={'build_exe': {'packages':Packages,
                             'include_files':Include_Files}},
      executables=[GUI_To_Exe])
