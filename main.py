# Import libraries
import os

# Create zone
rows, cols = (10, 20)
zone = [[' ']*20 for test in range (10)]

# Insert character
charac = "☺"
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
def move_character(pos_row, pos_col):
    direction=input("Choose a direction between N(orth) S(outh), E(st) W(est) : ")
    zone[pos_row][pos_col] = ' '
    if direction == "N":
        pos_row -= 1
        if pos_row == -1:
            pos_row = 8
    elif direction == "S":
        pos_row += 1
        if pos_row == 9:
            pos_row = 0
    elif direction == "E":
        pos_col += 1
        if pos_col == 19:
            pos_col = 0
    elif direction == "W":
        pos_col -= 1
        if pos_col == -1:
            pos_col = 18
    else:
        print("Wrong direction, choose antoher")
    zone[pos_row][pos_col] = charac
    os.system('clear')
    print_zone()
    return pos_row, pos_col

# Run program
if __name__ == "__main__":
    pos_row = start_row
    pos_col = start_col
    print_zone()
    for i in range(1, 20):
        pos_row, pos_col = move_character(pos_row, pos_col)