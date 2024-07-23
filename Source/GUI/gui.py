import pygame, sys
import math
from pygame.locals import *
from constants import *
from text import *
from menu import *
from credit import *

pygame.init()

#WINDOW_WIDTH = 1200
#WINDOW_HEIGHT = 800

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)

screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
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
        self.wall_cell_img = pygame.image.load(f'assets\\wall_cell_1.png')
        self.wall_cell_img = pygame.transform.scale(self.wall_cell_img, self.cell_size)
        
        self.vehicle_right_img = pygame.image.load(f'assets\\vehicle_3.png')
        self.vehicle_right_img = pygame.transform.scale(self.vehicle_right_img, self.cell_size)
        self.vehicle_up_img = pygame.transform.rotate(self.vehicle_right_img, 90)
        self.vehicle_left_img = pygame.transform.rotate(self.vehicle_up_img, 90)
        self.vehicle_down_img = pygame.transform.rotate(self.vehicle_left_img, 90)
        
        self.vehicle_num_right_img = pygame.image.load(f'assets\\vehicle_2.png')
        self.vehicle_num_right_img = pygame.transform.scale(self.vehicle_num_right_img, self.cell_size)
        self.vehicle_num_up_img = pygame.transform.rotate(self.vehicle_num_right_img, 90)
        self.vehicle_num_left_img = pygame.transform.rotate(self.vehicle_num_up_img, 90)
        self.vehicle_num_down_img = pygame.transform.rotate(self.vehicle_num_left_img, 90)
        
    def readMapData(self, _map_data):
        self.map_data = _map_data
    
    def showCell(self):
        screen.blit(self.empty_cell_img, (WINDOW_WIDTH * 0.1, WINDOW_HEIGHT * 0.1))
    
    def showBoard(self):
        i = 0
        j = 0
        '''for i in range (0, self.n):
            for j in range (0, self.m):
                if j < 3:
                    screen.blit(self.wall_cell_img, (WINDOW_WIDTH * 0.1 + i*self.cell_side, WINDOW_HEIGHT * 0.1 + j*self.cell_side))
                elif j < 8:
                    screen.blit(self.empty_cell_img, (WINDOW_WIDTH * 0.1 + i*self.cell_side, WINDOW_HEIGHT * 0.1 + j*self.cell_side))
                else:
                    screen.blit(self.fuel_cell_img, (WINDOW_WIDTH * 0.1 + i*self.cell_side, WINDOW_HEIGHT * 0.1 + j*self.cell_side))
        for i in range (0, self.n):
            for j in range (0, self.m):
<<<<<<< HEAD
                if j == 3:
                    screen.blit(self.vehicle_right_img, (WINDOW_WIDTH * 0.1 + i*self.cell_side, WINDOW_HEIGHT * 0.1 + j*self.cell_side))
                elif j == 4:
                    screen.blit(self.vehicle_up_img, (WINDOW_WIDTH * 0.1 + i*self.cell_side, WINDOW_HEIGHT * 0.1 + j*self.cell_side))
                elif j == 5:
                    screen.blit(self.vehicle_left_img, (WINDOW_WIDTH * 0.1 + i*self.cell_side, WINDOW_HEIGHT * 0.1 + j*self.cell_side))
                elif j == 6:
                    screen.blit(self.vehicle_down_img, (WINDOW_WIDTH * 0.1 + i*self.cell_side, WINDOW_HEIGHT * 0.1 + j*self.cell_side))'''
        for i in range (0, self.n):
            for j in range (0, self.m):
                if self.map_data[i][j] == '-1':
                    screen.blit(self.wall_cell_img, (WINDOW_WIDTH * 0.1 + i*self.cell_side, WINDOW_HEIGHT * 0.1 + j*self.cell_side))
                elif 'F' in self.map_data[i][j]:
                    screen.blit(self.fuel_cell_img, (WINDOW_WIDTH * 0.1 + i*self.cell_side, WINDOW_HEIGHT * 0.1 + j*self.cell_side))
                else:
                    screen.blit(self.empty_cell_img, (WINDOW_WIDTH * 0.1 + i*self.cell_side, WINDOW_HEIGHT * 0.1 + j*self.cell_side))
                if 'S' in self.map_data[i][j]:
                    if len(self.map_data[i][j]) == 1:
                        screen.blit(self.vehicle_right_img, (WINDOW_WIDTH * 0.1 + i*self.cell_side, WINDOW_HEIGHT * 0.1 + j*self.cell_side))
                    else:
                        screen.blit(self.vehicle_num_right_img, (WINDOW_WIDTH * 0.1 + i*self.cell_side, WINDOW_HEIGHT * 0.1 + j*self.cell_side))


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
    print(map_data)
    while True:
        screen.fill(black)

        #M1 = Board_UI(10, 10, 0, 0, 1)
        M1 = Board_UI(n, m, t, f, level)
        M1.readMapData(map_data)
        M1.showBoard()
        for event in pygame.event.get():
            pygame.display.flip()
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

main_test()
=======
                screen.blit(self.empty_cell_img, (WINDOW_WIDTH * 0.1 + i*40, WINDOW_HEIGHT * 0.1 + j*40))
                
                
choose_option = None
menu = Menu(screen)
credit = Credit(screen)

while True:
    is_up = False
    is_down = False
    
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            #sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                is_down = True
            if event.key == pygame.K_UP:
                is_up = True
            if event.key == pygame.K_RETURN: # press Enter to choose an option
                choose_option = menu.get_choice()
                
    # Menu
    screen.fill((0,0,0))   

    if choose_option is None:
        menu.display_menu(is_up, is_down)
    
    if choose_option is not None:
        if choose_option == 1:
            credit.display_credit()
            choose_option = credit.back_to_menu()
        if choose_option == 2:
            pygame.quit()
        # M1 = Board_UI(10, 10, 0, 0)
        # M1.showBoard()
            
    pygame.display.flip()
>>>>>>> bbda48d4f7c55d842b4677af1feb9439922a9e58
