import stddraw
import picture


class Player:
    def __init__(self, x, y, width, height, speed):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.speed = speed

        self.pic = picture.Picture("assets/ship.jpg")
        self.lives = 3
        self.game_timer = 0

    # Move player's position on screen
    def move(self, keys):
        if keys[stddraw.K_a] and self.x > self.width / 2:
            self.x -= self.speed
        if keys[stddraw.K_d] and self.x < 800 - self.width / 2:
            self.x += self.speed

    # Draw player on screen
    def draw(self):
        stddraw.setPenColor(stddraw.GREEN)
        stddraw.picture(
            self.pic, self.x, self.y - self.width / 2, self.width, self.height
        )
