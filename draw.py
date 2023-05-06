import pygame
from config import *
from drawing.pieces import *
from drawing.board import *

def change_state_white_king(new_pos):
    wk.moved = True
    wk.x, wk.y = new_pos

def change_state_black_king(new_pos):
    bk.moved = True
    bk.x, bk.y = new_pos

def draw_board(state):
    screen = pygame.display.set_mode(screen_size)
    screen.fill(screen_color)
    block_size = screen_size[0] / 8
    for i in range(8):
        for j in range(8):
            if (i + j) % 2 == 0:
                continue
            pygame.draw.rect(screen, black_block, (i * block_size, j * block_size, block_size, block_size))

    for i in range(8):
        for j in range(8):
            if state.board[i][j] == 'r':
                wr.draw(screen, i, j)
            elif state.board[i][j] == 'n':
                wn.draw(screen, i, j)
            elif state.board[i][j] == 'b':
                wb.draw(screen, i, j)
            elif state.board[i][j] == 'k':
                wk.draw(screen, i, j)
            elif state.board[i][j] == 'q':
                wq.draw(screen, i, j)
            elif state.board[i][j] == 'p':
                wp.draw(screen, i, j)
            elif state.board[i][j] == 'R':
                br.draw(screen, i, j)
            elif state.board[i][j] == 'N':
                bn.draw(screen, i, j)
            elif state.board[i][j] == 'B':
                bb.draw(screen, i, j)
            elif state.board[i][j] == 'K':
                bk.draw(screen, i, j)
            elif state.board[i][j] == 'Q':
                bq.draw(screen, i, j)
            elif state.board[i][j] == 'P':
                bp.draw(screen, i, j)
    return screen


def draw_highlighted_board(state, x, y):
    screen = pygame.display.set_mode(screen_size)
    screen.fill(screen_color)
    block_size = screen_size[0] / 8
    for i in range(8):
        for j in range(8):
            if i == x and j == y:
                if (i + j) % 2 == 0:
                    pygame.draw.rect(screen, highlighted_white_block, (i * block_size, j * block_size, block_size, block_size))
                else:
                    pygame.draw.rect(screen, highlighted_black_block, (i * block_size, j * block_size, block_size, block_size))
                continue
            if is_valid(state, (i, j), (x, y)):
                if (i + j) % 2 == 0:
                    pygame.draw.rect(screen, highlighted_white_block, (i * block_size, j * block_size, block_size, block_size))
                else:
                    pygame.draw.rect(screen, highlighted_black_block, (i * block_size, j * block_size, block_size, block_size))
                continue
            if (i + j) % 2 == 0:
                continue
            pygame.draw.rect(screen, black_block, (i * block_size, j * block_size, block_size, block_size))

    for i in range(8):
        for j in range(8):
            if state.board[i][j] == 'r':
                wr.draw(screen, i, j)
            elif state.board[i][j] == 'n':
                wn.draw(screen, i, j)
            elif state.board[i][j] == 'b':
                wb.draw(screen, i, j)
            elif state.board[i][j] == 'k':
                wk.draw(screen, i, j)
            elif state.board[i][j] == 'q':
                wq.draw(screen, i, j)
            elif state.board[i][j] == 'p':
                wp.draw(screen, i, j)
            elif state.board[i][j] == 'R':
                br.draw(screen, i, j)
            elif state.board[i][j] == 'N':
                bn.draw(screen, i, j)
            elif state.board[i][j] == 'B':
                bb.draw(screen, i, j)
            elif state.board[i][j] == 'K':
                bk.draw(screen, i, j)
            elif state.board[i][j] == 'Q':
                bq.draw(screen, i, j)
            elif state.board[i][j] == 'P':
                bp.draw(screen, i, j)
    return screen

def draw_text(screen, text):
    font = pygame.font.Font(text_font, text_size)
    txt = font.render(text, True, text_color)
    textRect = txt.get_rect()
    textRect.center = (screen_size[0] // 2, screen_size[1] // 2)
    screen.blit(txt, textRect)
