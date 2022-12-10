

raw_list = ["сельдь-черноспинка", "морская камбала", "тунец", "ставрида", "морской окунь", "треска", "сайра",
"морская камбала", "ставрида", "треска", "треска", "треска", "тунец", "ставрида", "морская камбала",
"тунец", "морская камбала", "морская камбала", "морская камбала", "морская камбала", "тунец",
           ]
unique_list = []
unique_list = set(raw_list)

#fish = sorted(list(unique_list))  так тоже правильно и короче код

unique_list = list(unique_list)
unique_list.sort()

print(f"Всего {len(unique_list)} видов рыб")

for new_list in unique_list:
    print(new_list)