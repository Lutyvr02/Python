import arcade

SCREEN_WIDTH = 1080
SCREEN_HEIGTH = 720
SCREEN_TITLE = "2"

class Hola(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH,SCREEN_HEIGTH,SCREEN_TITLE)
        arcade.set_background_color(arcade.color.GRAY)

    def on_draw(self):
        arcade.start_render()
        arcade.draw_circle_filled(100, 200, 300, arcade.color.RED,0,- 1)
        arcade.finish_render()
        arcade.run()
