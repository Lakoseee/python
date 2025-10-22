line="""Pierwsza linia.
Druga linia, z    wieloma spacjami.
Trzecia."""

lista_wyrazow = line.split()
print(lista_wyrazow)
sum=0
for element in lista_wyrazow:
    sum += len(element.strip(".,!"))

print(sum)