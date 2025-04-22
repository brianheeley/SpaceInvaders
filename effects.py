import picture
import stddraw


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


class EffectsManager:
    def __init__(self):
        self.effects = []

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
