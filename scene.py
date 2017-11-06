#Riley Karp
#03/17/2016
#scene.py

import shape_group as sg
import graphicsPlus as gr
import time

def saveFrame( name, win, frame ):
	'''
	  Saves the frame as a .ps file.
	'''
	win.postscript( file="%s_%000d.ps"%(name,frame), colormode='color')

def main():
	'''
	  Creates a scene with a dog licking an ice cream cone outside
	  in the sun. The sun's rays alternate between yellow and orange.
	  The ice cream tips over and the dog stops licking.
	'''
	win = gr.GraphWin( 'Ice Cream Dog', 600, 600, False )
	
	background = sg.background_init(0,0,1.5)
	dog = sg.dog_init(100,425,1.0)
	icecream = sg.icecream_init(383,463,2.0)
	
	images = [background,icecream,dog]
	
	for item in images:
		sg.draw(item,win)
		
	frame_num = 0
	while True:
		time.sleep(0.25)

		for item in images:
			sg.background_animation_frame( background, frame_num, win )
			sg.icecream_animation_frame( icecream, frame_num, win )
			sg.dog_animation_frame( dog, frame_num, win )

		frame_num += 1
		win.update()
# 		saveFrame( 'scenemovie', win, frame_num )
		if win.checkMouse():
			break

	win.close()
	
if __name__ == '__main__':
	main()