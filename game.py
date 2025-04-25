import stddraw
import gameinterface
import random
import sys
import math
from player import Player
from turret import Turret
from bullets import BulletManager, EnemyBulletManager
from enemies import EnemyManager
from power_ups import PowerUpManager, PowerUp
from picture import Picture
from effects import EffectsManager
from bunker import Bunker, BunkerManager
from sounds import SoundManager


# Function to display game over screen with score
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

    # Setup game window size and scale
    stddraw.setCanvasSize(800, 600)
    stddraw.setXscale(0, 800)
    stddraw.setYscale(0, 600)

    # Initialize variables for game start
    game_state = "menu"
    score = 0
    game_running = True
    level = 1
    lives = 3
    move_cooldown = 30
    chance = 0.2
    win_state = False

    # Load the effects and bunker manager classes
    effects_manager = EffectsManager()
    bunker_manager = BunkerManager()

    # Loop while game still running
    while game_running:
        stddraw.clear(stddraw.BLACK)
        keys = stddraw.getKeysPressed()

        # Exit if Escape or X pressed
        if keys[stddraw.K_ESCAPE] or keys[stddraw.K_x]:
            stddraw.clear(stddraw.BLACK)
            stddraw.setPenColor(stddraw.BLUE)
            stddraw.setFontSize(25)
            stddraw.text(400, 300, "Exiting...")
            stddraw.show(1000)
            sys.exit()

            game_running = False

        # Run when in menu state
        if game_state == "menu":
            key_pressed = gameinterface.titleScreen()

            # Start game if any key other than 'H' or 'X' is pressed
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
                bullet_manager = BulletManager(4, 3)
                enemy_bullet_manager = EnemyBulletManager(10, 10, 3)
                enemy_manager = EnemyManager(8, 4, move_cooldown)
                bunker = Bunker(250, 250, 200, 90)
                power_up_manager = PowerUpManager(0.2)  # Start with spawn rate of 0.2
                score = 0

        # Run when game has started
        if game_state == "playing":
            stddraw.clear(stddraw.BLACK)

            # Draw the background stars
            effects_manager.add_star()
            effects_manager.update()

            # Update for player movement
            player.move(keys)
            turret.update(keys)

            # Shoot if space is pressed
            if keys[stddraw.K_SPACE]:
                bullet_manager.create_bullet(turret.end_x, turret.end_y, turret.angle)

            # Update all managers to check for game events
            bullet_manager.update()
            enemy_manager.update()
            bunker_manager.update(enemy_bullet_manager, bullet_manager)
            enemy_manager.shoot(enemy_bullet_manager, chance)
            enemy_bullet_manager.update()

            # Increase score with enemy kill
            score += bullet_manager.check_enemy_collisions(enemy_manager)

            # Checking for game over conditions

            if enemy_manager.check_reached_bottom(player.y + player.height / 2):
                game_state = "game_over"

            if (
                enemy_bullet_manager.check_player_collision(player)
                and player.lives <= 1
            ):
                game_state = "game_over"

            # After a player gets hit while still having lives
            if enemy_bullet_manager.check_player_collision(player) and player.lives > 1:
                bullet_manager.bullets.clear()
                enemy_bullet_manager.bullets.clear()
                player.lives -= 1
                player.x = 400

            # Go to next level when all enemies killed
            if len(enemy_manager.enemies) == 0:
                game_state = "win"
                SoundManager.play_sound("assets/levelUp")
                stddraw.show(3000)
            # Draw player, turret, and bunkers
            player.draw()
            turret.draw()
            bunker_manager.draw()

            power_up_type = 0

            # Power ups implementation
            if player.game_timer % 10000 == 0 and player.game_timer != 0:
                if power_up_manager.spawn_rate >= random.random():
                    power_up_type = random.randint(1, 4)
                    new_power_up = PowerUp(
                        power_up_type, 33 + random.random() * 767, 610, 1
                    )
                    power_up_manager.power_ups.append(new_power_up)

            power_up_manager.move(player, bullet_manager)  # Move and draw power ups
            if keys[stddraw.K_f]:  # Activate on player press 'F'

                # Add to score if nuke powerup used
                score += power_up_manager.activate(
                    bullet_manager, player, enemy_manager, score
                )

            power_up_manager.timePowerUp(bullet_manager, player) # Time duration of power up

            # Draw player score and lives
            stddraw.setPenColor(stddraw.WHITE)
            stddraw.setFontSize(25)
            stddraw.text(75, 580, f"Score: {score}")
            stddraw.text(725, 580, f"Lives: {player.lives}")

            stddraw.show(10)
            player.game_timer += 10

        # Restart game if over when space is pressed
        elif game_state == "game_over":
            game_over_screen(score)
            if keys[stddraw.K_SPACE]:
                game_state = "menu"

        elif game_state == "win":
            # Increase difficulty for next level
            if not win_state:
                level += 1
                move_cooldown = max(1, move_cooldown - 2)
                enemy_manager = EnemyManager(8, 4, move_cooldown)
                chance += 0.025

                bunker_manager.regenerate()

                power_up_manager.spawn_rate += min(
                    ((player.game_timer / 160000)**2), 10
                )
                print(power_up_manager.spawn_rate)
                bullet_manager.bullets.clear()
                enemy_bullet_manager.bullets.clear()
                power_up_manager.power_ups.clear()
                power_up_manager.deactivate(bullet_manager, player)

                win_state = True

            # Draw next level screen until space is pressed
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
