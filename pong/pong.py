import random as rn, math as m, sys
from time import sleep
#Ping Pong Python
#Uncomment code with "np" to enable 2 player mode.
import pygame
from pygame.locals import *
pygame.init()
py = 0
clock = pygame.time.Clock()
d = 0
ps = 0
cs = 0
x = 250
sp = rn.random() * 10 + 10
y = 250
xa = 0; ya = 0
z = 0
pu, pd, cu, cd, cy = 0,0,0,0,0
r = (rn.random() * 2) + 2
a = (rn.random()) * 22 + 22 + (90 * m.floor(rn.random() * 4))
intel = m.floor(rn.random() * 100)
t = 400

scr = pygame.display.set_mode([500, 600])
c = pygame.Color((255,255,255))
# np = confirm('Please select a mode (1 player or 2 player). Press OK for 1 player, and press Cancel for 2 players.')
p = pygame.draw.rect(scr, c, (5, py, 10, 140)) #Player's paddle
b = pygame.draw.ellipse(scr, c, (x, y, 20, 20)) #Ball
cp = pygame.draw.rect(scr, c, (485, cy, 10, 140)) #computer's paddle
font = pygame.font.SysFont(None, 30)
def message(t, x, y):
    text = font.render(t, True, (255,255,255), (0,0,0))
    textr = text.get_rect()
    textr.center = (x,y)
    scr.blit(text, textr)
def scl(num, in_min, in_max, out_min, out_max):
    return (num - in_min) * (out_max - out_min) / (in_max - in_min) + out_min

def pause():
    paused = True
    while paused:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    paused = False

def ptc(dist, theta):
    xc = m.cos(theta * (m.pi/180)) * dist
    yc = m.sin(theta * (m.pi/180)) * dist
    return [xc, yc]

xa = ptc(r,a)[0]
ya = ptc(r,a)[1]

def collision(pdy):
    global x, y, xa, ya, a, py, cy, r
    # y = py + 70 -> ya = 0
    #y = py -> ya = -1
    #y = py + 140 -> ya = 1
    #print(x, y, xa, ya, a, py, cy, r, pdy, y - pdy)     
    a = 180 - scl(abs(y - pdy), 0, 140, 90, 270) + 360
    print(a)

def ai():
    global cy, y, ya
    # cy = y
    sp = abs((y - cy) / 10) 
    if y < cy:
        if ya < 0:
            cy -= (sp + 0) 
        else:
            cy -= (sp + 0)
    elif y > cy:
        if ya > 0:
            cy += (sp + 0) 
        else:
            cy += sp


def physics():
    global x, y, xa, ya, p, b, cp, ps, a, cs, d, py, cy, sp
    if x > t: #&& np and intel > 15:
        ai()
        
    
    if p.colliderect(b): #Ball has collided with player's paddle
        x = 25
        collision(py)
        sp = rn.random() * 10 + 7
        #xa = Math.abs(xa)
        # console.log(sp)
    
    if (cp.colliderect(b)): #Ball has collided with computer's paddle
        #xa = Math.abs(xa) * -1
        a = scl(abs(y - cy), 0, 140, 90, 270) 
        print(a)
        x = 465

    elif x > 500:
        a *= -1; ps += 1; d = 2; x = 250; y = 250; cy = 0
    elif x < 0:
        a *= -1; cs += 1; d = 2; x = 250; y = 250; cy = 0
    elif y > 490:
        a *= -1; y = 490
    elif y < 10:
        a *= -1; y = 10
    xa = ptc(r,a)[0]
    ya = ptc(r,a)[1] * -1
    
while True:    
    #print(clock.get_fps())
    a = a % 360
    c = pygame.Color((255,255,255))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_DOWN or event.key == K_s:
                pd = True
                pu = False
    
            elif event.key == K_UP or event.key == K_w:
                pu = True
                pd = False
            
    
            else:
                pu = False; pd = False
            if event.key == K_ESCAPE:
                pause()
        elif event.type == MOUSEMOTION:
            py = pygame.mouse.get_pos()[1]

    # if (! np):
    #     if (event.key == UP_ARROW)):
    #         cu = true
    #         cd = false
    #     
    #     else if (event.key == DOWN_ARROW)):
    #         cd = true
    #         cu = false
    #     
    #     else :
    #         cd = false; cu = false
    #     
    #     if(cu):cy -= 10
    #     else if(cd):cy += 10
    # 

    if pu:
        py -= 10
    elif pd:
        py += 10

    physics()
    scr.fill(0)
    p = pygame.draw.rect(scr, c, (5, py, 10, 140)) #Player's paddle
    b = pygame.draw.ellipse(scr, c, (x, y, 20, 20)) #Ball
    cp = pygame.draw.rect(scr, c, (485, cy, 10, 140)) #computer's paddle
    if d > 0:
        sleep(d)
        intel = m.floor(rn.random() * 100)
        r = (rn.random() * 3) + 0.2
        a = (rn.random()) + 45 + (90 * m.floor(rn.random() * 4))
        xa = ptc(r,a)[0]
        ya = ptc(r,a)[1]
        pygame.display.flip()
    
    d = 0
    x += xa
    y += ya
    message('Player score: ' + str(ps) + '    ' + 'Computer score: ' + str(cs), 250, 550)
    pygame.display.flip()
    clock.tick(100)
