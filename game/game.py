import pygame
import colors as c

class Game:
    def __init__(self):
        pygame.init()

        self.display = pygame.display.set_mode( (400, 300), 0, 32)
        pygame.display.set_caption('PyDungeon')
        
        self.font = pygame.font.Font('freesansbold.ttf', 16)
        self.display.fill(c.grey)
        
    def update(self, paramDict):
            self.display.fill(c.grey)
            #stuff
            self.updateHealth(paramDict['health'])
            self.updateTurn(paramDict['turn'])
            
            try:
                x = paramDict['alert']                
                if x:
                    if x == 1: #hero dies
                        self.alertMessage('Hero is dead')
                    elif x == 2: #level ends
                        self.alertMessage('Level Complete')
            except:
                pass            
            pygame.display.update()
            

    def alertMessage(self, msg):
        textSurface = self.font.render(msg, True, c.black, c.grey)
        textRect = textSurface.get_rect()
        textRect.midtop = (200, 75)
        self.display.blit(textSurface, textRect)
            
    def updateHealth(self, h):
        textSurface = self.font.render('HEALTH: ' + str(h), True, c.white, c.grey)
        textRect = textSurface.get_rect()
        textRect.topleft = (5, 5)
        self.display.blit(textSurface, textRect)
    
    def updateTurn(self, t):
        textSurface = self.font.render('TURN: ' + str(t), True, c.white, c.grey)
        textRect = textSurface.get_rect()
        textRect.topright = (395, 5)
        self.display.blit(textSurface, textRect)
            
    def destroy(self):
        pass
