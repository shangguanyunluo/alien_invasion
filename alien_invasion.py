# encoding: utf-8
'''
Created on 2018年8月25日

@author: Administrator
'''
import sys

import pygame
from pygame.sprite import Group
from settings import Settings
from ship import Ship
import game_functions as gf
from alien import Alien


def run_game():
    
    # 初始化游戏并创建第一个屏幕对象
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    
    pygame.display.set_caption("Alien Invasion")
    
    # create a ship
    ship = Ship(ai_settings, screen)

    # create a group of bullets
    bullets = Group()
    
    # create alien
    aliens = Group()
    
    gf.create_fleet(ai_settings, screen, ship, aliens)
    
    # 开始游戏的:
    while True:
        
        # listen keyboard and mouse click
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        gf.update_bullets(bullets)
        gf.update_screen(ai_settings, screen, ship, aliens, bullets)
        
run_game()
    
    
     

