from ursina import *
from ursina.prefabs.first_person_controller import  FirstPersonController

from time import sleep
app = Ursina()
grass_texture = load_texture('grass_block.png')
stone_texture = load_texture('stone_block.png')
brick_texture = load_texture('brick_block.png')
dirt_texture  = load_texture('dirt_block.png')
sky_texture = load_texture('skybox.png')
arm_texture = load_texture('arm_texture.png')
block_pick = 1
def update():
    global block_pick
    if held_keys['left mouse'] or held_keys['right mouse']:
        hand.active()
    else:
        hand.passive()
    if held_keys['1']:
        block_pick = 1
        sideBlock.change(grass_texture)
    elif held_keys['2']:
        block_pick = 2
        sideBlock.change(stone_texture)
    elif held_keys['3']:
        block_pick = 3
        sideBlock.change(brick_texture)
    elif held_keys['4']:
        block_pick = 4
        sideBlock.change(dirt_texture)
    if held_keys['backspace']: app.destroy(), quit()
    if player.y < -10:
        player.y = 0
        if player.x > 30:player.x = 59
        else:player.x = 0
        if player.z > 30:player.z = 59
        else:player.z = 0
class Block(Button):
    def __init__(self, position=(0, 0, 0), texture=grass_texture):
        super(Block, self).__init__(parent=scene, position=position, model='block.obj'
                                    , origin_y=0.5, texture=texture,
                                    color=color.color(0, 0, random.uniform(0.9, 1)),
                                    scale=0.5)
    def input(self, key):
        if self.hovered:
            if key == 'left mouse down':
                # noinspection PyShadowingNames
                if block_pick == 1:
                    block = Block(self.position + mouse.normal, grass_texture)
                if block_pick == 2:
                    block = Block(self.position + mouse.normal, stone_texture)
                if block_pick == 3:
                    block = Block(self.position + mouse.normal, brick_texture)
                if block_pick == 4:
                    block = Block(self.position + mouse.normal, dirt_texture)
            if key == 'right mouse down':
                destroy(self)
class Sky(Entity):
    def __init__(self):
        super(Sky, self).__init__(
            parent=scene, model='sphere', texture =sky_texture, scale=200, double_sided=True)
class Hand(Entity):
    def __init__(self):
        super(Hand, self).__init__(parent=camera.ui, model='arm.obj', texture=arm_texture, scale=0.2, rotation=Vec3(150, -10, 0), position=Vec2(0.4, -0.6))
    def active(self):
        self.position = Vec2(0.3, -0.5)
    def passive(self):
        self.position = Vec2(0.4, -0.6)
class SideBlock(Entity):
    def __init__(self):
        super(SideBlock, self).__init__(parent=camera.ui, model='block.obj', texture=grass_texture, scale=0.1, position=Vec2(0.6, 0.35), rotation=Vec3(20, -45, 0))
    def change(self, te=grass_texture):
        self.texture = te
for z in range(60):
    for x in range(60):
        block = Block((x, 0, z))
player = FirstPersonController()
hand = Hand()
sky = Sky()
sideBlock = SideBlock()
app.run()