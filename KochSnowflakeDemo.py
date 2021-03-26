import pygame, sys
from pygame.locals import *
from tkinter import * 
from math import *
from time import sleep
from numpy.core.defchararray import lower

BLACK = (0,0,0)
WHITE = (255,255,255)

root = Tk()
root.withdraw()
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
    display_surf.fill(BLACK)

#Set of all points on the snowflake.
points = []

offset = 60

#Calculates the length of the snowflake based on the window height.
length = 3*(window_height-2*offset)/(4*sin(pi/3))

#Starting 3 corners of the triangle at the beginning.
center = (window_width/2, offset)
left = (window_width/2-length*cos(pi/3),offset + length*sin(pi/3))
right = (window_width/2+length*cos(pi/3),offset + length*sin(pi/3))


# Remembers the start and end points of the side before the next iteration generates the new points.
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

#Calculates and adds the new points of the snowflake to the set of points on the snowflake
def findNextPoints(temp_prev, temp_next, i):
    isQuit()
    midLeft = ((2*temp_prev[0] + temp_next[0])/3 , (2*temp_prev[1] + temp_next[1])/3)
    midRight = ((temp_prev[0] + 2*temp_next[0])/3 , (temp_prev[1] + 2*temp_next[1])/3)
    points.insert(i+1, midLeft)
    distance = dist(temp_prev,midLeft)
    angle = atan2((midRight[1]-midLeft[1]),(midRight[0]-midLeft[0]))
    midMid = (midLeft[0] + distance*cos(angle + pi/3), midLeft[1] + distance*sin(angle + pi/3))
    points.insert(i+2,midMid)
    points.insert(i+3, midRight)

#Resets the points on the snowflake back to the original 3.
def resetPoints():
    points.clear()
    points.append(center)
    points.append(left)
    points.append(right)

#Checks if the program is closed out of.
def isQuit():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

#Prompts the user if they want to see each segment of the snowflake be drawn or just each iteration be drawn.
print("\n")
st = input("slow draw? (Y/N): ")
slowDraw = (lower(st) =="y")

#Main Loop
while True: 
    isQuit()
    num = 0
    resetPoints()
    while num < 6:            
        isQuit()
        display_surf.fill(BLACK)
        if slowDraw: 
            for i in range(len(points)):
                isQuit()
                if i == len(points)-1:
                    next = points[0]
                else:
                    next = points[i+1]
                pygame.draw.line(display_surf, WHITE, points[i], next, width=1)  
                pygame.display.flip()
                sleep(0.01)
        else:
            pygame.draw.polygon(display_surf, WHITE, points, 1)
        
        num = nextIteration(num)
        pygame.display.flip()
        sleep(1)
    sleep(2)
  
    

if __name__=='__main__':
    main()
