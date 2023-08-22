import arcade
import apple as ap
import snake as snk

# Constantes
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
GRID_SIZE = 20
SNAKE_SPEED = 7 

class SnakeGame(arcade.Window):
    def __init__(self, width, height):
        super().__init__(width, height, "Snake Game")
        self.snake = snk.Snake()
        self.apple = ap.Apple()
        self.score = 0
        self.frame_count = 0
        self.game_over = False 

    def on_draw(self):
        arcade.start_render()
        if not self.game_over:  # Mostrar elementos del juego si no se ha perdido
            for segment in self.snake.segments:
                arcade.draw_rectangle_filled(segment[0] * GRID_SIZE + GRID_SIZE / 2,
                                             segment[1] * GRID_SIZE + GRID_SIZE / 2,
                                             GRID_SIZE, GRID_SIZE, arcade.color.GREEN)
            arcade.draw_rectangle_filled(self.apple.position[0] * GRID_SIZE + GRID_SIZE / 2,
                                         self.apple.position[1] * GRID_SIZE + GRID_SIZE / 2,
                                         GRID_SIZE, GRID_SIZE, arcade.color.RED)
            arcade.draw_text(f"Score: {self.score}", 10, SCREEN_HEIGHT - 20, arcade.color.WHITE, 16)
        else:  # Mostrar mensaje de "Game Over" si se ha perdido
            arcade.draw_text("Game Over", SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2,
                             arcade.color.RED, font_size=50, anchor_x="center")


    def on_update(self, delta_time):
        if not self.game_over:
            self.frame_count += 1
            if self.frame_count % SNAKE_SPEED == 0:
                self.snake.move()
                if self.snake.collides_with_apple(self.apple.position):
                    self.snake.segments.append(self.apple.position)
                    self.apple.respawn()
                    self.score += 1
                elif self.snake.collides_with_self() or not self.is_snake_within_bounds():
                    self.game_over = True

    def is_snake_within_bounds(self):
        head_x, head_y = self.snake.segments[0]
        return 0 <= head_x < SCREEN_WIDTH // GRID_SIZE and 0 <= head_y < SCREEN_HEIGHT // GRID_SIZE

    def on_key_press(self, key, modifiers):
        if key == arcade.key.UP:
            self.snake.change_direction("up")
        elif key == arcade.key.DOWN:
            self.snake.change_direction("down")
        elif key == arcade.key.LEFT:
            self.snake.change_direction("left")
        elif key == arcade.key.RIGHT:
            self.snake.change_direction("right")
        elif self.game_over and key == arcade.key.SPACE:
            self.restart_game() 


    def restart_game(self):
        self.snake = snk.Snake()
        self.apple = ap.Apple()
        self.score = 0
        self.frame_count = 0
        self.game_over = False

def main():
    game = SnakeGame(SCREEN_WIDTH, SCREEN_HEIGHT)
    arcade.run()

if __name__ == "__main__":
    main()



