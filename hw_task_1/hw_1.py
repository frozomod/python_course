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


# Задание 5

def cnts(a, b):
    if a in b:
        print('Да')
    else:
        print('Нет')


str_1 = 'test'
str_2 = 'test1'
cnts(str_1, str_2)


# Задание 6

def count_positive_numbers(numbers):
    count = 0
    for num in numbers:
        if num > 0:
            count += 1
    return count


nmbrs = [1, -2, 3, -4, 5]
positive_count = count_positive_numbers(nmbrs)
print(positive_count)
