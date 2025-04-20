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


    def move(self, keys):
        if keys[stddraw.K_a] and self.x > self.width / 2:
            self.x -= self.speed
        if keys[stddraw.K_d] and self.x < 800 - self.width / 2:
            self.x += self.speed

    def draw(self):
        stddraw.setPenColor(stddraw.GREEN)
        stddraw.picture(
            self.pic, self.x, self.y - self.width / 2, self.width, self.height
        )
