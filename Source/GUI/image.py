import pygame
import math
from pygame.locals import *
from GUI.constants import *
from GUI.text import *
from GUI.menu import *
from GUI.credit import *
from GUI.level_list import *
from GUI.ui_level_1 import *

class Image_UI:
    def __init__(self, _screen, _cell_side=60):
        self.screen = _screen
        self.background = pygame.image.load('GUI/assets/menu_bg.png')
        self.cell_side = _cell_side
        self.cell_size = (self.cell_side, self.cell_side)
        self.empty_cell_img = pygame.image.load(f'GUI\\assets\\empty_cell.png')
        self.empty_cell_img = pygame.transform.scale(self.empty_cell_img, self.cell_size)
        #self.start_cell_img = pygame.image.load(f'GUI\\assets\\start_cell.png')
        #self.start_cell_img = pygame.transform.scale(self.start_cell_img, self.cell_size)
        self.wall_cell_img = pygame.image.load(f'GUI\\assets\\wall_cell_1.png')
        self.wall_cell_img = pygame.transform.scale(self.wall_cell_img, self.cell_size)
        self.fuel_cell_img = pygame.image.load(f'GUI\\assets\\fuel_cell.png')
        self.fuel_cell_img = pygame.transform.scale(self.fuel_cell_img, self.cell_size)
        self.time_cell_img = pygame.image.load(f'GUI\\assets\\time_cell.png')
        self.time_cell_img = pygame.transform.scale(self.time_cell_img, self.cell_size)

        self.start_cell_img = []
        self.goal_cell_img = []
        self.vehicle_right_img = []
        self.vehicle_up_img = []
        self.vehicle_left_img = []
        self.vehicle_down_img = []
        self.line_h_img = []
        self.line_h_img = []
        self.line_v_img = []
        self.left_down_img = []
        self.left_down_img = []
        self.left_up_img = []
        self.left_up_img = []
        self.right_down_img = []
        self.right_down_img = []
        self.right_up_img = []
        self.right_up_img = []
        count_img = 0
        for count_img in range (10):
            self.start_cell_img.append( pygame.image.load(f'GUI\\assets\\agent_{count_img}\\start_cell.png') )
            self.start_cell_img[count_img] = pygame.transform.scale(self.start_cell_img[count_img], self.cell_size)
            self.goal_cell_img.append( pygame.image.load(f'GUI\\assets\\agent_{count_img}\\goal_cell.png') )
            self.goal_cell_img[count_img] = pygame.transform.scale(self.goal_cell_img[count_img], self.cell_size)

            self.vehicle_right_img.append( pygame.image.load(f'GUI\\assets\\agent_{count_img}\\vehicle.png') )
            self.vehicle_right_img[count_img] = pygame.transform.scale(self.vehicle_right_img[count_img], self.cell_size)
            self.vehicle_up_img.append( pygame.transform.rotate(self.vehicle_right_img[count_img], 90) )
            self.vehicle_left_img.append( pygame.transform.rotate(self.vehicle_up_img[count_img], 90) )
            self.vehicle_down_img.append( pygame.transform.rotate(self.vehicle_left_img[count_img], 90) )
            self.line_h_img.append( pygame.image.load(f'GUI\\assets\\agent_{count_img}\\line.png') )
            self.line_h_img[count_img] = pygame.transform.scale(self.line_h_img[count_img], self.cell_size)
            self.line_v_img.append( pygame.transform.rotate(self.line_h_img[count_img], 90) )

            self.left_down_img.append( pygame.image.load(f'GUI\\assets\\agent_{count_img}\\L_left_down.png') )
            self.left_down_img[count_img] = pygame.transform.scale(self.left_down_img[count_img], self.cell_size)

            self.left_up_img.append( pygame.image.load(f'GUI\\assets\\agent_{count_img}\\L_left_up.png') )
            self.left_up_img[count_img] = pygame.transform.scale(self.left_up_img[count_img], self.cell_size)

            self.right_down_img.append( pygame.image.load(f'GUI\\assets\\agent_{count_img}\\L_right_down.png') )
            self.right_down_img[count_img] = pygame.transform.scale(self.right_down_img[count_img], self.cell_size)

            self.right_up_img.append( pygame.image.load(f'GUI\\assets\\agent_{count_img}\\L_right_up.png') )
            self.right_up_img[count_img] = pygame.transform.scale(self.right_up_img[count_img], self.cell_size)
    
    def writeNumber(self, pos_x=0, pos_y=0, content=''):
        font_size = FONT_MEDIUM
        if self.cell_side > 60:
            font_size = FONT_LARGE
        elif self.cell_side == 60:
            font_size = FONT_MEDIUM+5
        else:
            font_size = FONT_SMALL
        text_obj = Text_Display(content, font_size=font_size, text_color=DARK_GREEN_COLOR)
        text_content = text_obj.show_text()
        text_pos = (pos_x, pos_y)
        
        self.screen.blit(text_content, text_pos)
            
    def showEmpty(self, j, i):
        self.screen.blit(self.empty_cell_img, (BOARD_APPEEAR_WIDTH + i*self.cell_side, BOARD_APPEEAR_HEIGHT + j*self.cell_side))
    def showWall(self, j, i):
        self.screen.blit(self.wall_cell_img, (BOARD_APPEEAR_WIDTH + i*self.cell_side, BOARD_APPEEAR_HEIGHT + j*self.cell_side))
    def showStart(self, j, i, count_veh):
        self.screen.blit(self.start_cell_img[count_veh], (BOARD_APPEEAR_WIDTH + i*self.cell_side, BOARD_APPEEAR_HEIGHT + j*self.cell_side))
    def showGoal(self, j, i, count_veh):
        self.screen.blit(self.goal_cell_img[count_veh], (BOARD_APPEEAR_WIDTH + i*self.cell_side, BOARD_APPEEAR_HEIGHT + j*self.cell_side))
    def showTollBooths(self, j, i):
        self.screen.blit(self.time_cell_img, (BOARD_APPEEAR_WIDTH + i*self.cell_side, BOARD_APPEEAR_HEIGHT + j*self.cell_side))
    def showGasStation(self, j, i):
        self.screen.blit(self.fuel_cell_img, (BOARD_APPEEAR_WIDTH + i*self.cell_side, BOARD_APPEEAR_HEIGHT + j*self.cell_side))
    
    
    def showVehicle(self, j, i, jP, iP, count_veh):
        vehicle_img = self.vehicle_right_img[count_veh]
        if i == iP-1:
            vehicle_img = self.vehicle_left_img[count_veh]
        elif j == jP+1:
            vehicle_img = self.vehicle_down_img[count_veh]
        elif j == jP-1:
            vehicle_img = self.vehicle_up_img[count_veh]
        self.screen.blit(vehicle_img, (BOARD_APPEEAR_WIDTH + i*self.cell_side, BOARD_APPEEAR_HEIGHT + j*self.cell_side))
    
    def drawLeftDown(self, j, i, count_veh):
        self.screen.blit(self.left_down_img[count_veh], (BOARD_APPEEAR_WIDTH + i*self.cell_side, BOARD_APPEEAR_HEIGHT + j*self.cell_side))

    def drawRightDown(self, j, i, count_veh):
        self.screen.blit(self.right_down_img[count_veh], (BOARD_APPEEAR_WIDTH + i*self.cell_side, BOARD_APPEEAR_HEIGHT + j*self.cell_side))
        
    def drawRightUp(self, j, i, count_veh):
        self.screen.blit(self.right_up_img[count_veh], (BOARD_APPEEAR_WIDTH + i*self.cell_side, BOARD_APPEEAR_HEIGHT + j*self.cell_side))
            
    def drawLeftUp(self, j, i, count_veh):
        self.screen.blit(self.left_up_img[count_veh], (BOARD_APPEEAR_WIDTH + i*self.cell_side, BOARD_APPEEAR_HEIGHT + j*self.cell_side))
        

    def drawLineHorizontal(self, j, i, count_veh):
        self.screen.blit(self.line_h_img[count_veh], (BOARD_APPEEAR_WIDTH + i*self.cell_side, BOARD_APPEEAR_HEIGHT + j*self.cell_side))
    
    def drawLineVertical(self, j, i, count_veh):
        self.screen.blit(self.line_v_img[count_veh], (BOARD_APPEEAR_WIDTH + i*self.cell_side, BOARD_APPEEAR_HEIGHT + j*self.cell_side))

class Board_UI(Image_UI):
    def __init__(self, _screen, _n, _m, _t, _f, _level):
        cell_side = 60
        if max(_n, _m) <= 5:
            cell_side = 120
        elif max(_n, _m) <= 10:
            cell_side = 60
        elif max(_n, _m) <= 15:
            cell_side = 45
        elif max(_n, _m) <= 20:
            cell_side = 30
        else:
            cell_side = 20
        super().__init__(_screen, cell_side)
        self.n = _n
        self.m = _m
        self.t = _t
        self.f = _f
        self.map_data = []
        self.cells = []
        self.time = 0
        self.vehicle = []
        goals = []
        self.fuel_stations = []
        self.level = _level
        
    def readMapData(self, _map_data):
        self.map_data = _map_data
    
    def showCell(self):
        self.screen.blit(self.empty_cell_img, (BOARD_APPEEAR_WIDTH, BOARD_APPEEAR_HEIGHT))
    
    def returnCellSide(self):
        return self.cell_side
    
    def showBoard(self):
        i = 0
        j = 0
        for i in range (0, self.n):
            for j in range (0, self.m):
                #show wall
                if self.map_data[j][i] == '-1':
                    self.showWall(j, i)
                #show gas station
                elif 'F' in self.map_data[j][i]:
                    self.showGasStation(j, i)
                    self.writeNumber(pos_x=BOARD_APPEEAR_WIDTH + i*self.cell_side, pos_y=BOARD_APPEEAR_HEIGHT + j*self.cell_side, content=self.map_data[j][i][1:])
                #show goal
                elif 'G' in self.map_data[j][i]:
                    if len(self.map_data[j][i]) == 1:
                        self.showGoal(j, i, 0)
                    else:
                        num = int(self.map_data[j][i][1:])
                        self.showGoal(j, i, num)
                #show toll booths
                elif self.map_data[j][i].isdigit() and int(self.map_data[j][i]) > 0:
                    self.showTollBooths(j, i)
                    self.writeNumber(pos_x=BOARD_APPEEAR_WIDTH + i*self.cell_side, pos_y=BOARD_APPEEAR_HEIGHT + j*self.cell_side, content=self.map_data[j][i])
                #show empty/street
                else:
                    self.showEmpty(j, i)
                if 'S' in self.map_data[j][i]:
                    if len(self.map_data[j][i]) == 1:
                        self.showStart(j, i, 0)
                        self.showVehicle(j, i, -2, -2, 0)
                    else:
                        num = int(self.map_data[j][i][1:])
                        self.showStart(j, i, num)
                        self.showVehicle(j, i, -2, -2, num)