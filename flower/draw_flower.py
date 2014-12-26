import turtle

def draw_k(turtle,x,y):
	turtle.penup()
	turtle.setposition(x,y)
	turtle.pendown()
	turtle.right(90)
	turtle.forward(100)
	turtle.right(180)
	turtle.forward(50)
	turtle.right(45)
	turtle.forward(70)
	turtle.right(180)
	turtle.forward(70)
	turtle.left(90)
	turtle.forward(70)

def draw_c(turtle,x,y):
	turtle.penup()
	turtle.setposition(x,y)
	turtle.pendown()
	turtle.forward(70)
	turtle.right(180)
	turtle.forward(70)
	turtle.left(90)
	turtle.forward(100)
	turtle.left(90)
	turtle.forward(70)

def draw_art():
	window = turtle.Screen()
	window.bgcolor('red')
	
	brad = turtle.Turtle()
	brad.shape('turtle')
	brad.color('blue')
	brad.speed(2)

	brad.right(90)
	brad.forward(50)
	brad.right(90)
	brad.forward(5)
	brad.right(90)
	brad.forward(50)
	brad.right(3)
	brad.forward(50)
	brad.right(90)
	brad.forward(5)
	brad.right(90)
	brad.forward(50)

	window.exitonclick()

draw_art()