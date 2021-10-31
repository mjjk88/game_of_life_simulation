from dataclasses import dataclass

from PyQt5.QtWidgets import QLabel, QVBoxLayout, QWidget, QLineEdit
from PyQt5.QtGui import QIntValidator


@dataclass
class LifeSettings:
    alive_probability: int
    random_seed: int
    cell_size: int


class SettingsWidget(QWidget):
    def __init__(self, parent):
        super().__init__(parent)

        self.random_seed_label = QLabel()
        self.random_seed_line_edit = QLineEdit()
        self.alive_probability_label = QLabel()
        self.alive_probability_line_edit = QLineEdit()
        self.cell_size_label = QLabel()
        self.cell_size_line_edit = QLineEdit()

        self.set_random_seed_line_edit()
        self.set_alive_probability_line_edit()
        self.set_cell_size_line_edit()

        self.main_layout = QVBoxLayout()
        self.add_settings_widgets_to_layout()
        self.setLayout(self.main_layout)

    def set_random_seed_line_edit(self):
        self.random_seed_label.setText('Put random seed number')

        self.random_seed_line_edit.setText('1635412856')
        self.random_seed_line_edit.setToolTip('Set only number')
        self.random_seed_line_edit.setValidator(QIntValidator())

    def set_alive_probability_line_edit(self):
        self.alive_probability_label.setText('Put alive probability number in percent (0-99). Default is 25%.')

        self.alive_probability_line_edit.setText('25')
        self.alive_probability_line_edit.setToolTip('Set only number')
        self.alive_probability_line_edit.setValidator(QIntValidator(0, 99))  # TODO max min?

    def set_cell_size_line_edit(self):
        self.cell_size_label.setText('Put the size of the single alive cell')

        self.cell_size_line_edit.setText('5')
        self.cell_size_line_edit.setToolTip('Set only number')
        self.cell_size_line_edit.setValidator(QIntValidator(0, 100))

    def add_settings_widgets_to_layout(self):
        self.main_layout.addWidget(self.alive_probability_line_edit)
        self.main_layout.addWidget(self.random_seed_label)
        self.main_layout.addWidget(self.random_seed_line_edit)
        self.main_layout.addWidget(self.cell_size_label)
        self.main_layout.addWidget(self.cell_size_line_edit)

    def read_settings_from_input(self):
        alive_probability = int(
            self.alive_probability_line_edit.text()) / 100 if self.alive_probability_line_edit.text() else 0.25
        random_seed = int(self.random_seed_line_edit.text()) if self.random_seed_line_edit.text() else time.time()
        cell_size = int(self.cell_size_line_edit.text())

        return LifeSettings(alive_probability=alive_probability, random_seed=random_seed, cell_size=cell_size)
