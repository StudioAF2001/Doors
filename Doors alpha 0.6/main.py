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

#Images
doorOpenImg = pygame.image.load('img\doorOpen.png')
doorClosedImg = pygame.image.load('img\doorClosed.png')
pausedImg = pygame.image.load('img\paused.png')
menuImg = pygame.image.load('img\menu.png')
logoImg = pygame.image.load('img\logo.png')

#music
pygame.mixer.music.load("music/Düsseldorf Waltz.mp3")
pygame.mixer.music.play(-1)

# other required variables
score = 0
highScoreDoc = open("highScore.txt", "r")
highScore = int(highScoreDoc.read())
highScoreDoc.close
sound = True

destination = ""

menuImgScale = pygame.transform.scale(menuImg,(int((display_height-100)/1.5),display_height-100))
bgimgWidth, bgimgHeight = menuImgScale.get_rect().size

optionButtons = []
menuButtons = []

#template for each door
class door:
    size = 0 
    x = 0
    y = 0
    speed = 0
    doorOpen = False

#template for buttons
class button:
    imgA = pygame.image.load('img\doorOpen.png')
    imgB = pygame.image.load('img\doorOpen.png')
    width = 0
    height = 0
    x = 0
    y = 0

for i in range(0,2):
    newButton = button()
    newButton.imgA = pygame.transform.scale(pygame.image.load("img/buttons/menu/btn%sa.png" % (i+1)),(int(bgimgWidth*0.55),int(((bgimgWidth*0.5)/5)*3)))
    newButton.imgB = pygame.transform.scale(pygame.image.load("img/buttons/menu/btn%sb.png" % (i+1)),(int(bgimgWidth*0.55),int(((bgimgWidth*0.5)/5)*3)))
    newButton.width, newButton.height = newButton.imgA.get_rect().size
    newButton.x = int((display_width/2)-(newButton.width/5))
    newButton.y = int((display_height/3.25)+(i*100))

    menuButtons.append(newButton)

for i in range(0,2):
    newButton = button()
    newButton.imgA = pygame.transform.scale(pygame.image.load("img/buttons/options/btn%sa.png" % (i+1)),(int(bgimgWidth*0.55),int(((bgimgWidth*0.5)/5)*3)))
    newButton.imgB = pygame.transform.scale(pygame.image.load("img/buttons/options/btn%sb.png" % (i+1)),(int(bgimgWidth*0.55),int(((bgimgWidth*0.5)/5)*3)))
    newButton.width, newButton.height = newButton.imgA.get_rect().size
    newButton.x = int((display_width/2)-(newButton.width/5))
    newButton.y = int((display_height/3.25)+(i*100))

    optionButtons.append(newButton)

def menuFade(mode,menu):
    #scales background image
    menuImgScale = pygame.transform.scale(menuImg,(int((display_height-100)/1.5),display_height-100))
    bgimgWidth, bgimgHeight = menuImgScale.get_rect().size

    buttons = []
    if menu == "menu":
        buttons = menuButtons
    elif menu == "options":
        buttons = optionButtons

    myfont = pygame.font.Font('img/fonts/VINERITC.ttf', 40)
    textsurface = myfont.render('Highscore: %s' % (highScore), False, white)

    s = pygame.Surface((display_width,display_height)) 

    if mode == "in":
        for i in range(255,0,-3):
            #draws background image
            gameDisplay.blit(menuImgScale,(int((display_width/2)-(bgimgWidth/2)),int((display_height/2)-(bgimgHeight/2))))
            
            for j in range(0,len(buttons)):
                #draws button
                gameDisplay.blit(buttons[j].imgA,(buttons[j].x, buttons[j].y,))
                
            gameDisplay.blit(textsurface,(0,0))
            
            s.set_alpha(i)                
            s.fill((0,0,0))       
            gameDisplay.blit(s, (0,0))
            
            pygame.display.update()
            
    elif mode == "out":
        for i in range(0,255,3):
            #draws background image
            gameDisplay.blit(menuImgScale,(int((display_width/2)-(bgimgWidth/2)),int((display_height/2)-(bgimgHeight/2))))
            
            for j in range(0,len(buttons)):
                #draws button
                gameDisplay.blit(buttons[j].imgA,(buttons[j].x, buttons[j].y,))
                
            gameDisplay.blit(textsurface,(0,0))
            
            s.set_alpha(i)                
            s.fill((0,0,0))       
            gameDisplay.blit(s, (0,0))
            
            pygame.display.update()

# game function
def game():
    global score
    global highScore
    global destination

    paused = False

    doors = []

    #prints score in top ledt
    myfont = pygame.font.Font('img/fonts/VINERITC.ttf', 30)
    textsurface = myfont.render("Score: %s        Highscore: %s" % (0, highScore), False, white)
    
    mouseDownPast = False
    mouseDownNow = False

    score = 0
    
    # create first door
    newDoor = door()

    newDoor.size = random.randrange(40, 70)
    newDoor.x = random.randrange(0, display_width-newDoor.size)
    newDoor.y = random.randrange(display_height, display_height*2)
    newDoor.speed = (newDoor.size-30)/5
        
    doors.append(newDoor)

    # the game loop
    while True:

        #gets mouse position
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

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    #pauses/unpauses the game when space is pressed
                    if paused:
                        pygame.time.delay(500)
                        paused = False
                    else:
                        paused = True
                        gameDisplay.fill(black)
                        gameDisplay.blit(pausedImg,(display_width/2-100, display_height/2-150))
                        pygame.display.update()
        
        
        


        if not paused:
            # refresh the screen
            gameDisplay.fill(black)
            
            # move and draw doors
            for i in range(0,len(doors)):

                
                # scales door images to required size
                OpenImg = pygame.transform.scale(doorOpenImg, (doors[i].size, int(doors[i].size*1.5)))
                ClosedImg = pygame.transform.scale(doorClosedImg, (doors[i].size, int(doors[i].size*1.5)))

                #chance of door opening before halfway
                openchance = random.randrange(doors[i].speed*5,70)
                if doors[i].y < display_height and openchance >= 69:
                    if not doors[i].doorOpen:
                        doors[i].doorOpen = True

                # if door hasn't opened by certain point, open it
                elif doors[i].y < display_height/3:
                    if not doors[i].doorOpen:
                        doors[i].doorOpen = True

                # move door
                doors[i].y -= doors[i].speed

                #checks to see if the door was clicked
                if mouseX >= doors[i].x and mouseX <= doors[i].x + doors[i].size:
                    if mouseY >= doors[i].y and mouseY <= doors[i].y + doors[i].size*1.5:
                        if mouseDownNow == True and mouseDownPast == False:
                            if doors[i].doorOpen:
                                #increases score
                                score+=1

                                #checks for highscore
                                if score > highScore:
                                    highScore = score
                                    highScoreDoc = open("highScore.txt", "w")
                                    highScoreDoc.write(str(highScore))
                                    highScoreDoc.close

                                textsurface = myfont.render("Score: %s        Highscore: %s" % (score, highScore), False, white)

                                # resets the door
                                doors[i].size = random.randrange(40, 70)
                                doors[i].y = display_height
                                doors[i].x = random.randrange(0, display_width-newDoor.size)
                                doors[i].speed = (doors[i].size-35)/5

                                doors[i].doorOpen = False

                                #adds a new door every time the score if a multiple of 5 
                                if score>0 and score<=25 and score%5 == 0:
                                    newDoor = door()

                                    newDoor.size = random.randrange(40, 70)
                                    newDoor.x = random.randrange(0, display_width-newDoor.size)
                                    newDoor.y = random.randrange(display_height, display_height*2)
                                    newDoor.speed = (newDoor.size-30)/5
                                
                                    doors.append(newDoor)
                            

                #draws the door
                if doors[i].doorOpen:
                    pygame.draw.rect(gameDisplay, grey, pygame.Rect(doors[i].x,doors[i].y,doors[i].size, doors[i].size*1.5))
                    gameDisplay.blit(OpenImg, (doors[i].x,doors[i].y))
                else:
                    pygame.draw.rect(gameDisplay, black, pygame.Rect(doors[i].x,doors[i].y,doors[i].size, doors[i].size*1.5))
                    gameDisplay.blit(ClosedImg, (doors[i].x,doors[i].y))

                #if the door reaches the top, end game
                if doors[i].y < 0-(doors[i].size*1.5):
                    pygame.display.update()
                    destination = "gameOver"
                    return
        
            mouseDownPast = mouseDownNow
            
            gameDisplay.blit(textsurface,(0,0))
        
        
        # update screen and set FPS
        pygame.display.update()
        clock.tick(60)

# game over function
def gameOver():
    global destination
    # writes gameover + score
    myfont = pygame.font.Font('img/fonts/VINERITC.ttf', 50)
    textsurface = myfont.render('''Game Over - Score: %s   "Space"''' % (score), False, white)
    gameDisplay.blit(textsurface,(70,300))
    pygame.display.update()

    #waits for space press for menu or quit
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    menuFade("in","menu")
                    destination = "menu"
                    return

# menu function
def menu():
    global menuButtons
    global destination

    buttons = menuButtons

    #scales background image
    menuImgScale = pygame.transform.scale(menuImg,(int((display_height-100)/1.5),display_height-100))
    bgimgWidth, bgimgHeight = menuImgScale.get_rect().size

    mouseDownNow = False
        
    while True:

        gameDisplay.fill(black)

        mouseX, mouseY = pygame.mouse.get_pos()

        # checks for clicks
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                mouseDownNow = True

            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                mouseDownNow = False

        #draws background image
        gameDisplay.blit(menuImgScale,(int((display_width/2)-(bgimgWidth/2)),int((display_height/2)-(bgimgHeight/2))))

        #goes through buttons
        for i in range(0,len(buttons)):
            #checks if button was pressed
            if mouseX > buttons[i].x and mouseX < buttons[i].x+buttons[i].width:
                if mouseY > buttons[i].y and mouseY < buttons[i].y+buttons[i].height:
                    #draws button
                    gameDisplay.blit(buttons[i].imgB,(buttons[i].x, buttons[i].y,))
                    if mouseDownNow:
                        if i == 0:
                            menuFade("out", "menu")
                            destination = "game"
                            return
                        if i == 1:
                            menuFade("out","menu")
                            menuFade("in","options")
                            destination = "options"
                            return
                else:
                    #draws button
                    gameDisplay.blit(buttons[i].imgA,(buttons[i].x, buttons[i].y,))
            else:
                #draws button
                gameDisplay.blit(buttons[i].imgA,(buttons[i].x, buttons[i].y,))

        # draws highscore in the top left
        myfont = pygame.font.Font('img/fonts/VINERITC.ttf', 40)
        textsurface = myfont.render('Highscore: %s' % (highScore), False, white)
        gameDisplay.blit(textsurface,(0,0))
        
        pygame.display.update()
        
def startUp():
    global destination
    #scales background image
    menuImgScale = pygame.transform.scale(menuImg,(int((display_height-100)/1.5),display_height-100))
    bgimgWidth, bgimgHeight = menuImgScale.get_rect().size

    logoImgWidth, logoImgHeight = logoImg.get_rect().size

    myfont = pygame.font.Font('img/fonts/VINERITC.ttf', 40)
    textsurface = myfont.render('Highscore: %s' % (highScore), False, white)
    
    for i in range(255,0,-3):
        gameDisplay.blit(logoImg,((display_width/2)-(logoImgWidth/2),(display_height/2)-(logoImgHeight/2)))
        s = pygame.Surface((display_width,display_height)) 
        s.set_alpha(i)                
        s.fill((0,0,0))       
        gameDisplay.blit(s, (0,0))   
        pygame.display.update()
        
    for i in range(0,255,3):
        gameDisplay.blit(logoImg,((display_width/2)-(logoImgWidth/2),(display_height/2)-(logoImgHeight/2)))
        s = pygame.Surface((display_width,display_height)) 
        s.set_alpha(i)                
        s.fill((0,0,0))       
        gameDisplay.blit(s, (0,0))   
        pygame.display.update()

    menuFade("in","menu")

def options():
    global destination
    global buttons
    global sound
    buttons = []
    
    #scales background image
    menuImgScale = pygame.transform.scale(menuImg,(int((display_height-100)/1.5),display_height-100))
    bgimgWidth, bgimgHeight = menuImgScale.get_rect().size

    mouseDownNow = False

    #creates required buttons
    for i in range(0,2):
        newButton = button()
        newButton.imgA = pygame.transform.scale(pygame.image.load("img/buttons/options/btn%sa.png" % (i+1)),(int(bgimgWidth*0.55),int(((bgimgWidth*0.5)/5)*3)))
        newButton.imgB = pygame.transform.scale(pygame.image.load("img/buttons/options/btn%sb.png" % (i+1)),(int(bgimgWidth*0.55),int(((bgimgWidth*0.5)/5)*3)))
        newButton.width, newButton.height = newButton.imgA.get_rect().size
        newButton.x = int((display_width/2)-(newButton.width/5))
        newButton.y = int((display_height/3.25)+(i*100))

        buttons.append(newButton)

    while True:

        gameDisplay.fill(black)

        mouseX, mouseY = pygame.mouse.get_pos()

        # checks for clicks
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                mouseDownNow = True

            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                mouseDownNow = False

        #draws background image
        gameDisplay.blit(menuImgScale,(int((display_width/2)-(bgimgWidth/2)),int((display_height/2)-(bgimgHeight/2))))

        #goes through buttons
        for i in range(0,len(buttons)):
            #checks if button was pressed
            if mouseX > buttons[i].x and mouseX < buttons[i].x+buttons[i].width:
                if mouseY > buttons[i].y and mouseY < buttons[i].y+buttons[i].height:
                    #draws button
                    gameDisplay.blit(buttons[i].imgB,(buttons[i].x, buttons[i].y,))
                    if mouseDownNow:
                        if i == 0:
                            if sound:
                                sound = False
                                pygame.mixer.music.stop()
                                pygame.time.delay(100)
                            else:
                                sound = True
                                pygame.mixer.music.load("music/Düsseldorf Waltz.mp3")
                                pygame.mixer.music.play(-1)
                                pygame.time.delay(100)
                                
                        if i == 1:
                            menuFade("out","options")
                            menuFade("in","menu")
                            destination = "menu"
                            return
                else:
                    #draws button
                    gameDisplay.blit(buttons[i].imgA,(buttons[i].x, buttons[i].y,))
            else:
                #draws button
                gameDisplay.blit(buttons[i].imgA,(buttons[i].x, buttons[i].y,))

        # draws highscore in the top left
        myfont = pygame.font.Font('img/fonts/VINERITC.ttf', 40)
        textsurface = myfont.render('Highscore: %s' % (highScore), False, white)
        gameDisplay.blit(textsurface,(0,0))
        
        pygame.display.update()
        
# launch game
if __name__ == "__main__":
    startUp()
    menu()
    while True:
        if destination == "game":
            game()
        if destination == "menu":
            menu()
        if destination == "options":
            options()
        if destination == "gameOver":
            gameOver()

pygame.quit()
quit()
