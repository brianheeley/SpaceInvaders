import stddraw as sd
import color
from color import Color
import math
from player import Player
from bullets import BulletManager
from enemies import EnemyManager
from sounds import SoundManager


class PowerUpManager:
    def __init__(self, spawn_rate: float):
        self.spawn_rate: float = spawn_rate  # probability to spawn

        self.power_ups: list = []
        self.timer = 5000  # Duration of power ups
        self.b_active = False

    def move(self, player: Player, bullet_manager: BulletManager):
        for power_up in self.power_ups:
            if not power_up.b_posess:
                # Test if power up is hit by player
                if power_up.hit(player, bullet_manager):
                    print('hit')
                    # Remove other pu's if there are more than 1 in posession
                    for other_power_up in self.power_ups[:]:
                        if other_power_up.b_posess == True:
                            self.power_ups.remove(other_power_up)
                    power_up.b_posess = True


                elif power_up.outOfBounds():
                    self.power_ups.remove(power_up)
                else:
                    power_up._move()
                    power_up._draw()
            else:
                # Draw power up icon that is in posession in the corner
                sd.setPenColor(power_up.colour)
                sd.filledSquare(20, 20, power_up.size /2)
            

    def activate(self, bullet_manager: BulletManager, player: Player, enemy_manager: EnemyManager):
        # activate the power up that player has
        for power_up in self.power_ups:
            if power_up.b_posess == True:
                self.deactivate(bullet_manager, player) # Deactivate any current power up
                self.b_active = True
                power_up.b_posess = False
                print("activate pu")
                print(self.power_ups)

                if power_up.type == 1:
                    bullet_manager.cooldown = 11
                    print("fast shoot")
                elif power_up.type == 2:
                    bullet_manager.spreadshot = True
                    print("spread shot")
                elif power_up.type == 3:  # Kill all enemies on screen
                    print("nuke")
                    SoundManager.play_sound("assets/explode")
                    enemy_manager.destroyAll()
                    self.b_active = False
                    sd.show(700)
                elif power_up.type == 4:
                    player.lives += 1
                    print("extra life")
                    self.b_active = False
                else:
                    self.b_active = False
                self.screenFlash(power_up)
                self.power_ups.remove(power_up)


    def deactivate(self, bullet_manager: BulletManager, player: Player):
        print("deactivate pu")
        self.b_active = False
        bullet_manager.cooldown = 30
        bullet_manager.spreadshot = False
        self.timer = 5000


    def timePowerUp(self, bullet_manager: BulletManager, player: Player):

        if self.timer <= 0:
            self.deactivate(bullet_manager, player)
        elif self.b_active:
            self.timer -= 10

    def screenFlash(self, power_up):
        sd.setPenColor(power_up.colour)
        sd.setPenRadius(0.02)
        sd.rectangle(0,0, 800, 600)
        sd.show(200)
        

###############################################################


class PowerUp:

    def __init__(self, type, x, y, speed):
        self.type: int = (
            type  # 1--fastShoot 2--spreadShot 3--nuke 4--extraLife 5--instantKill
        )
        self.x: float = x
        self.y: float = y
        self.speed: float = speed

        self.size = 15
        self.b_posess: bool = False
        self.colour = color.GRAY
        match self.type:
            case 1: self.colour = color.YELLOW
            case 2: self.colour = color.BLUE
            case 3: self.colour = color.RED
            case 4: self.colour = color.GREEN
        


    def _draw(self):
        sd.setPenColor(self.colour)
        sd.setPenRadius(0.01)
        sd.filledSquare(self.x, self.y, self.size)


    def _move(self):
        self.y -= self.speed / 2
        


    def hit(self, player: Player, bullet_manager: BulletManager) -> bool:
        for bullet in bullet_manager.bullets:
            if (self.getDistance(player.x, player.y) <= self.size + player.height) or (self.getDistance(bullet.x, bullet.y) <= self.size +4):
                bullet_manager.bullets.remove(bullet)
                return True


    def getDistance(self, x, y) -> float:
        return math.sqrt((self.x - x) ** 2 + (self.y - y) ** 2)

    
    def outOfBounds(self) -> bool:
        if self.x < 0 or self.x > 800: return True
        if self.y < 0 or self.y > 1000: return True
        return False


