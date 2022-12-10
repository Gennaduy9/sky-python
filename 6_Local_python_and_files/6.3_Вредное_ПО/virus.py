
virus_code = 'print("Я вирус!")'

with open('answers0.py', 'a', encoding='utf-8') as file:
    file.write(f"\n{virus_code}\n")