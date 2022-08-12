class Point3D:
    def __init__(self, _x, _y, _z, _offset, _size):
        self.x = _x
        self.y = _y
        self.z = _z
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
