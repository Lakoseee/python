def fibonacci(n):
    if n < 0:
        raise ValueError("Z liczby ujemnej nie da sie obliczyc silni")

    if n == 0:
        return 0
    elif n == 1:
        return 1

    a, b = 0, 1
    for _ in range (2, n + 1):
        a, b = b, a + b
    return b


n = int(input("podaj którą liczbę ciągu fibonacciego chcesz znać: "))
liczba = fibonacci(n)
print(liczba)