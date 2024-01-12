import re

input_file = '/Users/hernan.perazzo/Desktop/AoC/input2.txt'

game_counter = 0

# Thresholds for each color
thresholds = {
    'red': 12,
    'green': 13,
    'blue': 14
}


lista = []
lista2 = []
# Read the input file line by line
with open(input_file, 'r') as file:
    for line in file:
        # Use regular expression to find color counts in each line
        matches = re.findall(r'(\d+) (\w+)', line)
        
        # Track highest counts for each color in the current game
        highest_counts = {'red': 0, 'green': 0, 'blue': 0}
        
        # Process each match and update highest counts for current game
        for count, color in matches:
            count = int(count)
            if color in highest_counts:
                highest_counts[color] = max(highest_counts[color], count)
        suma = highest_counts["red"] * highest_counts["green"] * highest_counts["blue"]
        lista2.append(suma)
        # Check if any count exceeds the threshold
        if any(highest_counts[color] > thresholds[color] for color in thresholds):
            continue  # Skip counting this game if any threshold is exceeded
        
        # If none of the thresholds are exceeded, count this game
        
        lista.append(line[5:8])
        game_counter += 1
print(lista)
print(sum(lista2))
# Print the total count of acceptable games
print(f"Total count of acceptable games: {game_counter}")
