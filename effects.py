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
        self.explosion_pic = None

    # Increase explosion effect timer
    def update(self):
        self.current_frame += 1
        return self.current_frame <= self.duration

    # Draw explosion effect on screen
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
        self.radius = radius
        self.speed = speed

    # Move star
    def update(self):
        self.y -= self.speed

    # Draw star on screen
    def draw(self):
        stddraw.filledCircle(self.x, self.y, self.radius)


class EffectsManager:
    def __init__(self):
        self.effects = []
        self.stars = []
        self.max_stars = 100

        # Load explosion image
        self.explosion_pic = picture.Picture("assets/explosion.jpg")

    # Add explosion effect
    def add_explosion(self, x, y, width, height, duration=100):
        explosion = ExplosionEffect(x, y, width, height, duration)
        explosion.explosion_pic = self.explosion_pic
        self.effects.append(explosion)

    def update(self):

        # Process effects
        effects_to_remove = []
        for i in range(len(self.effects)):
            effect = self.effects[i]
            if not effect.update():
                effects_to_remove.append(i)
            else:
                effect.draw()

        for i in sorted(effects_to_remove, reverse=True):
            self.effects.pop(i)

        # Process stars
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

    # Add star to screen
    def add_star(self):
        if len(self.stars) < self.max_stars:

            star_x = random.randint(0, 800)
            star_y = random.randint(0, 600)
            self.stars.append(Star(star_x, star_y, 1, 0.5))

