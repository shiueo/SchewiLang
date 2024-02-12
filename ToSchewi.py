import sys
import json
from functools import partial

from PySide6.QtWidgets import QWidget, QApplication, QMainWindow, QDialog, QVBoxLayout, QLabel, QScrollArea, QTextEdit, \
    QSizePolicy, QGridLayout, QPlainTextEdit, QSpacerItem, QHBoxLayout, QPushButton

with open("words.json", "r", encoding="utf8") as f:
    words_data = json.load(f)

with open("KrToSchewiUni.json", "r", encoding="utf8") as f:
    schewi_data = json.load(f)


def to_schewi_written(w: str):
    res = ''
    for word in w:
        if word in schewi_data.keys() and schewi_data[word] != '':
            res += schewi_data[word]
        else:
            res += word
    return res


class SchewiLangTranslator_Widget(QWidget):
    def __init__(self):
        super().__init__()

        self.GRID = QGridLayout()

        self.INPUT_BOX = QPlainTextEdit()
        self.INPUT_BOX.textChanged.connect(lambda: self.update())

        self.OUTPUT_BOX = QPlainTextEdit()

        self.L_Layout = QVBoxLayout()

        word_scroll_area = QScrollArea()
        word_scroll_area.setWidgetResizable(True)
        scroll_widget = QWidget()
        word_scroll_area.setWidget(scroll_widget)
        self.scroll_layout = QVBoxLayout(scroll_widget)
        self.L_Layout.addWidget(word_scroll_area)

        self.R_Layout = QVBoxLayout()
        self.SCHEWIFY_BTN = QPushButton("JUST Schewify")
        self.SCHEWIFY_BTN.clicked.connect(lambda: self.schewify())

        self.R_Layout.addWidget(self.SCHEWIFY_BTN)
        self.SCHEWIFY_BTN.setSizePolicy(QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding))

        self.setWindowTitle("shiüo / SchewiLang")
        # self.setWindowIcon(QIcon(global_path.get_proj_abs_path("assets/icon.png")))
        self.setMinimumSize(640, 360)
        self.resize(1280, 720)
        self.initUI()
        self.update()

    def initUI(self):
        with open(
                file="assets/stylesheet.txt", mode="r"
        ) as f:
            self.setStyleSheet(f.read())

        self.GRID.addWidget(self.OUTPUT_BOX, 0, 0, 1, 1)
        self.GRID.addWidget(self.INPUT_BOX, 1, 0, 1, 1)
        self.GRID.addLayout(self.L_Layout, 2, 0, 1, 1)
        self.GRID.addLayout(self.R_Layout, 0, 1, 3, 1)

        self.setLayout(self.GRID)

    def update(self):
        query = self.INPUT_BOX.toPlainText().split()
        self.clearScrollArea()
        found = False
        for word in words_data:
            for q in query:
                if q in word:
                    button = QPushButton(f'{word}: {words_data[word]} -> {to_schewi_written(words_data[word])}')
                    button.clicked.connect(partial(self.add_word_to_input_box, to_schewi_written(words_data[word])))
                    self.scroll_layout.addWidget(button)
                    found = True

        if not found:
            if query:
                label = QLabel("검색 결과가 없습니다.")
                label.setStyleSheet("background-color: #1A1A1A; color: #FFFFFF; padding: 5px;")
                label.setSizePolicy(QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed))
                self.scroll_layout.addWidget(label)
            else:
                for word in words_data:
                    button = QPushButton(f'{word}: {words_data[word]} -> {to_schewi_written(words_data[word])}')
                    button.clicked.connect(partial(self.add_word_to_input_box, to_schewi_written(words_data[word])))
                    self.scroll_layout.addWidget(button)
        self.scroll_layout.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

    def add_word_to_input_box(self, word):
        current_text = self.OUTPUT_BOX.toPlainText()
        self.OUTPUT_BOX.setPlainText(current_text + word + " ")

    def schewify(self):
        current_text = self.OUTPUT_BOX.toPlainText()
        self.OUTPUT_BOX.setPlainText(current_text + to_schewi_written(self.INPUT_BOX.toPlainText()) + " ")

    def clearScrollArea(self):
        while self.scroll_layout.count():
            child = self.scroll_layout.takeAt(0)
            if child.widget():
                child.widget().deleteLater()


if __name__ == "__main__":
    SchewiLangTranslator_QApplication = QApplication()
    SchewiLangTranslator_GUI = SchewiLangTranslator_Widget()
    SchewiLangTranslator_GUI.show()
    sys.exit(SchewiLangTranslator_QApplication.exec())
