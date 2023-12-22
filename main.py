import pygame
import sys
from player import Player


#MAKING THE CAMERA LOGIC
class Camera(pygame.sprite.Group):
    def __init__(self , surface):
        super().__init__()
        self.bg = pygame.image.load("/Users/zeeldarji/Desktop/python files/game/resources/bg/map.png")
        self.offset = pygame.math.Vector2()
        self.surface = surface
        self.midx = 625
        self.midy = 425
        self.player_rect = Player.rect

    def movin(self):
        self.offset.x = self.player_rect.centerx-self.midx
        self.offset.y = self.player_rect.centery-self.midy
        self.surface.blit(self.bg , (self.offset.x , self.offset.y))

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1250 , 850))
        #GETTING THE BG
        self.bg = pygame.image.load("/Users/zeeldarji/Desktop/python files/game/resources/bg/map.png")
        pygame.display.set_caption("the detect")
        
        #MAKING THE CAMERA LIST
        self.player_group = Camera(self.screen)

        #ALL THE CHARECTERS
        self.player = Player("/Users/zeeldarji/Desktop/python files/game/resources/player/down/0.png" , (50 , 50) , self.player_group)
        
            



    def running(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
            self.screen.fill("red")
            self.screen.blit(self.bg , (0 , 0))

            
            self.player_group.update()
            self.player_group.movin()
            self.player_group.draw(self.screen)
            print(self.player.rect.center) 
            pygame.display.update()




if __name__ == "__main__":
    game = Game()
    game.running()