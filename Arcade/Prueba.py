import arcade

SCREEN_WIDTH = 1080
SCREEN_HEIGTH = 720
SCREEN_TITLE = "Juego"

if __name__ == "__main__":
    arcade.open_window(SCREEN_WIDTH,SCREEN_HEIGTH,SCREEN_TITLE)

    arcade.set_background_color(arcade.color.DARK_RED)

    arcade.start_render()
    arcade.draw_circle_filled(100, 200, 300, arcade.color.RED,0,- 1)
    arcade.finish_render()

    arcade.run()