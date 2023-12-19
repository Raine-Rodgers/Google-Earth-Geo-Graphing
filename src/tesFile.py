import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QTabWidget, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QTableWidget, QTableWidgetItem, QHeaderView

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Set the window size
        self.setGeometry(100, 100, 600, 400)

        # Create a QTabWidget
        tab_widget = QTabWidget()

        # Create a QWidget for the Title tab
        title_tab = QWidget()
        title_layout = QVBoxLayout()

        # Create a QLabel and QLineEdit for the Title tab
        title_label = QLabel("Title:")
        title_edit = QLineEdit()

        # Add the QLabel and QLineEdit to the layout
        title_layout.addWidget(title_label)
        title_layout.addWidget(title_edit)

        # Create a QTableWidget for the Title tab
        title_table = QTableWidget()
        title_table.setColumnCount(4)
        title_table.setHorizontalHeaderLabels(["lat", "lot", "name", "value"])
        title_table.setRowCount(4)

        # Create a QHBoxLayout for the buttons
        button_layout = QHBoxLayout()

        # Create a QPushButton for adding rows
        add_row_button = QPushButton("Add Row")
        add_row_button.clicked.connect(lambda: self.add_row(title_table))

        # Create a QPushButton for deleting rows
        delete_row_button = QPushButton("Delete Row")
        delete_row_button.clicked.connect(lambda: self.delete_row(title_table))

        # Add the buttons to the layout
        button_layout.addWidget(add_row_button)
        button_layout.addWidget(delete_row_button)

        # Add the table and buttons to the layout
        title_layout.addWidget(title_table)
        title_layout.addLayout(button_layout)

        # Set the layout for the Title tab
        title_tab.setLayout(title_layout)

        # Add the Title tab to the QTabWidget
        tab_widget.addTab(title_tab, "Title")

        # Create a QWidget for the Graph Settings tab
        graph_settings_tab = QWidget()

        # Add the Graph Settings tab to the QTabWidget
        tab_widget.addTab(graph_settings_tab, "Graph Settings")

        # Set the QTabWidget as the central widget
        self.setCentralWidget(tab_widget)

        # Resize the columns to fill the screen
        header = title_table.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.Stretch)

    def add_row(self, table):
        row_count = table.rowCount()
        table.insertRow(row_count)

    def delete_row(self, table):
        if len(table.selectedItems()) == 0:
            if table.rowCount() > 1:
                table.removeRow(table.rowCount() - 1)
        elif len(table.selectedItems()) != 0:
            selected_rows = table.selectionModel().selectedRows()
            for row in selected_rows:
                table.removeRow(row.row())

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

# ALL VARIABLES:
# tab_widget = QTabWidget()
# title_tab = QWidget()
# title_layout = QVBoxLayout()
# title_label = QLabel("Title:")
# title_edit = QLineEdit()
# title_table = QTableWidget()
# button_layout = QHBoxLayout()
# add_row_button = QPushButton("Add Row")
# delete_row_button = QPushButton("Delete Row")
# graph_settings_tab = QWidget()
# header = title_table.horizontalHeader()