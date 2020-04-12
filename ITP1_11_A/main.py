class Dice:
    def __init__(self, top, front, right, left, back, bottom):
        self.top = top
        self.front = front
        self.right = right
        self.left = left
        self.back = back
        self.bottom = bottom

    def print_top(self):
        print(self.top)

    def roll(self, direction):
        if direction == 'S':
            self.south()
        elif direction == 'N':
            self.north()
        elif direction == 'E':
            self.east()
        elif direction == 'W':
            self.west()

    def north(self):
        [self.top, self.back, self.bottom, self.front] = [self.front, self.top, self.back, self.bottom]

    def south(self):
        [self.top, self.back, self.bottom, self.front] = [self.back, self.bottom, self.front, self.top]

    def east(self):
        [self.top, self.right, self.bottom, self.left] = [self.left, self.top, self.right, self.bottom]

    def west(self):
        [self.top, self.right, self.bottom, self.left] = [self.right, self.bottom, self.left, self.top]


labels = input().split()
directions = input()

dice = Dice(*labels)
for direction in directions:
    dice.roll(direction)
dice.print_top()
