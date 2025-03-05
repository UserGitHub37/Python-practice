#li = [5, 2, 1, 6, 4, 9, 5, 4, 3, 8, 10, 7, 1, 3]
li = [1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
# li = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0]
print(li, "Не отсортированный список")

listLength = len(li)

j = 0
iterationCounter = 0
changeCounter = 0
while j < listLength - 1:
    listIsChanged = False
    i = 0
    while i < listLength - 1:
        iterationCounter += 1
        num1 = li[i]
        num2 = li[i + 1]
        if num1 > num2:
            changeCounter += 1
            li[i] = num2
            li[i + 1] = num1
            listIsChanged = True
        i += 1
    if listIsChanged == False:
        break
    j += 1

print(li, "Отсортированный список")
print("Количество итераций", iterationCounter)
print("Количество изменений списка:", changeCounter)