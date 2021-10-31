from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QMainWindow, QPushButton, QVBoxLayout, QWidget

import game_of_life_simulation_package.settings_widget as sw
import game_of_life_simulation_package.simulation_painting_canvas as spc


class MainSimulationWindow(QMainWindow):
    def __init__(self, ls):
        super().__init__()
        self.ls = ls
        self.is_running = False

        self.setWindowTitle("Game of Life")
        self.main_layout = QVBoxLayout()

        self.window = sw.SettingsWidget(self)

        self.gen_life_button = QPushButton(self)
        self.run_button = QPushButton(self)
        self.set_generate_life_button()
        self.set_run_button()

        self.refresh_timer = QTimer()
        self.set_refresh_timer()

        self.painting_canvas = spc.SimulationPaintingCanvas(self, self.ls)

        self.widgets = QWidget()
        self.add_widgets_to_main_layout()
        self.widgets.setLayout(self.main_layout)

        self.setCentralWidget(self.widgets)  # TODO check where to put it

    def set_generate_life_button(self):
        self.gen_life_button.setText('Generate Life')
        self.gen_life_button.setToolTip('Create first alive generation')
        self.gen_life_button.clicked.connect(self.generate_button_clicked)

    def set_run_button(self):
        self.run_button.setText('Run')
        self.run_button.setToolTip('To run or pause the simulation')
        self.run_button.clicked.connect(self.run_button_clicked)
        self.run_button.setEnabled(False)

    def set_refresh_timer(self):
        self.refresh_timer.setInterval(1000)  # in ms
        self.refresh_timer.timeout.connect(self.display_new_state)

    def add_widgets_to_main_layout(self):
        self.main_layout.addWidget(self.window)
        self.main_layout.addWidget(self.gen_life_button)
        self.main_layout.addWidget(self.run_button)
        self.main_layout.addWidget(self.painting_canvas)

    def generate_button_clicked(self):
        settings = self.window.read_settings_from_input()

        self.ls.generate_initial_state(alive_probability=settings.alive_probability, random_seed=settings.random_seed)

        self.painting_canvas.cell_size = settings.cell_size
        self.painting_canvas.refresh()

        self.run_button.setEnabled(True)

    def run_button_clicked(self):
        if self.is_running:
            self.refresh_timer.stop()
            self.is_running = False
            self.gen_life_button.setEnabled(True)
            self.run_button.setText('Run')
        else:
            self.refresh_timer.start()
            self.is_running = True
            self.gen_life_button.setEnabled(False)
            self.run_button.setText('Stop')

    def display_new_state(self):
        self.ls.generate_next_state()
        self.painting_canvas.refresh()
