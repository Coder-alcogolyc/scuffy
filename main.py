import pygame
pygame.init()
q1 = pygame.image.load('IMG_4959.png')
q2 = pygame.image.load('IMG_5135.png')
q3 = pygame.image.load('IMG_4961.png')
q4 = pygame.image.load('IMG_4956.png')
q5 = pygame.image.load('IMG_4951.png')
q6 = pygame.image.load('IMG_4958.png')
tr = pygame.image.load("tr.png")
ro = pygame.image.load("ro.png")
ass = pygame.image.load("ass.png")
win = pygame.display.set_mode()
pygame.display.set_caption("Zephyr")
a = 0
ii = ""
left = False
right = False
clock = pygame.time.Clock()
disinf = pygame.display.Info()
x = disinf.current_w/2
y = disinf.current_h/2
xspeed = 5.2
yspeed = 2.85
us = disinf.current_h//3
e = x - disinf.current_h//6
n = y - disinf.current_h//6
ss = disinf.current_h//4
q1 = pygame.transform.scale(q1, (us, us))
q2 = pygame.transform.scale(q2, (us, us))
q3 = pygame.transform.scale(q3, (us, us))
q4 = pygame.transform.scale(q4, (us, us))
q5 = pygame.transform.scale(q5, (us, us))
q6 = pygame.transform.scale(q6, (us, us))
walkr = [q1, q2, q3, q2]
walkl = [q4, q5, q6, q5]
tr = pygame.transform.scale(tr, (ss, ss))
ass = pygame.transform.scale(ass, (ss, ss))
animCount = 0
bg = pygame.image.load('bg.png')
lvl1_1 = [ass, ass, ass, tr, tr, tr, tr, ass, ass, tr]
lvl1_2 = [tr, tr, tr, tr, tr, tr]
lvl1_3 = [tr, tr, tr, tr, tr, tr]
xx = x
def drawWindow():
    global animCount
    global a
    global x
    global s
    global xx
    global ii
    win.blit(bg, (0, 0))
    for i in lvl1_1:
        if i == ii:
            xx = xx + ss*(lvl1_1.index(i)+1)
        else:
            xx = xx + ss * (lvl1_1.index(i)+1)
        ii = i
        win.blit(i, (xx, y, ss, ss))
    xx = x
    if animCount + 1 >= 30:
        animCount = 0

    if right:
        win.blit(walkr[animCount // 8], (e, n))
        animCount += 1
        a = 1
    elif left:
        win.blit(walkl[animCount // 8], (e, n))
        animCount += 1
        a = 0

    elif right == False and left == False and a == 1:
        win.blit(q2, (e, n))
    elif right == False and left == False and a == 0:
        win.blit(q5, (e, n))

    pygame.display.update()

run = True
while run:
   ## x -= 1.40624757575*xx
    clock.tick(32)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_e]:
        x -= xspeed
        y += yspeed
        left = False
        right = True
    elif keys[pygame.K_d]:
        x -= xspeed
        y -= yspeed
        left = False
        right = True
    elif keys[pygame.K_q]:
        x += xspeed
        y += yspeed
        left = True
        right = False
    elif keys[pygame.K_a]:
        x += xspeed
        y -= yspeed
        left = True
        right = False
    else:
        left = False
        right = False
    if keys[pygame.K_BACKSPACE]:
        pygame.quit()

    drawWindow()



pygame.quit()