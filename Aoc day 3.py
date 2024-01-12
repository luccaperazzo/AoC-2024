def merge_adjacent_digits(grid):
    result = []
    for row in grid:
        merged_row = []
        i = 0
        while i < len(row):
            if row[i].isdigit():
                j = i + 1
                while j < len(row) and row[j].isdigit():
                    j += 1
                merged_row.append(int(''.join(row[i:j])))
                i = j
            else:
                merged_row.append(row[i])
                i += 1
        result.append(merged_row)
    return result



def symbol(grid, i, j):
    adjacent_positions = [
        (i, j-1), (i, j+1), (i+1, j), (i-1, j),
        (i+1, j+1), (i-1, j+1), (i-1, j-1), (i+1, j-1)
    ]

    for i, j in adjacent_positions:
        try:
            if i < 0 or j < 0:
                continue  # Skip positions with negative indices
            char = grid[i][j]
            if char != '.' and not str(char).isalnum():
                return True
        except IndexError:
            continue  # Ignore out-of-range indices

    return False  # Return False if no invalid characters were found in adjacent positions



def chequear(grid):
    suma = 0
    lista = []
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if isinstance(grid[i][j],int):
                if symbol(grid,i,j) == True:
                    suma += grid[i][j]
                    lista.append(grid[i][j])
                else:
                    continue
    return suma
                    


def read_engine_schematic(file_path):
    # Define the pattern of character counts for line breaks
    line_breaks = [87, 53]

    # Initialize a list to store result strings
    lista = []

    # Counter for tracking character positions
    char_count = 0

    # Read the content of the file
    with open(file_path, 'r') as file:
        content = file.read()

    # Initialize an empty result string for the current iteration
    result_string = ""

    # Iterate over each character in the file content
    for char in content:
        if char == '\n':
            continue
        else:
            result_string += char
            char_count += 1

        # Check if the current character count matches any in the line_breaks pattern
        if char_count == line_breaks[0]:
            char_count = 0
            line_breaks.reverse()
            
            # Append the current result string to the list and reset it
            lista.append(result_string)
            result_string = ""

    # Append any remaining content to the list if needed
    if result_string:
        lista.append(result_string)
    return lista

# Display the result list

grid_file = '/Users/hernan.perazzo/Desktop/Aoc/inputday3.txt'
engine_grid = read_engine_schematic(grid_file)

merged_grid = merge_adjacent_digits(engine_grid)
#for row in merged_grid:
    #print(row)
print(chequear(merged_grid))