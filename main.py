# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from point3D import Point3D


def setup():
    print("hello")
    point = Point3D(1, 1, 1, 0, 1)
    print(point.neighbors())


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    setup()