file_path = "/Users/hernan.perazzo/Desktop/AoC/inputday4 .txt"
import re
# Open the file and read its content
with open(file_path, 'r') as file:
    # Read the content of the file line by line
    lines = file.readlines()

# Create a new list with modified lines
modified_lines = [line[10:].strip() for line in lines]  # Added .strip() to remove leading/trailing whitespaces

# Define a regular expression pattern to extract numbers
pattern = re.compile(r'\b\d+\b')

posiciones = []
numbers_list = []  # Define numbers_list outside the loop
card = 1
for line in modified_lines:
    contar = 0
    matches = pattern.findall(line)
    current_numbers_list = [int(match) for match in matches]
    lista1 = list(current_numbers_list[:10])
    lista2 = list(current_numbers_list[10:])
    numbers_list.append(current_numbers_list)  # Append to numbers_list
    for item in lista2:
        if item in lista1:
            contar += 1
    for i in range(card + 1, card + contar + 1):
        posiciones.append(i)
    card += 1


lel = 0
while lel < len(posiciones):
    contar1 = 0
    current = posiciones[lel] - 1  # Adjusted index
    lista11 = list(numbers_list[current][:10])  
    lista22 = list(numbers_list[current][10:])
    for it in lista22:
        if it in lista11:
            contar1 += 1
    for j in range(current + 1, current + contar1 + 1):
        posiciones.append(j)
    lel += 1
    contar1 = 0
print(len(posiciones))
