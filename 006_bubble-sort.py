li = [5, 2, 1, 6, 4, 9, 5, 4, 3, 8, 10, 7, 1, 3]
print(li)

listLength = len(li)

j = 0

while j < listLength - 1:
    i = 0
    while i < listLength - 1:
        num1 = li[i]
        num2 = li[i + 1]
        if num1 > num2:
            li[i] = num2
            li[i + 1] = num1
        i += 1
    j += 1

print(li)
