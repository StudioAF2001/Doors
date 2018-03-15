#   "Doors" a game by Anrew Skelly & Fionn Ó Muirí
#   Started on the 15th of March 2018



#import required modules
import pygame, time, random

#set some basic variables
pygame.init()

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
doors = []

# sets up template for each door
class door:
    size = 0 
    x = 0
    y = 0
    speed = 0
    doorOpen = False

# game function
def game():

    # create desired number of doors
    for i in range(0,5):
        newDoor = door()

        newDoor.size = random.randrange(40, 70)
        newDoor.x = random.randrange(0, display_width-newDoor.size)
        newDoor.y = random.randrange(display_height, display_height*2)
        newDoor.speed = (newDoor.size-30)/5
        
        doors.append(newDoor)

    # the game loop
    while True:

        # check for events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        

        # refresh the screen
        gameDisplay.fill(white)

        # move and draw doors
        for i in range(0,len(doors)):

            openchance = random.randrange(doors[i].speed*5,70)
            if doors[i].y < display_height and openchance > 68:
                if not doors[i].doorOpen:
                    doors[i].doorOpen = True

            elif doors[i].y < display_height/2:
                if not doors[i].doorOpen:
                    doors[i].doorOpen = True
            
            doors[i].y -= doors[i].speed
            
            if doors[i].y < 0-(doors[i].size*1.5):
                doors[i].size = random.randrange(40, 70)
                doors[i].y = display_height
                doors[i].x = random.randrange(0, display_width-newDoor.size)
                doors[i].speed = (doors[i].size-35)/5

                doors[i].doorOpen = False

            if doors[i].doorOpen:
                pygame.draw.rect(gameDisplay, grey, pygame.Rect(doors[i].x,doors[i].y,doors[i].size, doors[i].size*1.5))
            else:
                pygame.draw.rect(gameDisplay, black, pygame.Rect(doors[i].x,doors[i].y,doors[i].size, doors[i].size*1.5))

        
        # update screen and set FPS
        pygame.display.update()
        clock.tick(60)

# launch game
if __name__ == "__main__":
    game()

pygame.quit()
quit()
