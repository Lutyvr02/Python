import arcade
import random
from weas import get_circle

# definicion de constantes
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
SCREEN_TITLE = "Circulos con bresenham"




class BresenhamWindow(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        arcade.set_background_color(arcade.color.BLACK)
        self.pixel_size = 5
        self.xc = 100
        self.yc = 70
        self.r = 20
        self.circle_color = arcade.color.ALMOND

        self.speed = 20
        self.velocity = [self.speed, self.speed]

    def on_update(self, delta_time: float):
        self.xc += delta_time * self.velocity[0]
        self.yc += delta_time * self.velocity[0]

        if self.xc > SCREEN_WIDTH // self.pixel_size or self.xc < 0:
            self.velocity[0] = self.velocity[0]

        if self.yc > SCREEN_HEIGHT // self.pixel_size or self.yc < 0:
            self.velocity[1] =-1 * self.velocity[1]


    def on_draw(self):
        arcade.start_render()
        points = get_circle(
            self.xc,
            self.yc,
            self.r
        )
  
        self.draw_grid()
        self.draw_circle_points(points, arcade.color.DARK_YELLOW)
        self.draw_scaled_circle(self.xc, self.yc, self.r)

    def draw_grid(self):
        # lineas verticales
        for v_l in range(0, SCREEN_WIDTH, self.pixel_size):
            arcade.draw_line(
                v_l + self.pixel_size / 2, 
                0, 
                v_l + self.pixel_size / 2, 
                SCREEN_HEIGHT, 
                [20, 20, 20]
            )

        for h_l in range(0, SCREEN_HEIGHT, self.pixel_size):
            arcade.draw_line(
                0, 
                h_l + self.pixel_size / 2, 
                SCREEN_WIDTH, 
                h_l + self.pixel_size / 2, 
                [20, 20, 20]
            )

    def draw_circle_points(self, points,  color):
        for p in points:
            arcade.draw_point(p[0] * self.pixel_size, p[1] * self.pixel_size, color, self.pixel_size)

    def draw_scaled_circle(self, xc, yc, r):
        arcade.draw_circle_outline(
            xc * self.pixel_size, 
            yc * self.pixel_size, 
            r * self.pixel_size, 
            [100, 255, 40, 150], 
            5
        )

if __name__ == "__main__":
    app = BresenhamWindow()
    arcade.run()