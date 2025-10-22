line="""Pierwsza linia.
Druga linia, z    wieloma spacjami.
Trzecia."""


slowa = []
lista_wyrazow=[]


#stworzenie listy długości każdego słowa
for element in line.split():
    lista_wyrazow.append(len(element.strip(".,!")))
    slowa.append(element.strip(".,!"))

print(lista_wyrazow)

#Znalezienie min/max elementu
print("Najwieksza liczba: "+ slowa[lista_wyrazow.index(max(lista_wyrazow))])
print("Najmniejsza liczba: "+ slowa[lista_wyrazow.index(min(lista_wyrazow))])