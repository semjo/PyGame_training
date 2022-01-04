import pygame

def draw_picture(screen, x, y, width, height):
    """
    Рисует картинку с домиком на фоне травы и неба.
    :param screen: дисплей pygame, на котором будет изображение
    :param x: левая координата прямоугольника с рисунком
    :param y: верхняя координата прямоугольника с рисунком
    :param width: ширина прямоугольника
    :param height: высота прямоугольника
    """
    print("Типа рисую картинку", x, y, width, height)

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