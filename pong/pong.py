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
levels = [x / 10 for x in range(2, 8)]
ln= 0
level = levels[ln]
r = (rn.random() * level) + (level)
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
pos = rn.randint(0, 140)
def msg(t, x, y):
    text = font.render(t, True, (255,255,255), (0,0,0))
    textr = text.get_rect()
    textr.center = (x,y)
    scr.blit(text, textr)
def scl(num, in_min, in_max, out_min, out_max):
    return (num - in_min) * (out_max - out_min) / (in_max - in_min) + out_min
def message(text, px, py):
    # get the height of the font
    fontHeight = font.size("Tg")[1]
    for l in text.split('\n'):
        tr = font.render(l, 1, (255,255,255), (0,0,0)).get_rect()
        tr.center = (px, py)
        scr.blit(font.render(l, 1, (255,255,255), (0,0,0)), tr)
        py += fontHeight


    
def pause(key=K_ESCAPE):
    paused = True
    while paused:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN:
                if event.key == key:
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
    a = 180 - scl(abs(y - pdy), 0, 140, 120, 240) + 360
    # print(a)

def ai():
    global cy, y, ya, pos
    # cy = y
    sp = (abs(y - cy) - pos) / 75
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
        global pos
        x = 25
        pos = rn.randint(-20, 160)
        print(pos)
        collision(py)
        sp = rn.random() * 10 + 7
        #xa = Math.abs(xa)
        # console.log(sp)
        #a = rn.randint(90, 270)
    
    if (cp.colliderect(b)): #Ball has collided with computer's paddle
        #xa = Math.abs(xa) * -1
        # a = scl(abs(y - cy), 0, 140, 90, 270)
        a = rn.randint(120, 240) 
        #print(a)
        print('Actual: ' + str(y - cy))
        x = 464

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
#ps = 494 
scr.fill(0)
message('''Instructions:\nUse Up/W to move up\nUse Down/S to move down\nH to show this message\nESC to pause\n\nSPACE to start''', 250, 100)
pygame.display.flip()
pause(K_SPACE)
while True:    
    if ps > 10:
        scr.fill(0)
        d = 3
        ln += 1
        message('Level ' + str(ln + 1), 250, 300)
        message('Press Space to start', 250, 330)
        pygame.display.flip()
        pause(K_SPACE)
        level = levels[ln % 6]
        ps = 0; cs = 0
    if ln >= 6:
        scr.fill(0)
        message('YOU WIN!\nPress Space to play again', 250, 300)
        pygame.display.flip()
        pause(K_SPACE)
        ln = 0
        ps, cs = 0, 0
        continue
        

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
            
            elif event.key == K_h:
                scr.fill(0)
                message('''Instructions:\nUse Up/W to move up\nUse Down/S to move down\nH to show this message\nESC to pause\n\nSPACE to resume''', 250, 100)
                pygame.display.flip()
                pause(K_SPACE)
    
            else:
                pu = False; pd = False
            if event.key == K_ESCAPE:
                pause()
        elif event.type == MOUSEMOTION:
            py = pygame.mouse.get_pos()[1] - 70

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
    x += xa
    y += ya
    message('Player score: ' + str(ps) + '    ' + 'Computer score: ' + str(cs), 250, 550)
    clock.tick(2000)
    pygame.display.flip()
    if d > 0:
        print('\n\n')
        pos = rn.randint(-20, 160)
        sleep(d)
        intel = m.floor(rn.random() * 100)
        r = (rn.random() * level * 2) + (level * 2)        
        a = (rn.random()) + 45 + (90 * m.floor(rn.random() * 4))
        xa = ptc(r,a)[0]
        ya = ptc(r,a)[1]
        pygame.display.flip()
    d = 0

