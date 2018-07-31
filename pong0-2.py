import pygame as pygame

def moveBall():
    global white, location, radius, thickness, black, ScreenSize, speedx, speedy
    """
    Moves the ball when it bounces it just mirrors the direction, does not alter magnitude of speed vector
    Currently it bounces off of all 4 walls
    """
    
    #Changes the direction of the ball if it hits the left or right side of screen
    if location[0] + radius >= ScreenSize[0] or location[0] - radius <= 0: 
        speedx = -speedx
    #Changes the direction of the ball if it hits the top or bottom of the screen
    if location[1] + radius >= ScreenSize[1] or location[1] - radius <= 0:
        speedy = -speedy
    
    #Update Position
    location[0] = location[0] + speedx
    location[1] = location[1] + speedy
    
    #Delete old circle, draw new circle, update display
    window.fill(black)
    pygame.draw.circle(window, white, location, radius, thickness)
    pygame.display.flip()

"""
Variables
"""

fps = 60

speedx = 1
speedy = 1
black = (0, 0, 0)
thickness = 0
radius = 20
location = [400, 400]
white = (255, 255, 255)
ScreenSize = (1000, 600)
timer = pygame.time.Clock()
window = pygame.display.set_mode(ScreenSize)

"""
Main Loop
"""
while True:
    moveBall()
    timer.tick(fps)