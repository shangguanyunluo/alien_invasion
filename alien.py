# encoding: utf-8
'''
Created on 2018年9月6日

@author: Administrator
'''
import pygame
from pygame.sprite import Sprite
from settings import Settings

class Alien(Sprite):
    """define a single alien"""
    
    def __init__(self, ai_settings, screen):
        """create the alien and set it's position"""
        super(Alien, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings
        
        # load alien image
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()
        
        # set the alien position 
        self.rect.x = self.rect.width 
        self.rect.y = self.rect.height
        
        # save the position 
        self.x = float(self.rect.x)
        
    def check_edgs(self):
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True
        
    def update(self):
        self.x += (self.ai_settings.alien_speed_factor * self.ai_settings.fleet_direction)
        self.rect.x = self.x
        
    def blitme(self):
        self.screen.blit(self.image, self.rect)
