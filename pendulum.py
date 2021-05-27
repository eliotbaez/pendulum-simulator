#!/usr/bin/python3
# importing image object from PIL
import math
from math import pi as PI, cos as cos, sin as sin
from PIL import Image, ImageDraw
from os import system

system('mkdir render')

w, h = 1920, 1080
start = (40, 40)
pivot = (960, 540)	# (px, px)

dt = 0.0001		# s ; smaller is better
t = 0			# s
r = 1			# m
m = 1			# kg
I = m * r * r	# kg * m^2
g = 9.8			# m / s^2
angle = 3 * PI / 4	# rad
omega = 0		# rad / s
framerate = 60	# frame / s

positions = []	# positions of the pendulum
positions += [angle]

while t < 10:
	# calculate torque
	# tau = r f sin theta
	tau = r * m * g * sin(angle)
	omega += dt * tau / I
	angle += dt * omega
	positions += [angle]
	t += dt

# creating new Image object
img = Image.new("RGB", (w, h), "black")

time = 0
frame = 0
timestep = round (1 / dt / framerate)

while time < len(positions):
	# create line image
	print ("rendering frame", frame)
	img1 = ImageDraw.Draw(img)
	endpoint = (pivot[0] + 540 * r * cos(positions[time] + PI / 2), pivot[1] - 540 * r * sin(positions[time] + PI / 2))
	
	img1.line([pivot, endpoint], fill ="white", width = 2)
	img.save("render/%04d.png" % frame, "png")
	img1.line([pivot, endpoint], fill ="black", width = 2)
	frame += 1; time += timestep