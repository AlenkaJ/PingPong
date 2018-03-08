from tkinter import *
import time

class Gui:
	def __init__(self,master, x,y):
	
		# player coordinates
		self.p1 = [[0,0],[x/20,y/7]]
		self.p2 = [[x-x/20,0],[x,y/7]]
		self.b  = [[x/20,0],[x/20+20,20]]
		
		# arena
		self.w = Canvas(master, width=x, height=y)
		self.w.pack()
		arena = self.w.create_rectangle(0, 0, x, y, fill="blue")
		
		# player init
		player1 = self.w.create_rectangle(self.p1, fill="red")
		player2 = self.w.create_rectangle(self.p2, fill="red")
		
		#ball init
		self.ball = self.w.create_rectangle(self.b, fill="black")
		
	def move(self,where):
		self.w.coords(self.ball, where)
		self.w.update()
		
		

root = Tk()
app = Gui(root,1000,700)

for i in range(100):
	app.move([i*10,0,20+i*10,20])
	time.sleep(0.02)
	
root.mainloop()
	