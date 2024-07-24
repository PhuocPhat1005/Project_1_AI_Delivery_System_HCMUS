import pygame
from GUI.constants import *
from GUI.text import *
from GUI.common import ChoiceList

class Menu:
    def __init__(self, screen):
        self.screen = screen
        self.background = pygame.image.load('GUI/assets/menu_bg.png')
        self.menu_screen_choice = [[True, 'choose level'], [False, 'credit'], [False, 'exit']]
    
    def get_choice(self):
        for i, element in enumerate(self.menu_screen_choice):
            if element[0]:
                return i
        return 0
            
    def display_menu(self, is_up, is_down):
        self.screen.blit(self.background, (0, 0))
        
        title_obj = Text_Display('Project 01: Delivery system', font_size=FONT_LARGE)
        title = title_obj.show_text()
        title_pos = title_obj.center_text(height=100)
        
        self.screen.blit(title, title_pos)
        
        choice_list = ChoiceList(self.screen)
        choice_list.choose_options(self.menu_screen_choice, is_up, is_down)
        
    