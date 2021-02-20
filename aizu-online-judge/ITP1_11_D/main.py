class Dice:
    def __init__(self, top: str, front: str, right: str, left: str, back: str, bottom: str) -> None:
        self.top = top
        self.front = front
        self.right = right
        self.left = left
        self.back = back
        self.bottom = bottom

    def __eq__(self, other) -> bool:
        for directions in ['', 'N', 'SE', 'WW', 'ES', 'S']:
            for direction in directions:
                other.roll(direction)

            for _ in range(4):
                other.rotate_right()
                if (
                        self.top == other.top
                        and self.front == other.front
                        and self.back == other.back
                        and self.right == other.right
                        and self.left == other.left
                        and self.bottom == other.bottom
                ):
                    return True
        return False

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


n = int(input())
dices = []
for _ in range(n):
    dices.append(Dice(*input().split()))

dice1 = dices[0]
all_different = all(map(lambda dice: dice != dice1, dices[1:]))
if all_different:
    print('Yes')
else:
    print('No')
