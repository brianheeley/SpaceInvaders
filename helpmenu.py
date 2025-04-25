import stddraw
import stdaudio
import sys
from picture import Picture
import gameinterface
import threading


# define function that plays sound when an option on menu is selected
def playClick():
    stdaudio.playFile("clickSound")


# defining help function that gives instructions when [H] is pressed
def help():

    helpBackground = Picture("assets/helpBackground.jpg")
    stddraw.picture(helpBackground)

    helpmenuTitle = "COSMIC CLASH: How to play"
    stddraw.setPenColor(stddraw.WHITE)
    stddraw.setFontFamily("Courier")
    stddraw.setFontSize(38)
    stddraw.text(400, 450, helpmenuTitle)

    step1 = "Move Left [A]"
    step2 = "Rotate Left [Q]"
    step3 = "Move Right [D]"
    step4 = "Rotate Right [E]"
    step5 = "Shoot [SpaceBar]"
    step6 = "Use power-up [F]"
    stddraw.setFontFamily("Times New Roman")
    stddraw.setFontSize(25)
    stddraw.text(400, 400, step1)
    stddraw.text(400, 350, step2)
    stddraw.text(400, 300, step3)
    stddraw.text(400, 250, step4)
    stddraw.text(400, 200, step5)
    stddraw.text(400, 150, step6)

    backButton = "Back to home screen [B]"
    stddraw.text(400, 120, backButton)
    exitGame = "Quit game [X]"
    stddraw.text(400, 90, exitGame)

    while True:

        stddraw.show(0)

        if stddraw.hasNextKeyTyped():

            # save key that was pressed by user in variable selectedKey
            selectedKey = stddraw.nextKeyTyped()

            # return back to title page if [B] is pressed, otherwise continue displaying instructions
            if selectedKey == "B" or selectedKey == "b":
                threading.Thread(target=playClick).start()
                return

            elif selectedKey == "X" or selectedKey == "x":
                threading.Thread(target=playClick).start()
                stddraw.clear()
                stddraw.clear(stddraw.BLACK)
                stddraw.setPenColor(stddraw.BLUE)
                stddraw.text(400, 300, "Exiting game...")
                stddraw.show(1000)
                sys.exit()

            else:
                break
