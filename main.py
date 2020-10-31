from itertools import combinations as cb
from itertools import permutations as pm
from math import factorial as f

from time import sleep
import pygame

pygame.init()

#the points
points=[1,2,3,4,5,6,7,8,9]

#this contains all possible pattern codes
ans=set()

#try all possible diffrent combinations
def get_combinations(number):
    combination=list(cb(points,number))
    for c in combination:
        permute(c)

#try all possible permutation
def permute(lis):
    permutation=list(pm(lis))
    for p in permutation:
        #condition
        if movable(p):
            ans.add(p)

#these are the points that can be traversed through
straight_elements={2:[(1,3),(3,1)],4:[(1,7),(7,1)],5:[(1,9),(9,1),(7,3),(3,7),(2,8),(8,2),(4,6),(6,4)],
6:[(3,9),(9,3)],8:[(7,9),(9,7)]}

straight_dict=dict()
for key,value in straight_elements.items():
    for val in value:
        straight_dict[val]=key

#direct traversible points
movable_dict={1:[2,5,8,4],2:[1,4,2,3,6,9,5],3:[6,2,5,8],
              4:[1,7,2,5,8],5:[1,2,3,4,6,7,8,9],6:[3,9,2,5,8],
              7:[4,2,5,8],8:[7,9,1,4,3,6,5],9:[6,2,5,8]}

#we can move only if we satify the below conditions
def movable(p):
    #to keep track of traversed nodes
    seen=set([p[0]])
    for i in range(1,len(p)):
        #if it is already visited then it will be invalid
        if p[i] in seen:
            break
        #if we can move directly
        if p[i] in movable_dict[p[i-1]]:
            seen.add(p[i])
            continue
        #if point passes through the point which is not visited yet
        #then this will be invalid
        if (p[i],p[i-1])in straight_dict and straight_dict[(p[i],p[i-1])] not in seen:
            break

        if (p[i-1],p[i])in straight_dict and straight_dict[(p[i-1],p[i])] not in seen:
            break

        #this will be valid point and add to seen set
        seen.add(p[i])

    #this returns False if it is broken from the above loop else return True
    else:
        return True
    return False

#try all different length patterns
for length in range(4,10):
    get_combinations(length)

#widht and hight of the window
WIDTH=600
HIGHT=600

#point positions
point_position={1:[150-50,150-50],2:[350-50,150-50],3:[550-50,150-50],
                4:[150-50,350-50],5:[350-50,350-50],6:[550-50,350-50],
                7:[150-50,550-50],8:[350-50,550-50],9:[550-50,550-50]}
#basic window
white=(255,255,255)
win=pygame.display.set_mode((WIDTH,HIGHT))
pygame.display.set_caption('PATTERNS')

#this is the basic window where we need to draw pattern
def start_win():
    win.fill((0,0,0)) #black color
    for i in range(1,10):
        pygame.draw.circle(win,white,point_position[i],10)

    pygame.display.update()

#waiting for user approval
start=False
while not start:

    for event in pygame.event.get():
        if event.type==pygame.KEYDOWN:
            start=True
        if event.type==pygame.KEYUP:
            start=True
        if event.type==pygame.QUIT:
            pygame.quit()
            quit()

    start_win()

#font for display the count and code
f=pygame.font.SysFont('comicsansms',50)

#draw the pattern that is stored in ans set
def draw_pattern(mode=1):
    #if automate mode
    if mode==1:
        count=1
        for pattern in ans:
            text=f.render(str(count),True,white)
            win.blit(text,[25,25])
            text=f.render(str(pattern),True,white)
            win.blit(text,[200,560])
            for point in range(1,len(pattern)):
                pygame.draw.line(win,white,point_position[pattern[point-1]],point_position[pattern[point]],5)
            pygame.display.update()
            sleep(0.05)
            start_win()
            pygame.display.update()
            count+=1
    else:
        count=1
        for pattern in ans:
            text=f.render(str(count),True,white)
            win.blit(text,[25,25])
            text=f.render(str(pattern),True,white)
            win.blit(text,[200,560])
            for point in range(1,len(pattern)):
                pygame.draw.line(win,white,point_position[pattern[point-1]],point_position[pattern[point]],5)
            pygame.display.update()
            pressed=False
            while not pressed:
                for event in pygame.event.get():
                    if event.type==pygame.KEYDOWN:
                        pressed=True

            start_win()
            pygame.display.update()
            count+=1

#ask the user for automate or manual
text=f.render('Number of valid patterns: '+str(len(ans)),True,white)
win.blit(text,[25,25])

pygame.display.update()

choice=input("enter your choice\n1]Automate all combinations\n2]Manual transition\n")
#if he enters invalid input then that will be automated
try:
    draw_pattern(int(choice))
except:
    draw_pattern()
