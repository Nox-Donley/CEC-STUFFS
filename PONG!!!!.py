import pygame
pygame.init()
from pygame import mixer

screen = pygame.display.set_mode ((700,500))
pygame.display.set_caption("pong")

doExit = False

clock = pygame.time.Clock()
#player postitions
p1x = 20
p1y = 200
p2x = 660
p2y = 200
#ball variables
bx = 350
by = 250
bVx = 5
bVy = 5

p1Score = 0
p2Score = 0

mixer.init()
mixer.music.load("Shrek.mp3")
mixer.music.set_volume(1)
mixer.music.play()
print("music is playibg")

    
while not doExit:
    
    clock.tick(60)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            doExit = True
        #game logic here --------------------------------------------------------------------------
    #controls
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        p1y-=5
    if keys[pygame.K_UP]:
        p2y-=5
    if keys[pygame.K_s]:
        p1y+=5
    if keys[pygame.K_DOWN]:
        p2y+=5
    #ball movement
    bx += bVx
    by += bVy
    #ball wall bounce
    if bx < 0 or bx + 20 > 700:
        bVx *= -1
    if by < 0 or by +20 > 500:
        bVy *= -1
    #ball paddle reflection
        #FIX THE DISPLACEMENT BUG
    if bx < p1x + 20 and by + 20 > p1y and by < p1y + 100:
        bVx *= -1
        print("ping left")
    if bx + 20 > p2x  and by + 20 > p2y and by < p2y + 100:
        bVx *= -1
        print("ping right")
        
    if bx < 1:
        bVx *= -1
        p2Score += 1
    elif bx >= 680:
        bVx *= -1
        p1Score += 1
    
        #render section here -----------------------------------------------------------------------
    screen.fill ((212,162,248))
            
    pygame.draw.line(screen, (255, 255, 255), [349, 0], [349, 500], 5)
            
    pygame.draw.rect(screen, (255, 255, 255), (p1x, p1y, 20, 100), 1)
    pygame.draw.rect(screen, (255, 255, 255), (p2x, p2y, 20, 100), 1)
    pygame.draw.rect(screen, (255, 255, 255), (bx, by, 20, 20), 1)
    
    #display scores
    font = pygame.font.Font(None, 74)
    text = font.render(str(p1Score), 1, (255, 255, 255))
    screen.blit(text, (250,10))
    text = font.render(str(p2Score), 1, (255, 255, 255))
    screen.blit(text, (420,10))
            
    pygame.display.flip()