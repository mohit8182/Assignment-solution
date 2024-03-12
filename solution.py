from enum import Enum

# Define enumeration for directions
class Direction(Enum):
    NORTH = 'N'
    EAST = 'E'
    SOUTH = 'S'
    WEST = 'W'

# Define class to represent the position of the rover
class Position:
    def __init__(self, x, y, direction):
        self.x = x  # x-coordinate
        self.y = y  # y-coordinate
        self.direction = direction  # direction of the rover

# Define class for the Rover
class Rover:
    def __init__(self, x, y, direction):
        # Initialize rover's position
        self.position = Position(x, y, Direction(direction))

    # Method to move the rover based on instructions
    def move(self, instructions):
        for instruction in instructions:
            if instruction == 'L':
                self.turn(-1)  # Rotate left
            elif instruction == 'R':
                self.turn(1)   # Rotate right
            elif instruction == 'M':
                self.move_forward()  # Move forward

    # Method to print the current position of the rover
    def get_position(self):
        print(f"{self.position.x} {self.position.y} {self.position.direction.value}")

    # Method to rotate the rover
    def turn(self, direction):
        directions = list(Direction)  # Get list of directions
        current_index = directions.index(self.position.direction)  # Get index of current direction
        new_index = (current_index + direction) % len(directions)  # Calculate new direction index
        self.position.direction = directions[new_index]  # Set new direction

    # Method to move the rover forward
    def move_forward(self):
        dx, dy = 0, 0
        # Determine movement based on current direction
        if self.position.direction == Direction.NORTH:
            dy = 1
        elif self.position.direction == Direction.EAST:
            dx = 1
        elif self.position.direction == Direction.SOUTH:
            dy = -1
        elif self.position.direction == Direction.WEST:
            dx = -1

        # Update rover's position
        self.position.x += dx
        self.position.y += dy

# Main program
if __name__ == "__main__":
    try:
        # Get upper-right coordinates of the plateau
        upper_x, upper_y = map(int, input("Enter upper-right coordinates of the plateau: ").split())
    except ValueError:
        print("Invalid coordinates format. Please enter integers separated by space.")
        exit()

    # Process rovers until end of input
    while True:
        try:
            # Get initial position and direction of the rover
            x, y, direction = input("Enter rover's initial position and direction: ").split()
            x, y = int(x), int(y)  # Convert coordinates to integers

            # Get movement instructions for the rover
            instructions = input("Enter movement instructions: ")

            # Create a new rover object
            rover = Rover(x, y, direction)
            # Move the rover according to instructions
            rover.move(instructions)
            
            # Print the final position of the rover
            rover.get_position()
        except ValueError:
            print("Invalid input format. Please enter integers for coordinates and a valid direction.")
        except EOFError:
            break  # Exit loop at end of input
