import sys

from PySide6.QtWidgets import QWidget, QApplication, QMainWindow, QDialog, QVBoxLayout, QLabel, QScrollArea, QTextEdit, \
    QSizePolicy


class SchewiLangTranslator_MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("shiüo / SchewiLang")
        # self.setWindowIcon(QIcon(global_path.get_proj_abs_path("assets/icon.png")))
        self.setMinimumSize(400, 300)
        self.resize(800, 600)
        self.initUI()

    def initUI(self):
        pass


if __name__ == "__main__":
    SchewiLangTranslator_QApplication = QApplication()
    SchewiLangTranslator_GUI = SchewiLangTranslator_MainWindow()
    SchewiLangTranslator_GUI.show()
    sys.exit(SchewiLangTranslator_QApplication.exec())
