import pygame, sys
from pygame.locals import *
from tkinter import * 
from math import *
from time import sleep


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

offset = 60

length = 3*(window_height-2*offset)/(4*sin(pi/3))

center = (window_width/2, offset)
left = (window_width/2-length*cos(pi/3),offset + length*sin(pi/3))
right = (window_width/2+length*cos(pi/3),offset + length*sin(pi/3))

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
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
    midLeft = ((2*temp_prev[0] + temp_next[0])/3 , (2*temp_prev[1] + temp_next[1])/3)
    midRight = ((temp_prev[0] + 2*temp_next[0])/3 , (temp_prev[1] + 2*temp_next[1])/3)
    points.insert(i+1, midLeft)
    distance = dist(temp_prev,midLeft)
    angle = atan2((midRight[1]-midLeft[1]),(midRight[0]-midLeft[0]))
    midMid = (midLeft[0] + distance*cos(angle + pi/3), midLeft[1] + distance*sin(angle + pi/3))
    points.insert(i+2,midMid)
    points.insert(i+3, midRight)

def resetPoints():
    points.clear()
    points.append(center)
    points.append(left)
    points.append(right)

#Main Loop
while True: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    num = 0
    resetPoints()
    while num < 6:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        drawArena()
        pygame.draw.polygon(display_surf, WHITE, points, 1)
        num = nextIteration(num)
        pygame.display.flip()
        sleep(0.4)
    sleep(1)
  
    

if __name__=='__main__':
    main()
