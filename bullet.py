# encoding: utf-8
'''
Created on 2018年9月3日

@author: Administrator
'''
import pygame
from pygame.sprite import Sprite
from ship import Ship

class Bullet(Sprite):
    
    def __init__(self, ai_settings, screen, ship):
        """在飞船所处的位置创建一个子弹对象"""
        super(Bullet, self).__init__()
        self.screen = screen
        
        # 在（0,0）处创建一个表示子弹的对象，在设置正确的位置
        self.rect = pygame.Rect(0, 0, ai_settings.bullet_width, ai_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top
        
        self.y = float(self.rect.y)
        
        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor
        
        
    def update(self):
        self.y -= self.speed_factor
        self.rect.y = self.y
        
    def draw_bullet(self):
        pygame.draw.rect(self.screen,self.color,self.rect)
