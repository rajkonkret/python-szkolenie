import pygame
import sys
import random

white = (255,255,255)
black = (0,0,0)
map_size = 500
move ='x'
finish = False
new_map_2 = []
map_to = []
def change_player():
    global move
    if move =='x':
        move ='o'
    else:
        move = 'x'
    return move

def draw_lines():
    global screen_size
    pygame.draw.line(screen,black, (500//3,0),(500//3,500),10)
    pygame.draw.line(screen,black, (0,500//3),(500,500//3),10)
    pygame.draw.line(screen,black, (2*500//3,0),(500//3*2,500),10)
    pygame.draw.line(screen,black, (0,500//3*2),(500,2*500//3),10)

def draw_map(map):
    for y in range(3):
        for x in range(3):
            banner = main_Font.render(map[x][y], False,black)
            screen.blit(banner, ((x * int(map_size / 3) + int (500/9)) ,y * int(map_size /3 )))
            draw_lines()

white = (255,255,255)
black = (0,0,0)
map_size = 500

pygame.init()
screen = pygame.display.set_mode((map_size, map_size))
pygame.display.set_caption("Kółko i Krzyżyk")
#screen.blit(circle_surface, 0)
main_Font = pygame.font.SysFont('Calibri', 170)
banner_Font = pygame.font.SysFont('Calibri', 100)
map = [
    [None,None,None],
    [None,None,None],
    [None,None,None]
    ]

pygame.font.init()
screen.fill((141,141,141))
draw_map(map)

def check_the_map_ending(map):
    for y in range(3):
        for x in range(3):
            if map[x][y] is None:
                return False
    
    return True

def mouse_to_map():
    (x,y) = pygame.mouse.get_pos()
    r_c_s = int(map_size /3)
    column = get_num(r_c_s,x)
    row = get_num(r_c_s,y)
    return  column, row

def get_num(r_c_s, x):
    if x < r_c_s:
        column = 0
    elif r_c_s <= x < r_c_s * 2:
        column =1
    else:
        column =2
    return column

def check_winner(map):
    global map_to
    map_to = map.copy()
    if (map_to[1][1] is not None and map_to[0][0]==map_to[1][1] and map_to[1][1]==map_to[2][2]):
        return map_to[1][1]

    if (map_to[1][1] is not None and map_to[0][2]==map_to[1][1] and map_to[1][1]==map_to[2][0]):
        return map_to[1][1]

    for i in range(3):
        if (map_to[i][0] is not None and map_to[i][0]==map_to[i][1] and map_to[i][1]==map_to[i][2]):
            return map_to[i][0]

    for i in range(3):
        if (map_to[0][i] is not None and map_to[0][i]==map_to[1][i] and map_to[1][i]==map_to[2][i]):
            return map_to[0][i]
    return None

def computer_move(map_this): 
    global new_map_2
    temp_list = change_list(map_this)

    
    
    #new_map_2[0][1] = move
    #print(new_map_2)

    for x in range(3):
        for y in range(3):
          
          if temp_list[y][x] is None:
              temp_list[y][x]=move
              check = check_winner(temp_list)
              if  check is not None:
                  print(check)
                  print('winner computer')
                  return y,x
              print(temp_list)
              temp_list = change_list(map_this)

    temp_list = change_list(map_this)
    
    #new_map_2[0][1] = move
    #print(new_map_2)
    change_player()
    for x in range(3):
        for y in range(3):
          
          if temp_list[y][x] is None:
              temp_list[y][x]=move
              check = check_winner(temp_list)
              if  check is not None:
                  print(check)
                  print('winner ja')
                  change_player()
                  return y,x
              print(temp_list)
              temp_list = change_list(map_this)
              
            

              #if check_winner(new_map_2):
    change_player()         
        

                

                
    print(temp_list)        
    x = random.randint(0,2)
    y = random.randint(0,2)
    return x,y

def change_list(map_to_change):
    temp_list = [[None,None,None],
                 [None,None,None],
                 [None,None,None]]
    print('kopiuję listę')
    for y in range(3):
                  for x in range(3):
                      temp_list[x][y] = map_to_change[x][y]    
    return temp_list

def start_game():
    screen.fill(backgroundColor)

def end_game():
    pygame.quit()
    sys.exit()

def win_the_game():
    global finish
    mark_win = str(winner)
    
    screen.blit(banner_Font.render("Wygrał!: " + mark_win.upper(), False, white),(50, int(map_size /2) - int(map_size /10 )))
    finish = True

while True:
  
    for action in pygame.event.get():
        if action.type == pygame.QUIT:
            
            print("break")
            end_game()
        
        if not finish and action.type is pygame.MOUSEBUTTONDOWN:
            (column, row) = mouse_to_map()
        
            if map[column][row] is None:
                
                map[column][row] = move
                move = change_player()
                draw_map(map)
                winner = check_winner(map)
                
                if winner is None and check_the_map_ending(map) is False:
                    print('Ruch komputera')
                    
                    (c_column, c_row) = computer_move(map)
                   
                    while map[c_column][c_row] is not None:
                      
                        print('losuje dalej')
                        print(map)
                        (c_column, c_row) = computer_move(map)
                        

                    map[c_column][c_row] = move
                    print('Ruch komputera',c_column,' ', c_row)
                    move = change_player()
                    draw_map(map)
                    winner = check_winner(map)
                    if winner is not None:
                        win_the_game()
        

                if winner is not None:
                    win_the_game()

                if winner is None and check_the_map_ending(map):
                    banner = banner_Font.render('Remis', False, white)
                    screen.blit(banner, (int(500//3.7), 500//2 - 500//9))
                

    pygame.display.update()