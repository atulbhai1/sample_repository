import turtle, random, time
window = turtle.Screen()
window.title('Tetris')
window.bgcolor('NavajoWhite2')
window.setup(width=600, height=800)
window.tracer(0)
class Shape:
    def __init__(self):
        self.x = 5
        self.y = 0
        self.color = random.randint(1, 7)
        square = [[1, 1],
                  [1, 1]]
        hLine = [[1, 1, 1, 1]]
        vLine = [[1],
                 [1],
                 [1],
                  [1]]
        leftL = [[1, 0, 0, 0],
                 [1, 1, 1, 1]]
        rightL = [[0, 0, 0, 1],
                 [1, 1, 1, 1]]
        leftS = [[1, 1, 0],
                 [0, 1, 1]]
        rightS = [[0, 1, 1],
                 [1, 1, 0]]
        t = [[0, 1, 0],
             [1, 1, 1]]
        shapes = [square, hLine, vLine, leftL, rightL, rightS, leftS, t]
        self.shape = random.choice(shapes)
        self.height = len(self.shape)
        self.width = len(self.shape[0])
    def moveLeft(self, g):
        if self.x > 0:
            if g[self.y][self.x - 1] == 0:
                self.erase(grid)
                self.x -= 1
    def moveRight(self, g):
        if self.x < 12 - self.width:
            if g[self.y][self.x + self.width] == 0:
                self.erase(grid)
                self.x += 1
    def draw(self, g):
        for y in range(self.height):
            for x in range(self.width):
                if self.shape[y][x] == 1:
                    g[self.y + y][self.x + x] = self.color
    def erase(self, g):
        for y in range(self.height):
            for x in range(self.width):
                if self.shape[y][x] == 1:
                    g[self.y + y][self.x + x] = 0
    def canMove(self, g):
        result = True
        for x in range(self.width):
            if self.shape[self.height - 1][x] == 1:
                if g[self.y + self.height][self.x + x] != 0:
                    result = False
        return result
    def rotate(self, g):
        # First erase_shape
        self.erase(g)
        rotated_shape = []
        for x in range(len(self.shape[0])):
            new_row = []
            for y in range(len(self.shape) - 1, -1, -1):
                new_row.append(self.shape[y][x])
            rotated_shape.append(new_row)
        right_side = self.x + len(rotated_shape[0])
        if right_side < len(g[0]):
            self.shape = rotated_shape
            self.height = len(self.shape)
            self.width = len(self.shape[0])
grid = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
pen = turtle.Turtle()
pen.penup()
pen.speed(0)
pen.shape('square')
pen.setundobuffer(None)
def draw_grid(p, g):
    pen.clear()
    top = 230
    left = -110
    colors = ['black', 'red', 'lightblue', 'blue', 'orange', 'yellow', 'green', 'purple']
    for y in range(len(g)):
        for x in range(len(g[0])):
            screenX = left + (x * 20)
            screenY = top - (y * 20)
            colorNumber = grid[y][x]
            color = colors[colorNumber]
            p.goto(screenX, screenY)
            p.color(color)
            p.stamp()
score = 0
def checkGrid(g):
    y = 23
    while y > 0:
        isFull = True
        for x in range(0, 12):
            if g[y][x] == 0:
                isFull = False
                y -= 1
                break
        if isFull:
            global score
            score += 10
            for copyY in range(y, 0, -1):
                for copyX in range(0, 12):
                    g[copyY][copyX] = g[copyY - 1][copyX]
def drawScore(p, s):
    p.color('blue')
    p.hideturtle()
    p.goto(-75, 350)
    p.write("Score: {}".format(s), move=False, align="left", font=("Arial", 24, "normal"))
shape = Shape()
grid[shape.y][shape.x] = shape.color
draw_grid(pen, grid)
window.listen()
window.onkeypress(lambda :shape.moveLeft(grid), 'Left')
window.onkeypress(lambda :shape.moveRight(grid), 'Right')
window.onkeypress(lambda :shape.rotate(grid), 'space')
drawScore(pen, score)
cont = True
while cont:
    nextCell = shape.y + 1
    if shape.y == 23 - shape.height + 1:
        shape = Shape()
        checkGrid(grid)
    elif shape.canMove(grid):
        shape.erase(grid)
        shape.y += 1
        shape.draw(grid)
    else:
        shape = Shape()
        checkGrid(grid)
    draw_grid(pen, grid)
    drawScore(pen, score)
    time.sleep(0.1)
    window.update()
window.mainloop()