X = "qwerty"

def func():
    print(X)

func()
# qwerty

X = "qwerty"

def func():
    X = "abc"

func()
print(X)

#qwerty

X = "qwerty"

def func():
    global X
    X = "abc"

func()
print(X)
#abc