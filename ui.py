import stddraw as sd
import color
import math
import random
from turrent import Turrent
from enemies import Enemies
from enemies import Enemy
from power_ups import PowerUps
from power_ups import PowerUp




class Ui:

    def __init__(self, level: int, time: float, bStart):
        self.time: int = time  # running time in ms
        self.bStart: bool = bStart
        self.highScore: int = 0
    

    def createCanvas(self) -> None:
        sd.setCanvasSize(500, 500)
        sd.setXscale(0,100)
        sd.setYscale(0,100)  


    def home(self, score) -> None:
        sd.clear()
        sd.setPenColor(color.BLUE)   
        sd.setFontSize(30)
        sd.text(50, 92, "Game")
        sd.setFontSize(15)
        sd.text(50, 85, "[A] move left, [D} move right")
        sd.text(50, 80, "[Q] rotate left, [E] rotate right")
        sd.text(50, 75, "[Space] to shoot") 
        sd.text(50, 70, "[H] for help") 
        sd.text(50, 65, "[X] to quit") 
        sd.setFontSize(20)
        sd.text(50, 55, "Press any key to start")
        if score > self.highScore:
            self.highScore = score
        if self.bStart and score > -1:
            sd.setFontSize(15)
            sd.text(50, 45, "High score: " + str(self.highScore))
    
        while True:
            sd.show(500)
            if sd.hasNextKeyTyped():             
                key = sd.nextKeyTyped()        
                if key == 'x' or key == 'X':
                    print("Closing window...")
                    break
                elif key == 'h' or key == 'H':
                    print("Loading help...")
                    # help()
                    break
                else:
                    print("Loading game...")
                    self.game()
                    break


    def game(self) -> None:
        self.bStart = True
        self.time = 0
        turrent = Turrent(50, 5, (math.pi / 2), 300, 0, -1)
        projectiles: list = []   
        level: int = 1
        enemies = Enemies([], True, 1) 
        powerUps = PowerUps(1)
    
        while True:
            self.updateBG()
            bShoot: bool = False
           
           
            # spawn enemies
            if self.time % 6000 == 0:
                enemies = Enemies(enemies.enemies, random.choice([True, False]), 1) 
                enemies.spawn(level)

            # spawn power ups
            if self.time == 6000:
                level += 1
                if True: #random.random() < powerUps.spawnRate:
                    puType = random.randint(1,3)
                    puX = 4 + 92 * random.random() 
                    newPowerUp = PowerUp(puType, puX, 110, enemies.speed)
                    powerUps.powerUps.append(newPowerUp)
                      
            turrent.draw()
            enemies.move()
            powerUps.move(turrent)

            # controls implementation
            if sd.hasNextKeyTyped():
                key = sd.nextKeyTyped()
                if (key == 'A' or key == 'a'):
                    turrent.move(False)        #false for bRight argument - move left
                elif (key == 'D' or key == 'd'):
                    turrent.move(True)
                elif (key == 'Q' or key == 'q'):
                    turrent.rotate(False)      #false for bRight argument - rotate left
                elif (key == 'E' or key == 'e'):
                    turrent.rotate(True)
                elif (key == 'F' or key == 'f'):
                    powerUps.activate()
                elif (key == ' '):
                    bShoot = True
        
            if powerUps.powerUps:
                projectiles = turrent.shoot(projectiles, enemies, bShoot, self.time, powerUps.powerUps[-1].type, powerUps.powerUps[-1].bActive)
            else: 
                projectiles = turrent.shoot(projectiles, enemies, bShoot, self.time, 0, False)
        
            self.displayScore(turrent)

            # Check if player loses
            bLose: bool = self.checkLose(enemies.enemies)
            if bLose:
                print("Game Over")
                sd.show(2000)
                self.gameLost(turrent)
                return

            sd.show(1000/96)
            self.time += int(1000/96)


    def displayScore(self, turrent: Turrent):
        sd.setPenColor(color.GRAY)
        sd.text(90, 95, "Score: " + str(turrent.score))
        sd.text(30, 95, "Time: " + str(round(self.time, 1)))


    def checkLose(self, enemies: list[Enemy]):
        if not enemies:
            return False
        for i in range(len(enemies)):
            if (enemies[i].y <= 10):
                return True
        


    def gameLost(self, turrent: Turrent) -> None:
        print("time: " + str(round(self.time, 1)))
        
        while True:
            sd.clear()
            sd.setFontSize(30)
            sd.setPenColor(color.GRAY)
            sd.text(50, 70, "GAME OVER")
            sd.setFontSize(15)
            sd.text(50, 50, "Score: " + str(turrent.score))
            sd.text(50, 40, "Press Enter to continue")
            sd.show(500)
            if sd.hasNextKeyTyped():
                key = sd.nextKeyTyped()
                if (key in ["\n", "\r", "return"]):
                    self.home(turrent.score)
                    break

        
    def updateBG(self):
        sd.clear(color.BLACK)
        sd.setPenColor(color.WHITE)
        sd.setPenRadius(0.004)
        for i in range(20):
            x: float = random.random() * 100
            y: float = random.random() * 100
            sd.point(x,y)
