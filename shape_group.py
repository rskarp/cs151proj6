#Riley Karp
#03/10/3016
#shape_group.py

import random
import time
import graphicsPlus as gr

def draw(objlist,win):
	'''
	  Draws all of the objects in objlist in the window (win).
	'''
	for thing in objlist:
		thing.draw(win)
		
def move(objlist,dx,dy):
	'''
	  Draws all of the objects in objlist by dx in the x-direction
	  and dy in the y-direction.
	'''
	for thing in objlist:
		thing.move(dx,dy)
		
def undraw(objlist):
	'''
	  Undraws all of the objects in objlist.
	'''
	for thing in objlist:
		thing.undraw()

def steam_init(x,y,scale):
	'''
	  Creates the list of objects needed to draw a steam plant
	  at position (x,y) with the given scale.
	'''
	shapes = []
	
	#steam plant
	r = gr.Rectangle(gr.Point(x,y),gr.Point(x+scale*100,y-scale*30))
	r.setFill(gr.color_rgb(185,185,185))
	shapes.append(r)
	
	#roof
	r = gr.Rectangle(gr.Point(x-scale*1,y-scale*30),gr.Point(x+scale*101,y-scale*40))
	r.setFill(gr.color_rgb(176,133,85))
	shapes.append(r)
	
	#smokestack
	r = gr.Rectangle(gr.Point(x,y),gr.Point(x+scale*10,y-scale*100))
	r.setFill(gr.color_rgb(136,96,90))
	shapes.insert(0,r)
	
	return shapes
	
def steam_animation_frame(shapes,frame_num,win):
	'''
	  Draws one frame of a steam plant animation. The animation will
	  involve smoke rising out of the chimney. shapes is a list containing
	  the graphics objects needed to draw the steam plant. frame_num is a
	  number indicating which frame of animation it is. win is the GraphWin
	  object containing the scene.
	  This animates by creating up to 20 steam circles. Each circle 
	  creeps up the screen until it gets to the top, when it is brought
	  back down to the smokestack so it can be used again.
	'''
	p1 = shapes[0].getP1()
	p2 = shapes[0].getP2()
	
	dx = p2.getX() - p1.getX()
	newx = (p2.getX() + p1.getX())*0.5
	newy = p2.getY() - dx*0.5
	
	if frame_num % 2 == 0 and len(shapes) < 20:
		c = gr.Circle(gr.Point(newx,newy),0.4*dx)
		c.setFill(gr.color_rgb(150,150,150))
		c.draw(win)
		shapes.append(c)
		
	for thing in shapes[3:]:
		thing.move(0,-10)
		center = thing.getCenter()
		if center.y < 0:
			mx = newx - center.getX()
			my = newy - center.getY()
			thing.move(mx,my)
	
def test_steam():
	'''
	  Create a window and plot a scene with a picture 
	  of a steam plant in it.
	'''
	win = gr.GraphWin( 'title', 400, 400, False )

	steamplant = steam_init( 100, 300, 1.0 )

	draw( steamplant, win )
	
	for frame_num in range(100):
		time.sleep(0.25)
		steam_animation_frame(steamplant, frame_num,win)
		win.update()
		if win.checkMouse():
			break
	
	win.update()

	win.getMouse()
	win.close()
	
def dog_init(x,y,scale):
	'''
	  Creates the list of objects needed to draw a dog
	  at position (x,y) with the given scale.
	'''
	shapes = []
	
	#body IDX 0
	o = gr.Oval(gr.Point(x,y),gr.Point(x+200*scale,y-75*scale))
	o.setFill(gr.color_rgb(139,69,19))
	shapes.append(o)
	
	#tail IDX 1
	t = gr.Polygon(gr.Point(x,y-40*scale),gr.Point(x+5*scale,y-45*scale),
		gr.Point(x-50*scale,y-100*scale))
	t.setFill(gr.color_rgb(139,69,19))
	shapes.append(t)
	
	#legs IDX 2-5
	o = gr.Oval(gr.Point(x+20*scale,y-20*scale),gr.Point(x+30*scale,y+60*scale))
	o.setFill(gr.color_rgb(139,69,19))
	shapes.append(o)
	
	o = gr.Oval(gr.Point(x+27*scale,y-20*scale),gr.Point(x+37*scale,y+60*scale))
	o.setFill(gr.color_rgb(139,69,19))
	shapes.append(o)
	
	o = gr.Oval(gr.Point(x+153*scale,y-20*scale),gr.Point(x+163*scale,y+60*scale))
	o.setFill(gr.color_rgb(139,69,19))
	shapes.append(o)
	
	o = gr.Oval(gr.Point(x+170*scale,y-20*scale),gr.Point(x+180*scale,y+60*scale))
	o.setFill(gr.color_rgb(139,69,19))
	shapes.append(o)
	
	#head IDX 6
	c = gr.Circle(gr.Point(x+210*scale,y-85*scale),40*scale)
	c.setFill(gr.color_rgb(139,69,19))
	shapes.append(c)
	
	#ear IDX 7
	o = gr.Oval(gr.Point(x+180*scale,y-120*scale),gr.Point(x+200*scale,y-60*scale))
	o.setFill(gr.color_rgb(160,82,45))
	shapes.append(o)
		
	#eye IDX 8
	c = gr.Circle(gr.Point(x+220*scale,y-110*scale),8*scale)
	c.setFill(gr.color_rgb(30,144,255))
	shapes.append(c)
		
	#nose IDX 9
	c = gr.Circle(gr.Point(x+250*scale,y-90*scale),10*scale)
	c.setFill(gr.color_rgb(199,21,133))
	shapes.append(c)
	
	#tongue IDX 10
	o = gr.Oval(gr.Point(x+245*scale,y-75*scale),gr.Point(x+280*scale,y-80*scale))
	o.setFill(gr.color_rgb(219,112,147))
	shapes.append(o)
	
	#neck
	neck = gr.Polygon(gr.Point(x+200*scale,y-46*scale),gr.Point(x+190*scale,y-40*scale),
		gr.Point(x+230*scale,y+27*scale),gr.Point(x+237*scale,y+20))
	neck.setFill(gr.color_rgb(139,69,19))
	shapes.append(neck)
	
	return shapes
	
def dog_animation_frame(shapes,frame_num,win):
	'''
	  Animates the dog by drawing and undrawing the tongue
	  and having the dog's tail wag, then moving the
	  dog's head and continuing the licking and tail wag.
	'''
	x = shapes[0].getP1().getX()
	y = shapes[0].getP1().getY()
	scale = shapes[0].getP2().getX() - (x+200)

	
	if frame_num % 2 == 0 and frame_num < 9:
		shapes[-1].undraw()
		shapes[1].move(0,2.5)
		shapes[10].undraw()
	elif frame_num % 2 == 1 and frame_num < 9:
		shapes[-1].undraw()
		shapes[1].move(0,-2.5)
		shapes[10].undraw()
		shapes[10].draw(win)
		
	elif frame_num == 26:
		shapes[-1].undraw()
		shapes[-1].draw(win)
		
	elif frame_num > 18 and frame_num < 32 and frame_num != 26:
		newy = (shapes[6].getCenter().getY()) - 20
		for shape in shapes[6:11]:
			if newy < (y+40*scale):
				shape.move(5,10)
		
	elif frame_num % 2 == 0 and frame_num > 32:
		shapes[1].move(0,2.5)
		undraw(shapes[10:11])
	elif frame_num % 2 == 1 and frame_num > 32:
		shapes[1].move(0,-2.5)
		undraw(shapes[10:11])
		draw(shapes[10:11],win)
		
def test_dog():
	'''
	  Creates a window and plots a scene with a picture 
	  of a dog in it, that wags its tail and sticks out
	  its tongue, then moves its head and continues licking.
	'''
	win = gr.GraphWin( 'title', 700, 700, False )

	dog1 = dog_init( 100, 500, 1.0 )
	dog2 = dog_init( 50, 200, 1.0 )
	dog3 = dog_init( 400, 400, 0.8 )
	
	dogs = [dog1,dog2,dog3]
	
	for dog in dogs:
		draw( dog, win )
		
	frame_num = 0
	while True:
		time.sleep(0.25)
		for dog in dogs:
			dog_animation_frame(dog, frame_num, win)
		frame_num += 1
		win.update()
		if win.checkMouse():
			break
	
	win.update()

	win.getMouse()
	win.close()	
	
def icecream_init(x,y,scale):
	'''
	  Creates the list of objects needed to draw an ice cream
	  cone at position (x,y) with the given scale.
	'''
	shapes = []
	
	#cone IDX 0
	t = gr.Polygon(gr.Point(x,y),gr.Point(x+5*scale,y-15*scale),
		gr.Point(x-5*scale,y-15*scale))
	t.setFill(gr.color_rgb(222,184,135))
	shapes.append(t)
	
	#scoops IDX 1-4
	c = gr.Circle(gr.Point(x,y-20*scale),6*scale)
	c.setFill(gr.color_rgb(255,0,127))
	shapes.append(c)
	
	c = gr.Circle(gr.Point(x,y-30*scale),6*scale)
	c.setFill(gr.color_rgb(0,255,128))
	shapes.append(c)
	
	c = gr.Circle(gr.Point(x,y-40*scale),6*scale)
	c.setFill(gr.color_rgb(153,255,255))
	shapes.append(c)
	
	c = gr.Circle(gr.Point(x,y-50*scale),6*scale)
	c.setFill(gr.color_rgb(255,153,153))
	shapes.append(c)
	
	return shapes

def icecream_animation_frame(shapes,frame_num,win):
	'''
	  Animates the ice cream cone by moving the scoops so
	  they tip over.
	'''
	(a,b,c) = shapes[0].getPoints()
	x = a.getX()
	y = a.getY()
	scale = shapes[1].getCenter().getY() - (y-20)
	
	if frame_num > 9:
		for i in range(1,5):
			p1i = shapes[i].getP1()
			p2i = shapes[i].getP2()
			dx = (p2i.getX() - p1i.getX())*i/6
			dy = (p1i.getY() - p2i.getY())*i/6
			newy = shapes[i].getCenter().getY() - dy
			if newy < y:
				shapes[i].move(dx,-dy)
				
def test_icecream():
	'''
	  Create a window and plot a scene with a picture 
	  of an ice cream cone in it, that tips over.
	'''
	win = gr.GraphWin( 'title', 400, 400, False )

	icecream1 = icecream_init( 100, 150, 2.0 )
	icecream2 = icecream_init( 50, 200, 0.5 )
	icecream3 = icecream_init( 300, 300, 1.0 )
	
	icecreams = [icecream1,icecream2,icecream3]
	
	for icecream in icecreams:
		draw( icecream, win )
	frame_num = 0
	while True:
		time.sleep(0.25)
		for icecream in icecreams:
			icecream_animation_frame(icecream, frame_num, win)
		frame_num += 1
		win.update()
		if win.checkMouse():
			break
	
	win.update()

	win.getMouse()
	win.close()
	
def background_init(x,y,scale):
	'''
	  Creates the list of objects needed to draw the background
	  scene at position (x,y) with the given scale.
	'''
	shapes = []
	
	#sky IDX 0
	r = gr.Rectangle(gr.Point(x,y),gr.Point(x+scale*400,y+scale*400))
	r.setFill(gr.color_rgb(107,142,35))
	shapes.append(r)
	
	#ground IDX 1
	r = gr.Rectangle(gr.Point(x,y+300*scale),gr.Point(x+scale*400,y-scale*400))
	r.setFill(gr.color_rgb(0,191,255))
	shapes.append(r)
	
	#sun IDX 2
	c = gr.Circle(gr.Point(x+325*scale,y+75*scale),20*scale)
	c.setFill(gr.color_rgb(255,255,0))
	shapes.append(c)
	
	#yellow rays IDX 3-6
	t = gr.Polygon(gr.Point(x+325*scale,y+40*scale),gr.Point(x+327*scale,y+50*scale),
		gr.Point(x+323*scale,y+50*scale))
	t.setFill(gr.color_rgb(255,255,0))
	shapes.append(t)
	
	t = gr.Polygon(gr.Point(x+360*scale,y+75*scale),gr.Point(x+350*scale,y+73*scale),
		gr.Point(x+350*scale,y+77*scale))
	t.setFill(gr.color_rgb(255,255,0))
	shapes.append(t)
	
	t = gr.Polygon(gr.Point(x+325*scale,y+110*scale),gr.Point(x+327*scale,y+100*scale),
		gr.Point(x+323*scale,y+100*scale))
	t.setFill(gr.color_rgb(255,255,0))
	shapes.append(t)
	
	t = gr.Polygon(gr.Point(x+290*scale,y+75*scale),gr.Point(x+300*scale,y+73*scale),
		gr.Point(x+300*scale,y+77*scale))
	t.setFill(gr.color_rgb(255,255,0))
	shapes.append(t)
	
	#orange rays IDX 7-10
	t = gr.Polygon(gr.Point(x+352*scale,y+50*scale),gr.Point(x+341*scale,y+57*scale),
		gr.Point(x+344*scale,y+60*scale))
	t.setFill(gr.color_rgb(255,150,0))
	shapes.append(t)
	
	t = gr.Polygon(gr.Point(x+352*scale,y+100*scale),gr.Point(x+341*scale,y+93*scale),
		gr.Point(x+344*scale,y+90*scale))
	t.setFill(gr.color_rgb(255,150,0))
	shapes.append(t)
	
	t = gr.Polygon(gr.Point(x+298*scale,y+100*scale),gr.Point(x+309*scale,y+93*scale),
		gr.Point(x+306*scale,y+90*scale))
	t.setFill(gr.color_rgb(255,150,0))
	shapes.append(t)
	
	t = gr.Polygon(gr.Point(x+298*scale,y+50*scale),gr.Point(x+309*scale,y+57*scale),
		gr.Point(x+306*scale,y+60*scale))
	t.setFill(gr.color_rgb(255,150,0))
	shapes.append(t)
	
	return shapes
	
def background_animation_frame(shapes,frame_num,win):
	'''
	  Animates the background by having the color of the sun's
	  rays alternate between orange and yellow.
	'''
	for i in range(3,7):
		for j in range(7,11):
			if frame_num % 2 == 1:
				shapes[i].setFill(gr.color_rgb(255,150,0))
				shapes[j].setFill(gr.color_rgb(255,255,0))
			else:
				shapes[i].setFill(gr.color_rgb(255,255,0))
				shapes[j].setFill(gr.color_rgb(255,150,0))
	
def test_background():
	'''
	  Creates a window and plots a scene with a background
	  image of a sky, ground, and sun that changes colors.
	'''
	win = gr.GraphWin( 'title', 800, 800, False )

	background1 = background_init( 0, 0, 1.0 )
	background2 = background_init( 50, 450, 0.5 )
	background3 = background_init( 450, 100, 0.7 )
	
	backgrounds = [background1,background2,background3]
	
	for background in backgrounds:
		draw( background, win )
	
	frame_num = 0
	while True:
		time.sleep(0.25)
		for background in backgrounds:
			background_animation_frame(background, frame_num, win)
		frame_num += 1
		win.update()
		if win.checkMouse():
			break
	
	win.update()

	win.getMouse()
	win.close()
	
if __name__ == '__main__':
# 	test_dog()
# 	test_steam()
#  	test_icecream()
	test_background()