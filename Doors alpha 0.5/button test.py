
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

playImg = pygame.image.load('play.png')

class button:
    x = 100
    y = 100
    width = 200
    height = 100
    pressed = False

    def press(self, mouseX, mouseY, mouseDown):
        if mouseX > self.x and mouseX < self.x+self.width:
            if mouseY > self.y and mouseY < self.y+self.height:
                if mouseDown:
                    print("Pressed")
                    self.pressed = True

        else:
            pressed = False
                

#colours
white = ((255,255,255))
black = ((0,0,0))
grey = ((150,150,150))

def game():

    buttonA = button()

    mouseDown = False
    
    while True:

        mouseX, mouseY = pygame.mouse.get_pos()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                mouseDown = True

            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                mouseDown = False


            buttonA.press(mouseX, mouseY, mouseDown)
            
            # refresh the screen
            gameDisplay.fill(white)

            pygame.draw.rect(gameDisplay, black, pygame.Rect(buttonA.x,buttonA.y,buttonA.width, buttonA.height))
            gameDisplay.blit(playImg, (buttonA.x,buttonA.y))
            
            # update screen and set FPS
            pygame.display.update()
            clock.tick(60)

if __name__ == "__main__":
    while True:
        game()

pygame.quit()
quit()





        
