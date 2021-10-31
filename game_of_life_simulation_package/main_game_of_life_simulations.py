import sys
from PyQt5.QtWidgets import QApplication

import game_of_life_simulation_package.life_simulation as life_sim
import game_of_life_simulation_package.simulation_window as msw


def crete_simulation_window():
    ls = life_sim.LifeSimulation.empty_simulation()

    app = QApplication(sys.argv)
    window = msw.MainSimulationWindow(ls)
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    crete_simulation_window()