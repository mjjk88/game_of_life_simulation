import random
from dataclasses import dataclass


@dataclass
class LifeSimulation:
    alive_cells_coordinates: set
    box_length: int

    @staticmethod
    def empty_simulation():   # factory method
        return LifeSimulation(alive_cells_coordinates=set(), box_length=100)

    def generate_initial_state(self, alive_probability=0.25, random_seed=10):
        self.alive_cells_coordinates = set()

        random.seed(random_seed)
        for x in range(self.box_length):
            for y in range(self.box_length):
                # cell = random.choices(population=[0, 1], weights=[0.95, 0.05])
                is_alive = random.random() < alive_probability    # [0.0, 1.0) < p

                if is_alive:
                    self.alive_cells_coordinates.add((x, y))

    def generate_next_state(self):
        next_alive_cells_coordinates = set()
        for x in range(self.box_length):
            for y in range(self.box_length):
                """ Check number of alive neighbours """
                alive_neighbours_number = self._check_alive_neighbours_number(x, y)

                """ Rules of living in next generation:
                    - cell stays alive when has 2 or 3 alive neighbours
                    - cell becomes alive when has 3 alive neighbours.
                    If means, regardless of the current state, 3 alive neighbours ensure life in the next generation.
                """
                if alive_neighbours_number == 3 or \
                            ((x, y) in self.alive_cells_coordinates and alive_neighbours_number == 2):

                    next_alive_cells_coordinates.add((x, y))

        self.alive_cells_coordinates = next_alive_cells_coordinates

    def _check_alive_neighbours_number(self, x, y):
        alive_neighbours = 0
        for i in range(x-1, x+2):
            for j in range(y - 1, y + 2):
                if (i, j) != (x, y) and (i, j) in self.alive_cells_coordinates:  # we cannot count current cell but just alive neighbours
                    alive_neighbours += 1

        return alive_neighbours

