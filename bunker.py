import stddraw
import picture


class Bunker:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.picture = picture.Picture("assets/bunkers.png")
        self.health = 3

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
            self.create_bunkers(x, y, 125, 90)

    def update(self, enemy_bullet_manager, player_bullet_manager):
        bunkers_to_remove = []

        for i in range(len(self.bunkers)):
            bunker = self.bunkers[i]
            bunker.draw()

            # Check for enemy bullet collisions
            enemy_hit = enemy_bullet_manager.check_bunker_collisions(bunker)
            if enemy_hit:
                enemy_bullet_manager.removeBullet(bunker)
                bunker.health -= 1

            # Check for player bullet collisions
            player_hit = player_bullet_manager.check_bunker_collisions(bunker)
            if player_hit:
                player_bullet_manager.removeBullet(bunker)
                bunker.health -= 1

            # Add to bunker removal list if no health
            if bunker.health <= 0:
                bunkers_to_remove.append(i)

        # Remove bunkers that were hit
        for i in sorted(bunkers_to_remove, reverse=True):
            if i < len(self.bunkers):
                self.bunkers.pop(i)

    # Regenerate bunkers after level up
    def regenerate(self):

        self.bunkers.clear()
        self.populate()


