import pygame


pygame.init()
width, height = screen_size = (300, 200)
screen = pygame.display.set_mode(screen_size)

# Здесь нужно рисовать

pygame.display.update()

work_flag = True
while work_flag:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            work_flag = False

print("Программа благополучно завершена")