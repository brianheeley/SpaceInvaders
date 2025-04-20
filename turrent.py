import math
import stddraw as sd
import color
from projectile import Projectile
from enemies import Enemies
from enemies import Enemy


class Turrent:

    def __init__(self, x_pos, y_pos, rotAngle, reloadTime, score, lastShootTime):
        self.x = x_pos
        self.y = y_pos
        self.rotAngle = rotAngle
        self.reloadTime = reloadTime
        self.score = score
        self.lastShootTime: float = lastShootTime

    def move(self, bRight: bool) -> None:
        if bRight == True:
            if self.x < 92.5:
                self.x += 4
        else:
            if self.x > 7.5:
                self.x -= 4

    def rotate(self, bRight: bool) -> None:
        if bRight == True:
            if self.rotAngle > 0:
                self.rotAngle -= 0.1
        else:
            if self.rotAngle < math.pi:
                self.rotAngle += 0.1

    def draw(self):
        sd.setPenColor(color.YELLOW)
        sd.filledCircle(self.x, self.y, 3.5)
        sd.setPenColor(color.BLACK)
        sd.circle(self.x, self.y, 3.5)

        # Draw aim
        aimX: float = self.x + 3.5 * math.cos(self.rotAngle)
        aimY: float = self.y + 3.5 * math.sin(self.rotAngle)
        sd.line(self.x, self.y, aimX, aimY)

    def shoot(
        self,
        projectiles: list,
        enemies: Enemies,
        bShoot: bool,
        shootTime: float,
        puValue: int,
        puActive: bool,
    ):

        if bShoot and (shootTime - self.lastShootTime >= self.reloadTime):
            # Add new projectile
            if puActive and puValue == 1:
                s1Projectile = Projectile(
                    self.x + 3.5 * math.cos(self.rotAngle - 0.1),
                    self.y + 3.5 * math.sin(self.rotAngle - 0.1),
                    self.rotAngle - 0.1,
                    15,
                )
                s2Projectile = Projectile(
                    self.x + 3.5 * math.cos(self.rotAngle + 0.1),
                    self.y + 3.5 * math.sin(self.rotAngle + 0.1),
                    self.rotAngle + 0.1,
                    15,
                )
            newProjectile = Projectile(
                self.x + 3.5 * math.cos(self.rotAngle),
                self.y + 3.5 * math.sin(self.rotAngle),
                self.rotAngle,
                15,
            )
            projectiles.append(newProjectile)
            self.lastShootTime = shootTime

        for projectile in projectiles[:]:  # Test per projectile
            projectile.draw()
            projectile.move()

            # Check for hit
            for enemy in enemies.enemies[:]:  # Test per enemy
                if projectile.hit(enemy):
                    if enemy in enemies.enemies:
                        enemies.enemies.remove(enemy)
                    if projectile in projectiles:
                        projectiles.remove(projectile)
                    self.score += 1
                    break

            if projectile.gone():
                projectiles.remove(projectile)

        return projectiles
