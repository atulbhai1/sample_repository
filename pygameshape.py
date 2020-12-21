import pygame
pygame.init()
white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
pink = (255, 0, 230)
purple = (162, 0, 255)
yellow = (247, 255, 0)
orange = (255, 119, 0)
gameDisplay = pygame.display.set_mode((int(input('What is the width of the image?')), int(input('What is the length of the image?'))))
color_input = input('What color  should the display be? white, black, red, green, blue, pink, purple, yellow or orange?')
if color_input == 'red':
        color = red
elif color_input == 'white':
        color = white
elif color_input == 'black':
        color = black
elif color_input == 'green':
        color = green
elif color_input == 'blue':
        color = blue
elif color_input == 'pink':
        color = pink
elif color_input == 'purple':
        color = purple
elif color_input == 'yellow':
        color = yellow
else:
        color = orange
gameDisplay.fill(color)
you_should_keep_going = True
while you_should_keep_going:
    shape = input('What do you want to add to the image a pentagon, circle, triangle, rectangle or line?').strip()
    color_input = input('What color white, black, red, green, blue, pink, purple, yellow or orange?')
    if color_input == 'red':
        color = red
    elif color_input == 'white':
        color = white
    elif color_input == 'black':
        color = black
    elif color_input == 'green':
        color = green
    elif color_input == 'blue':
        color = blue
    elif color_input == 'pink':
        color = pink
    elif color_input == 'purple':
        color = purple
    elif color_input == 'yellow':
        color = yellow
    else:
        color = orange
    if shape == 'line':
        pygame.draw.line(gameDisplay, color, (int(input('What is the x-coordinate of the start on the line?')), int(input('What is the y-coordinate of the start on the line?'))), (int(input('What is the x-coordinate of the end of the line?')), int(input('What is the y-coordinate of the end of the line?'))))
    elif shape == 'circle':
        pygame.draw.circle(gameDisplay, color, (int(input('What is the x-coordinate of the middle of the circle?')), int(input('What is the y-coordinate of the middle of the circle?'))), int(input('What is the radius of the circle?')))
    elif shape == 'rectangle':
        pygame.draw.rect(gameDisplay, color, (int(input('What is the x-coordinate of the upper right corner of the rectangle')), int(input('What is the y-coordinate of the upper right corner of the rectangle?')), int(input('How wide is the rectangle?')), int('How long is the rectangle?')))
    elif shape == 'triangle':
        pygame.draw.polygon(gameDisplay, color, ((int(input('What is the x-coordinate of the first corner of the triangle?')), int(input('What is the y-coordinate of the first corner of the triangle'))), (int(input('What is the x-coordinate of the second corner of the triangle?')), int(input('What is the y-coordinate of the second corner of the triangle?'))), (int(input('What is the x-coordinate of the third corner of the triangle?')), int(input('What is the y-coordinate of the third corner of the triangle?')))))
    elif shape == 'pentagon':
        pygame.draw.polygon(gameDisplay, color, ((int(input('What is the x-coordinate of the first corner of the pentagon?')), int(input('What is the y-coordinate of the first corner of the pentagon?'))), (int(input('What is the x-coordinate of the second corner of the pentagon?')), int(input('What is the y-coordinate of the second corner of the pentagon?'))), (int(input('What is the x-coordinate of the third corner of the pentagon?')), int(input('What is the y-coordinate of the third corner of the pentagon?'))), (int(input('What is the x-coordinate of the fourth corner of the pentagon?')), int(input('What is the y-coordinate of the fourth corner of the pentagon?'))), (int(input('What is the x-coordinate of the fifth corner of the pentagon?')), int(input('What is the y-coordinate of the fifth corner of the pentagon?')))))
    keep = input('Do you want to add more things?')
    if keep == 'no':
        you_should_keep_going = False
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    pygame.display.update()