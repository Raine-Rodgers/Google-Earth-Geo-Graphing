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
        self.filePath = os.path.expanduser("~/Desktop")
        if not QApplication.instance(): app = QApplication(sys.argv)
        else: app = QApplication.instance()
        global widgets
        widgets = self.ui
        tkinter.Tk().withdraw() # prevents an empty tkinter window from appearing
        save_file = "save.p"
        if os.path.isfile(save_file) and os.path.getsize(save_file) > 0:
            temp = pickle.load(open(save_file, "rb"))
            tempRow = 1
            while len(temp) > 0:
                tempRow += 1
                for column in range(widgets.tableWidget.columnCount()):
                    if tempRow > widgets.tableWidget.rowCount():
                        widgets.tableWidget.insertRow(tempRow-1)
                    widgets.tableWidget.setItem(tempRow-1, column, QTableWidgetItem(temp.pop(0)))

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
        widgets.btn_edit.clicked.connect(self.NewButton)
        widgets.btn_save.clicked.connect(self.SaveButton)
        widgets.btn_addRow.clicked.connect(self.AddRowButton)
        widgets.btn_deleteRow.clicked.connect(self.DeleteRowButton)
        widgets.btn_deleteSelected.clicked.connect(self.DeleteRowSelectedButton)
        widgets.btn_ChoseDir.clicked.connect(self.ChoseDirButton)
        app.aboutToQuit.connect(self.myExitHandler) # myExitHandler is a callable

        # EXTRA LEFT BOX
        def openCloseLeftBox():
            UIFunctions.toggleLeftBox(self, True)
        widgets.toggleLeftBox.clicked.connect(openCloseLeftBox)
        # widgets.extraCloseColumnBtn.clicked.connect(openCloseLeftBox)

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
            widgets.tableWidget.setItem(row_position+1, 0, QTableWidgetItem(" "))
            widgets.tableWidget.setItem(row_position+1, 1, QTableWidgetItem(" "))
            widgets.tableWidget.setItem(row_position+1, 2, QTableWidgetItem(" "))
            widgets.tableWidget.setItem(row_position+1, 3, QTableWidgetItem(" "))
            print(f'Button "{btnName}" pressed!')

    def DeleteRowButton(self):
        # GET BUTTON CLICKED
        btn = self.sender()
        btnName = btn.objectName()

        if widgets.tableWidget.rowCount() > 1:
            widgets.tableWidget.removeRow(widgets.tableWidget.rowCount() - 1)
        print(f'Button "{btnName}" pressed!')

#TODO: make it so that it only deletes the selected row
    def DeleteRowSelectedButton(self):
        # GET BUTTON CLICKED
        btn = self.sender()
        btnName = btn.objectName()

        if widgets.tableWidget.rowCount() > 1:
            widgets.tableWidget.removeRow(widgets.tableWidget.currentRow())
        print(f'Button "{btnName}" pressed!')

    def ChoseDirButton(self):
        #TODO: read kml file
        #TODO: set table size to what the parsed file declares
        #TODO: set all values to what the parsed file declares
        #TODO: set file name to what the parsed file declares
        self.filePath = filedialog.askdirectory()
        print(self.filePath)

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
        heightFactor = float(1)
        coordinates = []
        outlineIsChecked = False
        color = ""

        if not(widgets.lineEdit_Height_Factor.text() is None or widgets.lineEdit_Height_Factor.text() ==""):
            if float(widgets.lineEdit_Height_Factor.text()) >= 1: heightFactor = float(widgets.lineEdit_Height_Factor.text())

        def isCellEmpty(rowCheck, columnCheck):
            if widgets.tableWidget.item(rowCheck, columnCheck) is None or widgets.tableWidget.item(rowCheck, columnCheck).text() == "":
                return True
            else:
                return False
        
        def formatHex():
            if "#" in self.color:
                self.color = self.color.replace("#", "")
            temp = self.color[::-1]
            self.color = temp
            self.color = "ff" + self.color
            print(f'formated hex: {self.color}')

        def choseColor():
            if(widgets.comboBox_Color.currentIndex() == 0):
                if(widgets.lineEdit_Color_HexCode.text() == "" or widgets.lineEdit_Color_HexCode is None): self.color = "ffff0000" # if hexcode is empty, set color to blue
                else:
                    if self.exeptionHandler("InvalidHex"):
                        self.color = widgets.lineEdit_Color_HexCode.text()
                        print(f'unformated hex: {self.color}')
                        formatHex()
            elif(widgets.comboBox_Color.currentIndex() == 1): self.color = "ff0000ff"
            elif(widgets.comboBox_Color.currentIndex() == 2): self.color = "ff00ff00"
            elif(widgets.comboBox_Color.currentIndex() == 3): self.color = "ffff0000"
            elif(widgets.comboBox_Color.currentIndex() == 4): self.color = "ffff00ff"
            elif(widgets.comboBox_Color.currentIndex() == 5): self.color = "ff32CD32"
            elif(widgets.comboBox_Color.currentIndex() == 6): self.color = "ff000000"
        # create coords
        # ///////////////////////////////////////////////////////////////

        # 2D array iteration type beat
        for row in range(1, widgets.tableWidget.rowCount()):
            for column in range(widgets.tableWidget.columnCount()):
                if column == 0:
                    if isCellEmpty(row, column): x = 0
                    else: x=float(widgets.tableWidget.item(row, column).text())
                elif column == 1:
                    if isCellEmpty(row, column): y = 0
                    else: y=float(widgets.tableWidget.item(row, column).text())
                elif column == 2:
                    if isCellEmpty(row, column): polygonName = "No-Name"
                    else: polygonName=widgets.tableWidget.item(row, column).text()
                elif column == 3:
                    if isCellEmpty(row, column)==False and widgets.Radio_Height_AccordingToConstent.isChecked()==False: # and widgets.Radio_Height_AccordingToValue.isChecked()==False
                        value=float(widgets.tableWidget.item(row, column).text())
                    elif widgets.Radio_Height_AccordingToConstent.isChecked():
                        value=float(widgets.lineEdit_Height_SetConst.text())
                    else: value = 0
                    value *= heightFactor
            coordinates.append(CreateCoordinates(x, y, value, polygonName))

        if widgets.checkBox_Outline.isChecked(): outlineIsChecked = True
        if self.exeptionHandler("NameLess"):
            if widgets.Radio_Color_AccordingToConstent.isChecked():
                choseColor()
            else: self.color = "Na"
            finalFile = MakeFile(coordinates, widgets.lineEdit_FileName.text(), outlineIsChecked, self.color, self.filePath)
            finalFile.makePolygon()
            finalFile.saveFile()
        
        # PRINT BTN NAME
        print(f'Button "{btnName}" pressed!')

    def exeptionHandler(self, type):
        if type == "NameLess":
            if not (widgets.lineEdit_FileName.text() is None or widgets.lineEdit_FileName.text()==""):
                return True
            else: messagebox.showerror("Error", "Please enter a file name")

        elif type == "InvalidHex":
            if len(widgets.lineEdit_Color_HexCode.text()) == 6:
                return True
            else: messagebox.showerror("Error", "Please enter a valid hex code")
        else: return False

    def myExitHandler(self):
        pickledArray = []
        for row in range(1, widgets.tableWidget.rowCount()):
            for column in range(widgets.tableWidget.columnCount()):
                print(row, column)
                if widgets.tableWidget.item(row, column) is None: pickledArray.append(" ")
                else: pickledArray.append(widgets.tableWidget.item(row, column).text())
        pickle.dump( pickledArray, open( "save.p", "wb" ))


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