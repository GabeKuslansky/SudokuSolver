import os, constants    

def read_puzzle_files():
    if not os.path.exists(constants.PUZZLES_PATH):
        print("No puzzles found")
    else:
        filenames = os.listdir(constants.PUZZLES_PATH)
        if len(filenames) == 0:
            print("No puzzles found")
        else:
            for filename in filenames:
                f = open(f"{constants.PUZZLES_PATH}/{filename}", "r")
                puzzle = generate_puzzle_from_file(f)
                f.close()
                solve_puzzle(puzzle) and write_solution(puzzle, filename)

def write_solution(puzzle, filename: str):
    if not os.path.exists(constants.SOLUTIONS_PATH):
        os.makedirs(constants.SOLUTIONS_PATH)
    solution_filename = filename.split('.')
    solution_filename.insert(1, '.sln.')
    solution_filename = f"{constants.SOLUTIONS_PATH}/" + "".join(solution_filename)
    
    f = open(solution_filename, "w")
    for r in range(9):
        for c in range(9):
            f.write(puzzle[r][c])
            if c == 8: f.write('\n')

def solve_puzzle(puzzle):
    row, col = get_empty_cell(puzzle) 
    if [row,col].__contains__(None):
        return True

    for guess in range(1,10):
        is_valid_guess = validate_guess(puzzle, row, col, str(guess))
        if is_valid_guess:
            puzzle[row][col] = str(guess)
            if solve_puzzle(puzzle):
                return True

        puzzle[row][col] = constants.OPEN_CELL_INDICATOR
    return False


def get_empty_cell(puzzle):
    for r in range(9):
        for c in range(9):
            if puzzle[r][c] == constants.OPEN_CELL_INDICATOR:
                return r,c
    return None,None

def generate_puzzle_from_file(filename: str):
    puzzle = []
    for line in filename:
        newLine = []
        for char in line:
            if char != "\n":
                newLine.append(char)
        puzzle.append(newLine)
    return puzzle

def validate_guess(puzzle, row: int, col: int, guess: str):
    rowValues = puzzle[row]
    if guess in rowValues: return False

    for i in range(9):
        columnCell = puzzle[i][col]
        if guess == columnCell: return False

    row_start_index = row // 3 * 3
    col_start_index = col // 3 * 3
    for r in range(row_start_index, row_start_index+3):
        for c in range(col_start_index, col_start_index+3):
            if guess == puzzle[r][c]: return False
    return True

if __name__ == '__main__':
    read_puzzle_files()
