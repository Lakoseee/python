while True:
    x = input("Podaj liczbę lub wpisz stop aby zakończyć działanie programu ")

    if x.lower() == "stop":
        print ("koniec programu")
        break

    try:
        x = float(x)
        print(f"x = {x}, x³ = {x ** 3}")
    except ValueError:
        print("błąd, podana wartość nie jest liczbą")