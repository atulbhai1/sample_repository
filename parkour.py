from ursina import *
from ursina.prefabs.first_person_controller import  FirstPersonController
import tkinter.messagebox
app = Ursina()
grass_texture = load_texture('grass_block.png')
sky_texture = load_texture('skybox.png')
arm_texture = load_texture('arm_texture.png')
block_pick = 1
def update():
    if held_keys['backspace']: app.destroy(), quit()
    if player.z >= 48:
        app.destroy()
        quit()
    elif player.y < 0:
        app.destroy()
        quit()
class Block(Button):
    def __init__(self, position=(0, 0, 0)):
        super(Block, self).__init__(parent=scene, position=position, model='block.obj'
                                    , origin_y=0.5, texture=grass_texture,
                                    color=color.color(0, 0, random.uniform(0.9, 1)),
                                    scale=0.5)
class Sky(Entity):
    def __init__(self):
        super(Sky, self).__init__(
            parent=scene, model='sphere', texture =sky_texture, scale=150, double_sided=True)
class Hand(Entity):
    def __init__(self):
        super(Hand, self).__init__(parent=camera.ui, model='arm.obj', texture=arm_texture, scale=0.2, rotation=Vec3(150, -10, 0), position=Vec2(0.4, -0.6))
for z in range(50):
    if z % 2 == 0:
        for x in range(50):
            if x % 2 == 0:
                block = Block((x, 0, z))
player = FirstPersonController()
hand = Hand()
sky = Sky()
app.run()