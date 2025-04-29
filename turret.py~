import stddraw
import math


class Turret:
    def __init__(self, player, angle, speed):
        self.player = player
        self.angle = angle
        self.speed = speed
        self.length = player.width / 3
        self.end_x = 0
        self.end_y = 0
        self.update_end()

    # Change turret end position based on rotation angle
    def update_end(self):
        self.end_x = self.player.x + self.length * math.cos(math.radians(self.angle))
        self.end_y = (
            self.player.y
            - self.player.height / 2
            + self.length * math.sin(math.radians(self.angle))
        )

    # Rotate turret if keys pressed
    def update(self, keys):
        if keys[stddraw.K_q] and self.angle < 180:
            self.angle += self.speed
        if keys[stddraw.K_e] and self.angle > 0:
            self.angle -= self.speed

        self.angle = max(0, min(180, self.angle))
        self.update_end()

    # Draw turret on screen
    def draw(self):
        stddraw.setPenColor(stddraw.DARK_GRAY)
        stddraw.setPenRadius(2.5)
        stddraw.line(
            self.player.x,
            self.player.y - self.player.height / 2,
            self.end_x,
            self.end_y,
        )
