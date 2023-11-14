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
    print(len(args))
    for item in args:
        if isinstance(item, str):
            promt += item

    return promt


print(return_strings(3.0, 'test', '1', 'promt', ('list', 'tup')))