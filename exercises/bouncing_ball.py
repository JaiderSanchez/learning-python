"""BOUNCING BALL SIMULATION"""

import turtle

t = turtle.Turtle()
t.shape("circle")
t.speed(0)
t.up()  # Lift the pen to avoid drawing lines

x = -200 # Starting x position
y = 100 # Starting y position
vx = 3 # Velocity in x direction
vy = 0 # Velocity in y direction

while True:
    x += vx
    y += vy
    vy -= 0.5  # Gravity effect

    if y < -150:  # Bounce when hitting the ground
        y = -150
        vy = 10

    t.goto(x, y)

    if x > 200 or x < -200:  # Bounce when hitting the walls
        vx *= -1
