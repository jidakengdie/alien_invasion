class Settings():
    
    def __init__(self):
        """original setting"""
        self.screen_width = 1000
        self.screen_height = 600
        self.bg_color = (255, 255, 255)
        
        # ship_moving_speed
        self.ship_speed_factor = 1.5
        self.ship_limit = 3
        
        # 子弹设置
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 6
        
        # 外星人设置
        self.alien_speed_factor = 1
        self.fleet_drop_speed = 5
        # fleet_direction=1为右移，=-1为左移
        self.fleet_direction = 1
