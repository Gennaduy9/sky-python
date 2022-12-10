employees = [

 {"fio": "Киселёв Всеволод Эдуардович ", "vaccinated": True},
 {"fio": "Довлатова Эмилия Ефимовна", "vaccinated": False},
 {"fio": "Аверин Мартын Егорович", "vaccinated": True},
 {"fio": "Князева Августа Егоровна", "vaccinated": False},
 {"fio": "Шанская Аграфена Семёновна", "vaccinated": True},
 {"fio": "Куприна Марина Викторовна", "vaccinated": False},
 {"fio": "Селезнёв Константин Игоревич", "vaccinated": False},
]

vaccinated = []
not_vaccinated = []

for list_of_people in employees:
    if list_of_people["vaccinated"] == True:
        vaccinated.append(list_of_people["fio"])
    else:
        not_vaccinated.append(list_of_people["fio"])

print('Вакцинированные:')
[print(people) for people in vaccinated]

print("Остальные:")
[print(people) for people in not_vaccinated]

#vacc = "\n".join(vaccinated)
#not_vacc = "\n".join(not_vaccinated)
#print(f"Вакцинированные:\n{vacc}")
#print(f"Остальные:\n{not_vacc}")


