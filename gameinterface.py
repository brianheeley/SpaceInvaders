# Sofia Bollo

import stddraw
import sys
import stdio
import stdaudio
from picture import Picture
import helpmenu


# defining function titleScreen that is displyed when the game is opened.
def titleScreen():

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

    # keeps displaying title screen until a button is pressed by the user
    while True:

        # display immediately, no delay between drawing and displaying content
        stddraw.show(0)

        # returns true if user has pressed a key
        if stddraw.hasNextKeyTyped():

            # retrieves key that has been pressed by user
            selectedKey = stddraw.nextKeyTyped()

            if selectedKey == "X" or selectedKey == "x":
                stddraw.clear(stddraw.BLACK)
                stddraw.text(400, 300, "Exiting game...")
                stddraw.show(1000)
                sys.exit()

            elif selectedKey == "H" or selectedKey == "h":
                stddraw.clear()
                helpmenu.help()

            else:
                break
