import pygame
from pygame.locals import *
from OpenGL.GL import *
import time
from random import randrange

LARGURA_JANELA = 640
ALTURA_JANELA = 480

time_frame = 1/20
tamanho_pixel = 10
snake = [[(LARGURA_JANELA/2-tamanho_pixel), ALTURA_JANELA/2],[LARGURA_JANELA/2, ALTURA_JANELA/2]]
snake_size = 2
food = []
direction = [tamanho_pixel, 0]
game_over = False

def get_random_food_position(min_x, max_x, min_y, max_y):
    return [randrange(min_x, max_x, tamanho_pixel), randrange(min_y, max_y, tamanho_pixel)]

def atualizar():
    global snake, snake_size, food, direction, game_over

    snake.append([snake[-1][0]+direction[0], snake[-1][1]+direction[1]])
    if len(snake) > snake_size:
        snake.pop(0)

    if food == snake[-1]:
        food = get_random_food_position(0, LARGURA_JANELA, 0, ALTURA_JANELA)
        snake_size += 1

    for i in snake[:-1]:
        if snake[-1] == i:
            game_over = True

    if (snake[-1][0] + tamanho_pixel/2 >= LARGURA_JANELA or snake[-1][0] <= 0 or 
        snake[-1][1] + tamanho_pixel/2 >= ALTURA_JANELA or snake[-1][1] <= 0):
        game_over = True

    keys = pygame.key.get_pressed()

    if keys[K_UP] and direction != [0, -tamanho_pixel]:
        direction = [0, tamanho_pixel]

    if keys[K_DOWN] and direction != [0, tamanho_pixel]:
        direction = [0, -tamanho_pixel]

    if keys[K_LEFT] and direction != [tamanho_pixel, 0]:
        direction = [-tamanho_pixel, 0]

    if keys[K_RIGHT] and direction != [-tamanho_pixel, 0]:
        direction = [tamanho_pixel, 0]

def desenharRetangulo(x, y, largura, altura, r, g, b):
    glColor3f(r, g, b)

    glBegin(GL_QUADS)
    glVertex2f(x, y)
    glVertex2f(x + largura, y)
    glVertex2f(x + largura, y + altura)
    glVertex2f(x, y + altura)
    glEnd()

def desenhar():
    glViewport(0, 0, LARGURA_JANELA, ALTURA_JANELA)

    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0, LARGURA_JANELA + tamanho_pixel, 0, ALTURA_JANELA + tamanho_pixel, 0, 1)

    glClear(GL_COLOR_BUFFER_BIT)

    desenharRetangulo(food[0], food[1], tamanho_pixel, tamanho_pixel, 0, 0, 1)
    for i in snake:
        if i == snake[-1]:
            desenharRetangulo(i[0], i[1], tamanho_pixel, tamanho_pixel, 1, 0, 0)
        else:
            desenharRetangulo(i[0], i[1], tamanho_pixel, tamanho_pixel, 0, 1, 0)

    pygame.display.flip()    

pygame.init()
pygame.display.set_mode((LARGURA_JANELA, ALTURA_JANELA), DOUBLEBUF | OPENGL)

while True:
    food = get_random_food_position(0, LARGURA_JANELA, 0, ALTURA_JANELA)
    init_time = time.time()
    while game_over == False:
        if (time.time() - init_time) > time_frame:
            init_time = time.time()
            atualizar()
            desenhar()
        pygame.event.pump()
    time.sleep(1)

    game_over = False
    snake_size = 2
    snake = [[(LARGURA_JANELA/2-tamanho_pixel), ALTURA_JANELA/2],[LARGURA_JANELA/2, ALTURA_JANELA/2]]
    