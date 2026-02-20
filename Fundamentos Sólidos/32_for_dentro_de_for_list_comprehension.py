lista1 = []

for x in range(3):
    for y in range(3):
     lista1.append((x, y))

print(lista1)

# fazendo o mesmo com list comprehension
lista2 = [ (x, y) for x in range(3) for y in range(3)]
print(lista2)