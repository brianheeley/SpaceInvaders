import stddraw
import picture


class Bunker:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.picture = picture.Picture("assets/bunkers.png")

    def draw(self):
        stddraw.picture(
            self.picture, self.x, self.y - self.height / 2, self.width, self.height
        )


class BunkerManager:
    def __init__(self):
        self.bunkers = []
        self.populate()

    def draw(self):
        for bunker in self.bunkers:
            bunker.draw()

    def create_bunkers(self, x, y, width, height):
        self.bunkers.append(Bunker(x, y, width, height))

    def populate(self):
        x_spacing = 250
        y = 250

        for i in range(3):
            x = 150 + i * x_spacing
            self.create_bunkers(x, y, 200, 90)

    def update(self, enemy_bullet_manager, player_bullet_manager):
        bunkers_to_remove = []

        for i in range(len(self.bunkers)):
            bunker = self.bunkers[i]
            bunker.draw()

            if enemy_bullet_manager.check_bunker_collisions(bunker):
                enemy_bullet_manager.removeBullet(bunker)
                bunkers_to_remove.append(i)

            if player_bullet_manager.check_bunker_collisions(bunker):
                player_bullet_manager.removeBullet(bunker)
                bunkers_to_remove.append(i)

        for i in sorted(bunkers_to_remove, reverse=True):
            if i < len(self.bunkers):
                self.bunkers.pop(i)
