line = """Pie rwsza  lin ia.
Druga linia, z    wieloma spacjami.
Trz ec ia."""


#podział na linie
z= line.splitlines()[0].split()
print(''.join(z))
y = line.splitlines()[len(line.splitlines())-1]
print(''.join(y.split()))