import math


def multiply(mat1, mat2):
    if len(mat1[0]) != len(mat2):
        return -1
    m = len(mat1)
    n = len(mat1[0])
    p = len(mat2[0])
    mat3 = [[0] * p] * m
    for i in range(m):
        for j in range(p):
            mat3[i][j] = 0
            for k in range(n):
                mat3[i][j] += mat1[i][k] * mat2[k][j]
    return mat3


class Point3D:
    def __init__(self, _x, _y, _z, _offset, _size):
        self.rotations = None
        self.x = _x * _size + _offset
        self.y = _y * _size + _offset
        self.z = _z * _size + _offset
        self.offset = _offset
        self.size = _size
        self.binary = f'{int((self.x - self.offset) / self.size)}{int((self.y - self.offset) / self.size)}{int((self.z - self.offset) / self.size)}'

    def neighbors(self):
        ret = []
        print(self.binary)
        for i in range(len(list(self.binary))):
            clone = list(self.binary)
            if clone[i] == '1':
                clone[i] = '0'
            else:
                clone[i] = '1'
            print(clone)
            ret.append(int(''.join(clone), 2))
        return list(filter(lambda x: 0 <= x <= 7, ret))

    def get2dcoords(self):
        newcoords = multiply(
            [[math.sqrt(3), 0, -math.sqrt(3)], [1, 2, 1], [math.sqrt(2), -math.sqrt(2), math.sqrt(2)]],
            [[self.x], [self.y], [self.z]])
        return self.x,self.y
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
        print(newpoint)
        self.x = newpoint[0][0]
        self.y = newpoint[1][0]
        self.z = newpoint[2][0]
        print(self.x)
        print(self.y)
        print(self.z)
