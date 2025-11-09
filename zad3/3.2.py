L = [3, 5, 4] ; L = L.sort()
# .sort() sortuje liste ale zwraca nowej poukładanej listy tylko wartość none

x, y = 1, 2, 3
# zła ilosc elementów, indentyfikatorów musi być tyle samo co wartości

X = 1, 2, 3 ; X[1] = 4
# w wyrażeniu X = 1, 2, 3; tworzymy krotke a ta nie może byc modyfikowana (tutaj drugi człon - X[1] = 4)

X = [1, 2, 3] ; X[3] = 4
# indeksy listy to 0,1,2 a x[3] nie istnieje musielibyśmy użyć np. X.append(4)

X = "abc" ; X.append("d")
# str nie mogą być modyfikowane i nie mają metody .append()

L = list(map(pow, range(8)))
# pow wymaga 2 argumentów a map przekazuje jej tylko jeden

