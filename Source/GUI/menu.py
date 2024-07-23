import pygame
from constants import *
from text import *

class Menu:
    def __init__(self, screen):
        self.screen = screen
        self.background = pygame.image.load('assets/menu_bg.png')
        self.menu_screen_choice = [[True, 'choose level'], [False, 'credit'], [False, 'exit']]
    
    def choose_options(self, is_up, is_down):
        min_arrow_pox_x = 10e5
        current_index_active = None
        
        for i, element in enumerate(self.menu_screen_choice):
                
            text_obj = Text_Display(element[1])
            text_content = text_obj.show_text()
            text_pos = text_obj.center_text(height=WINDOW_HEIGHT + i * 300)
            x_text, y_text = text_pos[0], text_pos[1]
            
            arrow_img = pygame.image.load('assets/arrow.png')
            img_width = arrow_img.get_width()
            arrow_pos_x = x_text - img_width - 50
            min_arrow_pox_x = min(arrow_pos_x, min_arrow_pox_x)
            
            if element[0]:
                text_content = text_obj.show_text(color=ACTIVE_CHOICE_COLOR)
                current_index_active = i
                self.screen.blit(arrow_img, (min_arrow_pox_x, y_text + 8))
            
            self.screen.blit(text_content, text_pos)    
            
        # Key input
        menu_choice_lenth = len(self.menu_screen_choice)
            
        if is_down:
            is_down = False
            next_index = current_index_active + 1
            if next_index >= menu_choice_lenth:
                next_index = 0
            self.menu_screen_choice[current_index_active][0] = False
            self.menu_screen_choice[next_index][0] = True
        if is_up:
            is_up = False
            prev_index = current_index_active - 1
            if prev_index < 0:
                prev_index = menu_choice_lenth - 1
            self.menu_screen_choice[current_index_active][0] = False
            self.menu_screen_choice[prev_index][0] = True
                
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
        
        self.choose_options(is_up, is_down)
        
    