import sys
import json
import random

from PySide6.QtWidgets import (
    QApplication, QMainWindow, QVBoxLayout, QHBoxLayout, QWidget,
    QPushButton, QLabel, QInputDialog, QLineEdit, QMessageBox
)
from PySide6.QtCore import Qt

word_file = 'spanish_trainer.json'


def init_words():
    words = [
        {"ru": "привет", "es": "hola"},
        {"ru": "чай", "es": "té"},
        {"ru": "пожалуйста", "es": "por favor"},
        {"ru": "мороженое", "es": "helado"},
        {"ru": "пока", "es": "chao"},
        {"ru": "молоко", "es": "leche"}
    ]
    save_words(words)
    return words


def load_words():
    try:
        with open(word_file, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        return init_words()


def save_words(words):
    with open(word_file, 'w', encoding='utf-8') as f:
        json.dump(words, f, ensure_ascii=False, indent=2)


class MainWindow(QMainWindow):
    def init(self):
        super().init()
        self.setWindowTitle("Испанский тренажёр")
        self.words = load_words()
        self.current_word = None

        central = QWidget()
        self.setCentralWidget(central)
        layout = QVBoxLayout(central)

        self.label = QLabel("Нажмите «Новое слово»", self)
        self.label.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.label)

        self.input = QLineEdit()
        self.input.setPlaceholderText("Введите перевод")
        layout.addWidget(self.input)

        btn_layout = QHBoxLayout()
        self.check_btn = QPushButton("Проверить")
        self.next_btn = QPushButton("Новое слово")
        btn_layout.addWidget(self.check_btn)
        btn_layout.addWidget(self.next_btn)
        layout.addLayout(btn_layout)

        self.check_btn.clicked.connect(self.check_answer)
        self.next_btn.clicked.connect(self.new_word)
        self.input.returnPressed.connect(self.check_answer)

        self.new_word()

    def new_word(self):
        self.current_word = random.choice(self.words)
        self.label.setText(f"{self.current_word['ru']} → ?")
        self.input.clear()
        self.input.setFocus()

    def check_answer(self):
        answer = self.input.text().strip().lower()
        correct = self.current_word['es'].lower()
        if answer == correct:
            QMessageBox.information(self, "Правильно!", "верно!")
        else:
            QMessageBox.warning(self, "Неправильно", f"правильный ответ: {self.current_word['es']}")
        self.new_word()


app = QApplication(sys.argv)
window = MainWindow()
window.resize(300, 150)
window.show()
sys.exit(app.exec())
