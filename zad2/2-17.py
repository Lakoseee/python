line = "Ul był w domu, a woda w rzece."


new_line = []

for elements in line.split():
    new_line.append(elements.strip(".,!"))


by_alphabet = []
by_length = [] 

for elements in sorted(new_line, key=str.lower):
    by_alphabet.append(elements)

for elements in sorted(new_line, key=len):
    by_length.append(elements)

print("Ze wzgledu na alfabet" + str(by_alphabet))
print("Ze wzgledu na długość" + str(by_length))



