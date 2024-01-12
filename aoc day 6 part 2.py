tiempo = [55826490]
dist = [246144110121111]

suma1 = []
for i in range(0,tiempo[0]+1):
    lol = i * (tiempo[0]-i)
    if lol > dist[0]:
        suma1.append(lol)
    



print(len(suma1))