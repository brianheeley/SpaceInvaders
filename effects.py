import picture
import stddraw
import random

class ExplosionEffect:
    def __init__(self, x, y, width, height, duration=100):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.duration = duration
        self.current_frame = 0
        self.explosion_pic = picture.Picture("assets/explosion.jpg")

    def update(self):
        self.current_frame += 1
        return self.current_frame <= self.duration

    def draw(self):
        stddraw.picture(
            self.explosion_pic,
            self.x,
            self.y - self.height / 2,
            self.width,
            self.height,
        )

class Star:
    def __init__(self, x, y, radius, speed):
        self.x = x
        self.y = y
        self. radius = radius
        self.speed = speed

    def update(self):
        self.y -= self.speed

    def draw(self):
        stddraw.filledCircle(self.x, self.y, self.radius)


class EffectsManager:
    def __init__(self):
        self.effects = []
        self.stars = []

    def add_explosion(self, x, y, width, height, duration=100):
        self.effects.append(ExplosionEffect(x, y, width, height, duration))

    def update(self):

        effects_to_remove = []
        for i in range(len(self.effects)):
            effect = self.effects[i]
            if not effect.update():
                effects_to_remove.append(i)
            else:
                effect.draw()

        for i in sorted(effects_to_remove, reverse=True):
            self.effects.pop(i)

        stars_to_remove = []
        for i in range(len(self.stars)):
            star = self.stars[i]
            if star.y <= 0:
                stars_to_remove.append(i)
            else:
                star.update()
                star.draw()

        for i in sorted(stars_to_remove, reverse=True):
            self.stars.pop(i)

    def add_star(self):
        if len(self.stars) < 100:

            star_x = random.randint(0, 800)
            star_y = random.randint(0, 600)
            self.stars.append(Star(star_x, star_y, 1, 0.5))

