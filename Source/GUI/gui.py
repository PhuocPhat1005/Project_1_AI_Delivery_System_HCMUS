import pygame, sys
import math
from pygame.locals import *

pygame.init()

display_width = 1200
display_height = 800

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)

screen = pygame.display.set_mode((display_width, display_height))
title = pygame.display.set_caption('Graph run')

class Board_UI:
    def __init__(self, _n, _m, _f, _t, _level):
        self.n = _n
        self.m = _m
        self.f = _f
        self.t = _t
        self.map_data = []
        self.cells = []
        self.time = 0
        self.vehicle = []
        goals = []
        self.fuel_stations = []
        self.level = _level

        self.cell_side = 60
        self.cell_size = (self.cell_side, self.cell_side)
        self.empty_cell_img = pygame.image.load(f'assets\\empty_cell.png')
        self.empty_cell_img = pygame.transform.scale(self.empty_cell_img, self.cell_size)
        self.fuel_cell_img = pygame.image.load(f'assets\\fuel_cell.png')
        self.fuel_cell_img = pygame.transform.scale(self.fuel_cell_img, self.cell_size)
        self.vehicle_cell_img = pygame.image.load(f'assets\\vehicle_1.png')
        self.vehicle_cell_img = pygame.transform.scale(self.vehicle_cell_img, self.cell_size)
        self.wall_cell_img = pygame.image.load(f'assets\\wall_cell_1.png')
        self.wall_cell_img = pygame.transform.scale(self.wall_cell_img, self.cell_size)
    
    def readMapData(self, _map_data):
        self.map_data = _map_data
    
    def showCell(self):
        screen.blit(self.empty_cell_img, (display_width * 0.1, display_height * 0.1))
    
    def showBoard(self):
        i = 0
        j = 0
        for i in range (0, self.n):
            for j in range (0, self.m):
                if j < 3:
                    screen.blit(self.empty_cell_img, (display_width * 0.1 + i*self.cell_side, display_height * 0.1 + j*self.cell_side))
                elif j < 5:
                    screen.blit(self.wall_cell_img, (display_width * 0.1 + i*self.cell_side, display_height * 0.1 + j*self.cell_side))
                elif j < 8:
                    screen.blit(self.vehicle_cell_img, (display_width * 0.1 + i*self.cell_side, display_height * 0.1 + j*self.cell_side))
                else:
                    screen.blit(self.fuel_cell_img, (display_width * 0.1 + i*self.cell_side, display_height * 0.1 + j*self.cell_side))


def main_test():
    level = 1
    with open('input1_level4.txt', 'r') as file:
        # Read the first line and extract n, m, t, f
        first_line = file.readline().strip()
        n, m, t, f = map(int, first_line.split())

        # Read the next n lines to get the map information
        map_data = []
        for _ in range(n):
            line = file.readline().strip()
            map_data.append(line.split())
    
    while True:
        for event in pygame.event.get():
            screen.fill((0,0,0))

            #M1 = Board_UI(10, 10, 0, 0, 1)
            M1 = Board_UI(n, m, t, f, level)
            M1.readMapData(map_data)
            M1.showBoard()
            pygame.display.flip()
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

main_test()