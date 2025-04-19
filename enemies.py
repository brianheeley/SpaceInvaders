import stddraw as sd
import color
import random
import math



class Enemies:
    
    def __init__(self, enemies: list, bRight: bool, speed: float):
        self.enemies: list[Enemy] = enemies
        self.bRight: bool = bRight
        self.speed: float = speed
   
    
    def spawn(self, level: int) -> None:
        self.speed = 0.5 * math.log(level) + 1
        rows: int = random.randint(2, 4)
        cols: int = random.randint(3, 5)

        offset = random.randint(-7 , 99 - int(rows * 8))
        for i in range(1,rows):
            # Create list with type Enemy entries
            for j in range(1,cols):
                x: int = j * 8 + offset
                y: int = i * 8 + 95
                newEnemy = Enemy(x, y, self.speed, False)
                self.enemies.append(newEnemy)


    def move(self) -> None:
        if not self.enemies:
            return 
        rightIndex: int = self.findRight()
        leftIndex: int = self.findLeft()
        if self.enemies[leftIndex].x <= 2.5:
            self.bRight = True            
        if self.enemies[rightIndex].x >= 97.5:
            self.bRight = False
        for i in range(len(self.enemies)):
            self.enemies[i].move(self.bRight, self.speed)
            self.enemies[i]._draw()
            


    def findRight(self) -> int:
        mostIndex: int = 0
        for i in range(1, len(self.enemies)):
            if self.enemies[i].x > self.enemies[mostIndex].x: mostIndex = i
        return mostIndex 


    def findLeft(self) -> int:
        mostIndex: int = 0
        for i in range(1, len(self.enemies)):
            if self.enemies[i].x < self.enemies[mostIndex].x: mostIndex = i
        return mostIndex


##########################################################################


class Enemy:
    
    def __init__(self, x, y, speed, bRight):
        self.x = x
        self.y = y
        self.speed = speed
        self.bRight = bRight

    
    def move(self, bRight, speed):
        self.bRight = bRight 
        self.speed = speed
        self.y -= self.speed / 20
        if self.bRight:
            self.x += self.speed / 35
        else:
            self.x -= self.speed / 35

    
    def _draw(self):
        sd.setPenColor(color.RED)
        sd.filledCircle(self.x, self.y, 2.5)
