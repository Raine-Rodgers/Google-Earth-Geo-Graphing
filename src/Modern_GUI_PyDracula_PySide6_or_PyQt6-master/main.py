# ///////////////////////////////////////////////////////////////
#
# BY: WANDERSON M.PIMENTA
# PROJECT MADE WITH: Qt Designer and PySide6
# V: 1.0.0
#
# This project can be used freely for all uses, as long as they maintain the
# respective credits only in the Python scripts, any information in the visual
# interface (GUI) can be modified without any implication.
#
# There are limitations on Qt licenses if you want to use your products
# commercially, I recommend reading them on the official website:
# https://doc.qt.io/qtforpython/licenses.html
#
# ///////////////////////////////////////////////////////////////

import sys
import os
import platform
from BackEnd.polygonMake import *
import tkinter
from tkinter import filedialog, messagebox # import responsible for error messaging and file import
import pickle

# IMPORT / GUI AND MODULES AND WIDGETS
# ///////////////////////////////////////////////////////////////
from modules import *
from widgets import *
os.environ["QT_FONT_DPI"] = "96" # FIX Problem for High DPI and Scale above 100%

# SET AS GLOBAL WIDGETS
# ///////////////////////////////////////////////////////////////
widgets = None


class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        # SET AS GLOBAL WIDGETS
        # ///////////////////////////////////////////////////////////////
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        app = QApplication(sys.argv)
        global widgets
        widgets = self.ui
        tkinter.Tk().withdraw() # prevents an empty tkinter window from appearing

        # USE CUSTOM TITLE BAR | USE AS "False" FOR MAC OR LINUX
        # ///////////////////////////////////////////////////////////////
        Settings.ENABLE_CUSTOM_TITLE_BAR = True

        # APP NAME
        # ///////////////////////////////////////////////////////////////
        title = "GE Creator"
        description = "Google Earth Graphing Creator"
        # APPLY TEXTS
        self.setWindowTitle(title)
        widgets.titleRightInfo.setText(description)

        # TOGGLE MENU
        # ///////////////////////////////////////////////////////////////
        widgets.toggleButton.clicked.connect(lambda: UIFunctions.toggleMenu(self, True))

        # SET UI DEFINITIONS
        # ///////////////////////////////////////////////////////////////
        UIFunctions.uiDefinitions(self)

        # QTableWidget PARAMETERS
        # ///////////////////////////////////////////////////////////////
        widgets.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        # BUTTONS CLICK
        # ///////////////////////////////////////////////////////////////

        # LEFT MENUS
        widgets.btn_home.clicked.connect(self.HomeButton)
        widgets.btn_new.clicked.connect(self.NewButton)
        widgets.btn_save.clicked.connect(self.SaveButton)
        widgets.btn_addRow.clicked.connect(self.AddRowButton)
        widgets.btn_deleteRow.clicked.connect(self.DeleteRowButton)
        widgets.btn_importFile.clicked.connect(self.ImportFileButton)
        app.aboutToQuit.connect(myExitHandler) # myExitHandler is a callable
        #TODO: find the import file button and connect it to a function

        # EXTRA LEFT BOX
        def openCloseLeftBox():
            UIFunctions.toggleLeftBox(self, True)
        widgets.toggleLeftBox.clicked.connect(openCloseLeftBox)
#        widgets.extraCloseColumnBtn.clicked.connect(openCloseLeftBox)

        # EXTRA RIGHT BOX
        def openCloseRightBox():
            UIFunctions.toggleRightBox(self, True)
        widgets.settingsTopBtn.clicked.connect(openCloseRightBox)

        # SHOW APP
        # ///////////////////////////////////////////////////////////////
        self.show()

        # SET CUSTOM THEME
        # ///////////////////////////////////////////////////////////////
        useCustomTheme = False
        # themeFile = "themes\py_dracula_light.qss"

        # SET THEME AND HACKS
        # if useCustomTheme:
        #     # LOAD AND APPLY STYLE
        #     UIFunctions.theme(self, themeFile, True)

        #     # SET HACKS
        #     AppFunctions.setThemeHack(self)

        # SET HOME PAGE AND SELECT MENU
        # ///////////////////////////////////////////////////////////////
        widgets.stackedWidget.setCurrentWidget(widgets.widgets)
        widgets.widgets.setStyleSheet(UIFunctions.selectMenu(widgets.widgets.styleSheet()))


    # BUTTONS CLICK
    # Post here your functions for clicked buttons
    # ///////////////////////////////////////////////////////////////
    def HomeButton(self):
        # GET BUTTON CLICKED
        btn = self.sender()
        btnName = btn.objectName()

        widgets.stackedWidget.setCurrentWidget(widgets.widgets)
        UIFunctions.resetStyle(self, "btn_widget")
        btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))
        print(f'Button "{btnName}" pressed!')

    def NewButton(self):
        # GET BUTTON CLICKED
        btn = self.sender()
        btnName = btn.objectName()

        # SHOW NEW PAGE
        widgets.stackedWidget.setCurrentWidget(widgets.new_page) # SET PAGE
        UIFunctions.resetStyle(self, btnName) # RESET ANOTHERS BUTTONS SELECTED
        btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet())) # SELECT MENU
        print(f'Button "{btnName}" pressed!')

    def AddRowButton(self):
            # GET BUTTON CLICKED
            btn = self.sender()
            btnName = btn.objectName()

            row_position = widgets.tableWidget.rowCount()
            widgets.tableWidget.insertRow(row_position)
            print(f'Button "{btnName}" pressed!')

    def DeleteRowButton(self):
        # GET BUTTON CLICKED
        btn = self.sender()
        btnName = btn.objectName()

        if widgets.tableWidget.rowCount() > 1:
            widgets.tableWidget.removeRow(widgets.tableWidget.rowCount() - 1)
        print(f'Button "{btnName}" pressed!')

    def ImportFileButton(self):
        #TODO: read kml file
        #TODO: set table size to what the parsed file declares
        #TODO: set all values to what the parsed file declares
        #TODO: set file name to what the parsed file declares
        #TODO: 
        folder_path = filedialog.askdirectory()
        print(folder_path)

    def SaveButton(self):
        # GET BUTTON CLICKED
        btn = self.sender()
        btnName = btn.objectName()

        row = 0
        column = 0
        x = float(0)
        y = float(0)
        polygonName = ""
        value = float(0)
        coordinates = []
        outlineIsChecked = False
        print(f'Button "{btnName}" pressed!')

        def isCellEmpty(): # no clue what None is but it works... i think kinda at least
            if widgets.tableWidget.item(row, column) is None or not widgets.tableWidget.item(row, column).text().isdigit():
                return True
            else:
                return False

        # function which sets value variable to the input of line edit 5 if radio button 6 is checked
        # ///////////////////////////////////////////////////////////////
        def CheckConstantHeight():
            if widgets.radioButton_6.isChecked() and not CheckLineEdit5Empty():
                value = float(widgets.lineEdit_5.text())
            else: value = 0
        
        # is line edit 5 empty
        # ///////////////////////////////////////////////////////////////
        def CheckLineEdit5Empty():
            if widgets.lineEdit_5.text() == ('' or ""): return True
            else: return False
        # create coords
        # ///////////////////////////////////////////////////////////////
        
        # 2D array iteration type beat
        for row in range(1, widgets.tableWidget.rowCount()):
            for column in range(widgets.tableWidget.columnCount()):
                if column == 0:
                    if isCellEmpty(): x = 48.0677873; y = 12.8578328 #just realised this shit be fucked cuz if y is declared afterwards it might be funky but who asked
                    else: x=float(widgets.tableWidget.item(row, column).text())
                elif column == 1:
                    if isCellEmpty(): x = 48.0677873; y = 12.8578328
                    else: y=float(widgets.tableWidget.item(row, column).text())
                elif column == 2:
                    if isCellEmpty(): polygonName = "No-Name"
                    else: polygonName=widgets.tableWidget.item(row, column).text()
                elif column == 3:
                    if not isCellEmpty(): value=float(widgets.tableWidget.item(row, column).text())
                    elif CheckLineEdit5Empty(): value = 0
                    else: CheckConstantHeight()
            coordinates.append(CreateCoordinates(x, y, value, polygonName))

        if widgets.checkBox.isChecked(): outlineIsChecked = True
        if not (widgets.lineEdit.text() is None or widgets.lineEdit.text()==""):
            finalFile = MakeFile(coordinates, widgets.lineEdit.text(), outlineIsChecked)
            finalFile.makePolygon()
            finalFile.saveFile()
        else: messagebox.showerror("Error", "Please enter a file name")
        # PRINT BTN NAME
        print(f'Button "{btnName}" pressed!')

    def myExitHandler(self):
        tableValuesUnpickled = []
        for row in range(1, widgets.tableWidget.rowCount()):
            for column in range(widgets.tableWidget.columnCount()):
                tableValuesUnpickled.append(widgets.tableWidget.item(row, column).text())
        tableValuesPickled = pickle.dumps(tableValuesUnpickled)
        #TODO: save table values to a file when program is closed


        #TODO: set table size to what the parsed file declares
        #TODO: set table values to what the parsed file declares


    # RESIZE EVENTS
    # ///////////////////////////////////////////////////////////////
    def resizeEvent(self, event):
        # Update Size Grips
        UIFunctions.resize_grips(self)

    # MOUSE CLICK EVENTS
    # ///////////////////////////////////////////////////////////////
    def mousePressEvent(self, event):
        # SET DRAG POS WINDOW
        self.dragPos = event.globalPos()

        # PRINT MOUSE EVENTS
        if event.buttons() == Qt.LeftButton:
            print('Mouse click: LEFT CLICK')
        if event.buttons() == Qt.RightButton:
            print('Mouse click: RIGHT CLICK')

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("icon.ico"))
    window = MainWindow()
    sys.exit(app.exec())