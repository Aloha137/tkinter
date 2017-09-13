import tkinter
import random

WIDTH = 640
HEIGHT = 420
BG_COLOR = 'white'
ZERO = 0
BAD_COLOR = 'red'
COLORS = ['aqua', 'fuchsia', 'pink', 'yellow', 'gold', BAD_COLOR]

class Balls(object):
	"""balls class"""
	def __init__(self, x, y, r, color, dx=0,dy=0):
		self.x = x
		self.y = y		
		self.r = r
		self.color = color
		self.dx = dx
		self.dy = dy

	def draw(self):
		canvas.create_oval(self.x - self.r, self.y - self.r, self.x + self.r, self.y + self.r, fill=self.color, outline=self.color if self.color != BAD_COLOR else "black") 


	def hide(self):
		canvas.create_oval(self.x - self.r, self.y - self.r, self.x + self.r, self.y + self.r, fill=BG_COLOR, outline=BG_COLOR) 

	def is_collision(self, ball):
		a = abs(self.x + self.dx - ball.x)
		a = abs(self.y + self.dy - ball.y)
		return (a*a + b*b)**0,5 <= self.r + ball.r

	def move(self):
		if (self.x + self.r + self.dx) >= WIDTH or (self.x - self.r + self.dx <= ZERO):
			self.dx = -self.dx
		if (self.y + self.r + self.dy) >= HEIGHT or (self.y - self.r + self.dy <= ZERO):
			self.dy = -self.dy
		# colliding with balls
		for ball in balls:
			if self.is_collision(ball):
				if ball.color != BAD_COLOR:  # good ball
					ball.hide()
					balls.remove(ball)
					self.dx = - self.dx
					self.dy = - self.dy
				else:
					self.dx = self.dy = 0
		self.hide()
		self.x += self.dx
		self.y += self.dy
		self.draw()


def mouse_click(event):
	global main_ball
	if event.num == 1:
		if "main_ball" not in globals():
			main_ball = Balls(event.x, event.y, 30 , 'blue', 1, 1)	
			main_ball.draw()
		else: 
			if main_ball.dx * main_ball.dy > 0:  #turn left
				main_ball.dy = - main_ball.dy
			else:
				main_ball.dx = - main_ball.dx
	elif event.num == 3:   #turn right
		if main_ball.dx * main_ball.dy > 0:  #turn left
			main_ball.dx = - main_ball.dx
		else:
			main_ball.dy = - main_ball.dy

def create_list_of_balls(number):
	lst = []
	while len(lst) < number:
		next_ball = Balls(random.choice(range(0, WIDTH)),
					      random.choice(range(0, HEIGHT)),
					      random.choice(range(15, 35)),
					      random.choice(COLORS))
		lst.append(next_ball)
		next_ball.draw()
	return lst

def count_bad_balls():
	res = 0
	for ball in balls :
		if ball.color == BAD_COLOR:
			res += 1
		return res
					     
def main():
	if 'main_ball' in globals():
		main_ball.move()
		if len(balls) - len(num_of_bad_balls) == 0:
			canvas.create_text(WIDTH/2, HEIGHT/2, text="YOU WON!", font="Arial 20", fill = "blue" )
			main_ball.dx = main_ball.dy = 0
		elif main_ball.dx == 0:
			canvas.create_text(WIDTH/2, HEIGHT/2, text="YOU LOSE!", font="Arial 20", fill = BAD_COLOR )
	root.after(10, main)


root = tkinter.Tk()
root.title("Colliding_balls")
canvas = tkinter.Canvas(root,width=WIDTH,height=HEIGHT,bg=BG_COLOR)
canvas.pack()
canvas.bind('<Button-1>', mouse_click)
canvas.bind('<Button-3>', mouse_click)
if 'main_ball' in globals():
	del main_ball
balls = create_list_of_balls(10)
num_of_bad_balls = count_bad_balls(balls)
main()
root.mainloop()