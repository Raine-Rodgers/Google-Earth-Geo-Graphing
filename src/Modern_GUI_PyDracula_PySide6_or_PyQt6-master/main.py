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
import subprocess

import json  # Add this import at the top of the file

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
        user_home = os.path.expanduser("~") # Get the user's home directory
        global documents_folder
        self.extraValueBool = False
        documents_folder = os.path.join(user_home, 'Documents') # Get the relative path to the Documents folder
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.filePath = os.path.expanduser("~/Desktop")
        if not QApplication.instance(): app = QApplication(sys.argv)
        else: app = QApplication.instance()
        global widgets
        widgets = self.ui
        global save_file
        save_file = "save"  # No need to include the `.json` extension here; it will be added in the code

        self.OpenSaveFile()  # Call the function to open the saved JSON file and run the necessary functions


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
        widgets.btn_deleteSelected.clicked.connect(self.DeleteSelectedRowsButton)
        widgets.btn_toggleCol.clicked.connect(self.ToggleColumnButton)
        widgets.btn_newFile.clicked.connect(self.NewFileButton)
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

    # OPEN THE SAVED JSON FILE AND RUN THE NECESSARY FUNCITONS
    def OpenSaveFile(self):
        try:
            # Check if the JSON file exists
            if os.path.isfile(f"{documents_folder}/{save_file}.json"):
                with open(f"{documents_folder}/{save_file}.json", "r") as json_file:
                    data = json.load(json_file)
                    if len(data["tableData"]) <= 0: 
                        print("The file is empty, loading default sheet.")
                        return # if the file is empty load the default sheet

                    self.startupDeleteRows() # clear all rows on startup and only add the right amount back

                    # Restore the state of extraValueBool
                    self.extraValueBool = data.get("extraValueBool", False)  # Default to False if not found
                    if self.extraValueBool: # If extraValueBool is True, add the extra column
                        self.extraValueBool = True # i dont trust this so imma make sure its true
                        column_position = widgets.tableWidget.columnCount()
                        widgets.tableWidget.insertColumn(column_position)
                        widgets.tableWidget.setItem(0, column_position, QTableWidgetItem("Extra Value"))
                    # Restore table data
                    current_row = 0
                    for row_data in data["tableData"]:
                        current_row += 1
                        widgets.tableWidget.insertRow(current_row)
                        for column, cell_data in enumerate(row_data):
                            widgets.tableWidget.setItem(current_row, column, QTableWidgetItem(cell_data))

                # # Restore the state of extraValueBool
                # self.extraValueBool = data.get("extraValueBool", False)  # Default to False if not found
        except json.JSONDecodeError:
            print("Error decoding JSON file")
        except FileNotFoundError:
            print("File not found")
        except Exception as e:
            print(f"An error occurred: {e}")


    # delete all rows on startup when applicable
    def startupDeleteRows(self):
        for i in range(widgets.tableWidget.rowCount()-1):
            if widgets.tableWidget.rowCount() > 1:
                widgets.tableWidget.removeRow(widgets.tableWidget.rowCount() - 1)
                    
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

    def ToggleColumnButton(self):
        # GET BUTTON CLICKED
        btn = self.sender()
        btnName = btn.objectName()

        if self.extraValueBool == False: # if extra collumn doesnt exist, let it add a new one
            self.extraValueBool = True
            column_position = widgets.tableWidget.columnCount()
            widgets.tableWidget.insertColumn(column_position)
            widgets.tableWidget.setItem(0, column_position, QTableWidgetItem("Extra Value"))
        elif self.extraValueBool == True:
            self.extraValueBool = False
            column_position = widgets.tableWidget.columnCount()
            widgets.tableWidget.removeColumn(column_position-1)
            # widgets.tableWidget.setItem(0, column_position, QTableWidgetItem("Extra Value"))
        print(f'Button "{btnName}" pressed!')

    def DeleteRowButton(self):
        # GET BUTTON CLICKED
        btn = self.sender()
        btnName = btn.objectName()

        if widgets.tableWidget.rowCount() > 1:
            widgets.tableWidget.removeRow(widgets.tableWidget.rowCount() - 1)
        print(f'Button "{btnName}" pressed!')

    def DeleteSelectedRowsButton(self):
        # GET BUTTON CLICKED
        btn = self.sender()
        btnName = btn.objectName()

        selected_rows = widgets.tableWidget.selectedItems()
        if len(selected_rows) > 0:
            rows_to_delete = set()
            for item in selected_rows:
                row = item.row()
                if row != 0:  # Check that it is not the first row
                    rows_to_delete.add(row)
            rows_to_delete = sorted(rows_to_delete, reverse=True)  # Reverse order to avoid index issues
            for row in rows_to_delete:
                widgets.tableWidget.removeRow(row)

        print(f'Button "{btnName}" pressed!')

    def ChoseDirButton(self):

        applescript = '''
            tell application "Finder"
                set folderPath to POSIX path of (choose folder)
            end tell
            '''
                #set selectedFolder to (choose folder with prompt "Select a folder") as text
    
        # Run the AppleScript via osascript
        result = subprocess.run(['osascript', '-e', applescript], capture_output=True, text=True)
        
        # Get the result (folder path)
        self.filePath = result.stdout.strip()
        print(self.filePath)

        # self.filePath = filedialog.askdirectory()
        # print(self.filePath)

    def NewFileButton(self):
        # GET BUTTON CLICKED
        btn = self.sender()
        btnName = btn.objectName()

        # Reset the table widget
        self.startupDeleteRows()  # Clear all rows on startup
        for i in range(10):
            widgets.tableWidget.insertRow(i+1)
            widgets.tableWidget.setItem(i+1, 0, QTableWidgetItem(" "))
            widgets.tableWidget.setItem(i+1, 1, QTableWidgetItem(" "))
            widgets.tableWidget.setItem(i+1, 2, QTableWidgetItem(" "))
            widgets.tableWidget.setItem(i+1, 3, QTableWidgetItem(" "))

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
        extraValue = float(0)
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
            elif(widgets.comboBox_Color.currentIndex() == 1): self.color = "ff0000ff" # Blue
            elif(widgets.comboBox_Color.currentIndex() == 2): self.color = "ff00ff00" # Green
            elif(widgets.comboBox_Color.currentIndex() == 3): self.color = "ffff0000" # Red
            elif(widgets.comboBox_Color.currentIndex() == 4): self.color = "ffff00ff" # Magenta
            elif(widgets.comboBox_Color.currentIndex() == 5): self.color = "ff32CD32" # Lime
            elif(widgets.comboBox_Color.currentIndex() == 6): self.color = "ff000000" # Black
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
                    elif widgets.Radio_Height_AccordingToConstent.isChecked() and widgets.lineEdit_Height_SetConst.text() != "":
                        value=float(widgets.lineEdit_Height_SetConst.text())
                    else: value = 1
                    value *= heightFactor
                elif column == 4:
                    if isCellEmpty(row, column): extraValue = 0
                    else: extraValue=float(widgets.tableWidget.item(row, column).text())
            coordinates.append(CreateCoordinates(x, y, value, polygonName, extraValue))

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
            else: 
                applescript = f'''
                tell application "System Events"
                    display dialog "Please enter a file name" with title "NameLess" buttons {{"OK"}} default button "OK"
                end tell
                '''
                # Run the AppleScript via osascript
                subprocess.run(['osascript', '-e', applescript])
                
                
                #messagebox.showerror("Error", "Please enter a file name")

        elif type == "InvalidHex":
            if len(widgets.lineEdit_Color_HexCode.text()) == 6:
                return True
            else: 
                applescript = f'''
                tell application "System Events"
                    display dialog "Please enter a valid Hex Code" with title "InvalidHex" buttons {{"OK"}} default button "OK"
                end tell
                '''
                # Run the AppleScript via osascript
                subprocess.run(['osascript', '-e', applescript])
                
                
                #messagebox.showerror("Error", "Please enter a valid hex code")
        else: return False


    

    def myExitHandler(self):
        # Prepare data to save
        data = {
            "tableData": [],
            "extraValueBool": self.extraValueBool  # Save the state of extraValueBool
        }

        # Collect table data
        for row in range(1, widgets.tableWidget.rowCount()):
            row_data = []
            for column in range(widgets.tableWidget.columnCount()):
                if widgets.tableWidget.item(row, column) is None or widgets.tableWidget.item(row, column).text() == "":
                    blankCount = 0
                    for i in range (widgets.tableWidget.columnCount()): # if one cell is empty, check if the entire row is as well
                        if widgets.tableWidget.item(row, i) is None or widgets.tableWidget.item(row, i).text() == "":
                            blankCount += 1
                        else:
                            break
                    if blankCount >= 3:
                        break
                    row_data.append("")  # Save empty cells as empty strings
                else:
                    row_data.append(widgets.tableWidget.item(row, column).text())
            if len(row_data) > 0:  # Only append non-empty rows
                data["tableData"].append(row_data)
            

        # Save to a JSON file
        with open(f"{documents_folder}/{save_file}.json", "w") as json_file:
            json.dump(data, json_file, indent=4)
        print(f"Data saved to {documents_folder}/{save_file}.json")


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