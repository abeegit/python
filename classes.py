class Animal:
    __name = None
    __weight = 0
    __height = 0

    def set_name(self, name):
        self.__name = name

    def __init__(self, name, weight, height):
        self.__name = name
        self.__weight = weight
        self.__height = height
