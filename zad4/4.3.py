def factorial(n):
    if n < 0:
        raise ValueError("Z liczby ujemnej nie da sie obliczyc silni")

    wynik = 1
    for i in range (2, n + 1):
        wynik *= i
    return wynik

n = int(input("podaj liczbę której silnie chcesz obliczyć: "))
silnia = factorial(n)
print(silnia)