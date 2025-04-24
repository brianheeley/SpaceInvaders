# Sofia Bollo

import stddraw
import sys
import stdio
import stdaudio
from picture import Picture
import helpmenu
import threading


# defining function that makes click sound on selection
def playClick():
    stdaudio.playFile("clickSound")


# define function that sets title screen of the game
def drawTitleScreen():

    TSBackground = Picture("assets/TSBackground.jpg")
    stddraw.picture(TSBackground)

    gameTitle = "COSMIC CLASH!"
    stddraw.setPenColor(stddraw.BLUE)
    stddraw.setFontFamily("Courier")
    stddraw.setFontSize(70)
    stddraw.text(400, 450, gameTitle)

    helpScreen = "Need Help! [H]"
    startGame = "Start game [Press any key]"
    exitGame = "Quit game [X]"
    stddraw.setFontFamily("Times New Roman")
    stddraw.setFontSize(25)
    stddraw.text(400, 350, startGame)
    stddraw.text(400, 300, exitGame)
    stddraw.text(400, 250, helpScreen)
    stddraw.show(0)


# defining function that displays titlescreen when the game is opened
def titleScreen():

    drawTitleScreen()
    # keeps displaying title screen until a button is pressed by the user
    while True:

        # display immediately, no delay between drawing and displaying content
        stddraw.show(0)

        # returns true if user has pressed a key
        if stddraw.hasNextKeyTyped():

            # retrieves key that has been pressed by user
            selectedKey = stddraw.nextKeyTyped()

            if selectedKey == "X" or selectedKey == "x":
                threading.Thread(target=playClick).start()
                stddraw.clear(stddraw.BLACK)
                stddraw.text(400, 300, "Exiting game...")
                stddraw.show(1000)
                sys.exit()

            elif selectedKey == "H" or selectedKey == "h":
                threading.Thread(target=playClick).start()
                stddraw.clear()
                helpmenu.help()

                # Make sure no keys are left in buffer
                while stddraw.hasNextKeyTyped():
                    stddraw.nextKeyTyped()

                # Redraws title screen
                drawTitleScreen()

            else:
                # Returns the key that was pressed to function call
                return selectedKey
