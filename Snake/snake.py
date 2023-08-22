class Snake:
    def __init__(self):
        self.segments = [(5, 5)]
        self.direction = (1, 0)

    def move(self):
        new_head = (self.segments[0][0] + self.direction[0], self.segments[0][1] + self.direction[1])
        self.segments.insert(0, new_head)
        self.segments.pop()

    def change_direction(self, direction):
        if direction == "up" and self.direction != (0, -1):
            self.direction = (0, 1)
        elif direction == "down" and self.direction != (0, 1):
            self.direction = (0, -1)
        elif direction == "left" and self.direction != (1, 0):
            self.direction = (-1, 0)
        elif direction == "right" and self.direction != (-1, 0):
            self.direction = (1, 0)

    def collides_with_apple(self, apple_position):
        return self.segments[0] == apple_position

    def collides_with_self(self):
        return self.segments[0] in self.segments[1:]