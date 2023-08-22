import random
import main as ma

class Apple:
    def __init__(self):
        self.position = (random.randint(0, (ma.SCREEN_WIDTH - ma.GRID_SIZE) // ma.GRID_SIZE),
                        random.randint(0, (ma.SCREEN_HEIGHT - ma.GRID_SIZE) // ma.GRID_SIZE))

    def respawn(self):
        self.position = (random.randint(0, (ma.SCREEN_WIDTH - ma.GRID_SIZE) // ma.GRID_SIZE),
                        random.randint(0, (ma.SCREEN_HEIGHT - ma.GRID_SIZE) // ma.GRID_SIZE))
        