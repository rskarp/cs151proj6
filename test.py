#Riley Karp
#03/10/2016
#test.py

import time
import random
import graphicsPlus as gr

def main():
	'''
	  Draws circles with radius 10 in random colors and in
	  random places in the window of given title and size
	  until mouse is clicked in the window.
	'''
	win = gr.GraphWin('Press a key',400,400,False)

	shapes = []

	c = gr.Circle(gr.Point(250,250),10)
	c.draw(win)
	shapes.append(c)

	while True:
		time.sleep(0.5)
		for thing in shapes:
			r = random.randrange(0,255)
			g = random.randrange(0,255)
			b = random.randrange(0,255)
			color = gr.color_rgb(r,g,b)
			thing.setFill(color)
			dx = random.randint(-10,10)
			dy = random.randint(-10,10)
			thing.move(dx,dy)
	if random.random() < 0.2:
		oldthing = random.choice(shapes)
		newthing = oldthing.clone()
		newthing.draw(win)
		shapes.append(newthing)

	win.update()

	if win.checkMouse():
		break

	win.close()

if __name__ == '__main__':
	main()