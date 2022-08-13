# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import math
import pygame


class Point3D:
    def __init__(self, _coordinates, _offset, _size):
        self.rotations = None
        self.x = int(_coordinates[0]) * _size + _offset
        self.y = int(_coordinates[1]) * _size + _offset
        self.z = int(_coordinates[2]) * _size + _offset
        self.offset = _offset
        self.size = _size
        self.binary = f'{int((self.x - self.offset) / self.size)}{int((self.y - self.offset) / self.size)}{int((self.z - self.offset) / self.size)} '

    def neighbors(self):
        ret = []
        for i in range(len(list(self.binary))):
            clone = list(self.binary)
            if clone[i] == '1':
                clone[i] = '0'
            else:
                clone[i] = '1'
            ret.append(int(''.join(clone), 2))
        return list(filter(lambda x: 0 <= x <= 7, ret))

    def get2dcoords(self):
        newcoords = multiply(
            [[math.sqrt(3), 0, -math.sqrt(3)], [1, 2, 1], [math.sqrt(2), -math.sqrt(2), math.sqrt(2)]],
            [[self.x], [self.y], [self.z]])
        return (1 / math.sqrt(6)) * newcoords[0][0], (1 / math.sqrt(6)) * newcoords[1][0]

    def rotate(self, theta, axis):
        theta = math.radians(theta)
        self.rotations = {
            'x': [
                [1, 0, 0],
                [0, math.cos(theta), -math.sin(theta)],
                [0, math.sin(theta), math.cos(theta)],
            ],
            'y': [
                [math.cos(theta), 0, math.sin(theta)],
                [0, 1, 0],
                [-math.sin(theta), 0, math.cos(theta)],
            ],
            'z': [
                [math.cos(theta), -math.sin(theta), 0],
                [math.sin(theta), math.cos(theta), 0],
                [0, 0, 1],
            ]
        }
        newpoint = multiply(self.rotations[axis], [[self.x], [self.y], [self.z]])
        self.x = newpoint[0][0]
        self.y = newpoint[1][0]
        self.z = newpoint[2][0]


def multiply(mat1, mat2):
    if len(mat1[0]) != len(mat2):
        return -1
    m = len(mat1)
    n = len(mat1[0])
    p = len(mat2[0])
    mat3 = []
    for i in range(m):
        mat3.append([])
        for j in range(p):
            mat3[i].append(0)
    for i in range(m):
        for j in range(p):
            for k in range(n):
                mat3[i][j] += mat1[i][k] * mat2[k][j]
    return mat3


def center_origin(surf, p):
    return p[0] + surf.get_width() // 2, p[1] + surf.get_height() // 2


def setup():
    window_width = 400
    window_height = 400
    pygame.init()
    size = (window_width, window_height)
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("3Dcube")
    cube = []
    offset = -50
    length = 100
    for i in range(8):
        index = list(bin(i).replace('0b', ''))
        while len(index) < 3:
            index.insert(0, '0')
        cube.append(Point3D(index, offset, length))
    finish = False
    while not finish:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finish = True
        draw(cube, screen)
        pygame.display.flip()
    pygame.quit()


def draw(cube, screen):
    screen.fill((0, 0, 0))
    for i in range(len(cube)):
        cube[i].rotate(0.02, 'y')
        pygame.draw.circle(screen, (255, 255, 255),
                           center_origin(screen, cube[i].get2dcoords()), 5)
    for i in range(len(cube)):
        for index in cube[i].neighbors():
            pygame.draw.line(screen, (255, 255, 255), center_origin(screen, cube[i].get2dcoords()),
                             center_origin(screen, cube[index].get2dcoords()))


if __name__ == '__main__':
    setup()
