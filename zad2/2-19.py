L = [7, 105, 12, 999, 1, 42, 500, 8]

txt = ""
for elements in L:
        txt = txt + " " +(str(elements).zfill(3))


print(txt)