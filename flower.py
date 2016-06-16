'''
Author: Chin-Chwen Tien
Version: 1.0
Create Date: Wed June 15, 2016
Objective: draw a flower!!
'''

import turtle

def drawSquare(someTurtle):
	for i in range(1, 5):
		someTurtle.forward(100)
		someTurtle.right(90)

def drawFlower():
	# Call window
	window = turtle.Screen()
	window.bgcolor("red")

	# Create tutrle object
	pencil = turtle.Turtle()
	pencil.shape("turtle")
	pencil.color("yellow")

	# Draw flower
	for i in range(1, 37):
		drawSquare(pencil)
		pencil.right(10)
	pencil.color("green")
	pencil.right(90)
	pencil.forward(275)

	# Auxiliary func for window
	window.exitonclick()

drawFlower()
	
