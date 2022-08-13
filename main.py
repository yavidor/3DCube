# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import random

from point3D import Point3D
import pygame


def center_origin(surf, p):
    return p[0] + surf.get_width() // 2, p[1] + surf.get_height() // 2


def setup():
    print("hello")
    point = Point3D(1, 1, 1, 0, 1)
    print(point.neighbors())
    window_width = 400
    window_height = 400
    pygame.init()
    size = (window_width, window_height)
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Game")
    cube = []
    offset = -50
    length = 10
    cube.append(Point3D(0, 0, 0, offset, length))
    cube.append(Point3D(0, 0, 1, offset, length))
    cube.append(Point3D(0, 1, 0, offset, length))
    cube.append(Point3D(0, 1, 1, offset, length))
    cube.append(Point3D(1, 0, 0, offset, length))
    cube.append(Point3D(1, 0, 1, offset, length))
    cube.append(Point3D(1, 1, 0, offset, length))
    cube.append(Point3D(1, 1, 1, offset, length))
    finish = False
    while not finish:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finish = True
        draw(cube, screen)
        pygame.display.flip()
    pygame.quit()


def draw(cube, screen):
    for i in range(len(cube)):
        cube[i].rotate(0.1, 'x')
        pygame.draw.circle(screen, (255,255,255),
                           center_origin(screen, cube[i].get2dcoords()), 5)
    # pygame.draw.rect(screen,(255,255,255),)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    setup()
