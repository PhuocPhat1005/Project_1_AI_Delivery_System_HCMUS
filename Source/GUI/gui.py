import pygame

import pygame, sys
from pygame.locals import *
from constants import *

pygame.init()

screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
title = pygame.display.set_caption('Graph run')

class Board_UI:
    def __init__(self, _n, _m, _f, _t):
        self.cell_side = 40
        self.cell_size = (self.cell_side, self.cell_side)
        self.empty_cell_img = pygame.image.load('assets/empty_cell.png')
        self.empty_cell_img = pygame.transform.scale(self.empty_cell_img, self.cell_size)
        self.n = _n
        self.m = _m
        self.f = _f
        self.t = _t
        self.map_data = []
        self.cells = []
        self.time = 0
        self.vehicle = []
        goals = []
    
    def showCell(self):
        screen.blit(self.empty_cell_img, (WINDOW_WIDTH * 0.1, WINDOW_HEIGHT * 0.1))
    
    def showBoard(self):
        i = 0
        j = 0
        for i in range (0, self.n):
            for j in range (0, self.m):
                screen.blit(self.empty_cell_img, (WINDOW_WIDTH * 0.1 + i*40, WINDOW_HEIGHT * 0.1 + j*40))


while True:
    for event in pygame.event.get():
        screen.fill((0,0,0))

        M1 = Board_UI(10, 10, 0, 0)
        M1.showBoard()
        pygame.display.flip()
        if event.type == QUIT:
            pygame.quit()
            #sys.exit()