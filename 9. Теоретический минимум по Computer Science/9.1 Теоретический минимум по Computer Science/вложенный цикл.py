max_number = 3

for row in range(2, max_number + 1):
    for column in range(2, max_number + 1):
        print(row * column, end='  ')
    print()