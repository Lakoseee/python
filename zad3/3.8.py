a = input("podaj pierwszy dowolny ciąg znaków")
b = input("podaj drugi dowolny ciąg znaków")

set_a = set(a)
set_b = set(b)

wspolne = list(set_a & set_b)
wszystkie = list(set_a | set_b)

print("a) elementy wspólne: ", wspolne)
print("b) wszystkie elementy: ", wszystkie)