import pygame
from pygame.locals import *
from math import *

RED_COLOR = (255, 0, 0)
GREEN_COLOR = (0, 255, 0)
BLUE_COLOR = (0, 0, 255)
CYAN_COLOR = (0, 255, 255)
BROWN_COLOR = (100, 100, 0)
BLACK_COLOR = (0, 0, 0)


def draw_picture(screen, x, y, width, height):
    """
    Рисует картинку с домиком на фоне травы и неба.
    :param screen: дисплей pygame, на котором будет изображение
    :param x: левая координата прямоугольника с рисунком
    :param y: верхняя координата прямоугольника с рисунком
    :param width: ширина прямоугольника
    :param height: высота прямоугольника
    """
    draw_background(screen, x, y, width, height)
    house_x = x + width // 2
    house_y = y + height * 3 // 4
    house_height = min(height, width) * 2 // 3
    house_width = int(house_height * 1.5)
    draw_house(screen, house_x, house_y, house_width, house_height)
    sun_radius = min(width, height) // 10
    draw_sun(screen, x, y, sun_radius)

def draw_background(screen, x, y, width, height):
    """
    Рисует прямоугольный фон для картинки с травой и небом.
    :param screen: дисплей pygame, на котором будет изображение
    :param x: левая координата прямоугольника с фоном
    :param y: верхняя координата прямоугольника с фоном
    :param width: ширина прямоугольника
    :param height: высота прямоугольника
    """
    pygame.draw.rect(screen, GREEN_COLOR, pygame.Rect((0, height // 2),(width, height // 2)))
    pygame.draw.rect(screen, CYAN_COLOR, pygame.Rect((0, 0), (width, height // 2)))


def draw_house(screen, x, y, width, height):
    """
    Рисует домик заданных размеров от точки (x, y).
    Внимание! Опорная точка находится посередине внизу основания!
    :param screen: дисплей pygame, на котором будет изображение
    :param x: горизонтальная координата опорной точки
    :param y: вертикальная координата опорной точки
    :param width: полная ширина домика
    :param height: полная высота домика
    """
    print("Типа рисую домик", x, y, width, height)


def draw_sun(screen, x, y, radius):
    """
    Рисует солнышко в виде.
    :param screen: дисплей pygame, на котором будет изображение
    :param x: левая координата прямоугольника с рисунком
    :param y: верхняя координата прямоугольника с рисунком
    :param radius: ширина прямоугольника
    """
    print("Типа рисую солнышко", x, y, radius)



pygame.init()
width, height = screen_size = (300, 200)
screen = pygame.display.set_mode(screen_size)

# Здесь нужно рисовать
draw_picture(screen, 0, 0, width, height)



pygame.display.update()

work_flag = True
while work_flag:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            work_flag = False

print("Программа благополучно завершена")