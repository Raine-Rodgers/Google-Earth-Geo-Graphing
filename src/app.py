#Importing the components we need
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton
from button_holder import ButtonHolder
import polygontest
#The sys module is responsible for processing commmand line arguments
import sys

app = QApplication(sys.argv)

window = ButtonHolder()
window.show()

#Start the event loop
app.exec()