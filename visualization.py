import pygame
import numpy as np
import sys
import time
import pvsp
import pvsc    

def table_list_creator(board_size:int) -> list:
    table_list = np.full((board_size, board_size), ' ', dtype=str)
    return table_list


def position_searcher(position: list, table_list: list) -> bool:
    (x, y) = position
    return table_list[x, y] == ' '


def main():

    pygame.init()

    screen_size = 800
    board_size = 10

    screen = pygame.display.set_mode((screen_size, screen_size))
    pygame.display.set_caption("Noughts and Crosses Board")
    font = pygame.font.Font(None, 36)
    button_width, button_height = 150, 50

    def draw_button(x, y, text):
        pygame.draw.rect(screen,"saddle brown",(x,y,button_width, button_height))
        text_surface = font.render(text, True, "black")
        text_rect = text_surface.get_rect(center=(x + button_width // 2, y + button_height // 2))
        screen.blit(text_surface, text_rect)

    pvp = -1

    while pvp == -1:
        screen.fill("burlywood1")
        draw_button(50, 70, "P vs. P")
        draw_button(580, 70, "P vs. C")
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                if 50 <= x <= 50 + button_width and 70 <= y <= 70 + button_height:
                    pvp = 1
                elif 580 <= x <= 580 + button_width and 70 <= y <= 70 + button_height:
                    pvp = 0
    time.sleep(0.3)

    screen.fill("burlywood1")
    cell_size = screen_size // board_size
    for row in range(board_size):
        for col in range(board_size):
            x = col * cell_size
            y = row * cell_size
            pygame.draw.rect(screen,'saddle brown', (x, y, cell_size, cell_size), 1)

    table_list = table_list_creator(board_size)

    xoro = 1
    win = 0

    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                click_location = event.dict["pos"]
                [x, y] = click_location
                pos_x = x // cell_size
                pos_y = y // cell_size
                position = [pos_y, pos_x]
                if position_searcher(position, table_list):
                    table_list[pos_y, pos_x] = xoro
                    if pvp == 0:
                        if (win_line := pvsp.winner(str(xoro), table_list, cell_size)) is not False:
                            win = 1
                        if win == 0:
                            [pos_x, pos_y] = pvsc.next_step(table_list, str((xoro % 2) +1), str(xoro))
                            table_list[pos_y, pos_x] = 2
                            xoro = (xoro % 2) +1
                    if (win_line := pvsp.winner(str(xoro), table_list, cell_size)) is not False:
                        win = 1
                    xoro = (xoro % 2) +1

        for i in range(board_size):
            for j in range(board_size):
                b = table_list[j, i]
                if b == '1':
                    [x, y] = [i*cell_size, j*cell_size]
                    pygame.draw.line(screen, "blue", (x+10, y+10), (x+cell_size-10, y+cell_size-10), 5)
                    pygame.draw.line(screen, "blue", (x+10, y+cell_size-10), (x+cell_size-10, y+10), 5)
                elif b == '2':
                    [x, y] = [i*cell_size, j*cell_size]
                    pygame.draw.circle(screen, "red", (x+cell_size//2, y+cell_size//2), cell_size//2-5, 5)

        if win == 1:
            [[x1, y1], [x2, y2]] = win_line
            pygame.draw.line(screen, "red", (x1, y1), (x2, y2), 10)
            pygame.display.flip()
            time.sleep(2)
            pygame.quit()
            sys.exit()

        pygame.display.flip()

if __name__ == "__main__":
    main()
