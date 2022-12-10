# Алгоритм 1

numbers = [1,2,3,4,5]

odd, even = [], []

for num in numbers:
    if num % 2 == 0:
        even.append(num)

for num in numbers:
    if num % 2 != 0:
        odd.append(num)


# Алгоритм 2
numbers = [1, 2, 3, 4, 5]

odd, even = [], []

for num in numbers:
    if num % 2 == 0:
        even.append(num)
    else:
        odd.append(num)

