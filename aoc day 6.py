tiempo = [55,82,64,90]
dist = [246,1441,1012,1111]

suma1 = []
for i in range(0,tiempo[0]+1):
    lol = i * (tiempo[0]-i)
    if lol > dist[0]:
        suma1.append(lol)
    
    
    
suma2 = []
for o in range(0,tiempo[1]+1):
    lol2 = o * (tiempo[1]-o)
    if lol2 > dist[1]:
        suma2.append(lol2)
print(sum(suma2))

suma3 = []
for l in range(0,tiempo[2]+1):
    lol3 = l * (tiempo[2]-l)
    if lol3 > dist[2]:
        suma3.append(lol3)
print(sum(suma3))

suma4 = []
for j in range(0,tiempo[3]+1):
    lol4 = j * (tiempo[3]-j)
    if lol4 > dist[3]:
        suma4.append(lol4)
print(sum(suma4))


result =  len(suma1) * len(suma2) * len(suma3)* len(suma4)
print(result)