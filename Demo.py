import pygame, sys
from pygame.locals import *
from tkinter import * 
from math import *
from pygame.event import wait



BLACK = (0,0,0)
WHITE = (255,255,255)

root = Tk()
window_width = root.winfo_screenwidth()-100
window_height = root.winfo_screenheight()-100
point_thickness = 3
display_surf = pygame.display.set_mode((window_width,window_height))

#Main Function
def main():
    pygame.init()
    global display_surf
    display_surf = pygame.display.set_mode((window_width,window_height))
    pygame.display.set_caption('Koch Snowflake')

#Draws the black window. 
def drawArena():
    display_surf.fill((0,0,0))
    #Draw outline of arena
    pygame.draw.rect(display_surf, BLACK, ((0,0),(window_width,window_height)))

points = []

length = 500

center = (window_width/2, window_height/8)
left = (window_width/2-length*cos(pi/3),window_height/8 + length*sin(pi/3))
right = (window_width/2+length*cos(pi/3),window_height/8 + length*sin(pi/3))

points.append(center)
points.append(left)
points.append(right)

def nextIteration(num):
    i = 0
    size = len(points)
    while i< len(points):
        temp_prev = points[i]
        if (i == len(points)-1):
            temp_next = points[0]
        else:
            temp_next = points[i+1]
        findNextPoints(temp_prev,temp_next,i)
        i += 4
    return num +1


def findNextPoints(temp_prev, temp_next, i):
    midLeft = ((2*temp_prev[0] + temp_next[0])/3 , (2*temp_prev[1] + temp_next[1])/3)
    midRight = ((temp_prev[0] + 2*temp_next[0])/3 , (temp_prev[1] + 2*temp_next[1])/3)
    points.insert(i+1, midLeft)
    distance = dist(temp_prev,midLeft)
    angle = atan2((midRight[1]-midLeft[1]),(midRight[0]-midLeft[0]))
    midMid = (midLeft[0] + distance*cos(angle + pi/3), midLeft[1] + distance*sin(angle + pi/3))
    points.insert(i+2,midMid)
    points.insert(i+3, midRight)


#Main Loop
while True: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    num = 0
    while num < 4:
        drawArena()
        num = nextIteration(num)
        pygame.draw.polygon(display_surf, WHITE, points, 1)
        pygame.display.flip()
        wait(1000)
    points.clear()
    points.append(center)
    points.append(left)
    points.append(right)
    

if __name__=='__main__':
    main()
