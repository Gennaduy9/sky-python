fish = [

{"specie": "Белуга", "water": "fresh"},
{"specie": "Карась", "water": "fresh"},
{"specie": "Красноперка", "water": "fresh"},

{"specie": "Морской окунь", "water": "sea"},
{"specie": "Тунец", "water": "sea"},
{"specie": "Скумбрия", "water": "sea"},

]

sea_water = []
fresh_water = []

for new_fish in fish:
    if new_fish['water'] == 'fresh':
        fresh_water.append(new_fish['specie'])
    else:
        new_fish['water'] == 'sea'
        sea_water.append(new_fish['specie'])

print(f"Морские: {', '.join(sea_water)}")
print(f"Пресноводные: {', '.join(fresh_water)}")
