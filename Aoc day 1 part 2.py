def extract_written_numbers(input_string):
    # Define a mapping dictionary for written numbers
    number_mapping = {
        'one': '1',
        'two': '2',
        'three': '3',
        'four': '4',
        'five': '5',
        'six': '6',
        'seven': '7',
        'eight': '8',
        'nine': '9',
    }

    # Replace written numbers with their numerical equivalents
    for word, digit in number_mapping.items():
        input_string = input_string.replace(word, digit)

    return input_string


def extract_digits(word):
    result = ''.join(filter(str.isdigit, word))
    return result



# Test the function with your examples
file_path = "/Users/hernan.perazzo/Desktop/AoC/input.txt"
with open(file_path, 'r') as file:
    content = file.read()

strings = content.split()

lista = []
for s in range(len(strings)):
    word = ""
    lista2 = []
    for j in strings[s]:
        word += j
        result = extract_written_numbers(word)
        lol = extract_digits(result)
        lista2.append(lol)
    lista.append(lista2)


# Filter out empty strings from each sublist
cleaned_list = [[digit for digit in sublist if digit] for sublist in lista]

# Print the first and last digit of the last element in the result_list
listafinal =[]
for i in range(len(cleaned_list)):
    lol= ""
    lol = cleaned_list[i][0][-1] + cleaned_list[i][-1][-1]
    listafinal.append(int(lol))
    lol = ""

print(cleaned_list)
print(sum(listafinal))
            