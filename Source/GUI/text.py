import pygame
from GUI.constants import *

# https://www.geeksforgeeks.org/python-display-text-to-pygame-window/

class Text_Display:
    def __init__(self, content, font_type=FONT_TYPE, font_size=FONT_MEDIUM, text_color=WHITE_COLOR):
        self.content = content
        self.font_type = font_type
        self.font_size = font_size
        self.text_color = text_color
        self.text_content = ''
        self.font = pygame.font.Font(font_type, font_size)
        
    def get_text_position(self):
        text_position = self.text_content.get_rect()
        return text_position
    
    def show_text(self, color=None):
        if color is None:
            color = self.text_color
        self.text_content = self.font.render(self.content, True, color)
        return self.text_content
    
    def center_text(self, width=WINDOW_WIDTH, height=WINDOW_HEIGHT):
        text_rect = self.text_content.get_rect(center=(width / 2, height / 2))
        return text_rect
        
        