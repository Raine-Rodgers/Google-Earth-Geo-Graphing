from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QToolBar, QLineEdit, QTableWidget, QTableWidgetItem, QSizePolicy, QPushButton, QLabel, QTabWidget
from PySide6.QtCore import Qt
from PySide6.QtGui import QFont
from GUIDisplay import TitleTab


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Google Earth Graphing")

        # Create the toolbar
        self.toolbar = QToolBar()
        self.addToolBar(Qt.LeftToolBarArea, self.toolbar)

        # Create the tab widget
        self.tab_widget = QTabWidget()
        self.toolbar.addWidget(self.tab_widget)

        # Create the tabs
        self.title_tab = TitleTab()
        self.graph_settings_tab = QWidget()
        self.tab_widget.addTab(self.title_tab, "Title")
        self.tab_widget.addTab(self.graph_settings_tab, "Graph Settings")

app = QApplication([])
window = MainWindow()
window.show()
app.exec()
