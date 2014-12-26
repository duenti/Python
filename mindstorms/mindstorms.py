import turtle

def draw_square(turtle):
	for i in range(1,5):
		turtle.forward(100)
		turtle.right(90)

def draw_art():
	window = turtle.Screen()
	window.bgcolor('red')
	
	brad = turtle.Turtle()
	brad.shape('turtle')
	brad.color('blue')
	brad.speed(5)

	for i in range(0,360,3):
		draw_square(brad)
		brad.right(3)

	#angie = turtle.Turtle()
	#angie.shape('turtle')
	#angie.color('yellow')
	#angie.circle(100)

	window.exitonclick()

draw_art()