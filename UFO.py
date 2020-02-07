import pygame
import random
import math
import os
from pygame import mixer
#Initializing Game
pygame.init()

#Game Window
screen = pygame.display.set_mode((800,600))

#Adding BackGround Image
background = pygame.image.load(os.getcwd() + "/background.png")
mixer.music.load("C:/Users/Jaswanth/Desktop/Curriculum/MINI PROJECT/SpaceShooter_Theme.wav")
mixer.music.play(-1)

#setting game icon and caption
pygame.display.set_caption("THE UFO")
icon = pygame.image.load(os.getcwd() + "/spaceship.png")
pygame.display.set_icon(icon)

#score variable for counting score
score = 0

#Diemnsions of player Spaceship
playerImg = pygame.image.load(os.getcwd() + "/space-invaders.png")
playerX = 370
playerY = 480
playerX_change = 0

#Dimensions od enemy
enemyImg = []
enemyX = []
enemyY = []
enemyX_change= []
enemyY_change = []
enemies = 6
for i in range(enemies):
    enemyImg.append(pygame.image.load(os.getcwd() + "/space-ship (1).png"))
    enemyX.append(random.randint(0,736))
    enemyY.append(random.randint(50,150))
    enemyX_change.append(3.5)
    enemyY_change.append(40)


bulletImg = pygame.image.load(os.getcwd() + '/bullet.png')
bulletX = 0
bulletY = playerY
bulletX_change = 0
bulletY_change = 10
bullet_state = "ready"

score = 0
font = pygame.font.Font("freesansbold.ttf",32)
textX = 10
textY = 10

over_font = pygame.font.Font("freesansbold.ttf",128)

def show_score(x,y):
    score_value = font.render("Score : " + str(score),True,(255,255,255))
    screen.blit(score_value,(x,y))
    
def game_over():
    over_text = font.render("GAME OVER",True,(255,255,255))
    screen.blit(over_text,(250, 250))

def isCollision(enemyX , enemyY , bulletX , bulletY):
    distance = math.sqrt((enemyX - bulletX)**2 + (enemyY - bulletY)**2)
    if distance <= 35:
        return True
    else:
        return False

def player(x,y):
    screen.blit(playerImg , (x,y))
    
def enemy(x,y,i):
    screen.blit(enemyImg[i] , (x,y))
    
def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, (x + 16, y + 10))
    
    
running = True
while running:
    
    screen.fill((0,0,0))
    screen.blit(background,(0,0))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            quit()
            
        if event.type == pygame.KEYDOWN:  
            if event.key == pygame.K_LEFT:
                playerX_change = -5
            if event.key == pygame.K_RIGHT:
                playerX_change = 5
            if event.key == pygame.K_SPACE:
                if bullet_state is "ready":
                    bullet_state = "fire"
                    bullet_music = mixer.Sound("C:/Users/Jaswanth/Desktop/Curriculum/MINI PROJECT/laser1.wav")
                    bullet_music.play()
                    bulletX = playerX
                    fire_bullet(bulletX,bulletY)
                
        if event.type == pygame.KEYUP:
            if event.key  == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0
        
    playerX += playerX_change
    
    if playerX <= 0:
        playerX=0
    elif playerX >= 736:
        playerX = 736
        
    for i in range(enemies):

        if enemyY[i] > 430:
                for j in range(enemies):
                    enemyY[j] = 2000
                game_over()
                break
        
        enemyX[i] += enemyX_change[i]
        if enemyX[i] <= 0:
            enemyX_change[i] = 4
            enemyY[i] += enemyY_change[i]
        elif enemyX[i] >= 736:
            enemyX_change[i] = -4
            enemyY[i] += enemyY_change[i]
            
        collision = isCollision(enemyX[i], enemyY[i], bulletX, bulletY)
        if collision:
            collision_music = mixer.Sound("C:/Users/Jaswanth/Desktop/Curriculum/MINI PROJECT/small_explosion.wav")
            collision_music.play()
            bulletY = playerY
            bullet_state = "ready"
            score +=1
            enemyX[i] = random.randint(0,736)
            enemyY[i] = random.randint(50,150)
        enemy(enemyX[i] ,enemyY[i] ,i)
     
    if bulletY <= 0:
        bulletY = playerY
        bullet_state = "ready"
        
    if bullet_state is "fire":
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change
    
    player(playerX,playerY)
    show_score(textX,textY)
    pygame.display.update()