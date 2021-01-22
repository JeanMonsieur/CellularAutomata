import random as rnd
import pyglet


class GameOfLife:

    def __init__(self, window_width, window_height, cell_size, initial_percent_alive):
        self.grid_width = int(window_width / cell_size)
        self.grid_height = int(window_height / cell_size)
        self.cell_size = cell_size
        self.cells = []
        self.initial_percent_alive = initial_percent_alive

        # Game of life standard rules
        # self.generate_cells()

        # Initial 5 by 5 square centered (lower frames)
        self.generate_5by5_square()

    def generate_cells(self):
        for row in range(0, self.grid_height):
            self.cells.append([])
            for col in range(0, self.grid_width):
                if rnd.random() < self.initial_percent_alive:
                    self.cells[row].append(1)
                else:
                    self.cells[row].append(0)

    def generate_5by5_square(self):
        row_center = self.grid_width // 2
        col_center = self.grid_height // 2
        for row in range(0, self.grid_height):
            self.cells.append([])
            for col in range(0, self.grid_width):
                self.cells[row].append(0)

        for row in range(row_center - 2, row_center + 3):
            for col in range(col_center - 2, col_center + 3):
                self.cells[row][col] = 1

    def draw(self):
        for row in range(0, self.grid_height):
            for col in range(0, self.grid_width):
                if self.cells[row][col] == 1:
                    square_coords = (row * self.cell_size, col * self.cell_size,
                                     row * self.cell_size, col * self.cell_size + self.cell_size,
                                     row * self.cell_size + self.cell_size, col * self.cell_size,
                                     row * self.cell_size + self.cell_size, col * self.cell_size + self.cell_size)
                    pyglet.graphics.draw_indexed(4,
                                                 pyglet.gl.GL_TRIANGLES,
                                                 [0, 1, 2, 1, 2, 3],
                                                 ("v2i", square_coords))

    def generate_next_gen(self):
        cells_next_gen = []
        for row in range(0, self.grid_height):
            cells_next_gen.append([])
            for col in range(0, self.grid_width):
                if row == 0 or row == self.grid_height - 1 or col == 0 or col == self.grid_width - 1:
                    cells_next_gen[row].append(self.cells[row][col])
                else:
                    neighbours_alive = self.count_cell_neighbours(row, col)

                    # RULES
                    if self.cells[row][col] == 1 and (neighbours_alive == 2 or neighbours_alive == 3):
                        cells_next_gen[row].append(1)
                    elif self.cells[row][col] == 0 and neighbours_alive == 3:
                        cells_next_gen[row].append(1)
                    else:
                        cells_next_gen[row].append(0)

        self.cells = cells_next_gen

    def count_cell_neighbours(self, row, col):
        neighbours_alive = 0
        for neighbour_x in range(row - 1, row + 2):
            for neighbour_y in range(col - 1, col + 2):
                if self.cells[neighbour_x][neighbour_y] == 1:
                    neighbours_alive += 1

        if self.cells[row][col] == 1:
            neighbours_alive -= 1

        return neighbours_alive

    def bring_cell_to_life(self, x, y):
        row = x // self.cell_size
        col = y // self.cell_size
        self.cells[row][col] = 1

