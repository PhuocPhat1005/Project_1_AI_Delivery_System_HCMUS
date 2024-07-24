import pygame
from text import *
from constants import *
from common import *

class LeveList:
    def __init__(self, screen):
        self.screen = screen
        self.is_click_back = False
        self.option_back_to = None
        self.level_list = [[True, 'Level 01'], [False, 'Level 02'], [False, 'Level 03'], [False, 'Level 04']]
        
    def get_choice(self):
        for i, element in enumerate(self.level_list):
            if element[0]:
                return i
        return 0
    
    def get_back_to(self):
        if self.is_click_back:
            self.is_click_back = False
            return self.option_back_to
        return 0
        
    def show_level_list(self, is_up, is_down):
        self.screen.fill(BACKGROUND_COLOR)
        
        back_button = BackButton(self.screen)
        back_button_rect = back_button.get_back_button_rect()
        
        text_obj = Text_Display('Choose the level', font_size=FONT_LARGE)
        text_content = text_obj.show_text()
        text_pos = text_obj.center_text(height=100)
        
        self.screen.blit(text_content, text_pos)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if back_button_rect.collidepoint(mouse_pos):
                    self.is_click_back = True
                    self.option_back_to = back_button.back_to(self.is_click_back, None, 0)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN and is_down == False and is_up == False:
                    is_down = True
                if event.key == pygame.K_UP and is_up == False and is_down == False:
                    is_up = True
                if event.key == pygame.K_LEFT and self.is_click_back == False:
                    self.is_click_back = True
                    self.option_back_to = back_button.back_to(self.is_click_back, None, 0)
                if event.key == pygame.K_RETURN:
                    pass
                
        choice_list = ChoiceList(self.screen)
        choice_list.choose_options(self.level_list, is_up, is_down, 500)
        