list_numbers = [2, 90, -2, 8, -36, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# Создаем две переменные: для максимального индекса и для текущего максимального числа
max_index = 0
max_number = list_numbers[max_index]

# Запускаем перебор
for current_index, current_number in enumerate(list_numbers):  # перебираем пары индекс - число
    if current_number >= max_number:  # если текущее число больше принятого в max_number
        max_index = current_index  # то перезаписываем индекс
        max_number = current_number  # и само число в переменной max_number

# Меняеем местами последний максимальный и последний элементы в списке
list_numbers[-1], list_numbers[max_index] = list_numbers[max_index], list_numbers[-1]

print(list_numbers)  # Ответ [2, 90, -2, 8, -36, -44, -1, -85, -14, 25, -22, -90, -100, -8, 38, -92, -45, 67, 53, 90]
