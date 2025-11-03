import sys               #退出工具
from time import sleep
from scoreboard import Scoreboard # type: ignore
import pygame
from pygame.sprite import Sprite            #游戏界面
from settings import Settings  # type: ignore
from game_stats import GameStats # type: ignore
from button import Button
from 飞船 import Ship
from Bullet import Bullet # type: ignore
from alien import Alien # type: ignore

class AlienInvasion:     #定义类，管理游戏资源
    def __init__(self): 
        pygame.init()    #初始化pygame   
        self.clock = pygame.time.Clock()                   #创建一个游戏时钟对象

        self.settings = Settings()

        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))  #创建窗口，1200，800是窗口尺寸
        pygame.display.set_caption("Alien Invasion")       #创建标题

        self.stats = GameStats(self)

        self.ship = Ship(self)

        self.bullet = pygame.sprite.Group()

        self.aliens = pygame.sprite.Group()

        self._create_fleet()

        self.game_active = False

        self.play_button = Button(self,"Play")

        self.sb = Scoreboard(self)


    def _create_fleet(self):
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size

        current_x, current_y = alien_width, alien_height
        while current_y < (self.settings.screen_height - 4 * alien_height):
            while current_x < (self.settings.screen_width - 2 * alien_width):
                self._create_alien(current_x, current_y)
                current_x += 4 * alien_width
            
            current_x = alien_width
            current_y += 3 * alien_height

    def _create_alien(self, x_position, y_position):
        new_alien = Alien(self)
        new_alien.x = x_position
        new_alien.rect.x = x_position
        new_alien.rect.y = y_position    
        self.aliens.add(new_alien)

    def run_game(self):                                    #游戏内部
        while True:
            self._check_events()                           #监控鼠标,键盘
            self._update_screen()                          #刷新屏幕  
            if self.game_active:
                self.ship.update()                          #飞船移动
                self._update_bullet()                       #子弹移动
                self._update_aliens()                       #外星人移动  
                self.clock.tick(60)                         #设置游戏帧率

    def _ship_hit(self):
        if self.stats.ships_left > 0:                       #当生命值大于三时
            self.stats.ships_left -= 1
            self.sb.prep_ships()
            self.bullet.empty()
            self.aliens.empty()
            self._create_fleet()
            self.ship.center_ship()

            sleep(0.5)
        else:
            self.game_active = False

    def _update_aliens(self):
        self._check_fleet_edges()
        self.aliens.update()
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()
        self._check_aliens_bottom()
         
    def _check_aliens_bottom(self):
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= self.settings.screen_height:
                self._ship_hit()
                break

    def _check_fleet_edges(self):
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break
    
    def _change_fleet_direction(self):
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1
            

    def _check_events(self):
        for event in pygame.event.get():               #键盘和鼠标的每一个事件
            if event.type == pygame.QUIT:              #如果点退出则利用sys退出
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)         
            elif event.type == pygame.KEYUP:           #键盘上的某个键被松开(KEYUP)
                self._check_keyup_events(event)

    def _check_play_button(self, mouse_pos):
            button_clicked = self.play_button.rect.collidepoint(mouse_pos)
            if button_clicked and not self.game_active:
                self.settings.initialize_dynamic_settings()
                self.stats.reset_stats()                      #点play全部重置
                self.game_active = True
                self.bullet.empty()
                self.aliens.empty()
                self._create_fleet()
                self.ship.center_ship()
                pygame.mouse.set_visible(False)
                self.sb.prep_score()
                self.sb.prep_level()
                self.sb.prep_ships()

    def _check_keydown_events(self, event):
        if event.key == pygame.K_RIGHT:                #移动键
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:      
            self.ship.moving_left = True
        elif event.key == pygame.K_UP:      
            self.ship.moving_up = True 
        elif event.key == pygame.K_DOWN:      
            self.ship.moving_down = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _check_keyup_events(self, event):
        if event.key == pygame.K_RIGHT:        
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:        
            self.ship.moving_left = False
        elif event.key == pygame.K_UP:        
            self.ship.moving_up = False
        elif event.key == pygame.K_DOWN:        
            self.ship.moving_down = False 

    def _fire_bullet(self):
        if len(self.bullet) < self.settings.bullet_allowed:
            new_bullet = Bullet(self)
            self.bullet.add(new_bullet)   

    def _update_bullet(self):
        self.bullet.update()                           #刷新子弹位置
        for bullet in self.bullet.copy(): 
            if bullet.rect.bottom <= 0:
                self.bullet.remove(bullet)             #删除已消失的子弹

        self._check_bullet_alien_collisions()

    def _check_bullet_alien_collisions(self):
        collisions = pygame.sprite.groupcollide(self.bullet, self.aliens, True, True)
        if not self.aliens:
            self.bullet.empty()
            self._create_fleet()
            self.settings.increase_speed()
            self.stats.level += 1
            self.sb.prep_level()
        if collisions:
            for aliens in collisions.values():
                self.stats.score += self.settings.alien_points * len(aliens)
            self.sb.prep_score()
            self.sb.check_high_score()

    def _update_screen(self):                          # = pygame.display.flip(), 刷新屏幕 
        self.screen.fill(self.settings.color)          #设置背景色
        for bullet in self.bullet.sprites():
            bullet.draw_bullet()
        self.ship.blitme()
        self.aliens.draw(self.screen)
        self.sb.show_score()
        if not self.game_active:
            self.play_button.draw_button()
            pygame.mouse.set_visible(True)

        pygame.display.flip()



if __name__ == "__main__":                              #当你直接运行这个文件时，这段代码才会被执行
    ai = AlienInvasion()
    ai.run_game()


