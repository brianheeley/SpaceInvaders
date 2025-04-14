
# Sofia Bollo

import stddraw
import sys
import stdio
import stdaudio
from picture import Picture
import helpmenu

# defining function titleScreen that is displyed when the game is opened. 
def titleScreen():

    TSBackground = Picture("TSBackground.jpg")
    stddraw.picture(TSBackground)
    
    gameTitle = "COSMIC CLASH!"
    stddraw.setPenColor(stddraw.BLUE)
    stddraw.setFontFamily("Courier")
    stddraw.setFontSize(70)
    stddraw.text(0, 15, gameTitle)
    

    helpScreen = "Need Help! [H]"
    startGame = "Start game [Press any key]"
    exitGame = "Quit game [X]"
    stddraw.setFontFamily("Times New Roman")
    stddraw.setFontSize(25)
    stddraw.text(0, 0, startGame)
    stddraw.text(0, -5, exitGame)
    stddraw.text(0, -10, helpScreen)

    
    # keeps displaying title screen until a button is pressed by the user
    while True:
        
        # display immediately, no delay between drawing and displaying content       
        stddraw.show(0)
        
        # returns true if user has pressed a key
        if stddraw.hasNextKeyTyped():

            #retrieves key that has been pressed by user
            selectedKey = stddraw.nextKeyTyped()
            
            if selectedKey == 'X' or selectedKey == 'x':
                stddraw.clear(stddraw.BLACK)
                stddraw.text(0, 0 ,"Exiting game...")
                stddraw.show(1000)
                sys.exit()
            
            elif selectedKey == 'H' or selectedKey == 'h':
                stddraw.clear()
                helpmenu.help()

            else:
                stddraw.clear()
                ##gamePlay()
   
    
'''
def gamePlay():

    gameBackground = Picture("gameBackground.jpg")
    stddraw.picture(gameBackground)

    ## option1 = "Solo mode [1]"
    ## option2 = "Duo mode [2]"
    ##display options on screen

    while True:

        stddraw.show(0)
        
        if stddraw.hasNextKeyTyped():

            selectedKey = stddraw.nextKeyTyped()

            if selectedKey == 1:
                stddraw.clear()
                ## call 1player game function

            elif selectedKey == 2:
                stddraw.clear()
                ## call 2player game function



    backButton = "Back to home screen [B]"
    stddraw.text(0, -15, backButton)

    while True:

        stddraw.show(0)
        
        if stddraw.hasNextKeyTyped():

            selectedKey = stddraw.nextKeyTyped()

            if selectedKey == "B" or selectedKey == "b":
                stddraw.clear()
                titleScreen()

def level():

    gameBackground = Picture(gameBackground.jpg)
    stddraw.picture(gameBackground)

    level1 = "Easy [E]"
    level2 = "Hard [H]"
    # display text to screen

    while True:

        stddraw.show(0)
        
        if stddraw.hasNextKeyTyped():

            selectedKey = stddraw.nextKeyTyped()

            if selectedKey == 'E' or selectedKey == 'e':
                stddraw.clear()
                ## call easy game function

            elif selectedKey == 'H' or selectedKey == 'h':
                stddraw.clear()
                ## call hard game function


    backButton = "Back to home screen [B]"
    stddraw.text(0, -15, backButton)

    while True:

        stddraw.show(0)
        
        if stddraw.hasNextKeyTyped():

            selectedKey = stddraw.nextKeyTyped()

            if selectedKey == "B" or selectedKey == "b":
                stddraw.clear()
                titleScreen()




'''


            


 













    
    
    










                
        



    
    


    

