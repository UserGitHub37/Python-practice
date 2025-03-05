list_1 = [5, 2, 1, 6, 4, 9, 5, 4, 3, 8, 10, 7, 1, 3]
list_2 = [1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
list_3 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0]

def sort_bubble(list):
    print(f"\n{list} Не отсортированный список")

    list_length = len(list)
    j = 0
    iteration_counter = 0
    change_counter = 0

    while j < list_length - 1:
        listIs_changed = False
        i = 0
        while i < list_length - 1:
            iteration_counter += 1
            num_1 = list[i]
            num_2 = list[i + 1]
            if num_1 > num_2:
                change_counter += 1
                list[i] = num_2
                list[i + 1] = num_1
                listIs_changed = True
            i += 1
        if listIs_changed == False:
            break
        j += 1

    print(list, "Отсортированный список")
    print("Количество итераций:", iteration_counter)
    print("Количество изменений списка:", change_counter, "\n")

sort_bubble(list_1)
sort_bubble(list_2)
sort_bubble(list_3)