import pyglet
from pyglet.window import mouse
from Game_Of_Life import GameOfLife


class window(pyglet.window.Window):

    def __init__(self):
        super().__init__(600, 600)
        self.set_location(500, 100)
        self.frames = 1.0 / 3
        self.gameOfLife = GameOfLife(self.get_size()[0],
                                     self.get_size()[1],
                                     10,
                                     0.0)
        pyglet.clock.schedule_interval(self.update, self.frames)

    def on_draw(self):
        self.clear()
        self.gameOfLife.draw()

    def update(self, dt):
        self.gameOfLife.generate_next_gen()

    def on_mouse_press(self, x, y, button, modifiers):
        if button == mouse.LEFT:
            self.gameOfLife.bring_cell_to_life(x, y)


if __name__ == "__main__":
    win = window()
    pyglet.app.run()
