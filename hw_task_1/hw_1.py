# Задание 1
def lngth(prmt):
    return len(prmt)


print(lngth('hello'))


# Задание 2

def mxlst(a, b):
    if len(a) > len(b):
        return len(a)
    else:
        return len(b)


x = [1, 2, 3, 4, 5, 6]
y = ['a', 'b', 'c', 'd', 'e', 'f', 'g']

print(mxlst(x, y))


# Задание 3

def appnd(a, b):
    a.append(b)
    return a


x = [1, 2, 3, 4, 5, 6]
y = 'a'

print(appnd(x, y))


# Задание 4

def prnt(a):
    if -100 < a < 100:
        print('-')
    else:
        print('+')


prnt(0)
prnt(-101)

