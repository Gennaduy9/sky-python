import os

directory = "inner"
filename = "lesson6/1.txt"

path = os.path.join(directory, filename)

with open(path, "r", encoding='utf-8') as file:
    file_content = file.read().strip()

data_split = file_content.split(" ")

x = data_split[0]
y = data_split[1]
z = data_split[2]

print(x,y,z, sep="\n---\n")
