def odwracanie_iter(L): #prostsza dla mnie przynajmniej
    left = 0
    right = len(L) - 1

    while left < right:
        L[left], L[right] = L[right], L[left]
        left += 1
        right -= 1

L = [1, 2, 3, 4, 5, 6]
odwracanie_iter(L)
print(L)

def odwracanie_rek(L_2, left=0, right=None):
    if right is None:
        right = len(L_2) - 1
    if left >= right:
        return
    L_2[left], L_2[right] = L_2[right], L_2[left]
    odwracanie_rek(L_2, left + 1, right - 1)

L_2 = [1, 2, 3, 4, 5, 6]
odwracanie_rek(L_2)
print(L_2)