import pygame
from GUI.text import *
from GUI.constants import *
from GUI.common import *

class LeveList:
    def __init__(self, screen):
        self.screen = screen
        self.is_click_back = False
        self.option_back_to = None
        self.option_result = None
        self.level_list = [[True, 'Level 01'], [False, 'Level 02'], [False, 'Level 03'], [False, 'Level 04']]
        
    def get_choice(self):
        for i, element in enumerate(self.level_list):
            if element[0]:
                return i
        return 0
    
    def get_level(self):
        for i, element in enumerate(self.level_list):
            if element[0]:
                return element
        return 0
    
    def get_back_to(self):
        if self.is_click_back:
            self.is_click_back = False
            res = self.option_back_to
            self.option_back_to = None
            return res
        return 0
    
    def get_option_result(self):
        res = self.option_result
        self.option_result = None
        return res
        
    def show_level_list(self, is_up, is_down, is_left, is_enter):
        self.screen.fill(BACKGROUND_COLOR)
        
        back_button = BackButton(self.screen)
        # back_button_rect = back_button.get_back_button_rect()
        
        text_obj = Text_Display('Choose the level', font_size=FONT_LARGE)
        text_content = text_obj.show_text()
        text_pos = text_obj.center_text(height=100)
        
        self.screen.blit(text_content, text_pos)
        
        if is_left:
            is_left = False
            self.is_click_back = True
            self.option_back_to = back_button.back_to(self.is_click_back, None, 0)
        if is_enter:
            is_enter = False
            self.option_result = self.get_choice()
            return self.get_choice()
                
        choice_list = ChoiceList(self.screen)
        choice_list.choose_options(self.level_list, is_up, is_down, 500)
        