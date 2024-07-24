import pygame
from constants import *
from text import *

class BackButton:
    def __init__(self, screen, btn_pos_x=50, btn_pos_y=700, content='back'):
        self.screen = screen
        self.is_click_back = False
        self.back_btn_sprite = None
        
        text_obj = Text_Display(content)
        text_content = text_obj.show_text()
        text_pos = (50, 700)
        
        self.back_btn_sprite = text_obj.get_text_position()
        self.back_btn_sprite.x = btn_pos_x
        self.back_btn_sprite.y = btn_pos_y
        
        self.screen.blit(text_content, text_pos)
        
        
    def get_back_button_rect(self):
        return self.back_btn_sprite
    
    def back_to(self, is_click=False, option=None, current=None):
        self.is_click_back = is_click
        if self.is_click_back:
            self.is_click_back = False
            return option
        return current
    
class ChoiceList:
    def __init__(self, screen):
        self.screen = screen
        
    def choose_options(self, choice_list, is_up, is_down, letter_spacing=WINDOW_HEIGHT):
        min_arrow_pox_x = 10e5
        current_index_active = None
        
        for i, element in enumerate(choice_list):
                
            text_obj = Text_Display(element[1])
            text_content = text_obj.show_text()
            text_pos = text_obj.center_text(height=letter_spacing + i * 300)
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
        menu_choice_lenth = len(choice_list)
            
        if is_down:
            is_down = False
            next_index = current_index_active + 1
            if next_index >= menu_choice_lenth:
                next_index = 0
            choice_list[current_index_active][0] = False
            choice_list[next_index][0] = True
        if is_up:
            is_up = False
            prev_index = current_index_active - 1
            if prev_index < 0:
                prev_index = menu_choice_lenth - 1
            choice_list[current_index_active][0] = False
            choice_list[prev_index][0] = True