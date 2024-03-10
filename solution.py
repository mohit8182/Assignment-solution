from enum import Enum

class Direction(Enum):
    N = 'N'
    E = 'E'
    S = 'S'
    W = 'W'

class Position:
    def __init__(self, x, y, dir):
        self.x = x
        self.y = y
        self.dir = dir

class Rover:
    def __init__(self, x, y, dir):
        # Convert the dir parameter to the appropriate Direction enum member
        dir_enum = Direction[dir]
        self.position = Position(x, y, dir_enum)

    # The rest of the class remains the same

    def move(self, instructions):
        for instruction in instructions:
            if instruction == 'L':
                self.turnLeft()
            elif instruction == 'R':
                self.turnRight()
            elif instruction == 'M':
                self.moveForward()

    def getPosition(self):
        print(self.position.x, self.position.y, self.position.dir.value)

    def turnLeft(self):
        if self.position.dir == Direction.N:
            self.position.dir = Direction.W
        elif self.position.dir == Direction.E:
            self.position.dir = Direction.N
        elif self.position.dir == Direction.S:
            self.position.dir = Direction.E
        elif self.position.dir == Direction.W:
            self.position.dir = Direction.S

    def turnRight(self):
        if self.position.dir == Direction.N:
            self.position.dir = Direction.E
        elif self.position.dir == Direction.E:
            self.position.dir = Direction.S
        elif self.position.dir == Direction.S:
            self.position.dir = Direction.W
        elif self.position.dir == Direction.W:
            self.position.dir = Direction.N

    def moveForward(self):
        if self.position.dir == Direction.N:
            self.position.y += 1
        elif self.position.dir == Direction.E:
            self.position.x += 1
        elif self.position.dir == Direction.S:
            self.position.y -= 1
        elif self.position.dir == Direction.W:
            self.position.x -= 1

if __name__ == "__main__":
    upper_x, upper_y = map(int, input().split())

    # Read input line by line until EOF
    while True:
        try:
            # Read the coordinates and direction
            x, y, dir = input().split()
            x, y = int(x), int(y)

            # Read the instructions
            instructions = input()

            # Create the Rover object and move it
            rover = Rover(x, y, dir)
            rover.move(instructions)
            
            # Print the final position
            rover.getPosition()
        except EOFError:
            break
