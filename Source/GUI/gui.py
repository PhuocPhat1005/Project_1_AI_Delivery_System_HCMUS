import pygame, sys
import math
from pygame.locals import *
from GUI.constants import *
from GUI.text import *
from GUI.menu import *
from GUI.credit import *
from GUI.level_list import *

pygame.init()
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

        self.background = pygame.image.load('GUI/assets/menu_bg.png')
        self.cell_side = 60
        self.cell_size = (self.cell_side, self.cell_side)
        self.empty_cell_img = pygame.image.load(f'GUI\\assets\\empty_cell.png')
        self.empty_cell_img = pygame.transform.scale(self.empty_cell_img, self.cell_size)
        self.goal_cell_img = pygame.image.load(f'GUI\\assets\\goal_cell.png')
        self.goal_cell_img = pygame.transform.scale(self.goal_cell_img, self.cell_size)
        self.wall_cell_img = pygame.image.load(f'GUI\\assets\\wall_cell_1.png')
        self.wall_cell_img = pygame.transform.scale(self.wall_cell_img, self.cell_size)
        self.fuel_cell_img = pygame.image.load(f'GUI\\assets\\fuel_cell.png')
        self.fuel_cell_img = pygame.transform.scale(self.fuel_cell_img, self.cell_size)
        self.time_cell_img = pygame.image.load(f'GUI\\assets\\time_cell.png')
        self.time_cell_img = pygame.transform.scale(self.time_cell_img, self.cell_size)
        
        self.vehicle_right_img = pygame.image.load(f'GUI\\assets\\vehicle_3.png')
        self.vehicle_right_img = pygame.transform.scale(self.vehicle_right_img, self.cell_size)
        self.vehicle_up_img = pygame.transform.rotate(self.vehicle_right_img, 90)
        self.vehicle_left_img = pygame.transform.rotate(self.vehicle_up_img, 90)
        self.vehicle_down_img = pygame.transform.rotate(self.vehicle_left_img, 90)
        
        self.vehicle_num_right_img = pygame.image.load(f'GUI\\assets\\vehicle_2.png')
        self.vehicle_num_right_img = pygame.transform.scale(self.vehicle_num_right_img, self.cell_size)
        self.vehicle_num_up_img = pygame.transform.rotate(self.vehicle_num_right_img, 90)
        self.vehicle_num_left_img = pygame.transform.rotate(self.vehicle_num_up_img, 90)
        self.vehicle_num_down_img = pygame.transform.rotate(self.vehicle_num_left_img, 90)
        
    def readMapData(self, _map_data):
        self.map_data = _map_data
    
    def showCell(self):
        screen.blit(self.empty_cell_img, (WINDOW_WIDTH * 0.08, WINDOW_HEIGHT * 0.08))
    
    def returnCellSide(self):
        return self.cell_side
    
    def showBoard(self):
        i = 0
        j = 0
        for i in range (0, self.n):
            for j in range (0, self.m):
                #show wall
                if self.map_data[j][i] == '-1':
                    screen.blit(self.wall_cell_img, (WINDOW_WIDTH * 0.08 + i*self.cell_side, WINDOW_HEIGHT * 0.08 + j*self.cell_side))
                #show gas station
                elif 'F' in self.map_data[j][i]:
                    screen.blit(self.fuel_cell_img, (WINDOW_WIDTH * 0.08 + i*self.cell_side, WINDOW_HEIGHT * 0.08 + j*self.cell_side))
                #show goal
                elif 'G' in self.map_data[j][i]:
                    if len(self.map_data[j][i]) == 1:
                        screen.blit(self.goal_cell_img, (WINDOW_WIDTH * 0.08 + i*self.cell_side, WINDOW_HEIGHT * 0.08 + j*self.cell_side))
                #show toll Booths
                elif self.map_data[j][i].isdigit() and int(self.map_data[j][i]) > 0:
                    screen.blit(self.time_cell_img, (WINDOW_WIDTH * 0.08 + i*self.cell_side, WINDOW_HEIGHT * 0.08 + j*self.cell_side))
                #show empty/street
                else:
                    screen.blit(self.empty_cell_img, (WINDOW_WIDTH * 0.08 + i*self.cell_side, WINDOW_HEIGHT * 0.08 + j*self.cell_side))
                if 'S' in self.map_data[j][i]:
                    if len(self.map_data[j][i]) == 1:
                        screen.blit(self.vehicle_right_img, (WINDOW_WIDTH * 0.08 + i*self.cell_side, WINDOW_HEIGHT * 0.08 + j*self.cell_side))
                    else:
                        screen.blit(self.vehicle_num_right_img, (WINDOW_WIDTH * 0.08 + i*self.cell_side, WINDOW_HEIGHT * 0.08 + j*self.cell_side))
        
    #def vehicle(self, x, y):
        #screen.blit(self.vehicle_right_img, (WINDOW_WIDTH * 0.08 + i*self.cell_side, WINDOW_HEIGHT * 0.08 + j*self.cell_side))


def map_UI(n, m, t, f, map_data, level):
    level = 1
    background = pygame.image.load('GUI/assets/menu_bg.png')
    screen.blit(background, (0, 0))
    #print(map_data)
    #screen.fill(BLACK_COLOR)
    M1 = Board_UI(n, m, t, f, level)
    #print(map_data)
    M1.readMapData(map_data)
    M1.showBoard()
    while True:
        #screen.fill(BLACK_COLOR)
        M1.showBoard()
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    return M1.returnCellSide()
        pygame.display.flip()

def path_UI(n, m, paths, cell_side):
    i = 0
    j = 0
    cell_size = (cell_side, cell_side)
    print(cell_side)
    vehicle_right_img = pygame.image.load(f'GUI\\assets\\vehicle_3.png')
    vehicle_right_img = pygame.transform.scale(vehicle_right_img, cell_size)
    vehicle_up_img = pygame.transform.rotate(vehicle_right_img, 90)
    vehicle_left_img = pygame.transform.rotate(vehicle_up_img, 90)
    vehicle_down_img = pygame.transform.rotate(vehicle_left_img, 90)
    
    vehicle_num_right_img = pygame.image.load(f'GUI\\assets\\vehicle_2.png')
    vehicle_num_right_img = pygame.transform.scale(vehicle_num_right_img, cell_size)
    vehicle_num_up_img = pygame.transform.rotate(vehicle_num_right_img, 90)
    vehicle_num_left_img = pygame.transform.rotate(vehicle_num_up_img, 90)
    vehicle_num_down_img = pygame.transform.rotate(vehicle_num_left_img, 90)

    count = 0
    count_veh = 0
    path = paths[0]
    len_of_n_veh = []
    for count_veh in range (0, len(paths)):
        len_of_n_veh.append( len(paths[count]) )
    count_veh = 0
    max_len_of_n_veh = max(len_of_n_veh)

    while True:
        for count in range (0, max_len_of_n_veh):
            for count_veh in range (0, len(paths)):
                for event in pygame.event.get():
                    if event.type == QUIT:
                        pygame.quit()
                        sys.exit()
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_RETURN:
                            return
                
                if len_of_n_veh[count_veh] >= count:
                    i, j = paths[count_veh][count]
                    if (i, j) in paths[count_veh]:
                        if count_veh == 0:
                            screen.blit(vehicle_right_img, (WINDOW_WIDTH * 0.08 + j*cell_side, WINDOW_HEIGHT * 0.08 + i*cell_side))
                        else:
                            screen.blit(vehicle_num_right_img, (WINDOW_WIDTH * 0.08 + j*cell_side, WINDOW_HEIGHT * 0.08 + i*cell_side))
            pygame.time.wait(200)
            pygame.display.flip()
        
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    return
        pygame.display.flip()

def menu_UI():                
    choose_option = None
    level_option = None
    menu = Menu(screen)
    credit = Credit(screen)
    level_list = LeveList(screen)
    while_loop = True
    while while_loop:
        is_up = False
        is_down = False
        
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN and is_down == False and is_up == False:
                    is_down = True
                if event.key == pygame.K_UP and is_up == False and is_down == False:
                    is_up = True
                elif event.key == pygame.K_RETURN: # press Enter to choose an option
                    choose_option = menu.get_choice()
                    
        # Menu
        screen.fill((0,0,0))   

        if choose_option is None:
            menu.display_menu(is_up, is_down)
        
        if choose_option is not None:
            if choose_option == 0:
            # Them level list
                level_option = level_list.show_level_list(is_up, is_down)
                if level_option != None:
                    print(level_option)
                    return level_option
                choose_option = level_list.get_back_to()
                #while_loop = False
                #map_show(n, m, t, f, map_data, paths) #run and show map
                # map_show() #run and show map
            if choose_option == 1:
                credit.display_credit()
                choose_option = credit.get_back_to()
            if choose_option == 2:
                pygame.quit()
                sys.exit()
                
        pygame.display.flip()