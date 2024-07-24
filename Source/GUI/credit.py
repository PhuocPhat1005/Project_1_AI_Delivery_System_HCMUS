import pygame
from GUI.constants import *
from GUI.text import *

class Credit:
    def __init__(self, screen):
        self.screen = screen
        self.back_btn_sprite = None
        self.is_click_back = False
            
    def back_button(self):
        text_obj = Text_Display('back')
        text_content = text_obj.show_text()
        text_pos = (50, 700)
        
        self.back_btn_sprite = text_obj.get_text_position()
        self.back_btn_sprite.x = 50
        self.back_btn_sprite.y = 700
        
        self.screen.blit(text_content, text_pos)
            
    def back_to_menu(self):
        if self.is_click_back:
            self.is_click_back = False
            return None
        return 1
    
    def write_text_content(self, font_size=FONT_MEDIUM, is_center=False, width=WINDOW_WIDTH, height=WINDOW_HEIGHT, pos_x=0, pos_y=0, content=''):
        text_obj = Text_Display(content, font_size=font_size)
        text_content = text_obj.show_text()
        text_pos = (pos_x, pos_y)
        
        if is_center:
            text_pos = text_obj.center_text(width, height)
        
        self.screen.blit(text_content, text_pos)
            
    def display_credit(self):
        self.screen.fill((40,40,43))   
        
        self.back_button()
        
        text_obj = Text_Display('credit', font_size=FONT_LARGE)
        text_content = text_obj.show_text()
        text_pos = text_obj.center_text(height=100)
        
        self.screen.blit(text_content, text_pos)
        
        self.write_text_content(content='22127174 - Ngo van Khai', is_center=True, height=500)
        self.write_text_content(content='22127322 - Le Phuoc Phat', is_center=True, height=700)
        self.write_text_content(content='22127388 - To Quoc Thanh', is_center=True, height=900)
        self.write_text_content(content='22127441 - Thai Huyen Tung', is_center=True, height=1100)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    self.is_click_back = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if self.back_btn_sprite.collidepoint(mouse_pos):
                    self.is_click_back = True
                
        
    