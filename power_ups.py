import stddraw as sd
import color
from color import Color
import math
from player import Player
from bullets import BulletManager
from enemies import EnemyManager
from sounds import SoundManager
import picture


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
                pic = power_up.pic
                sd.picture(pic, 20, 20, 20, 20)

    def activate(
        self, bullet_manager: BulletManager, player: Player, enemy_manager: EnemyManager
    ):
        # activate the power up that player has
        for power_up in self.power_ups:
            if power_up.b_posess == True:
                self.deactivate(
                    bullet_manager, player
                )  # Deactivate any current power up
                self.b_active = True
                power_up.b_posess = False

                if power_up.type == 1:
                    bullet_manager.cooldown = 11
                elif power_up.type == 2:
                    bullet_manager.spreadshot = True
                elif power_up.type == 3:  # Kill all enemies on screen
                    SoundManager.play_sound("assets/explode")
                    enemy_manager.destroyAll()
                    self.b_active = False
                    sd.show(1300)
                elif power_up.type == 4:
                    player.lives += 1
                    self.b_active = False
                else:
                    self.b_active = False
                self.screenFlash(power_up)
                self.power_ups.remove(power_up)

    def deactivate(self, bullet_manager: BulletManager, player: Player):
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
        sd.rectangle(0, 0, 800, 600)
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
        self.colour = sd.WHITE
        self.pic = picture.Picture("assets/extra_life_powerup.png")
        match self.type:
            case 1:
                self.pic = picture.Picture("assets/speed_powerup.png")
                self.colour = sd.YELLOW
            case 2:
                self.pic = picture.Picture("assets/multishoot_powerup.png")
                self.colour = sd.BLUE
            case 3:
                self.pic = picture.Picture("assets/nuke_powerup.jpg")
                self.colour = sd.RED
            case 4:
                self.colour = sd.GREEN

    def _draw(self):
        self.size = 30
        sd.picture(self.pic, self.x, self.y, 30, 30)

    def _move(self):
        self.y -= self.speed / 2

    def hit(self, player: Player, bullet_manager: BulletManager) -> bool:

        # Check for player collision
        if self.getDistance(player.x, player.y) <= self.size + player.height / 2:
            return True

        # Check for bullet collisions
        for bullet in bullet_manager.bullets[:]:  # Create safe copy
            if self.getDistance(bullet.x, bullet.y) <= self.size + bullet.size:
                try:
                    bullet_manager.bullets.remove(bullet)
                    return True
                except ValueError:
                    # If bullet was already removed
                    pass
        return False

    def getDistance(self, x, y) -> float:
        return math.sqrt((self.x - x) ** 2 + (self.y - y) ** 2)

    def outOfBounds(self) -> bool:
        if self.x < 0 or self.x > 800:
            return True
        if self.y < 0 or self.y > 1000:
            return True
        return False
