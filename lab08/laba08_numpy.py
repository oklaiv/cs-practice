import numpy as np

print("="*50)
print("ЗАДАНИЕ 1. Создание векторов и матриц")
print("="*50)
hours = np.arange(0, 22, 3)
line = np.linspace(0, 1, 5)
zeros = np.zeros(6, dtype=int)
unknown_table = np.full((2, 3), -1)
identity = np.eye(3)


print(f"hours: {hours}")
print(f"shape: {hours.shape}, ndim: {hours.ndim}, size: {hours.size}, dtype: {hours.dtype}")
print(f"line: {line}")
print(f"zeros: {zeros}")
print(f"unknown_table:\n{unknown_table}")
print(f"identity:\n{identity}")


print("\n" + "="*50)
print("ЗАДАНИЕ 2. Индексы и срезы в векторе")
print("="*50)
print(f"Третий элемент (индекс 2): {hours[2]}")
print(f"Последний элемент: {hours[-1]}")
print(f"Элементы с индексами 2-5 (срез [2:6], т.к. правая граница не входит): {hours[2:6]}")
print(f"Каждый второй элемент (шаг 2): {hours[::2]}")
print(f"Массив в обратном порядке: {hours[::-1]}")


print("\n" + "="*50)
print("ЗАДАНИЕ 3. Строки и столбцы таблицы")
print("="*50)
temperatures = np.array([
    [12, 14, 13, 15],
    [11, 13, 16, 17],
    [10, 12, 15, 18],
])

print(f"Форма: {temperatures.shape}, размерность: {temperatures.ndim}, элементов: {temperatures.size}")
print(f"Значение из 2-й строки и 3-го столбца: {temperatures[1, 2]}")
print(f"Первая строка: {temperatures[0]}")
print(f"Последний столбец: {temperatures[:, -1]}")
print(f"Первые две строки без первого столбца:\n{temperatures[:2, 1:]}")
center_fragment = temperatures[0:2, 1:3]
print(f"Центральный фрагмент 2x2:\n{center_fragment}")
print(f"Проверка формы фрагмента: {center_fragment.shape}")


print("\n" + "="*50)
print("ЗАДАНИЕ 4. Прямоугольные срезы")
print("="*50)
matrix = np.arange(1, 26).reshape(5, 5)
print(f"Исходная матрица:\n{matrix}")

print(f"\nПервые три строки:\n{matrix[:3]}")
print(f"shape: {matrix[:3].shape}")

print(f"\nПоследние две строки:\n{matrix[-2:]}")
print(f"shape: {matrix[-2:].shape}")

print(f"\nПервые два столбца:\n{matrix[:, :2]}")
print(f"shape: {matrix[:, :2].shape}")


print(f"\nФрагмент из строк 1-3 и столбцов 2-4:\n{matrix[1:4, 2:5]}")
print(f"shape: {matrix[1:4, 2:5].shape}")


print(f"\nУгловой блок 2x2 в правом нижнем углу:\n{matrix[-2:, -2:]}")
print(f"shape: {matrix[-2:, -2:].shape}")


print("\n" + "="*50)
print("ЗАДАНИЕ 5. Изменение массива с помощью срезов")
print("="*50)

changed_hours = hours.copy()
print(f"Исходный hours до изменений: {hours}")


changed_hours[2:5] = 99
changed_hours[::2] = -1

print(f"changed_hours после изменений: {changed_hours}")
print(f"Исходный hours после изменений: {hours}")

print("\n--- Матрица ---")
changed_matrix = matrix.copy()
changed_matrix[1, :] = 0
# Последний столбец на -1
changed_matrix[:, -1] = -1
# Центральный блок 3x3 (строки 1:4, столбцы 1:4) на 100
changed_matrix[1:4, 1:4] = 100

print(f"Измененная матрица:\n{changed_matrix}")
print(f"Исходная матрица (должна остаться прежней):\n{matrix}")


print("\n" + "="*50)
print("ЗАДАНИЕ 6. Изменение формы")
print("="*50)
numbers = np.arange(12)
print(f"Исходный numbers: {numbers}")
print(f"Форма numbers: {numbers.shape}")

table = numbers.reshape(3, 4)
print(f"\ntable (3, 4):\n{table}")
print(f"Форма table: {table.shape}")


transposed = table.T
print(f"\ntransposed (.T):\n{transposed}")
print(f"Форма transposed: {transposed.shape}")
#лабораторная готова
