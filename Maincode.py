import pygame #import library (called "modules" in python)
from math import sin #so we don't have to type "math.sin" each time
from math import cos
import random

pygame.init()#initializes Pygame
pygame.display.set_caption("Da Quiz 5")#sets the window title
screen = pygame.display.set_mode((800, 800))#creates game screen
screen.fill((0, 0, 150))#paint background black

GameLoop = True #variable to run game loop


class butterfly:
    def __init__(self, xpos, ypos):
        self.x = xpos
        self.y = ypos
    def draw(self):
        #draws a heart using circles and triangles
        pygame.draw.circle(screen, (250, 0, 130), (self.x+0, self.y+170), 60) #bottom of wing 1
        pygame.draw.circle(screen, (250, 0, 250), (self.x, self.y+100), 60) #wing 1 // top wing
        pygame.draw.circle(screen, (250, 0, 130), (self.x+100, self.y+170), 60) #bottom of wing 1
        pygame.draw.circle(screen, (250, 0, 250), (self.x+100, self.y+100), 60) #wing 1
        pygame.draw.circle(screen, (250, 50, 100), (self.x+50, self.y+130), 60) #body
        pygame.draw.arc(screen, (0, 255, 0), (self.x+5, self.y+55, 90, 100), 7*3.14/6, 11*3.14/6, 8)
        pygame.draw.arc(screen, (0, 255, 0), (self.x+5, self.y+35, 90, 100), 7*3.14/6, 11*3.14/6, 8)
        pygame.draw.arc(screen, (0, 255, 0), (self.x+5, self.y+75, 90, 100), 7*3.14/6, 11*3.14/6, 8)
        pygame.draw.arc(screen, (50, 100, 100), (self.x+5, self.y+20, 90, 100), 3.14/2, 7*3.14/6, 8)
        pygame.draw.arc(screen, (50, 100, 100), (self.x+75, self.y+20, 90, 100), 3.14/2, 7*3.14/6, 8)
        
        

        
#instantiate
r1 =butterfly(200, 300)
r2 =butterfly(400, 400)
r3 =butterfly(600,500)
# GAME LOOP-----------------------------------------------------------
while GameLoop:
    
    r1.draw()
    r2.draw()
    r3.draw()
    
    
    
    pygame.display.flip()
pygame.quit()
