import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QPushButton, QTabWidget, QFrame
from PyQt5.QtGui import QColor, QPainter, QPalette, QIcon

class KJ_CSGOTab(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        layout.addWidget(QPushButton("Function 1", clicked=self.call_function1))
        layout.addWidget(QPushButton("Function 2", clicked=self.call_function2))
        layout.addWidget(QPushButton("Function 3", clicked=self.call_function3))
        layout.addWidget(QPushButton("Function 4", clicked=self.call_function4))
        layout.addWidget(QPushButton("Function 5", clicked=self.call_function5))
        layout.addWidget(QPushButton("Function 6", clicked=self.call_function6))
        layout.addWidget(QPushButton("Function 7", clicked=self.call_function7))
        layout.addWidget(QPushButton("Function 8", clicked=self.call_function8))
        layout.addStretch()
        self.setLayout(layout)

    def call_function1(self):
        print("Function 1 called.")

    def call_function2(self):
        print("Function 2 called.")

    def call_function3(self):
        print("Function 3 called.")

    def call_function4(self):
        print("Function 4 called.")

    def call_function5(self):
        print("Function 5 called.")

    def call_function6(self):
        print("Function 6 called.")

    def call_function7(self):
        print("Function 7 called.")

    def call_function8(self):
        print("Function 8 called.")


class DarkTab(QFrame):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setAutoFillBackground(True)
        pal = self.palette()
        pal.setColor(QPalette.Background, QColor(40, 40, 40))
        self.setPalette(pal)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("KJ_CSGO_Menu | Version v0.0.1")
        self.setGeometry(100, 100, 800, 600)

        self.setWindowIcon(QIcon("_ico\\favicon.ico"))

        tab_widget = QTabWidget()
        dark_tab = DarkTab()
        dark_tab_layout = QVBoxLayout(dark_tab)
        dark_tab_layout.addWidget(KJ_CSGOTab())
        dark_tab.setLayout(dark_tab_layout)
        tab_widget.addTab(dark_tab, "KJ_CSGO_Menu")
        tab_widget.setStyleSheet("QTabBar::tab { background-color: #CCCCCC; }")

        self.setStyleSheet(
            """
            QMainWindow {
                background-color: #282828;
            }
            """
        )

        self.setCentralWidget(tab_widget)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
