x = 2; y = 3;
if (x > y):
    result = x;
    print(x) # to dodałem żeby zobaczyć czy program działa
else:
    result = y;
    print(y) # to dodałem żeby zobaczyć czy program działa

# program się skompiluje i wykona ale nie jest to optymalne składniowo.
# python nie wymaga abyśmy użwali średników (;) oraz nawiasów w przypadku wyrażenia "if"

for i in "axby": if ord(i) < 100: print (i)

# nie poprawnie, nie kompiluje sie powinno być wcięcie w nowej linijce po ":"
#for i in "axby":
#    if ord (i) < 100:
#        print (i)

for i in "axby": print (ord(i) if ord(i) < 100 else i)
# poprawne i sie skompiluje