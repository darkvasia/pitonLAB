import csv
from collections import defaultdict

# Ініціалізація

file_name = 'база_даних_автомобілів.csv'
headers = ['Марка', 'Модель', 'Рік', 'Колір']
cars = [
    {'Марка': 'Toyota', 'Модель': 'Corolla', 'Рік': '2005', 'Колір': 'червоний'},
    {'Марка': 'Hyundai', 'Модель': 'Elantra', 'Рік': '2018', 'Колір': 'синій'},
    {'Марка': 'Ford', 'Модель': 'Focus', 'Рік': '2012', 'Колір': 'білий'},
    {'Марка': 'BMW', 'Модель': 'X5', 'Рік': '2016', 'Колір': 'чорний'},
    {'Марка': 'Mercedes', 'Модель': 'C-Class', 'Рік': '2020', 'Колір': 'сріблястий'}
]

# Створення бази даних

with open(file_name, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.DictWriter(file, fieldnames=headers)
    writer.writeheader()
    writer.writerows(cars)  # Запис автомобілів одразу при створенні файлу

# Читання бази даних

print("База даних автомобілів:")
with open(file_name, mode='r', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(f"{row['Марка']} {row['Модель']} {row['Рік']} {row['Колір']}")

# Оновлення записів

cars_updated = []
change_field = {'Марка': 'Ford', 'Модель': 'Focus'}
new_data = {'Колір': 'зелений'}

with open(file_name, mode='r', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    for row in reader:
        if row['Марка'] == change_field['Марка'] and row['Модель'] == change_field['Модель']:
            row.update(new_data)
        cars_updated.append(row)

with open(file_name, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.DictWriter(file, fieldnames=headers)
    writer.writeheader()
    writer.writerows(cars_updated)

# Видалення запису

cars_remaining = []
remove_criteria = {'Марка': 'Toyota', 'Модель': 'Corolla'}

with open(file_name, mode='r', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    for row in reader:
        if row['Марка'] == remove_criteria['Марка'] and row['Модель'] == remove_criteria['Модель']:
            continue
        cars_remaining.append(row)

with open(file_name, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.DictWriter(file, fieldnames=headers)
    writer.writeheader()
    writer.writerows(cars_remaining)

# Статистика

brand_years = defaultdict(list)

with open(file_name, mode='r', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    for row in reader:
        brand_years[row['Марка']].append(int(row['Рік']))

for brand, years in brand_years.items():
    average_year = sum(years) / len(years)
    print(f"Марка: {brand}, Середній рік випуску: {average_year:.2f}")
