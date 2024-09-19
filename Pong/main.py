import sys, pygame
import random
from screeninfo import get_monitors


pygame.init()
clock = pygame.time.Clock()

bg1 = pygame.image.load('Pong/BG1.png')
bg2 = pygame.image.load('Pong/Bg2.png')
bg3 = pygame.image.load('Pong/BG3.jpg')
bg4 = pygame.image.load('Pong/BG4.png')
bg5 = pygame.image.load('Pong/BG5.jpg')
bg6 = pygame.image.load('Pong/BG6.png')

print("PICK a background: 1 - 6:")

i = 0
BG = None
while i < 1 or i > 6:
    i = int(input("Enter a number between 1 and 6: "))
    if i == 1:
        BG = bg1
    elif i == 2:
        BG = bg2
    elif i == 3:
        BG = bg3
    elif i == 4:
        BG = bg4
    elif i == 5:
        BG = bg5
    elif i == 6:
        BG = bg6
    else:
        print("Invalid input. Please enter a number between 1 and 6.")
        

w = get_monitors()[0].width - 20
h = get_monitors()[0].height - 70

b1 = pygame.mixer.Sound('Pong/error.wav')
b2 = pygame.mixer.Sound('Pong/ka-ching.wav')
b3 = pygame.mixer.Sound('Pong/quack_5.wav')

l1 = pygame.image.load('Pong/cat (1).jpg')
l2 = pygame.image.load('Pong/mutahar_laugh (1).jpg')
l3 = pygame.image.load('Pong/laugh (1).jpg')
l4 = pygame.image.load('Pong/laugh2 (1).jpg')

L1 = pygame.mixer.Sound('Pong/cat.wav')
L2 = pygame.mixer.Sound('Pong/odnr.wav')
L3 = pygame.mixer.Sound('Pong/goofy.wav')
L4 = pygame.mixer.Sound('Pong/cat.wav')

print(w, h)

screen = pygame.display.set_mode((w, h))
pygame.display.set_caption('Ponggggggg')

ball = pygame.Rect(w/2 - 15, h/2 - 15, 30, 30)
player = pygame.Rect(w - 30, h/2 - 70, 10, 140)
opp = pygame.Rect(30,  h/2 - 70, 10, 140)

x_speed = 5
y_speed = 5
player_speed = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                player_speed += 10
            if event.key == pygame.K_UP:
                player_speed -= 10
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                player_speed -= 10
            if event.key == pygame.K_UP:
                player_speed += 10
                
        
    ball.x += x_speed
    ball.y += y_speed
    
    if ball.top <= 0 or ball.bottom >= h:
        y_speed *= -1
    if ball.left <= 0 or ball.right >= w:
        if ball.right >= w:
            idx = random.choice((1,2,3,4))
            if idx == 1:
                screen.blit(l1, (0, 0))
                pygame.display.flip()
                pygame.mixer.Sound.play(L1)
            if idx == 2:
                screen.blit(l2, (0, 0))
                pygame.display.flip()
                pygame.mixer.Sound.play(L2)
            if idx == 3:
                screen.blit(l3, (0, 0))
                pygame.display.flip()
                pygame.mixer.Sound.play(L3)
            if idx == 4:
                screen.blit(l4, (0, 0))
                pygame.display.flip()
                pygame.mixer.Sound.play(L4)
            pygame.time.wait(3000)
            
        ball.center = (w/2, h/2)
        x_speed *= random.choice((1,-1))
        y_speed *= random.choice((1,-1))
        
        
    if ball.colliderect(player) or ball.colliderect(opp):
        idx = random.choice((1,2,3))
        if idx == 1:
            pygame.mixer.Sound.play(b1)
        if idx == 2:
            pygame.mixer.Sound.play(b2)
        if idx == 3:
            pygame.mixer.Sound.play(b3)
        x_speed *= -1
        if ball.centery < player.centery:
            y_speed = -abs(y_speed)
        else:
            y_speed = abs(y_speed)
    
    player.y += player_speed
    if player.top <= 5:
        player.top = 5
    if player.bottom >= h-5:
        player.bottom = h-5
        
    if opp.top < ball.y:
        opp.top += 40
    if opp.bottom > ball.y:
        opp.bottom -= 40
    if opp.top <= 10:
        opp.top = 10
    if opp.bottom >= h - 10:
        opp.bottom = h - 10

    screen.blit(BG, (0,0))
    pygame.draw.ellipse(screen, (0, 0, 255), ball)
    pygame.draw.rect(screen, (0, 255, 0), player)
    pygame.draw.rect(screen, (255, 0, 0), opp)
    pygame.display.flip()
    clock.tick(120)