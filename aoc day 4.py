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

# Initialize puntostotal
puntostotal = 0
# Process each line separately
for line in modified_lines:
    # Find all matches in the current line
    puntos = 0
    contar = 0
    matches = pattern.findall(line)
    # Convert the matched strings to integers and create a list
    numbers_list = [int(match) for match in matches]
    lista1 = list(numbers_list[:10])  # Simplified the code for creating lista1
    lista2 = list(numbers_list[10:])
    for item in lista2:
        if item in lista1:
            contar += 1
    puntos = 2**(contar-1) if contar > 1 else contar
    print(puntos)# Simplified the points calculation
    puntostotal += puntos
    puntos = 0

print(puntostotal)

# If you want to print the modified lines, you can do something like:
# for line in modified_lines:
#     print(line)