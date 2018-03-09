# Animation
from tkinter import *
import time

arena_size = [500,500]

ball_radius = 20
ball_direction = [1,2]
ball_velocity = 10

# init GUI
root = Tk()
w = Canvas(root,width = arena_size[0],height = arena_size[1])
w.pack()
w.create_rectangle(0,0,arena_size[0],arena_size[1], fill = "black")


class Ball:
	def __init__(self, canvas,position, radius, direction, velocity, color):
		
		self.can = canvas
		self.pos = position # the center of the ball
		self.rad = radius
		self.dir = direction
		self.vel = velocity
		self.step = 0.01
		self.col = color
		
		self.last_moved = 0
		
		self.ball = canvas.create_oval(*self._position())
		self.can.itemconfig(self.ball,fill = color)
		
	def _position(self):
		# position, radius
		return [self.pos[0]-self.rad,self.pos[1]-self.rad,self.pos[0]+self.rad,self.pos[1]+self.rad]
	
	# vyjizdeni z mapy by slo osetrit pres max(vzdalenost od zdi, vlastni step)?
	def move(self, t):
		if self.step+self.last_moved<= t:
			self._collide([500,500])
			self.pos = [self.pos[0]+self.dir[0]*self.vel, self.pos[1]+self.dir[1]*self.vel]
			self.can.coords(self.ball,self._position())
			self.can.update()
			self.last_moved = t
		
	def _collide(self, a_s):
		if self.pos[0]+self.rad >= a_s[0] or self.pos[0]-self.rad <=0:
			self.dir[0] = -self.dir[0]
			
		if self.pos[1]+self.rad >= a_s[1] or self.pos[1]-self.rad <=0:
			self.dir[1] = -self.dir[1]

		
		

b = Ball(w,[50,50],20,[2,1],3,"white")

start = time.time()
while (time.time()-start<10):
	b.move(time.time()-start)





root.mainloop()




		
		
		
		
		
		