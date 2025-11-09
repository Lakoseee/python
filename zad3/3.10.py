def roman2int(s):
    roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    #
    #roman = dict(I=1, V=5, X=10, L=50, C=100, D=500, M=1000)
    #
    #roman = dict([
    #('I', 1),
    #('V', 5),
    #('X', 10),
    #('L', 50),
    #('C', 100),
    #('D', 500),
    #('M', 1000)
    #])
    #
    #keys = ['I', 'V', 'X', 'L', 'C', 'D', 'M']
    #values = [1, 5, 10, 50, 100, 500, 1000]
    #roman = dict(zip(keys, values))

    total = 0
    prev_value = 0

    for char in reversed(s):  # czytamy od końca
        value = roman[char]
        if value < prev_value:
            total -= value
        else:
            total += value
            prev_value = value
    print(total)

x = input("Podaj liczbe w systemie rzmyskim (używając I,V,X,L,C,D,M): ")
roman2int(x)