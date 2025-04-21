import stddraw as sd
import color
import math
from player import Player
from bullets import BulletManager


class PowerUpManager:
    def __init__(self, spawn_rate: float):
        self.spawn_rate: float = spawn_rate  # probability to spawn

        self.power_ups: list = []
        self.timer = 1000
        self.b_active = False

    def move(self, player: Player, bullet_manager: BulletManager):
        for power_up in self.power_ups:
            if not power_up.b_posess:
                # Test if power up hit player
                if power_up.hit(player):
                    print("hit")
                    power_up.b_posess = True
                else:
                    power_up._move()
                    power_up._draw()
            else:
                self.timePowerUp(bullet_manager, player)

    def activate(self, bullet_manager: BulletManager, player: Player):
        print('activate powerup')
        # activate the power up that player has
        for power_up in self.power_ups:
            if power_up.b_posess == True:
                self.b_active = True
                self.timer = 1000
                power_up.b_active == True
                print('activate pu')

                if power_up.type == 1:
                    bullet_manager.cooldown = 0
                    print("fast shoot")
                elif power_up.type == 2:
                    bullet_manager.spreadshot = True
                    print("spread shot")
                elif power_up.type == 3:  # Kill all enemies on screen
                    print("nuke")
                    self.power_ups.remove(power_up)
                elif power_up.type == 4:
                    player.lives += 1
                    print("extra life")
                    self.power_ups.remove(power_up)

    def deactivate(self, bullet_manager: BulletManager, player: Player):
        for power_up in self.power_ups:
            if power_up.b_active:
                if power_up.type == 1:
                    bullet_manager.cooldown = 30
                elif power_up.type == 2:
                    bullet_manager.spreadShot = False
                self.power_ups.remove(power_up)  # Delete power up from list
                self.b_active = False
                print('deactivate pu')

    def timePowerUp(self, bullet_manager: BulletManager, player: Player):
        if self.timer <= 0:
            self.deactivate(bullet_manager, player)
        elif self.b_active:
            self.timer -= 1


###############################################################


class PowerUp:

    def __init__(self, type, x, y, speed):
        self.type: int = (
            type  # 1--fastShoot 2--spreadShot 3--nuke 4--extraLife 5--instantKill
        )
        self.x: float = x
        self.y: float = y
        self.speed: float = speed
        self.b_active: bool = False
        self.b_posess: bool = False

    def _draw(self):
        if self.type == 1:
            sd.setPenColor(color.YELLOW)
        elif self.type == 2:
            sd.setPenColor(color.BLUE)
        elif self.type == 3:
            sd.setPenColor(color.RED)
        elif self.type == 4:
            sd.setPenColor(color.GREEN)

        sd.setPenRadius(0.01)
        sd.filledCircle(self.x, self.y, 15)
  

    def _move(self):
        self.y -= self.speed / 2

    def hit(self, player: Player) -> bool:
        return self.getDistance(player.x, player.y) <= player.height

    def getDistance(self, x, y) -> float:
        return math.sqrt((self.x - x) ** 2 + (self.y - y) ** 2)
