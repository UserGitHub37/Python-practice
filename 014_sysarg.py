import sys

# Пример: Вывод всех переданных аргументов
print("Имя скрипта:", sys.argv[0])
print("Переданные аргументы:", sys.argv[1:])
print("Тип -", type(sys.argv))

# Пример: Обработка аргументов
if len(sys.argv) > 1:
    print("Первый аргумент:", sys.argv[1])
else:
    print("Аргументы не переданы.")

# $ python.exe ./014_sysarg.py test1 test2 test3
# Имя скрипта: ./014_sysarg.py
# Переданные аргументы: ['test1', 'test2', 'test3']
# Тип - <class 'list'>
# Первый аргумент: test1
