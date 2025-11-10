def rysuj_miarke(n):
    miarka = '|'
    liczby = '0'

    for i in range(1, n + 1):
        miarka += '....|'
        liczby += f'{i:>5}'
    wynik = miarka + '\n' + liczby

    return wynik

def rysuj_prostokat(wysokosc, szerokosc):
    linia = "+---" * szerokosc + "+\n"
    srodek = "|   " * szerokosc + "|\n"

    prostokat = ""
    for i in range(wysokosc):
        prostokat += linia
        prostokat += srodek
    prostokat += linia

    return prostokat

n = int(input("podaj długość miarki "))
miarka = rysuj_miarke(n)
print(miarka)

wysokosc = int(input("podaj wysokosc siatki "))
szerokosc = int(input("podaj szerokosc siatki "))
prostokat = rysuj_prostokat(wysokosc, szerokosc)
print(prostokat)