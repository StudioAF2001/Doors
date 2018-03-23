#   "Doors" a game by Anrew Skelly & Fionn Ó Muirí
#   Started on the 15th of March 2018



#import required modules
import pygame, time, random

#set some basic variables
pygame.init()

pygame.font.init()

display_width = 800
display_height = 600

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Doors')
clock = pygame.time.Clock()

#colours
white = ((255,255,255))
black = ((0,0,0))
grey = ((150,150,150))



# other required variables
score = 0


# sets up template for each door
class door:
    size = 0 
    x = 0
    y = 0
    speed = 0
    doorOpen = False

# game function
def game():
    global score

    highScoreDoc = open("highScore.txt", "r")
    highScore = int(highScoreDoc.read())
    highScoreDoc.close

    #Images
    doorOpenImg = pygame.image.load('img\doorOpen.png')
    doorClosedImg = pygame.image.load('img\doorClosed.png')

    doors = []
    
    myfont = pygame.font.SysFont('Comic Sans MS', 30)
    textsurface = myfont.render("Score: %s        Highscore: %s" % (0, highScore), False, white)
    
    mouseDownPast = False
    mouseDownNow = False

    score = 0
    
    # create first number of doors
    newDoor = door()

    newDoor.size = random.randrange(40, 70)
    newDoor.x = random.randrange(0, display_width-newDoor.size)
    newDoor.y = random.randrange(display_height, display_height*2)
    newDoor.speed = (newDoor.size-30)/5
        
    doors.append(newDoor)

    # the game loop
    while True:

        mouseX, mouseY = pygame.mouse.get_pos()

        
        # check for events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                mouseDownNow = True

            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                mouseDownNow = False
        

        # refresh the screen
        gameDisplay.fill(black)

        # move and draw doors
        for i in range(0,len(doors)):

            OpenImg = pygame.transform.scale(doorOpenImg, (doors[i].size, int(doors[i].size*1.5)))
            ClosedImg = pygame.transform.scale(doorClosedImg, (doors[i].size, int(doors[i].size*1.5)))

            openchance = random.randrange(doors[i].speed*5,70)
            if doors[i].y < display_height and openchance > 68:
                if not doors[i].doorOpen:
                    doors[i].doorOpen = True

            elif doors[i].y < display_height/2:
                if not doors[i].doorOpen:
                    doors[i].doorOpen = True
            
            doors[i].y -= doors[i].speed

            if mouseX >= doors[i].x and mouseX <= doors[i].x + doors[i].size:
                if mouseY >= doors[i].y and mouseY <= doors[i].y + doors[i].size*1.5:
                    if mouseDownNow == True and mouseDownPast == False:
                        if doors[i].doorOpen:
                            score+=1
                            if score > highScore:
                                highScore = score
                                highScoreDoc = open("highScore.txt", "w")
                                highScoreDoc.write(str(highScore))
                                highScoreDoc.close

                            textsurface = myfont.render("Score: %s        Highscore: %s" % (score, highScore), False, white)
                                
                            doors[i].size = random.randrange(40, 70)
                            doors[i].y = display_height
                            doors[i].x = random.randrange(0, display_width-newDoor.size)
                            doors[i].speed = (doors[i].size-35)/5

                            doors[i].doorOpen = False

                            if score>0 and score%5 == 0:
                                newDoor = door()

                                newDoor.size = random.randrange(40, 70)
                                newDoor.x = random.randrange(0, display_width-newDoor.size)
                                newDoor.y = random.randrange(display_height, display_height*2)
                                newDoor.speed = (newDoor.size-30)/5
                            
                                doors.append(newDoor)
                        

            if doors[i].doorOpen:
                pygame.draw.rect(gameDisplay, grey, pygame.Rect(doors[i].x,doors[i].y,doors[i].size, doors[i].size*1.5))
                gameDisplay.blit(OpenImg, (doors[i].x,doors[i].y))
            else:
                pygame.draw.rect(gameDisplay, black, pygame.Rect(doors[i].x,doors[i].y,doors[i].size, doors[i].size*1.5))
                gameDisplay.blit(ClosedImg, (doors[i].x,doors[i].y))

            if doors[i].y < 0-(doors[i].size*1.5):
                pygame.display.update()
                return
        
        mouseDownPast = mouseDownNow
        
        gameDisplay.blit(textsurface,(0,0))
        
        
        # update screen and set FPS
        pygame.display.update()
        clock.tick(60)

def gameOver():
    myfont = pygame.font.SysFont('Comic Sans MS', 50)
    textsurface = myfont.render('''Game Over - Score: %s''' % (score), False, white)
    gameDisplay.blit(textsurface,(70,70))
    pygame.display.update()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    return

# launch game
if __name__ == "__main__":
    while True:
        game()
        gameOver()

pygame.quit()
quit()
