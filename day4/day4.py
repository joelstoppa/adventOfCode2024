import re

with open('input','r') as file:
    data = file.read()


lines = data.splitlines()
grid = [list(line) for line in lines]

def findVertical(grid):

    total = 0

    for col in range(len(grid[0])):
        vertical = ''.join(row[col] for row in grid)
        found = re.finditer(r'(?=(XMAS|SAMX))', vertical)
        total += sum(1 for _ in found)
    return total

def findHorizontal(data):
    total = sum(1 for _ in re.finditer(r'(?=(XMAS|SAMX))', data))
    return total

def extract_top_left_to_bottom_right(grid):
    diagonals = []
    rows, cols = len(grid), len(grid[0])

    # Start from first row
    for col in range(cols):
        diag = ''.join(grid[row][col + row] for row in range(min(rows, cols - col)))
        diagonals.append(diag)

    # Start from first column (skip grid[0][0] to avoid duplicate diagonal)
    for row in range(1, rows):
        diag = ''.join(grid[row + col][col] for col in range(min(rows - row, cols)))
        diagonals.append(diag)

    return diagonals

def extract_top_right_to_bottom_left(grid):
    diagonals = []
    rows, cols = len(grid), len(grid[0])

    # Start from first row
    for col in range(cols - 1, -1, -1):
        diag = ''.join(grid[row][col - row] for row in range(min(rows, col + 1)))
        diagonals.append(diag)

    # Start from last column of each row (skip grid[0][-1] to avoid duplicate)
    for row in range(1, rows):
        diag = ''.join(grid[row + col][cols - 1 - col] for col in range(min(rows - row, cols)))
        diagonals.append(diag)

    return diagonals

def findDiagonal(grid):
    total = 0

    # Extract diagonals and search for patterns
    diagonals = extract_top_left_to_bottom_right(grid) + extract_top_right_to_bottom_left(grid)

    for diagonal in diagonals:
        found = re.finditer(r'(?=(XMAS|SAMX))', diagonal)
        total += sum(1 for _ in found)

    return total

all = findHorizontal(data) + findVertical(grid) + findDiagonal(grid)

print(all)
