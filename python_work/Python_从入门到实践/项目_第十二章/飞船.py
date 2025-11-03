import pygame
from pygame.sprite import Sprite
class Ship(Sprite):           #管理飞船类
    def __init__(self,ai_game):                              # ai_game 是主游戏对象
        super().__init__()
        self.screen = ai_game.screen                         #保存游戏屏幕和初始屏幕区域对等
        self.screen_rect = ai_game.screen.get_rect()

        self.settings = ai_game.settings

        self.image = pygame.image.load("images.bmp")         #加载飞船图片
        self.rect = self.image.get_rect()                    #飞船图像的边界


        self.rect.midbottom = self.screen_rect.midbottom     #把飞船的位置设置在屏幕底部中间


        self.moving_right = False                            #飞船初始不动(False),True 的时候持续移动
        self.moving_left = False  
        self.moving_up = False 
        self.moving_down = False 

    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            if self.moving_right:
              self.rect.x += self.settings.ship_speed
        elif self.moving_left and self.rect.left > self.screen_rect.left:
            if self.moving_left:
                self.rect.x -= self.settings.ship_speed
        elif self.moving_up and self.rect.top > self.screen_rect.top:
            if self.moving_up:
                self.rect.y -= self.settings.ship_speed
        elif self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            if self.moving_down:
                self.rect.y += self.settings.ship_speed
        


    def blitme(self):
        self.screen.blit(self.image, self.rect)              #将 self.image 这张图片绘制（blit）到 self.rect 指定的位置

    def center_ship(self):
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)
