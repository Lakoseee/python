n = int(input("Podaj długość miarki: "))
miarka = '|'
liczby = '0'

for i in range(1, n + 1):
    miarka += '....|'
    liczby += f'{i:>5}'

print(miarka)
print(liczby)