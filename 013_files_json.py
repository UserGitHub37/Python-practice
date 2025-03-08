import json

'''dump/load: Когда нужно работать с файлами (например, сохранять или загружать данные в/из файла).

dumps/loads: Когда нужно работать со строками (например, передавать JSON по сети или обрабатывать JSON-строки в памяти).'''

'''----------------------------------------------------------------------------------------'''

# Исходный объект Python
data = {"name": "Alice", "age": 25}

# Сериализация в файл
with open('013_files_data.json', 'w') as file:
    json.dump(data, file, indent=4)

# Десериализация из файла
with open('013_files_data.json', 'r') as file:
    data_from_file = json.load(file)
    print("Объект из файла:", data_from_file)


#https://docs-python.ru/standart-library/modul-json-python/funktsija-dumps-modulja-json/

# лайфаки
# 1- синхронизация через файлы
# 2 - конфиг хранить в словаре или json файле