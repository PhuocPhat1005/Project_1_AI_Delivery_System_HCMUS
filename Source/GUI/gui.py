import pygame, sys
import math
from pygame.locals import *
from GUI.constants import *
from GUI.text import *
from GUI.menu import *
from GUI.credit import *
from GUI.level_list import *
from GUI.ui_level_1 import *
from GUI.image import *

pygame.init()
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
title = pygame.display.set_caption('Graph run')
        
def map_UI(n, m, t, f, map_data, level, algo):
    background = pygame.image.load('GUI/assets/menu_bg.png')
    screen.blit(background, (0, 0))
    
    #print(number_of_agents)
    
    M1 = Board_UI(screen, n, m, t, f, level)
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
    I1 = Image_UI(screen, cell_side)
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
    #ui_lv_1.write_text_content(FONT_SMALL, False, BOARD_APPEEAR_WIDTH, WINDOW_HEIGHT, BOARD_APPEEAR_WIDTH, BOARD_APPEEAR_HEIGHT, '')
    
    while True:
        if is_go_path:
            for count in range (0, max_len_of_n_veh):
                for count_veh in range (0, len(line_list)):
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
                                if len(map_change[iP][jP]) == 1:
                                    I1.showStart(iP, jP, 0)
                                elif count_veh != int(map_change[iP][jP][1:]):
                                    I1.showStart(iP, jP, int(map_change[iP][jP][1:]) )
                            elif 'F' in map_change[iP][jP]:
                                I1.showGasStation(iP, jP)
                                line_list[count_veh][count-1][5] = map_change[iP][jP]
                                #I1.writeNumber(BOARD_APPEEAR_WIDTH + jP*cell_side, BOARD_APPEEAR_HEIGHT + iP*cell_side, map_change[iP][jP][1:])
                            elif 'G' in map_change[iP][jP] and type(line_list[count_veh][count-1][5]) == int and line_list[count_veh][count-1][5] != -1:
                                map_change[iP][jP] = '0'
                                I1.showEmpty(iP, jP)
                                if count_veh == 0:
                                    map_change[ line_list[count_veh][count-1][5] ][ line_list[count_veh][count-1][6] ] = "G"
                                else:
                                    map_change[ line_list[count_veh][count-1][5] ][ line_list[count_veh][count-1][6] ] = "G" + str(count_veh)
                            elif 'G' in map_change[iP][jP]:
                                if len(map_change[iP][jP]) == 1:
                                    I1.showGoal(iP, jP, 0)
                                elif count_veh != int(map_change[iP][jP][1:]):
                                    I1.showGoal(iP, jP, int(map_change[iP][jP][1:]) )
                            elif map_change[iP][jP] == '0':
                                I1.showEmpty(iP, jP)
                            elif map_change[iP][jP].isdigit() and int(map_change[iP][jP]) > 0:
                                I1.showTollBooths(iP, jP)
                                line_list[count_veh][count-1][5] = "T" + str(map_change[iP][jP])
                                #I1.writeNumber(BOARD_APPEEAR_WIDTH + jP*cell_side, BOARD_APPEEAR_HEIGHT + iP*cell_side, map_change[iP][jP])
                            if count>1:
                                iPP = line_list[count_veh][count-2][0]
                                jPP = line_list[count_veh][count-2][1]
                                if (jP == jPP and iP == iPP):
                                    iPP, jPP, kPP, _ = paths[count_veh][count-3]
                                if (j == jP and i == iP):
                                    I1.showVehicle(i, j, iPP, jPP, count_veh)
                                elif (jP == jPP+1 and i == iP+1) or (iP == iPP-1 and j == jP-1):
                                    line_list[count_veh][count-1][2] = 1
                                    #I1.drawLeftDown(iP, jP, count_veh)
                                elif (jP == jPP+1 and i == iP-1) or (iP == iPP+1 and j == jP-1):
                                    line_list[count_veh][count-1][2] = 2
                                    #I1.drawLeftUp(iP, jP, count_veh)
                                elif (jP == jPP-1 and i == iP+1) or (iP == iPP-1 and j == jP+1):
                                    line_list[count_veh][count-1][2] = 3
                                    #I1.drawRightDown(iP, jP, count_veh)
                                elif (jP == jPP-1 and i == iP-1) or (iP == iPP+1 and j == jP+1):
                                    line_list[count_veh][count-1][2] = 4
                                    #I1.drawRightUp(iP, jP, count_veh)
                                elif i == iP and iP == iPP:
                                    line_list[count_veh][count-1][2] = 5
                                    #I1.drawLineHorizontal(iP, jP, count_veh)
                                elif j == jP and jP == jPP:
                                    line_list[count_veh][count-1][2] = 6
                                    #I1.drawLineVertical(iP, jP, count_veh)
                            
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
                                    _is_show_num = str(line_list[_count_veh][_count][5])
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
                                    if 'T' in _is_show_num:
                                        I1.writeNumber(BOARD_APPEEAR_WIDTH + _i*cell_side, BOARD_APPEEAR_HEIGHT + _j*cell_side, _is_show_num[1:])
                                    if 'F' in _is_show_num:
                                        I1.writeNumber(BOARD_APPEEAR_WIDTH + _i*cell_side, BOARD_APPEEAR_HEIGHT + _j*cell_side, _is_show_num[1:])
                for _ in range (0, len(line_list)):
                    if count < len(line_list[_])-1 and count > 0:
                        _i = line_list[_][count][0]
                        _j = line_list[_][count][1]
                        _iP = line_list[_][count-1][0]
                        _jP = line_list[_][count-1][1]
                        if _ < len(line_list[count_veh]):
                            I1.showVehicle(_i, _j, _iP, _jP, _)
                    elif count >= len(line_list[_])-1:
                        _i = line_list[_][-1][0]
                        _j = line_list[_][-1][1]
                        _iP = line_list[_][-2][0]
                        _jP = line_list[_][-2][1]
                        I1.showVehicle(_i, _j, _iP, _jP, _)
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
                        # print(map_order_return)
                        
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
                        choose_level_input = ui_lv_1.get_back_to(current_state=choose_level_input)
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