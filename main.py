import pygame
import random
import math

pygame.init()

#VARIABLES
SCREEN_WIDTH=800
SCREEN_HEIGHT=600
WIN=pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))

pygame.display.set_caption('Space Shooter Game')

FONT=pygame.font.SysFont('Arial',32,'bold')
FONT_GAMEOVER=pygame.font.SysFont('Arial',64,'bold')
def gameover():
    img2=FONT.render(f'GAME OVER',True,'white')
    WIN.blit(img2,(SCREEN_WIDTH/2 -100,SCREEN_HEIGHT/2))
    exit(1)

def score():
    img=FONT.render(f'Score:{SCORE}',True,'white')
    WIN.blit(img,(10,10))
icon=pygame.image.load('icon.png')
pygame.display.set_icon(icon)

BG=pygame.transform.scale(pygame.image.load('bg.png'),(SCREEN_WIDTH,SCREEN_HEIGHT))

PLAYER=pygame.image.load('spaceship.png')
PLAYER_X=(SCREEN_WIDTH/2 - 64)
PLAYER_Y= (SCREEN_HEIGHT-74)

DED=True

PC_X=0
BULLET=pygame.image.load('bullet.png')
BULLET_X=PLAYER_X+16
BULLET_Y=PLAYER_Y-16
BYS=5
CHECK=False

SCORE=0

ALIENIMG=[]
ALIENX=[]
ALIENY=[]
ACX=[]
ABY=[]
ALIENBULLETIMG=[]
ALIENBULLETX=[]
ALIENBULLETY=[]

no_of_aliens=3
alive_aliens_count = no_of_aliens


ADED=[True]*no_of_aliens

for i in range (no_of_aliens):
    ALIENIMG.append(pygame.image.load('alien.png'))
    ALIENX.append(random.randint(0,SCREEN_WIDTH-74))
    ALIENY.append(random.randint(0,SCREEN_HEIGHT/2 -64))
    ALIENBULLETX.append(ALIENX[i]+16)
    ALIENBULLETY.append(ALIENY[i]+16)
    ALIENBULLETIMG.append(pygame.image.load('alienbullet.png'))
    ABY.append(1)
    ACX.append(1)

ACHECK=False


run=True
while run:
    WIN.blit(BG,(0,0))
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False
        if event.type==pygame.KEYDOWN:
            
            if event.key==pygame.K_LEFT :
                PC_X= -3    
               
            elif event.key==pygame.K_RIGHT :
                PC_X= 3
            elif event.key ==pygame.K_SPACE: 
                BULLET_X = PLAYER_X + 16  
                BULLET_Y = PLAYER_Y - 16  
                BYS = 5
                for i in range(no_of_aliens):
                    ALIENBULLETX[i]=ALIENX[i]+16
                    CHECK=True
                    ACHECK=True
        elif event.type == pygame.KEYUP:  
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                PC_X = 0        
    PLAYER_X+=PC_X
    if PLAYER_X<=0:
        PLAYER_X=0
    elif PLAYER_X>= SCREEN_WIDTH-64:
        PLAYER_X=SCREEN_WIDTH-64

    if DED:
        WIN.blit(PLAYER,(PLAYER_X ,PLAYER_Y))
    
    if BULLET_Y<=0:
        BULLET_Y=PLAYER_Y-16
        BULLET_X=PLAYER_X+16
        CHECK=False
        
    if CHECK:
        WIN.blit(BULLET,(BULLET_X,BULLET_Y))
        BULLET_Y-=BYS
        
    for i in range(no_of_aliens):
        if ADED[i]:
            WIN.blit(ALIENIMG[i],(ALIENX[i],ALIENY[i]))

        ALIENX[i]+=ACX[i]
        if ALIENX[i] >= SCREEN_WIDTH-64:
            ACX[i]=-2.5
        elif ALIENX[i]<=0:
            ACX[i]=2.5

        DIST1=math.sqrt(math.pow((BULLET_X-ALIENX[i]),2)+math.pow((BULLET_Y-ALIENY[i]),2))
        if DIST1<27:
            BULLET_Y=PLAYER_Y-16
            BULLET_X=PLAYER_X+16
            CHECK=False
            ADED[i]=False
            SCORE+=1
            alive_aliens_count -= 1
            break
        
        DIST2=math.sqrt(math.pow((ALIENBULLETX[i]-PLAYER_X),2)+math.pow((ALIENBULLETY[i]-PLAYER_Y),2))
        if DIST2<27:
            DED=False
            gameover()
            ADED[i]=False
            ALIENBULLETX[i] = -100  
            ALIENBULLETY[i] = -100
            break
        
        if ALIENBULLETY[i]>=SCREEN_HEIGHT:
            ALIENBULLETX[i]=ALIENX[i]+16
            ALIENBULLETY[i]=ALIENY[i]+16

        if ACHECK and ADED[i]:
            for i in range(no_of_aliens):
                WIN.blit(ALIENBULLETIMG[i],(ALIENBULLETX[i],ALIENBULLETY[i]))
                ALIENBULLETY[i] += ABY[i]
            
    score()
    if alive_aliens_count == 0:
        win_text = FONT.render("You Won", True, (255, 255, 255))
        WIN.blit(win_text, (SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2))
        pygame.display.update()
        break
    
    pygame.display.update()