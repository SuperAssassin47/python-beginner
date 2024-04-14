class Square:
    def __init__(self, side):
        self.side = side
    def area(self):
        return self.side**2
    def perimeter(self):
        return 4 * self.side
    def __repr(self):
        s = 'Square side length: ' + str(self.side) + '\n' + \
            'Area = ' + str(self.area()) + '\n' + \
            'Perimeter = ' + str(self.perimeter())
        return s

if __name__ == '__main__':
    side = int(input('Enter Length of side: '))

    square = Square(side)

    print(square)
