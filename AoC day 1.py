

file_path = '/Users/hernan.perazzo/Desktop/AoC/input.txt'


with open(file_path, 'r') as file:
    content = file.read()
    
    
words = content.split()

suma = 0 
for i in words:
    reves = i[::-1]
    numero = 0
    for x in i:
        if x.isdigit():
            suma1 = x
            break
    for z in reves:
        if z.isdigit():
            suma2 = z
            break
    numero = int(suma1 + suma2)
    suma += numero
            
            
print(suma)