import pygame, sys
import math
from pygame.locals import *
from GUI.constants import *
from GUI.text import *
from GUI.menu import *
from GUI.credit import *
from GUI.level_list import *
from GUI.ui_level_1 import *

pygame.init()
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
title = pygame.display.set_caption('Graph run')
BOARD_APPEEAR_WIDTH = WINDOW_WIDTH* 0.08
BOARD_APPEEAR_HEIGHT = WINDOW_HEIGHT* 0.08

class Image_UI:
    def __init__(self, _cell_side=60):
        self.background = pygame.image.load('GUI/assets/menu_bg.png')
        self.cell_side = _cell_side
        self.cell_size = (self.cell_side, self.cell_side)
        self.empty_cell_img = pygame.image.load(f'GUI\\assets\\empty_cell.png')
        self.empty_cell_img = pygame.transform.scale(self.empty_cell_img, self.cell_size)
        self.start_cell_img = pygame.image.load(f'GUI\\assets\\start_cell.png')
        self.start_cell_img = pygame.transform.scale(self.start_cell_img, self.cell_size)
        self.goal_cell_img = pygame.image.load(f'GUI\\assets\\goal_cell.png')
        self.goal_cell_img = pygame.transform.scale(self.goal_cell_img, self.cell_size)
        self.wall_cell_img = pygame.image.load(f'GUI\\assets\\wall_cell_1.png')
        self.wall_cell_img = pygame.transform.scale(self.wall_cell_img, self.cell_size)
        self.fuel_cell_img = pygame.image.load(f'GUI\\assets\\fuel_cell.png')
        self.fuel_cell_img = pygame.transform.scale(self.fuel_cell_img, self.cell_size)
        self.time_cell_img = pygame.image.load(f'GUI\\assets\\time_cell.png')
        self.time_cell_img = pygame.transform.scale(self.time_cell_img, self.cell_size)

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

        '''self.line_h_img = pygame.image.load(f'GUI\\assets\\line_3.png')
        self.line_h_img = pygame.transform.scale(self.line_h_img, self.cell_size)
        self.line_v_img = pygame.transform.rotate(self.line_h_img, 90)
        self.left_down_img = pygame.image.load(f'GUI\\assets\\L_3_left_down.png')
        self.left_down_img = pygame.transform.scale(self.left_down_img, self.cell_size)
        self.left_up_img = pygame.image.load(f'GUI\\assets\\L_3_left_up.png')
        self.left_up_img = pygame.transform.scale(self.left_up_img, self.cell_size)
        self.right_down_img = pygame.image.load(f'GUI\\assets\\L_3_right_down.png')
        self.right_down_img = pygame.transform.scale(self.right_down_img, self.cell_size)
        self.right_up_img = pygame.image.load(f'GUI\\assets\\L_3_right_up.png')
        self.right_up_img = pygame.transform.scale(self.right_up_img, self.cell_size)
        
        self.vehicle_right_img = pygame.image.load(f'GUI\\assets\\vehicle_3.png')
        self.vehicle_right_img = pygame.transform.scale(self.vehicle_right_img, self.cell_size)
        self.vehicle_up_img = pygame.transform.rotate(self.vehicle_right_img, 90)
        self.vehicle_left_img = pygame.transform.rotate(self.vehicle_up_img, 90)
        self.vehicle_down_img = pygame.transform.rotate(self.vehicle_left_img, 90)
        
        self.line_h_num_img = pygame.image.load(f'GUI\\assets\\line_2.png')
        self.line_h_num_img = pygame.transform.scale(self.line_h_num_img, self.cell_size)
        self.line_v_num_img = pygame.transform.rotate(self.line_h_num_img, 90)
        self.left_down_num_img = pygame.image.load(f'GUI\\assets\\L_2_left_down.png')
        self.left_down_num_img = pygame.transform.scale(self.left_down_num_img, self.cell_size)
        self.left_up_num_img = pygame.image.load(f'GUI\\assets\\L_2_left_up.png')
        self.left_up_num_img = pygame.transform.scale(self.left_up_num_img, self.cell_size)
        self.right_down_num_img = pygame.image.load(f'GUI\\assets\\L_2_right_down.png')
        self.right_down_num_img = pygame.transform.scale(self.right_down_num_img, self.cell_size)
        self.right_up_num_img = pygame.image.load(f'GUI\\assets\\L_2_right_up.png')
        self.right_up_num_img = pygame.transform.scale(self.right_up_num_img, self.cell_size)

        self.vehicle_num_right_img = pygame.image.load(f'GUI\\assets\\vehicle_2.png')
        self.vehicle_num_right_img = pygame.transform.scale(self.vehicle_num_right_img, self.cell_size)
        self.vehicle_num_up_img = pygame.transform.rotate(self.vehicle_num_right_img, 90)
        self.vehicle_num_left_img = pygame.transform.rotate(self.vehicle_num_up_img, 90)
        self.vehicle_num_down_img = pygame.transform.rotate(self.vehicle_num_left_img, 90)'''
    
    def showEmpty(self, j, i):
        screen.blit(self.empty_cell_img, (BOARD_APPEEAR_WIDTH + i*self.cell_side, BOARD_APPEEAR_HEIGHT + j*self.cell_side))
    def showWall(self, j, i):
        screen.blit(self.wall_cell_img, (BOARD_APPEEAR_WIDTH + i*self.cell_side, BOARD_APPEEAR_HEIGHT + j*self.cell_side))
    def showStart(self, j, i):
        screen.blit(self.start_cell_img, (BOARD_APPEEAR_WIDTH + i*self.cell_side, BOARD_APPEEAR_HEIGHT + j*self.cell_side))
    def showGoal(self, j, i):
        screen.blit(self.goal_cell_img, (BOARD_APPEEAR_WIDTH + i*self.cell_side, BOARD_APPEEAR_HEIGHT + j*self.cell_side))
    def showTollBooths(self, j, i):
        screen.blit(self.time_cell_img, (BOARD_APPEEAR_WIDTH + i*self.cell_side, BOARD_APPEEAR_HEIGHT + j*self.cell_side))
    def showGasStation(self, j, i):
        screen.blit(self.fuel_cell_img, (BOARD_APPEEAR_WIDTH + i*self.cell_side, BOARD_APPEEAR_HEIGHT + j*self.cell_side))
    
    
    def showVehicle(self, j, i, jP, iP, count_veh):
        vehicle_img = self.vehicle_right_img[count_veh]
        if i == iP-1:
            vehicle_img = self.vehicle_left_img[count_veh]
        elif j == jP+1:
            vehicle_img = self.vehicle_down_img[count_veh]
        elif j == jP-1:
            vehicle_img = self.vehicle_up_img[count_veh]
        screen.blit(vehicle_img, (BOARD_APPEEAR_WIDTH + i*self.cell_side, BOARD_APPEEAR_HEIGHT + j*self.cell_side))
    
    def drawLeftDown(self, j, i, count_veh):
        screen.blit(self.left_down_img[count_veh], (BOARD_APPEEAR_WIDTH + i*self.cell_side, BOARD_APPEEAR_HEIGHT + j*self.cell_side))

    def drawRightDown(self, j, i, count_veh):
        screen.blit(self.right_down_img[count_veh], (BOARD_APPEEAR_WIDTH + i*self.cell_side, BOARD_APPEEAR_HEIGHT + j*self.cell_side))
        
    def drawRightUp(self, j, i, count_veh):
        screen.blit(self.right_up_img[count_veh], (BOARD_APPEEAR_WIDTH + i*self.cell_side, BOARD_APPEEAR_HEIGHT + j*self.cell_side))
            
    def drawLeftUp(self, j, i, count_veh):
        screen.blit(self.left_up_img[count_veh], (BOARD_APPEEAR_WIDTH + i*self.cell_side, BOARD_APPEEAR_HEIGHT + j*self.cell_side))
        

    def drawLineHorizontal(self, j, i, count_veh):
        screen.blit(self.line_h_img[count_veh], (BOARD_APPEEAR_WIDTH + i*self.cell_side, BOARD_APPEEAR_HEIGHT + j*self.cell_side))
    
    def drawLineVertical(self, j, i, count_veh):
        screen.blit(self.line_v_img[count_veh], (BOARD_APPEEAR_WIDTH + i*self.cell_side, BOARD_APPEEAR_HEIGHT + j*self.cell_side))

class Board_UI(Image_UI):
    def __init__(self, _n, _m, _t, _f, _level):
        super().__init__(60)
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
        screen.blit(self.empty_cell_img, (BOARD_APPEEAR_WIDTH, BOARD_APPEEAR_HEIGHT))
    
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
                #show goal
                elif 'G' in self.map_data[j][i]:
                    self.showGoal(j, i)
                #show toll booths
                elif self.map_data[j][i].isdigit() and int(self.map_data[j][i]) > 0:
                    self.showTollBooths(j, i)
                #show empty/street
                else:
                    self.showEmpty(j, i)
                if 'S' in self.map_data[j][i]:
                    self.showStart(j, i)
                    if len(self.map_data[j][i]) == 1:
                        screen.blit(self.vehicle_right_img[0], (BOARD_APPEEAR_WIDTH + i*self.cell_side, BOARD_APPEEAR_HEIGHT + j*self.cell_side))
                    else:
                        num = int(self.map_data[j][i][1:])
                        screen.blit(self.vehicle_right_img[num], (BOARD_APPEEAR_WIDTH + i*self.cell_side, BOARD_APPEEAR_HEIGHT + j*self.cell_side))
        
def map_UI(n, m, t, f, map_data, level, algo):
    background = pygame.image.load('GUI/assets/menu_bg.png')
    screen.blit(background, (0, 0))
    
    M1 = Board_UI(n, m, t, f, level)
    M1.readMapData(map_data)
    M1.showBoard()
    
    if level == 1:
        ui_lv_1 = UI_Level_1(screen)
        ui_lv_1.draw_ui(750, 100, 'search algorithm:')
        ui_lv_1.draw_ui(900, 200, algo)
    elif level == 2:
        ui_lv_1 = UI_Level_1(screen)
        ui_lv_1.draw_ui(750, 100, 'Time:')
        ui_lv_1.draw_ui(950, 100, str(t) + 's')
    elif level == 3:
        ui_lv_1 = UI_Level_1(screen)
        ui_lv_1.draw_ui(750, 100, 'Time:')
        ui_lv_1.draw_ui(950, 100, str(t) + 's')
        ui_lv_1.draw_ui(750, 200, 'Fuel:')
        ui_lv_1.draw_ui(950, 200, str(f))
    elif level==4:
        ui_lv_1 = UI_Level_1(screen)
        ui_lv_1.draw_ui(750, 100, 'Time:')
        ui_lv_1.draw_ui(950, 100, str(t) + 's')
            
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    return M1.returnCellSide()
        pygame.display.flip()

def path_UI(n, m, t, f, map_data, paths, cell_side, number_of_agents=0):
    print('Time:', t)
    I1 = Image_UI(cell_side)
    i = 0
    j = 0
    map_change = map_data.copy()
    cell_size = (cell_side, cell_side)
    ui_lv_1 = UI_Level_1(screen)
    prev_time = 0

    is_go_path = True
    count = 0
    count_veh = 0
    len_of_n_veh = []
    for count_veh in range (0, len(paths)):
        len_of_n_veh.append( len(paths[count_veh]) )
    count = 0
    count_veh = 0

    max_len_of_n_veh = 0
    min_len_of_n_veh = 0
    if len(paths) != 0:
        max_len_of_n_veh = max(len_of_n_veh)
        min_len_of_n_veh = min(len_of_n_veh)
    
    print(paths)
    line_list = [[(0,0,0) for _ in range(1)] for _ in range(len(paths))]
    for count_veh in range (len(paths)):
        for count in range (len(paths[count_veh])):
            line_list[count_veh].append( [paths[count_veh][count][0] , paths[count_veh][count][1] , 0 , paths[count_veh][count][2] , paths[count_veh][count][3] , -1 , -1] )
    count = 0
    count_veh = 0
    for count_veh in range (len(paths)):
        line_list[count_veh].pop(0)
    count = 1
    count_veh = 0
    for count_veh in range (len(line_list)):
        for count in range (len(line_list[count_veh]) - 1):
            if line_list[count_veh][count][0] == line_list[count_veh][count-1][0] and line_list[count_veh][count][1] == paths[count_veh][count-1][1]:
                del line_list[count_veh][count]
                _count = 0
                for _count in range (len(line_list[count_veh]) - 1):
                    if line_list[count_veh][_count][0] == line_list[count_veh][_count-1][0] and line_list[count_veh][_count][1] == paths[count_veh][_count-1][1]:
                        line_list[count_veh][count-1][5] = line_list[count_veh][_count][0]
                        line_list[count_veh][count-1][6] = line_list[count_veh][_count][1]
                    else:
                        line_list[count_veh][count-1][5] = line_list[count_veh][-1][0]
                        line_list[count_veh][count-1][6] = line_list[count_veh][-1][1]
                count = 0
    count = 0
    count_veh = 0
    
    if all(ele == [] for ele in paths):
        ui_lv_1.draw_ui(750, 20, 'NO PATH FOUND')
    
    while True:
        if is_go_path:
            for count in range (0, max_len_of_n_veh):
                for count_veh in range (0, len(paths)):
                    for event in pygame.event.get():
                        if event.type == QUIT:
                            pygame.quit()
                            sys.exit()
                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_RETURN:
                                return
                    
                    #if len_of_n_veh[count_veh] >= count:
                    if count < len(line_list[count_veh]) and count > 0:
                        i = line_list[count_veh][count][0]
                        j = line_list[count_veh][count][1]
                        k = line_list[count_veh][count][3]
                        l = line_list[count_veh][count][4]
                        
                        if t and k != float('inf'):
                            pygame.draw.rect(screen, BACKGROUND_COLOR, pygame.Rect(950, 100, 500, 50))
                            ui_lv_1.draw_ui(950, 100, str(int(t - prev_time)) + 's')
                            prev_time = k
                        if f and l != float('inf'):
                            pygame.draw.rect(screen, BACKGROUND_COLOR, pygame.Rect(950, 200 + count_veh * 50, 500, 50))
                            ui_lv_1.draw_ui(950,  200 + count_veh * 50, str(int(l)))
                            
                            for idx in range(number_of_agents):
                                pygame.draw.rect(screen, BACKGROUND_COLOR, pygame.Rect(950, 200 + idx * 50, 500, 50))
                                ui_lv_1.draw_ui(750, 200 + idx * 50, 'Fuel:')
                                ui_lv_1.draw_ui(950, 200 + idx * 50, str(l))
                        #P: past | PP: past past
                        if count>0:
                            iP = line_list[count_veh][count-1][0]
                            jP = line_list[count_veh][count-1][1]
                        
                            #if [i, j, k, l] in line_list[count_veh]:
                            
                            if 'S' in map_change[iP][jP]:
                                I1.showStart(iP, jP)
                            elif 'F' in map_change[iP][jP]:
                                I1.showGasStation(iP, jP)
                            elif 'G' in map_change[iP][jP] and line_list[count_veh][count-1][5] != -1:
                                map_change[iP][jP] = '0'
                                I1.showEmpty(iP, jP)
                                if count_veh == 0:
                                    map_change[ line_list[count_veh][count-1][5] ][ line_list[count_veh][count-1][6] ] = "G"
                                else:
                                    map_change[ line_list[count_veh][count-1][5] ][ line_list[count_veh][count-1][6] ] = "G" + str(count_veh)
                                I1.showGoal( line_list[count_veh][count-1][5] , line_list[count_veh][count-1][6] )
                            elif map_change[iP][jP] == '0':
                                I1.showEmpty(iP, jP)
                            elif map_change[iP][jP].isdigit() and int(map_change[iP][jP]) > 0:
                                I1.showTollBooths(iP, jP)
                            if count>1:
                                iPP = line_list[count_veh][count-2][0]
                                jPP = line_list[count_veh][count-2][1]
                                if (jP == jPP and iP == iPP):
                                    iPP, jPP, kPP, _ = paths[count_veh][count-3]
                                if (j == jP and i == iP):
                                    I1.showVehicle(i, j, iPP, jPP, count_veh)
                                elif (jP == jPP+1 and i == iP+1) or (iP == iPP-1 and j == jP-1):
                                    line_list[count_veh][count-1][2] = 1
                                    I1.drawLeftDown(iP, jP, count_veh)
                                elif (jP == jPP+1 and i == iP-1) or (iP == iPP+1 and j == jP-1):
                                    line_list[count_veh][count-1][2] = 2
                                    I1.drawLeftUp(iP, jP, count_veh)
                                elif (jP == jPP-1 and i == iP+1) or (iP == iPP-1 and j == jP+1):
                                    line_list[count_veh][count-1][2] = 3
                                    I1.drawRightDown(iP, jP, count_veh)
                                elif (jP == jPP-1 and i == iP-1) or (iP == iPP+1 and j == jP+1):
                                    line_list[count_veh][count-1][2] = 4
                                    I1.drawRightUp(iP, jP, count_veh)
                                elif i == iP and iP == iPP:
                                    line_list[count_veh][count-1][2] = 5
                                    I1.drawLineHorizontal(iP, jP, count_veh)
                                elif j == jP and jP == jPP:
                                    line_list[count_veh][count-1][2] = 6
                                    I1.drawLineVertical(iP, jP, count_veh)
                            
                        #I1.showVehicle(i, j, iP, jP, count_veh)
                        _count_veh = 0
                        _count = 0
                        for _count in range (count+1):
                            for _count_veh in range (len(line_list)):
                                if _count >= len(line_list[_count_veh]):
                                    pass
                                else:
                                    _j = line_list[_count_veh][_count][0]
                                    _i = line_list[_count_veh][_count][1]
                                    _type = line_list[_count_veh][_count][2]
                                    if _type == 1:
                                        I1.drawLeftDown(_j, _i, _count_veh)
                                    elif _type == 2:
                                        I1.drawLeftUp(_j, _i, _count_veh)
                                    elif _type == 3:
                                        I1.drawRightDown(_j, _i, _count_veh)
                                    elif _type == 4:
                                        I1.drawRightUp(_j, _i, _count_veh)
                                    elif _type == 5:
                                        I1.drawLineHorizontal(_j, _i, _count_veh)
                                    elif _type == 6:
                                        I1.drawLineVertical(_j, _i, _count_veh)
                        for _ in range (count_veh + 1):
                            if _ < len(line_list[count_veh]):
                                I1.showVehicle(i, j, iP, jP, count_veh)
                        #pygame.display.flip()
                if len(line_list) == 1:
                    pygame.time.wait(200)
                else:
                    pygame.time.wait(200)
                pygame.display.flip()
            is_go_path = False
        
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
    menu = Menu(screen)
    credit = Credit(screen)
    level_list = LeveList(screen)

    level_option = 0
    search_option = ""

    choose_level_result = None
    ui_lv_1 = UI_Level_1(screen)
    option_result_in_lv_1 = None
    
    map_order_return = None
    choose_level_input = None

    while True:
        is_up = False
        is_down = False
        is_left = False
        is_enter = False
        
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN and is_down == False and is_up == False and is_left == False and is_enter == False:
                    is_down = True
                elif event.key == pygame.K_UP and is_down == False and is_up == False and is_left == False and is_enter == False:
                    is_up = True
                elif event.key == pygame.K_LEFT and is_down == False and is_up == False and is_left == False and is_enter == False:
                    is_left = True
                elif event.key == pygame.K_RETURN and is_down == False and is_up == False and is_left == False and is_enter == False:
                    is_enter = True
        # Menu
        screen.fill((0,0,0))   
        
        if choose_option is None:
            menu.display_menu(is_up, is_down, is_enter)
            choose_option = menu.get_choose_option()
        else:
            if choose_option == 0:
                
                # Them level list, choose level
                if choose_level_result is None:
                    level_list.show_level_list(is_up, is_down, is_left, is_enter)
                    choose_level_result = level_list.get_option_result()
                elif choose_level_result == 0: # hien ra cac option cua level 1
                    
                    if choose_level_input is None: # hien ra level cua file input 1 -> 5, choose input level
                        ui_lv_1.show_level_inputs(choose_level_result, is_up, is_down, is_left, is_enter)
                        choose_level_input = ui_lv_1.get_option_result()
                    else: # neu chon bat ky input 1 -> 5
                        map_order_return = choose_level_input + 1
                        
                        if option_result_in_lv_1 is None: #  hien ra cac thuat toan BFS, DFS,... cua level input duoc chon
                            ui_lv_1.show_level_list(is_up, is_down, is_left, is_enter)
                            option_result_in_lv_1 = ui_lv_1.get_option_result()
                        else:
                            if option_result_in_lv_1 == 0: # option BFS cua level 1
                                algo = 'BFS'
                                return map_order_return, choose_level_result, algo
                            elif option_result_in_lv_1 == 1: # option DFS cua level 1
                                algo = 'DFS'
                                return map_order_return, choose_level_result, algo
                            elif option_result_in_lv_1 == 2: # option UCS cua level 1
                                algo = 'UCS'
                                return map_order_return, choose_level_result, algo
                            elif option_result_in_lv_1 == 3: # option GBFS cua level 1
                                algo = 'GBFS'
                                return map_order_return, choose_level_result, algo
                            elif option_result_in_lv_1 == 4: # option A* cua level 1
                                algo = 'A*'
                                return map_order_return, choose_level_result, algo
                            option_result_in_lv_1 = ui_lv_1.get_back_to()
                        choose_level_input = ui_lv_1.get_back_to()
                    choose_level_result = ui_lv_1.get_back_to()
                elif choose_level_result >= 1: # option level 2->4
                    if choose_level_input is None: # hien ra level cua file input 1 -> 5, choose input level
                        ui_lv_1.show_level_inputs(choose_level_result, is_up, is_down, is_left, is_enter)
                        choose_level_input = ui_lv_1.get_option_result()
                    else:
                        map_order_return = choose_level_input + 1
                        algo = "algo"
                        return map_order_return, choose_level_result, algo
                    choose_level_result = ui_lv_1.get_back_to(current_state=choose_level_result)

                choose_option = level_list.get_back_to()
                
            if choose_option == 1:
                credit.display_credit(is_left)
                choose_option = credit.get_back_to()
            if choose_option == 2:
                pygame.quit()
                sys.exit()
                
        pygame.display.flip()