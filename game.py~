import stddraw
import gameinterface
import random
import sys
from player import Player
from turret import Turret
from bullets import BulletManager, EnemyBulletManager
from enemies import EnemyManager
from power_ups import PowerUpManager, PowerUp
from picture import Picture
from effects import EffectsManager
from bunker import Bunker, BunkerManager


def game_over_screen(score):
    stddraw.clear(stddraw.BLACK)

    stddraw.setPenColor(stddraw.RED)
    stddraw.setFontSize(40)
    stddraw.text(400, 400, "GAME OVER!")

    stddraw.setPenColor(stddraw.WHITE)
    stddraw.setFontSize(30)
    stddraw.text(400, 320, f"Final Score: {score}")

    stddraw.setFontSize(25)
    stddraw.text(400, 250, "PRESS SPACE TO PLAY AGAIN")
    stddraw.text(400, 220, "PRESS ESC TO EXIT")

    stddraw.show(10)


def main():
    stddraw.setCanvasSize(800, 600)
    stddraw.setXscale(0, 800)
    stddraw.setYscale(0, 600)

    background = Picture("assets/gameBackground.jpg")

    game_state = "menu"
    score = 0
    game_running = True
    level = 1
    lives = 3
    move_cooldown = 30
    chance = 0.05
    win_state = False
    b_power_up: bool = False

    power_up_manager = PowerUpManager(1)  # Temporary spawn rate of 1
    effects_manager = EffectsManager()
    bunker_manager = BunkerManager()

    if power_up_manager.spawn_rate >= random.random():
        new_power_up = PowerUp(random.randint(1, 5), 3 + random.random() * 897, 510, 1)
        power_up_manager.power_ups.append(new_power_up)

    while game_running:
        stddraw.clear(stddraw.BLACK)
        keys = stddraw.getKeysPressed()

        if keys[stddraw.K_ESCAPE] or keys[stddraw.K_x]:
            stddraw.clear(stddraw.BLACK)
            stddraw.setPenColor(stddraw.BLUE)
            stddraw.setFontSize(25)
            stddraw.text(400, 300, "Exiting...")
            stddraw.show(1000)
            sys.exit()

            game_running = False

        if game_state == "menu":
            key_pressed = gameinterface.titleScreen()
            if (
                key_pressed
                and key_pressed != "h"
                and key_pressed != "H"
                and key_pressed != "x"
                and key_pressed != "X"
            ):
                game_state = "playing"

                # Initialising entities
                player = Player(400, 100, 49, 62, 2)
                turret = Turret(player, 90, 1)
                bullet_manager = BulletManager(5, 4, 3)
                enemy_bullet_manager = EnemyBulletManager(10, 10, 3)
                enemy_manager = EnemyManager(8, 4, move_cooldown)
                bunker = Bunker(250,250,200,90)
                # power_up_manager = PowerUpManager(1)  # Temporary spawn rate of 1
                score = 0

        if game_state == "playing":
            stddraw.clear(stddraw.BLACK)

            # Currently disabled due to non transparent sprites
            # stddraw.picture(background)

            player.move(keys)
            turret.update(keys)

            if keys[stddraw.K_SPACE]:
                bullet_manager.create_bullet(turret.end_x, turret.end_y, turret.angle)

            bullet_manager.update()
            enemy_manager.update()
            bunker_manager.update(enemy_bullet_manager)

            enemy_manager.shoot(enemy_bullet_manager, chance)
            enemy_bullet_manager.update()

            score += bullet_manager.check_enemy_collisions(enemy_manager)

            if enemy_manager.check_reached_bottom(player.y + player.height / 2):
                game_state = "game_over"

            if enemy_bullet_manager.check_player_collision(player):
                game_state = "game_over"

            if len(enemy_manager.enemies) == 0:
                game_state = "win"

            player.draw()
            turret.draw()
            bunker_manager.draw()

            # Power ups implementation
            power_up_manager.move(player, bullet_manager)  # Move and draw power ups
            if keys[stddraw.K_f] and win_state:  # Activate on player press 'F'
                power_up_manager.activate(bullet_manager, player)
            power_up_manager.timePowerUp(bullet_manager, player)

            stddraw.setPenColor(stddraw.WHITE)
            stddraw.setFontSize(25)
            stddraw.text(75, 580, f"Score: {score}")

            effects_manager.update()

            stddraw.show(10)

        elif game_state == "game_over":
            game_over_screen(score)
            if keys[stddraw.K_SPACE]:
                game_state = "menu"

        elif game_state == "win":
            if not win_state:
                level += 1
                move_cooldown = max(1, move_cooldown - 2)
                enemy_manager = EnemyManager(8, 4, move_cooldown)
                chance += 0.025
                if power_up_manager.spawn_rate >= random.random():
                    new_power_up = PowerUp(
                        random.randint(1, 5), 3 + random.random() * 897, 510, 1
                    )
                    power_up_manager.power_ups.append(new_power_up)

                win_state = True

            stddraw.clear(stddraw.BLACK)
            stddraw.setPenColor(stddraw.GREEN)
            stddraw.setFontSize(40)
            stddraw.text(400, 400, f"Level {level}")

            stddraw.setFontSize(25)
            stddraw.text(400, 350, "PRESS SPACE TO CONTINUE")
            if keys[stddraw.K_SPACE]:
                game_state = "playing"
                win_state = False

            stddraw.show(10)


if __name__ == "__main__":
    main()
