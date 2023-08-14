import arcade
from bresenham import get_line

# definicion de constantes
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
SCREEN_TITLE = "Lineas con bresenham"

class BresenhamWindow(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        arcade.set_background_color(arcade.color.BLACK)
        self.pixel_size = 20

    def on_draw(self):
        arcade.start_render()

        points = get_line(5, 5, 30, 15)
        self.draw_grid()
        self.draw_line_blocks(points, arcade.color.DARK_YELLOW)  # Cambio de método
        self.draw_scaled_line(30, 15, 5, 5)

    def draw_grid(self):
        for v_l in range(0, SCREEN_WIDTH, self.pixel_size):
            arcade.draw_line(
                v_l + self.pixel_size / 2, 
                0, 
                v_l + self.pixel_size / 2, 
                SCREEN_HEIGHT, 
                arcade.color.DARK_GRAY
            )

        for h_l in range(0, SCREEN_HEIGHT, self.pixel_size):
            arcade.draw_line(
                0, 
                h_l + self.pixel_size / 2, 
                SCREEN_WIDTH, 
                h_l + self.pixel_size / 2, 
                arcade.color.LIGHT_GRAY
            )

    def draw_line_blocks(self, points, color):
        for p1, p2 in zip(points[:-1], points[1:]):
            dx, dy = p2[0] - p1[0], p2[1] - p1[1]
            if dx == 0:
                start, end = sorted([p1[1], p2[1]])
                for y in range(start, end):
                    arcade.draw_rectangle_filled(p1[0] * self.pixel_size, y * self.pixel_size,
                                                 self.pixel_size, self.pixel_size, color)
            elif dy == 0:
                start, end = sorted([p1[0], p2[0]])
                for x in range(start, end):
                    arcade.draw_rectangle_filled(x * self.pixel_size, p1[1] * self.pixel_size,
                                                 self.pixel_size, self.pixel_size, color)

    def draw_scaled_line(self, x0, y0, x1, y1):
        arcade.draw_line(
            x0 * self.pixel_size, 
            y0 * self.pixel_size, 
            x1 * self.pixel_size, 
            y1 * self.pixel_size,
            [100, 255, 40, 150],
            5
        )

if __name__ == "__main__":
    app = BresenhamWindow()
    arcade.run()