# Snake Game!

#games imports
import pygame
import sys
import random
import time

check_errors = pygame.init()
if check_errors[1] > 0:                                                          # (6,0) if the value of the index 1 is greater than 0 it will enter if be true to if statement 
    print("(!) Had {0} initialing errors, exiting...".format(chech_errors[1]))
    sys.exit(-1)
else:
    print("(+) PyGame succesfully initialized!")
    
# Play surface
playSurface = pygame.display.set_mode((720, 460))
#time.sleep(5)
pygame.display.set_caption('Snake game!')

# Colors
# ### = pygame.Color(R, G, B)
red = pygame.Color(255, 0, 0)           # Gameover
green = pygame.Color(0, 255, 0)         # Snake
blue = pygame.Color(0, 0, 255)          
black = pygame.Color(0, 0, 0)           # Score
white = pygame.Color(255, 255, 255)     # Background
brown = pygame.Color(165,42,42)         # Food

# FPS (Frame Per Second Controller)
fpsController = pygame.time.Clock()

# Important variables

snakePosition = [100, 50]                           # snake = [x, y]
snakeBody = [ [100,50], [90,50], [80,50] ]  # List of List [ [x,y], [x,y], [x,y] ]

foodPosition = [random.randrange(1,72)*10, random.randrange(1,46)*10]   # random generate a position

foodSpawn = True

direction = 'RIGHT'
changeTo = direction

score = 0

# Game over function
def gameOver():
    myFont = pygame.font.SysFont('monaco', 72)
    gameOverSurface = myFont.render('Game over!', True, red)    # Define text
    gameOverRectangle = gameOverSurface.get_rect()
    gameOverRectangle.midtop = (360, 15)
    playSurface.blit(gameOverSurface, gameOverRectangle)
    showScore(0)
    pygame.display.flip()                                       # Display text
    time.sleep(2)
    pygame.quit()                                               # pygame exit
    sys.exit()                                                  # console exit

def showScore(choice=1):
    scoreFont = pygame.font.SysFont('monaco', 24 )
    scoreSurface = scoreFont.render('Score: {0}'.format(score), True, black)
    scoreRectangle = scoreSurface.get_rect()
    if choice ==1:
        scoreRectangle.midtop = (80, 10)
    else:
        scoreRectangle.midtop = (360, 120)
    playSurface.blit(scoreSurface, scoreRectangle)
    # pygame.display.flip()
    
    
# Main Logic of the game
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT or event.key == ord('d'):
                changeTo = 'RIGHT'
            if event.key == pygame.K_LEFT or event.key == ord('a'):
                changeTo = 'LEFT'
            if event.key == pygame.K_UP or event.key == ord('w'):
                changeTo = 'UP'
            if event.key == pygame.K_DOWN or event.key == ord('s'):
                changeTo = 'DOWN'    
            if event.key == pygame.K_ESCAPE:
                pygame.event.post(pygame.event.Event(pygame.QUIT))
                
    # validation of direction
    if changeTo == 'RIGHT' and not direction =='LEFT':
        direction = 'RIGHT'
    if changeTo == 'LEFT' and not direction =='RIGHT':
        direction = 'LEFT'
    if changeTo == 'UP' and not direction =='DOWN':
        direction = 'UP'
    if changeTo == 'DOWN' and not direction =='UP ':
        direction = 'DOWN'
    
    # Update snake position [x, y]
    if direction == 'RIGHT':
        snakePosition[0] += 10
    if direction == 'LEFT':
        snakePosition[0] -= 10
    if direction == 'UP':
        snakePosition[1] -= 10
    if direction == 'DOWN':
        snakePosition[1] += 10
        
        
    # Snake body mechanism
    snakeBody.insert(0, list(snakePosition))
    if snakePosition[0] == foodPosition[0] and snakePosition[1] == foodPosition[1]:
        score +=1
        foodSpawn = False
    else:
        snakeBody.pop()
    # Food Spawn
    if foodSpawn == False:
        foodPosition = [random.randrange(1,72)*10, random.randrange(1,46)*10]
    foodSpawn = True
    
    # Background
    playSurface.fill(white)
    
    #Draw Snake
    for pos in snakeBody:
        pygame.draw.rect(playSurface, green,        # pygame.draw.rect(playSurface, green,       
        pygame.Rect(pos[0], pos[1], 10, 10))        # pygame.Rect(x,y,sizex,sizey))
        
        pygame.draw.rect(playSurface, brown,              
        pygame.Rect(foodPosition[0], foodPosition[1], 10, 10))         
        
        # Bound
        if  snakePosition[0] > 710 or snakePosition[0] < 0 :
            gameOver()
        if  snakePosition[1] > 450 or snakePosition[1] < 0 :
            gameOver()
        
        for block in snakeBody[1:]:
            if snakePosition[0] == block[0] and snakePosition[1] == block[1]:
                gameOver()
                
    
    showScore()
    pygame.display.flip()
    fpsController.tick(15)
        
    
    # pyinstaller to create an executable 
    
        
        
