import numpy as np
import re

# Задание 1
random_vector = np.random.rand(10)
sorted_vector = np.sort(random_vector)
print(sorted_vector)

# Задание 2
chessboard_matrix = np.zeros((8, 8), dtype=int)
chessboard_matrix[1::2, ::2] = 1
chessboard_matrix[::2, 1::2] = 1
print(chessboard_matrix)

# Задание 3
matrix_a = np.random.rand(8, 4)
matrix_b = np.random.rand(4, 2)

# Перемножаем матрицы
result_matrix = np.dot(matrix_a, matrix_b)
print("Матрица A (8x4):")
print(matrix_a)
print("\nМатрица B (4x2):")
print(matrix_b)
print("\nРезультат перемножения (8x2):")
print(result_matrix)

# Задание 4
vector = np.linspace(0.1, 0.9, 10)
print(vector)


# Задание 5

def build_matrices(num):
    # Проверяем, можно ли разбить число на множители без остатка
    divisors = [i for i in range(2, num) if num % i == 0]

    if not divisors:
        print(f"Нельзя разбить число {num} на множители без остатка.")
        return

    print(f"Возможные матрицы для числа {num}:")

    for divisor in divisors:
        other_divisor = num // divisor

        # Пропускаем случаи, где один из множителей равен 1
        if divisor == 1 or other_divisor == 1:
            continue

        matrix_shape = (divisor, other_divisor)
        matrix = np.random.rand(*matrix_shape)

        print(f"Матрица {matrix_shape}:")
        print(matrix)
        print()


# Пример вызова функции с числом 12
build_matrices(12)


# Задание 6
class FileAnalyzer:
    def __init__(self, file_path):
        self.file_path = file_path
        self.data = None
        self.read_file()

    def read_file(self):
        try:
            with open(self.file_path, 'r', encoding='utf-8') as file:
                self.data = file.readlines()
        except FileNotFoundError:
            print(f"Файл {self.file_path} не найден.")
        except Exception as e:
            print(f"Произошла ошибка при чтении файла: {e}")

    def search_text(self, pattern):
        if self.data is None:
            print("Файл не был прочитан. Вызовите метод read_file() для чтения файла.")
            return []

        matches = []
        for line_number, line in enumerate(self.data, start=1):
            found = re.findall(pattern, line)
            if found:
                matches.append({
                    'line_number': line_number,
                    'matches': found
                })

        return matches


# Пример использования класса
file_analyzer = FileAnalyzer("path/to/your/file.txt")
file_analyzer.read_file()

if file_analyzer.data is not None:
    search_pattern = r'\b\w+ing\b'  # Пример паттерна поиска (найти слова, заканчивающиеся на "ing")
    search_results = file_analyzer.search_text(search_pattern)

    print(f"Результаты поиска для паттерна '{search_pattern}':")
    for result in search_results:
        print(f"В строке {result['line_number']}: {result['matches']}")


# Задание 7


def forward_prop(A, S, last=False):
    B = np.random.rand(S, len(A))
    Prod = np.dot(A, B)
    S = np.sum(Prod, axis=1)
    if not last:
        S = np.sin(S)
    else:
        S = np.maximum(S, 0)
    return S, B


S1, B1 = forward_prop(np.random.rand(5), 10)
S2, B2 = forward_prop(S1, 10)
S3, B3 = forward_prop(S2, 5, last=True)