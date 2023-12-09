from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QToolBar, QLineEdit, QTableWidget, QTableWidgetItem, QSizePolicy, QPushButton, QLabel, QTabWidget
from PySide6.QtCore import Qt
from PySide6.QtGui import QFont

class TitleTab(QWidget):
    def __init__(self):
        super().__init__()

        # Create the layout
        layout = QVBoxLayout()
        self.setLayout(layout)

        # Create the title label
        self.title_label = QLabel("Google Earth Graphing")
        self.title_label.setFont(QFont('Arial', 20))
        layout.addWidget(self.title_label)

        # Create the QLineEdit for the graph title
        self.graph_title = QLineEdit()
        self.graph_title.setPlaceholderText("Enter the graph title...")
        self.graph_title.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        layout.addWidget(self.graph_title)

        # Create the table
        self.table = QTableWidget(5, 4)
        self.table.setHorizontalHeaderLabels(["lat", "lon", "name", "value"])
        self.table.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        layout.addWidget(self.table)

        # Create the buttons
        self.add_row_button = QPushButton("Add Row")
        self.add_row_button.clicked.connect(self.add_row)
        layout.addWidget(self.add_row_button)

        self.delete_row_button = QPushButton("Delete Row")
        self.delete_row_button.clicked.connect(self.delete_row)
        layout.addWidget(self.delete_row_button)

    def add_row(self):
        row_position = self.table.rowCount()
        self.table.insertRow(row_position)

    def delete_row(self):
        if self.table.rowCount() > 0:
            self.table.removeRow(self.table.rowCount() - 1)
