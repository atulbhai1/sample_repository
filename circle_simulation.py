import pyglet, pymunk, time
from pymunk.pyglet_util import DrawOptions
from tkinter.messagebox import showinfo
window = pyglet.window.Window(1280, 720, 'Simulation', resizable=False)
options = DrawOptions()
space = pymunk.Space()
space.gravity = 0, -1000
mass = 1
radius = 30
segment = pymunk.Segment(space.static_body, (0, 0), (800, 40), 2)
segment.body.position = 500, 400
segment.elasticity = 0.8
segment.friction = 0.1
space.add(segment)
segment2 = pymunk.Segment(space.static_body, (0, 60), (800, 0), 2)
segment2.body.position = 100, 100
segment2.elasticity = 0.8
segment2.friction = 0.1
space.add(segment2)
@window.event
def on_draw():
    window.clear()
    space.debug_draw(options)
# noinspection PyUnusedLocal
@window.event
def on_mouse_press(x, y, buttons, modifiers):
    circle_moment = pymunk.moment_for_circle(mass, 0, radius)
    circle_body = pymunk.Body(mass, circle_moment)
    circle_body.position = x, y
    circle = pymunk.Circle(circle_body, radius)
    circle.elasticity = 0.8
    circle.friction = 1.0
    space.add(circle_body, circle)
def update(dt):
    space.step(dt)
    for circle in space.shapes:
        if circle.body.position.y < 0:
            space.remove(circle.body, circle)
pyglet.clock.schedule_interval(update, 1/60)
pyglet.app.run()