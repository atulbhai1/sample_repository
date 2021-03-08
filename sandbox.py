from ursina import *
from ursina.prefabs.first_person_controller import  FirstPersonController
import tkinter
from time import sleep
grass_strength = 1
stone_strength = 1
brick_strength = 1
dirt_strength = 1
width = 60
length = 60
window = tkinter.Tk()
tkinter.Label(window, text='Length: ').grid(row=0, column=0)
heightEntry = tkinter.Entry(window)
heightEntry.insert(0, '60')
heightEntry.grid(row=0, column=1)
tkinter.Label(window, text='Width: ').grid(row=1, column=0)
widthEntry = tkinter.Entry(window)
widthEntry.insert(0, '60')
widthEntry.grid(row=1, column=1)
tkinter.Label(window, text='Grass Strength: ').grid(row=2, column=0)
grassStrengthEntry = tkinter.Entry(window)
grassStrengthEntry.insert(0, '1')
grassStrengthEntry.grid(row=2, column=1)
tkinter.Label(window, text='Stone Strength: ').grid(row=3, column=0)
stoneStrengthEntry = tkinter.Entry(window)
stoneStrengthEntry.insert(0, '1')
stoneStrengthEntry.grid(row=3, column=1)
tkinter.Label(window, text='Brick Strength: ').grid(row=4, column=0)
brickStrengthEntry = tkinter.Entry(window)
brickStrengthEntry.insert(0, '1')
brickStrengthEntry.grid(row=4, column=1)
tkinter.Label(window, text='Dirt Strength: ').grid(row=5, column=0)
dirtStrengthEntry = tkinter.Entry(window)
dirtStrengthEntry.insert(0, '1')
dirtStrengthEntry.grid(row=5, column=1)
def ok():
    global width, length, grass_strength, dirt_strength, brick_strength, stone_strength
    width, length, grass_strength, stone_strength, brick_strength, dirt_strength = int(widthEntry.get()), int(heightEntry.get()), int(grassStrengthEntry.get()), int(stoneStrengthEntry.get()), int(brickStrengthEntry.get()), int(dirtStrengthEntry.get())
    window.destroy()
tkinter.Button(window, text='Load Game', command=ok).grid(row=6, columnspan=2)
window.mainloop()
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
        if player.x > width/2:player.x = width-1
        else:player.x = 0
        if player.z > length/2:player.z = length-1
        else:player.z = 0
class Block(Button):
    def __init__(self, position=(0, 0, 0), texture=grass_texture, strength=grass_strength):
        super(Block, self).__init__(parent=scene, position=position, model='block.obj'
                                    , origin_y=0.5, texture=texture,
                                    color=color.color(0, 0, random.uniform(0.9, 1)),
                                    scale=0.5)
        self.strength = strength
    def input(self, key):
        if self.hovered:
            if key == 'left mouse down':
                # noinspection PyShadowingNames
                if block_pick == 1:
                    block = Block(self.position + mouse.normal, grass_texture, grass_strength)
                if block_pick == 2:
                    block = Block(self.position + mouse.normal, stone_texture, stone_strength)
                if block_pick == 3:
                    block = Block(self.position + mouse.normal, brick_texture, brick_strength)
                if block_pick == 4:
                    block = Block(self.position + mouse.normal, dirt_texture, dirt_strength)
            if key == 'right mouse down':
                self.strength -= 1
                if self.strength <= 0:
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
for z in range(width):
    for x in range(length):
        block = Block((x, 0, z))
player = FirstPersonController()
hand = Hand()
sky = Sky()
sideBlock = SideBlock()
app.run()