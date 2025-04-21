import stddraw as sd
import color
import math
from enemies import Enemies
from enemies import Enemy


class Projectile:

    def __init__(self, x, y, angle, speed):
        self.x = x
        self.y = y
        self.angle = angle
        self.speed = speed

    def move(self) -> None:
        self.x += (self.speed / 10) * math.cos(self.angle)
        self.y += (self.speed / 10) * math.sin(self.angle)

    def draw(self) -> None:
        sd.setPenColor(color.YELLOW)
        sd.filledCircle(self.x, self.y, 1)

    def hit(self, enemy: Enemy) -> bool:
        return self.getDistance(self.x, self.y, enemy.x, enemy.y) < 2.75

    def gone(self) -> bool:
        return self.x > 105 or self.x < -5 or self.y > 105

    def getDistance(self, x1, y1, x2, y2) -> float:
        d: float = math.sqrt(math.pow(x2 - x1, 2) + math.pow(y2 - y1, 2))
        return d
