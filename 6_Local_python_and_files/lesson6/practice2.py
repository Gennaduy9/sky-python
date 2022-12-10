# Напишите функцию load_list_from_file(path)
# которая получает из файла, путь которого передан,
# список и возвращает его в виде типа list.

def load_list_from_file(path):
    lines = []
    with open(path) as file:
        for line in file:
            value = int(line.strip())
            lines.append(value)
    return lines

result = load_list_from_file("2.txt")
print(result)



