# Sofia Bollo

import stddraw
import stdaudio
import sys
from picture import Picture
import gameinterface

#defining help function that gives instructions when [H] is pressed
def help():

    helpBackground = Picture("helpBackground.jpg")
    stddraw.picture(helpBackground)

    helpmenuTitle = "COSMIC CLASH: How to play"
    stddraw.setPenColor(stddraw.BLACK)
    stddraw.setFontFamily("Courier")
    stddraw.setFontSize(38)
    stddraw.text(0, 25, helpmenuTitle)
    
    step1 = "Move Left [A]"
    step2 = "Rotate Left [Q]"
    step3 = "Move Right [D]"
    step4 = "Rotate Right [E]"
    step5 = "Shoot [SpaceBar]"
    stddraw.setFontFamily("Times New Roman")
    stddraw.setFontSize(25)
    stddraw.text(0, 10, step1)
    stddraw.text(0, 5, step2)
    stddraw.text(0, 0, step3)
    stddraw.text(0, -5, step4)
    stddraw.text(0, -10, step5)

    backButton = "Back to home screen [B]"
    stddraw.text(0, -15, backButton)

    while True:

        stddraw.show(0)
        
        if stddraw.hasNextKeyTyped():

            selectedKey = stddraw.nextKeyTyped()
            # return back to title page if [B] is pressed, otherwise continue displaying instructions
            if selectedKey == "B" or selectedKey == "b":
                stddraw.clear()
                gameinterface.titleScreen()
