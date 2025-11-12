from math import gcd

def _simplify(frac):
    num, den = frac
    if den == 0:
        raise ZeroDivisionError("Mianownik nie może być zerem.")
    if num == 0:
        return [0, 1]
    g = gcd(num, den)
    num //= g
    den //= g
    # przenosimy znak do licznika
    if den < 0:
        num *= -1
        den *= -1
    return [num, den]


def add_frac(frac1, frac2):
    n1, d1 = frac1
    n2, d2 = frac2
    num = n1 * d2 + n2 * d1
    den = d1 * d2
    return _simplify([num, den])


def sub_frac(frac1, frac2):
    n1, d1 = frac1
    n2, d2 = frac2
    num = n1 * d2 - n2 * d1
    den = d1 * d2
    return _simplify([num, den])


def mul_frac(frac1, frac2):
    n1, d1 = frac1
    n2, d2 = frac2
    num = n1 * n2
    den = d1 * d2
    return _simplify([num, den])


def div_frac(frac1, frac2):
    n1, d1 = frac1
    n2, d2 = frac2
    if n2 == 0:
        raise ZeroDivisionError("Nie można dzielić przez zero.")
    num = n1 * d2
    den = d1 * n2
    return _simplify([num, den])


def is_positive(frac):
    num, den = _simplify(frac)
    return num * den > 0


def is_zero(frac):
    num, _ = frac
    return num == 0


def cmp_frac(frac1, frac2):
# zwraca    -1 jeśli frac1 < frac2
#            0 jeśli równe
#           +1 jeśli frac1 > frac2
    n1, d1 = _simplify(frac1)
    n2, d2 = _simplify(frac2)
    left = n1 * d2
    right = n2 * d1
    if left < right:
        return -1
    elif left > right:
        return 1
    else:
        return 0


def frac2float(frac):
    num, den = frac
    return num / den
