wysokosc = int(input("podaj ilosc wierszy"))
szerokosc = int(input("podaj ilosc kolumn"))

linia = "+---" * szerokosc + "+\n"
srodek = "|   " * szerokosc + "|\n"

prostokat = ""
for i in range(wysokosc):
    prostokat += linia
    prostokat += srodek
prostokat += linia

print(prostokat)