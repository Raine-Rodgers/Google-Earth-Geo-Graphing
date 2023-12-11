import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QTabWidget, QVBoxLayout, QWidget, QLineEdit, QTableWidget, QTableWidgetItem, QPushButton, QDockWidget, QSizePolicy, QHBoxLayout
from PySide6.QtCore import Qt, QSize

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Set window size to 75% of the screen resolution
        screen = QApplication.primaryScreen()
        screen_size = screen.size()
        self.resize(screen_size * 0.5)

        # Create a tab widget
        self.tab_widget = QTabWidget()

        # Create tabs
        self.title_tab = QWidget()
        self.graph_settings_tab = QWidget()

        # Add tabs to the tab widget
        self.tab_widget.addTab(self.title_tab, "Title")
        self.tab_widget.addTab(self.graph_settings_tab, "Graph Settings")

        # Set up Title tab
        self.setup_title_tab()

        # Create a main layout
        self.main_layout = QHBoxLayout()

        # Add the tab widget and a placeholder widget to the main layout
        # The placeholder widget will take up the rest of the space in the window
        self.main_layout.addWidget(self.tab_widget)
        self.main_layout.addWidget(QWidget())

        # Create a central widget and set the main layout on it
        self.central_widget = QWidget()
        self.central_widget.setLayout(self.main_layout)

        # Set the central widget on the main window
        self.setCentralWidget(self.central_widget)

    def setup_title_tab(self):
        # Create a vertical layout for the right side of the title tab
        right_side_layout = QVBoxLayout()

        # Create a text box for file name input
        self.file_name_input = QLineEdit()
        self.file_name_input.setPlaceholderText("Enter a file name")
        right_side_layout.addWidget(self.file_name_input)

        # Create a table
        self.table = QTableWidget(5, 4)  # Start with 5 rows
        self.table.setHorizontalHeaderLabels(["lat", "lon", "name", "value"])
        self.table.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)  # Set size policy
        right_side_layout.addWidget(self.table)

        # Create a horizontal layout for the Add and Delete buttons
        button_layout = QHBoxLayout()

        # Create Add and Delete buttons
        self.add_button = QPushButton("Add")
        self.add_button.clicked.connect(self.add_row)
        button_layout.addWidget(self.add_button)

        self.delete_button = QPushButton("Delete")
        self.delete_button.clicked.connect(self.delete_row)
        button_layout.addWidget(self.delete_button)

        # Add the button layout to the right side layout
        right_side_layout.addLayout(button_layout)

        # Set the right side layout on the title tab
        self.title_tab.setLayout(right_side_layout)

    def add_row(self):
        row_position = self.table.rowCount()
        self.table.insertRow(row_position)

    def delete_row(self):
        if self.table.rowCount() > 0:
            self.table.removeRow(self.table.rowCount() - 1)

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())
