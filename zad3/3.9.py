from unittest import expectedFailure

seq = [[], [4], (1, 2), [3, 4], (5, 6, 7)]

wynik = []
for s in seq:
    suma = sum(s)
    wynik.append(suma)

print(wynik)

