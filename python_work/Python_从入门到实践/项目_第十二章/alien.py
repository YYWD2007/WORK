import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        self.image = pygame.image.load("alien2.bmp")
        # print("图片大小：", self.image.get_size())         图片太大显示不了

        self.image = pygame.transform.scale(self.image, (40, 40))  #改变尺寸

        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width             #x为宽度
        self.rect.y = self.rect.height            #y为高度

        self.x = float(self.rect.x)

    
    def update(self):
        self.x += self.settings.alien_speed * self.settings.fleet_direction
        self.rect.x = self.x

    def check_edges(self):
        screen_rect = self.screen.get_rect()
        return (self.rect.right >= screen_rect.right) or (self.rect.left <= 0)
    

        

