import pygame
from GUI.constants import *
from GUI.text import *
from GUI.common import *

class UI_Level_1:
    def __init__(self, screen):
        self.screen = screen
        self.is_click_back = False
        self.option_back_to = None
        self.option_result = None
        self.level_list = [[True, 'BFS'], [False, 'DFS'], [False, 'UCS'], [False, 'GBFS'], [False, 'A*']]
        
    def get_choice(self):
        for i, element in enumerate(self.level_list):
            if element[0]:
                return i
        return 0
    
    def get_back_to(self, current_state=0, is_force_left=False):
        if self.is_click_back or is_force_left:
            self.is_click_back = False
            res = self.option_back_to
            self.option_back_to = None
            return res
        return current_state
    
    def get_option_result(self):
        res = self.option_result
        self.option_result = None
        return res
    
    def write_text_content(self, font_size=FONT_MEDIUM, is_center=False, width=WINDOW_WIDTH, height=WINDOW_HEIGHT, pos_x=0, pos_y=0, content=''):
        text_obj = Text_Display(content, font_size=font_size)
        text_content = text_obj.show_text()
        text_pos = (pos_x, pos_y)
        
        if is_center:
            text_pos = text_obj.center_text(width, height)
        
        self.screen.blit(text_content, text_pos)
    
    def draw_ui(self, pos_x, pos_y, content=''):
        self.write_text_content(pos_x=pos_x, pos_y=pos_y, content=content)
        back_button = BackButton(self.screen)
        
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
            self.option_result = self.get_choice()
            
        choice_list = ChoiceList(self.screen)
        choice_list.choose_options(self.level_list, is_up, is_down, 300)
                