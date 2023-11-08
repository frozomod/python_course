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


# Задание 7
def calculate_days(years, months):
    days = years * 365 + months * 29
    return days


years = 2
months = 6
total_days = calculate_days(years, months)
print(total_days)


# Задание 8

def generate_abbreviations(input_string):
    if not isinstance(input_string, str):
        raise ValueError("Вход должен быть строкой")

    words = input_string.split()
    abbreviations = "".join(word[0].upper() for word in words)
    return abbreviations


input_string = "Названием файла, названием функции или комментарием помечайте номер задачи"
abbreviations = generate_abbreviations(input_string)
print("Аббревиатуры:", abbreviations)


# Задание 9

def factorial(n):
    if n < 0:
        return "Факториал отрицательного числа не определен"
    if n == 0:
        return 1
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


number = 6
fact = factorial(number)
print("Факториал числа", number, "равен", fact)

# Задание 10

lst = [2, 4, 5, 8, 9, 13]
number = 0
while number < len(lst):
    lst[number] *= number
    number += 1
    print(lst)
