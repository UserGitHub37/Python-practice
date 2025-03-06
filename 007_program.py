# Пример программы
def process_data(data):
    print(data, "- исходные данные")
    # Разделяем строку по запятым и получаем из строки список
    items = data.split(",")
    print(items, "- получаем список")

    # Создаем словарь для подсчета элементов
    count_dict = {}

    # Перебираем список и считаем количество каждого элемента в списке
    for item in items:
        item = item.strip().lower()  # Убираем пробелы и приводим к нижнему регистру
        if item in count_dict:
            count_dict[item] += 1
        else:
            count_dict[item] = 1

    # Перебираем словарь для вывода результата
    for key, value in count_dict.items():
        print(f"{key}: {value}")


# Входные данные
input_data = "  apple, banana , Apple, Orange , banana, apple "
process_data(input_data)