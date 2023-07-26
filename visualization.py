import pygame
import sys
import pvp
import pvc    

def table_list_creator(board_size:int) -> list:
    table_list = []
    for i in range(board_size):
        row_list = []
        for j in range(board_size):
            row_list.append(0)    
        table_list.append(row_list)
    return table_list


def position_searcher(position: list, table_list: list) -> bool:
    (x, y) = position
    return table_list[x][y] == 0


def main():
    pygame.init()
    screen_size = 800
    board_size = 10
    screen = pygame.display.set_mode((screen_size, screen_size))
    pygame.display.set_caption("Noughts and Crosses Board")
    screen.fill("burlywood1")
    cell_size = screen_size // board_size
    for row in range(board_size):
        for col in range(board_size):
            x = col * cell_size
            y = row * cell_size
            pygame.draw.rect(screen,'saddle brown', (x, y, cell_size, cell_size), 1)

    table_list = table_list_creator(board_size)

    pvp = 1
    xoro = 1

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
                position = [pos_x, pos_y]
                if position_searcher(position, table_list):
                    table_list[pos_x][pos_y] = xoro
                    if pvp == 0:
                        if (win_line := pvp.winner(xoro, position, table_list)) is not False:
                            win = 1
                        if win == 0 and pvp.empty_space(table_list) is not False:
                            [pos_x, pos_y] = pvc.next_step(table_list)
                            position = [pos_x, pos_y]
                            table_list[pos_x][pos_y] = 2
                            xoro = (xoro % 2) +1
                    #if (win_line := winner(xoro, position, table_list)) is not False:
                    #    win = 1
                    xoro = (xoro % 2) +1

        for i in range(board_size):
            a = table_list[i]
            for j in range(board_size):
                b = a[j]
                if b == 1:
                    [x, y] = [i*cell_size, j*cell_size]
                    pygame.draw.line(screen, "blue", (x+10, y+10), (x+cell_size-10, y+cell_size-10), 5)
                    pygame.draw.line(screen, "blue", (x+10, y+cell_size-10), (x+cell_size-10, y+10), 5)
                elif b == 2:
                    [x, y] = [i*cell_size, j*cell_size]
                    pygame.draw.circle(screen, "red", (x+cell_size//2, y+cell_size//2), cell_size//2-5, 5)


        pygame.display.flip()

if __name__ == "__main__":
    main()
