import pygame
from constants import *
from text import *
from common import *

class UI_Level_1:
    def __init__(self, screen):
        self.screen = screen
        self.is_click_back = False
        self.option_back_to = None
        self.level_list = [[True, 'BFS'], [False, 'DFS'], [False, 'UCS'], [False, 'GBFS'], [False, 'A*']]
        
    def get_choice(self):
        for i, element in enumerate(self.level_list):
            if element[0]:
                return i
        return 0
    
    def get_back_to(self):
        if self.is_click_back:
            self.is_click_back = False
            res = self.option_back_to
            self.option_back_to = None
            return res
        return 0
        
    def show_level_list(self, is_up, is_down, is_left, is_enter):
        self.screen.fill(BACKGROUND_COLOR)
        
        back_button = BackButton(self.screen)
        # back_button_rect = back_button.get_back_button_rect()
        
        text_obj = Text_Display('Choose the search algorithm', font_size=FONT_LARGE)
        text_content = text_obj.show_text()
        text_pos = text_obj.center_text(height=100)
        
        self.screen.blit(text_content, text_pos)
            
        if is_left:
            is_left = False
            self.is_click_back = True
            self.option_back_to = back_button.back_to(self.is_click_back, None, 0)
        if is_enter:
            is_enter = False
            
            
        choice_list = ChoiceList(self.screen)
        choice_list.choose_options(self.level_list, is_up, is_down, 300)
                