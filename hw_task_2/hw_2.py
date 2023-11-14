# Задание 1
def remove_stop_words(input_words, stop_words):
    words = input_words.split()
    format_input = list(filter(lambda x: not (x in stop_words), words))
    return format_input


test_string = 'C test Python promt go words php'
stops = ['Python', 'php', 'go', 'C']
print(remove_stop_words(test_string, stops))

# Задание 2
