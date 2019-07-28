import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    
    def __init__(self, ai_settings, screen):
        super(Alien, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings
        
        # 加载滑稽图像
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()
        
        # 滑稽上左边距
        self.rect.x = 10
        self.rect.y = 10
        
        # 存储准确位置
        self.x = float(self.rect.x)
        
    def blitme(self):
        """指定位置绘制外星人"""
        self.screen.blit(self.image, self.rect)
        
    def check_edges(self):
        """如果外星人位于屏幕边缘，则返回TRUE"""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True
        
    def update(self):
        """向左向右移动外星人"""
        self.x += (self.ai_settings.alien_speed_factor * 
                        self.ai_settings.fleet_direction)
        self.rect.x = self.x