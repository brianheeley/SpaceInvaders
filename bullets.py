import stddraw
import math
from sounds import SoundManager
from effects import EffectsManager
from bunker import BunkerManager


class Bullet:
    def __init__(self, x, y, dx, dy, size):
        self.x = x
        self.y = y
        self.dx = dx
        self.dy = dy
        self.size = size

    def update(self):
        self.x += self.dx
        self.y += self.dy

    def draw(self):
        stddraw.filledCircle(self.x, self.y, self.size)

    def out_of_bounds(self):
        return self.x < 0 or self.x > 800 or self.y < 0 or self.y > 600


class BulletManager:
    def __init__(self, size, speed):
        self.size = size
        self.speed = speed
        self.bullets = []

        self.max_bullets = 100
        self.cooldown = 30
        self.current_cooldown = 0
        self.spreadshot = False
        self.effects_manager = EffectsManager()

    def create_bullet(self, x, y, angle):
        if self.current_cooldown == 0 and len(self.bullets) < self.max_bullets:

            # Spread shot activated
            if self.spreadshot:
                dx = math.cos(math.radians(angle) + 0.1) * self.speed
                dy = math.sin(math.radians(angle) + 0.1) * self.speed
                self.bullets.append(Bullet(x, y, dx, dy, self.size))

                dx = math.cos(math.radians(angle) - 0.1) * self.speed
                dy = math.sin(math.radians(angle) - 0.1) * self.speed
                self.bullets.append(Bullet(x, y, dx, dy, self.size))

            # Normal bullet
            dx = math.cos(math.radians(angle)) * self.speed
            dy = math.sin(math.radians(angle)) * self.speed
            self.bullets.append(Bullet(x, y, dx, dy, self.size))

            self.current_cooldown = self.cooldown

            # SoundManager.play_sound("assets/playerShoot")

    def removeBullet(self, bunker):
        bullets_to_remove = []

        for i in range(len(self.bullets)):
            bullet = self.bullets[i]
            if (
                bullet.x > bunker.x - bunker.width / 2
                and bullet.x < bunker.x + bunker.width / 2
                and bullet.y > bunker.y - bunker.height / 2
                and bullet.y < bunker.y + bunker.height / 2
            ):
                bullets_to_remove.append(i)

        for i in sorted(bullets_to_remove, reverse=True):
            if i < len(self.bullets):
                self.bullets.pop(i)

    def update(self):
        stddraw.setPenColor(stddraw.WHITE)

        if self.current_cooldown > 0:
            self.current_cooldown -= 1

        bullets_to_remove = []

        for i in range(len(self.bullets)):
            bullet = self.bullets[i]
            bullet.update()
            bullet.draw()

            if bullet.out_of_bounds():
                bullets_to_remove.append(i)

        for i in sorted(bullets_to_remove, reverse=True):
            self.bullets.pop(i)

    def check_enemy_collisions(self, enemy_manager):
        score = 0
        bullets_to_remove = []
        enemies_to_hit = []

        for i in range(len(self.bullets)):
            bullet = self.bullets[i]
            for j in range(len(enemy_manager.enemies)):
                enemy = enemy_manager.enemies[j]

                if (
                    bullet.x > enemy.x - enemy.width / 2
                    and bullet.x < enemy.x + enemy.width / 2
                    and bullet.y > enemy.y - enemy.height / 2
                    and bullet.y < enemy.y + enemy.height / 2
                ):
                    self.effects_manager.add_explosion(
                        enemy.x, enemy.y, enemy.width, enemy.height, 100
                    )
                    bullets_to_remove.append(i)
                    enemies_to_hit.append(j)
                    score += 10
                    break

        for i in sorted(bullets_to_remove, reverse=True):
            if i < len(self.bullets):
                self.bullets.pop(i)

        for i in enemies_to_hit:
            if i < len(enemy_manager.enemies):
                enemy = enemy_manager.enemies[i]
                enemy.is_exploding = True
                enemy.explosion_timer = 20
                SoundManager.play_sound("assets/explode")

        return score

    def check_bunker_collisions(self, bunker):
        for bullet in self.bullets:
            if (
                bullet.x > bunker.x - bunker.width / 2
                and bullet.x < bunker.x + bunker.width / 2
                and bullet.y > bunker.y - bunker.height / 2
                and bullet.y < bunker.y + bunker.height / 2
            ):
                return True
        return False


class EnemyBulletManager:
    def __init__(self, max_bullets, size, speed):
        self.max_bullets = max_bullets
        self.size = size
        self.speed = speed
        self.bullets = []

    def create_bullet(self, x, y):
        if len(self.bullets) < self.max_bullets:
            dx = 0
            dy = -self.speed
            self.bullets.append(Bullet(x, y, dx, dy, self.size))

    def update(self):
        stddraw.setPenColor(stddraw.YELLOW)

        bullets_to_remove = []

        for i in range(len(self.bullets)):
            bullet = self.bullets[i]
            bullet.update()
            bullet.draw()

            if bullet.out_of_bounds():
                bullets_to_remove.append(i)

        for i in sorted(bullets_to_remove, reverse=True):
            if i < len(self.bullets):
                self.bullets.pop(i)

    def check_bunker_collisions(self, bunker):
        for bullet in self.bullets:

            if (
                bullet.x > bunker.x - bunker.width / 2
                and bullet.x < bunker.x + bunker.width / 2
                and bullet.y > bunker.y - bunker.height / 2
                and bullet.y < bunker.y + bunker.height / 2
            ):
                return True
        return False

    def removeBullet(self, bunker):

        stddraw.setPenColor(stddraw.YELLOW)
        bullets_to_remove = []

        for i in range(len(self.bullets)):
            bullet = self.bullets[i]
            bullet.update()
            bullet.draw()

            if (
                bullet.x > bunker.x - bunker.width / 2
                and bullet.x < bunker.x + bunker.width / 2
                and bullet.y > bunker.y - bunker.height / 2
                and bullet.y < bunker.y + bunker.height / 2
            ):
                bullets_to_remove.append(i)

        for i in sorted(bullets_to_remove, reverse=True):
            if i < len(self.bullets):
                self.bullets.pop(i)

    def check_player_collision(self, player):
        for bullet in self.bullets:
            if (
                bullet.x > player.x - player.width / 2
                and bullet.x < player.x + player.width / 2
                and bullet.y > player.y - player.height / 2
                and bullet.y < player.y + player.height / 2
            ):
                return True
        return False
