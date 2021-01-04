# Import libraries
import os

# Create zone
rows, cols = (10, 20)
zone = [[' ']*20 for test in range (10)]

# Create character
charac = "☺"

# Insert character
start_row, start_col = (5, 5)
zone[start_row][start_col] = charac

# Print zone
def print_zone():
    print("╔" + "═" * (cols-1) + "╗")
    for i in range(rows-1):
        print('║', end='')
        for j in range(cols-1):
            print(zone[i][j], end='')
        print('║')
    print("╚" + "═" * (cols-1) + "╝")

# Function for move character on array
def move_character():
    direction=input("Choose a direction between N(orth) S(outh), E(st) W(est) : ")
    pos_row, pos_col = (5, 5)
    position = zone[pos_row][pos_col]
    if direction == "N":
        position =  zone[pos_row][pos_col + 1]
        os.system('clear')
        print_zone()
    elif direction == "S":
        position =  zone[pos_row][pos_col - 1]
        os.system('clear')
        print_zone()
    elif direction == "E":
        position =  zone[pos_row + 1][pos_col]
        os.system('clear')
        print_zone()
    elif direction == "W":
        position =  zone[pos_row - 1][pos_col]
        os.system('clear')
        print_zone()

    else:
        print("Wrong direction, choose antoher")

# Run program
if __name__ == "__main__":
    print_zone()
    move_character()
