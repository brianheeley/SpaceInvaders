import stddraw as sd
import color
import math
from turrent import Turrent

class PowerUps:    
    def __init__(self, spawnRate: float):
        self.powerUps: list = []
        self.spawnRate: float = spawnRate  # probability to spawn
    
    def move(self, turrent: Turrent):
        for powerUp in self.powerUps:
            if not powerUp.bPosess:
                if powerUp.hit(turrent):
                    print('hit')
                else:
                    powerUp._move()
                    powerUp._draw()

    def activate(self):
        for powerUp in self.powerUps:
            if powerUp.bPosess == True:
                powerUp.bActive == True


###############################################################

class PowerUp:
    
    def __init__(self, type, x, y, speed):
        self.type: int = type # 1--fastShoot 2--spreadShot 3-nuke 4-instantKill
        self.x: float = x
        self.y: float = y
        self.speed: float = speed
        self.bActive: bool = False
        self.bPosess: bool = False

    
    def _draw(self):
        sd.setPenColor(color.BLUE)
        sd.setPenRadius(0.01)
        sd.filledSquare(self.x, self.y, 3)
    

    def _move(self):
        self.y -= self.speed / 20

    def hit(self, turrent: Turrent) -> bool:
        self.bPosess = True
        return self.getDistance(turrent.x, turrent.y) <= 5
    

    def getDistance(self, x, y) -> float:
        return math.sqrt((self.x - x)**2 + (self.y - y)**2)
