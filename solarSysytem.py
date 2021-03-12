from ursina import *
import numpy as np
from ursina.prefabs.first_person_controller import FirstPersonController
def update():
    global t
    t += .02
    angle = np.pi * 40/180
    radius = 1
    mercury.x = np.cos(t)*radius*2
    mercury.z = np.sin(t) * radius*2
    radius = 1.4
    venus.x = np.cos(t + angle) * radius*2
    venus.z = np.sin(t + angle) * radius*2
    radius = 1.8
    earth.x = np.cos(t + angle*2) * radius*2
    earth.z = np.sin(t + angle*2) * radius*2
    radius = 2.2
    mars.x = np.cos(t + angle*3) * radius*2
    mars.z = np.sin(t + angle*3) * radius*2
    radius = 2.6
    jupiter.x = np.cos(t + angle*4) * radius*2
    jupiter.z = np.sin(t + angle*4) * radius*2
    radius = 3
    saturn.x = np.cos(t + angle*5) * radius*2
    saturn.z = np.sin(t + angle*5) * radius*2
    radius = 3.4
    uranus.x = np.cos(t + angle*6) * radius*2
    uranus.z = np.sin(t + angle*6) * radius*2
    radius = 3.8
    neptune.x = np.cos(t + angle*7) * radius*2
    neptune.z = np.sin(t + angle*7) * radius*2
    print(held_keys)
    if held_keys['up arrow']:
        player.y += 0.05
    if held_keys['down arrow']:
        player.y -= 0.05
app = Ursina()
sun = Entity(model='sphere', color = color.yellow, scale=2)
mercury = Entity(model='sphere', color = color.gray, scale=0.2)
venus = Entity(model='sphere', color = color.orange, scale=0.3)
earth = Entity(model='sphere', color = color.blue, scale=0.4)
mars = Entity(model='sphere', color = color.red, scale=0.25)
jupiter = Entity(model='sphere', color = color.white, scale=0.9)
saturn = Entity(model='sphere', color = color.light_gray, scale=0.8)
uranus = Entity(model='sphere', color = color.blue, scale=0.7)
neptune = Entity(model='sphere', color = color.black, scale=0.7)
t = -np.pi
player = FirstPersonController()
player.gravity = 0
app.run()