import pygame,csv
from math import sqrt

pygame.init()
screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption("Golfer")
pygame.display.set_icon((pygame.image.load("icon.png")))
hole = 25
xspeed = 0
yspeed = 0
x = 500
y = 500
ballspeed= 60
import random
holex,holey=100,100
score=0

def reset_level():
    global score,x,y,holex,holey
    x = 500
    y = 500
    holex = random.randint(25, 575)
    holey = random.randint(25,575)
    score +=1
    return x, y, holex, holey, score


def load_high_score():
    try:
        with open('score.csv', 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                return int(row[0])
    except FileNotFoundError:
        return 0

def save_high_score(high_score):
    scores = []
    try:
        with open('score.csv', 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                scores.append(int(row[0]))
    except FileNotFoundError:
        pass

    scores.append(high_score)

    with open('score.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([str(max(scores))])

high_score = load_high_score()
def game():
    global holey,holex,x,y,score,highscore,xspeed,ballspeed,yspeed,hole,screen,pygame
    screen.fill((114, 182, 113))
    screen.blit((pygame.font.SysFont("Arial", 20).render(f"Score: {score}",True,(255,255,255))),(0,20))
    screen.blit((pygame.font.SysFont("Arial", 20).render(f"Highscore: {high_score}",True,(255,255,255))),(0,0))
    menu.stop()



    pos = pygame.mouse.get_pos() #MOUSE POSITION

    pygame.draw.circle(screen, (255, 255, 255), (holex,holey), hole)#hole  border
    pygame.draw.circle(screen, (0, 0, 0), (holex,holey), hole - 1)#hole

    pygame.draw.circle(screen, (255, 255, 255), (x,y), 15) #ball

    if xspeed < 0.00001 and yspeed < 0.001: #checks if ball stopped
        pygame.draw.line(screen, (192,192,192), (x, y), pos)  #golf club

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False
            pygame.quit()
        if event.type == pygame.MOUSEBUTTONUP:
            xspeed = int((pos[0] + x) / ballspeed)
            yspeed = int((pos[1] + y) /ballspeed)
    # Collisions ofr the border 
    if x > 599 or x < 1:
        xspeed *= -1
    if y > 599 or y < 1:
        yspeed *= -1


    x += xspeed
    y += yspeed

    
    # CONSTANTLY slows the ball
    xspeed = xspeed * 0.99
    yspeed = yspeed * 0.99


    if (sqrt((holex - x) ** 2 + (holey - y) ** 2)) < 25+15:
        xspeed *= 0.000000000000000000000000000000000000000000001
        yspeed *= 0.00000000000000000000000000000000000000000000001 
        text = pygame.font.SysFont("Arial", 20).render("Congrats you scored",True,(255,255,255))
        screen.blit(text,(300,300))
        reset_level()
        pygame.display.update()
    

run=True
start=False
tutorial=False
bg=pygame.transform.scale(pygame.image.load("bg.png"),(600,600))
menu=pygame.mixer.Sound("menu.wav")
run = True
while run:
    screen.blit(bg, (0, 0))
    screen.blit((pygame.font.SysFont("Arial", 20).render(f"Score: {score}",True,(255,255,255))),(0,20))
    screen.blit((pygame.font.SysFont("Arial", 20).render(f"Highscore: {high_score}",True,(255,255,255))),(0,0))
    menu.play()

    for event in pygame.event.get():
        if event.type == pygame.QUIT: run = False

        if event.type == pygame.KEYDOWN:
            if event.key==pygame.K_LSHIFT: tutorial=True
            if event.key==pygame.K_RETURN: tutorial=False
            if event.key == pygame.K_SPACE: start = True



    if tutorial: screen.blit(pygame.transform.scale(pygame.image.load("tutorial.png"),(400+200,400+200)), (0, 0))
    if start:
        game()
        MUSIC=pygame.mixer.Sound("game.wav")
        MUSIC.play()
    pygame.display.update()

