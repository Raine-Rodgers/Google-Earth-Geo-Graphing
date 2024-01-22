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
        global widgets
        widgets = self.ui

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
        widgets.btn_home.clicked.connect(self.buttonClick)
#        widgets.btn_widgets.clicked.connect(self.buttonClick)
        widgets.btn_new.clicked.connect(self.buttonClick)
#        widgets.btn_new.clicked.connect(self.buttonClick)
        widgets.btn_save.clicked.connect(self.buttonClick)
#        widgets.btn_save.clicked.connect(self.buttonClick)
        widgets.AddRowButton.clicked.connect(self.buttonClick)
#        widgets.btn_save.clicked.connect(self.buttonClick)
        widgets.DeleteRowButton.clicked.connect(self.buttonClick)
#        widgets.btn_save.clicked.connect(self.buttonClick)

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
    def buttonClick(self):
        # GET BUTTON CLICKED
        btn = self.sender()
        btnName = btn.objectName()

        # SHOW HOME PAGE
        # if btnName == "btn_home":
        #     widgets.stackedWidget.setCurrentWidget(widgets.home)
        #     UIFunctions.resetStyle(self, btnName)
        #     btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))

        if btnName == "btn_home":
            widgets.stackedWidget.setCurrentWidget(widgets.widgets)
            UIFunctions.resetStyle(self, "btn_widget")
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))

        # SHOW WIDGETS PAGE
        if btnName == "btn_widgets":
            widgets.stackedWidget.setCurrentWidget(widgets.widgets)
            UIFunctions.resetStyle(self, btnName)
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))

        # SHOW NEW PAGE
        if btnName == "btn_new":
            widgets.stackedWidget.setCurrentWidget(widgets.new_page) # SET PAGE
            UIFunctions.resetStyle(self, btnName) # RESET ANOTHERS BUTTONS SELECTED
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet())) # SELECT MENU

        if btnName == "AddRowButton":
            row_position = widgets.tableWidget.rowCount()
            widgets.tableWidget.insertRow(row_position)

        if btnName == "DeleteRowButton":
            if widgets.tableWidget.rowCount() > 1:
                widgets.tableWidget.removeRow(widgets.tableWidget.rowCount() - 1)

        if btnName == "btn_save":
            row = 0
            column = 0
            x = float(0)
            y = float(0)
            polygonName = ""
            value = float(0)
            coordinates = []
            outlineIsChecked = False

            def isCellEmpty():
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
            
            for row in range(1, widgets.tableWidget.rowCount()):
                for column in range(widgets.tableWidget.columnCount()):
                    if column == 0:
                        if isCellEmpty(): x = 48.0677873; y = 12.8578328
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

            finalFile = MakeFile(coordinates, widgets.lineEdit.text(), outlineIsChecked)
            finalFile.makePolygon()
            finalFile.saveFile()
        # PRINT BTN NAME
        print(f'Button "{btnName}" pressed!')


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
            #TODO: test

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("icon.ico"))
    window = MainWindow()
    sys.exit(app.exec())