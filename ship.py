import pygame

class Ship():
    def __init__(self, ai_settings, screen):
        self.screen = screen
        self.ai_settings = ai_settings
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        
        # ship location
        self.rect.centerx = self.screen_rect.centerx    # X
        self.rect.bottom = self.screen_rect.bottom      # Y
        # make float stored in center
        self.center = float(self.rect.centerx)
        
        #moving flag
        self.moving_right = False
        self.moving_left = False
        
    def update(self):
        """judging ship's location by flag"""
        # 更新飞船的center值，而不是rect
        if self.moving_right and (self.rect.right < self.screen_rect.right):
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and (self.rect.left > 0):
            self.center -= self.ai_settings.ship_speed_factor
        # 根据self.center更新rect对象
        self.rect.centerx = self.center
            
    def blitme(self):
        self.screen.blit(self.image, self.rect)
        
    def center_ship(self):
        """居中飞船"""
        self.center = self.screen_rect.centerx
