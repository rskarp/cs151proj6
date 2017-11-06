# Bruce Maxwell
# originally written in fall 2012
#

import time
import graphicsPlus as gr
import shape_group as sg

def saveFrame( basename, win, frame ):
    win.postscript( file="%s_%000d.ps"%(basename,frame), colormode='color')

def main():
    """ creates a scene with several animated steam plants"""
    # create a window
    win = gr.GraphWin( 'Steam Plants', 600, 600, False )

    # create three steam plants
    sp1 = sg.steam_init( 100, 500, 2.0 )
    sp2 = sg.steam_init( 300, 200, 0.4 )
    sp3 = sg.steam_init( 400, 300, 1.0 )

    # put all the steam plant objects in a list
    steamplants = [sp1, sp2, sp3]

    # draw all the steam plants
    for plant in steamplants:
        sg.draw( plant, win )
    
    # loop until the user clicks
    t = 0
    while True:
        time.sleep(0.25)

        # loop over the steam plant objects and animate them
        for plant in steamplants:
            sg.steam_animation_frame( plant, t, win )

        # increment the frame counter
        t += 1
        
        # Update the display
        win.update()
        
        # save frame
        saveFrame( 'lab6testmovie', win, t )

        # check for a mouse event and break if it occurs
        if win.checkMouse():
            break

    # close the window
    win.close()

if __name__ == "__main__":
    main()

        
