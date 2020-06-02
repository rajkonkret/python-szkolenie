import pygame
import sys

white = (255,255,255)
black = (0,0,0)
map_size = 500

def draw_lines():
    global screen_size
    pygame.draw.line(screen,black, (500/3,0),(500/3,500),10)
    pygame.draw.line(screen,black, (0,500/3),(500,500/3),10)
    pygame.draw.line(screen,black, (2*500/3,0),(500/3*2,500),10)
    pygame.draw.line(screen,black, (0,500/3*2),(500,2*500/3),10)

def draw_map(map):
    for y in range(3):
        for x in range(3):
            banner = main_Font.render(map[x][y], False,black)
            screen.blit(banner, ((y * int(map_size / 3) + int (500/9)) ,x * int(map_size /3 )))

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
    ['x','x','x'],
    ['x','o','x'],
    ['x','x','x']
]

pygame.font.init()
screen.fill((141,141,141))
draw_lines()
pygame.draw.circle(screen, (4,4,4), (100,100), 40,1)
draw_map(map)


def start_game():
    screen.fill(backgroundColor)

def end_game():
    pygame.quit()
    sys.exit()



def draw_lines():
    pygame.draw.line(screen,black, (500/3,0),(500/3,300),10)



while True:
    for action in pygame.event.get():
        if action.type == pygame.QUIT:
            
            print("break")
            end_game()

    pygame.display.update()