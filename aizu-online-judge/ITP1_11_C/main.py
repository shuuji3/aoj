class Dice:
    def __init__(self, top: str, front: str, right: str, left: str, back: str, bottom: str) -> None:
        self.top = top
        self.front = front
        self.right = right
        self.left = left
        self.back = back
        self.bottom = bottom

    def __eq__(self, other) -> bool:
        top, front = self.top, self.front

        # find top
        found = False
        for direction in 'SSSS':
            other.roll(direction)
            if other.top == top:
                found = True
                break
        if not found:
            for direction in 'EEE':
                other.roll(direction)
                if other.top == top:
                    break

        # find front
        for _ in range(4):
            other.rotate_right()
            if other.front == front:
                break

        return (
                self.right == other.right
                and self.left == other.left
                and self.back == other.back
                and self.bottom == other.bottom
        )

    def print_top(self):
        print(self.top)

    def print_right(self):
        print(self.right)

    def roll(self, direction: str) -> None:
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

    def rotate_right(self) -> None:
        for direction in 'SWN':
            self.roll(direction)


dice1 = Dice(*input().split())
dice2 = Dice(*input().split())

if dice1 == dice2:
    print('Yes')
else:
    print('No')
