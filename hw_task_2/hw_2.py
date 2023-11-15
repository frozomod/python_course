import time


# Задание 1
def remove_stop_words(input_words, stop_words):
    words = input_words.split()
    format_input = list(filter(lambda x: not (x in stop_words), words))
    return format_input


test_string = 'C test Python promt go words php'
stops = ['Python', 'php', 'go', 'C']
print(remove_stop_words(test_string, stops))


# Задание 2
def denom_list(input_nums, denom):
    mod_nums = list(filter(lambda x: x % denom == 0, input_nums))
    return mod_nums


test_nums = [3, 1, 6, 9, 12, 5]
den = 3
print(denom_list(test_nums, den))


# Задание 3
def return_strings(*args):
    promt = ''
    for item in args:
        if isinstance(item, str):
            promt += item

    return promt


print(return_strings(3.0, 'test', '1', 'promt', ('list', 'tup')))


# Задание 4
def common_items(list_one, list_two):
    format_list = list(filter(lambda x: x in list_two, list_one))
    return format_list


list_first = [1, 3, 31, 5, 'test', 'go', 3.0]
list_second = [40, 3, 5, 'go', 'promt', 3.0]
print(common_items(list_first, list_second))


# Задание 5
def ladder(k, n):
    sum = 0
    if n == 0:
        return sum + 1
    elif k < n:
        for i in range(k + 1, n + 1):
            sum += ladder(i, n - i)
        return sum
    else:
        return sum


print(ladder(0, 7))


# Задание 6
def check_return_type(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if not isinstance(result, int):
            raise TypeError(f"Функция {func.__name__} должна выводить int, но вывела {type(result)}.")
        return result

    return wrapper


@check_return_type
def add_numbers(a, b):
    return a + b


@check_return_type
def multiply_numbers(x, y):
    return x * y


try:
    result1 = add_numbers(3, 4)
    print(f"Результат сложения: {result1}")
except TypeError as e:
    print(f"Error: {e}")

try:
    result2 = multiply_numbers(5, '2')
    print(f"Результат произведения: {result2}")
except TypeError as e:
    print(f"Error: {e}")


# Задание 7
def retry_once(func):
    def wrapper(*args, **kwargs):
        try:
            result = func(*args, **kwargs)
            return result
        except Exception as t:
            print(f"Ошибка: {t}. Повторный запуск...")
            try:
                return func(*args, **kwargs)
            except Exception as e_retry:
                print(f"Ошибка при повторном запуске: {e_retry}")

    return wrapper


@retry_once
def add_numbers(a, b):
    return a + b


@retry_once
def divide(a, b):
    return a / b


# Тестовые вызовы
result1 = add_numbers(3, 4)
print(f"Результат сложения: {result1}")

result2 = divide(10, 0)
print(f"Результат деления: {result2}")

# Задание 8
elements = [(2, 12, "Mg"), (1, 11, "Na"), (1, 3, "Li"), (2, 4, "Be")]

sorted_elements = sorted(elements, key=lambda x: x[1])

print(sorted_elements)


# Задание 9
def timing_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"Время выполнения функции: {func.__name__}: {execution_time:.4f} секунд")
        return result

    return wrapper


@timing_decorator
def slow_function():
    time.sleep(2)
    print("Медленная функция выполнена!")


@timing_decorator
def fast_function():
    print("Быстрая функция выполнена!")


# Тестовые вызовы
slow_function()
fast_function()
