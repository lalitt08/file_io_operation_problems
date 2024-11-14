import random
import json
all_birthdays = []

for i in range(50):
    month = random.randint(1, 12)
    year = random.randint(92, 93)
    
    if month in [4, 6, 9, 11]:
        day = random.randint(1, 30)
    elif month == 2:
        day = random.randint(1, 28)
    else:
        day = random.randint(1, 31)
    
    birthday = f"Person {i+1}: {day:02d}-{month:02d}-{year}"
    all_birthdays.append(birthday) 

month_lists = {}
for i in range(1, 13): 
    month_lists[i] = []

for i in all_birthdays:
    month = int(i.split('-')[1])
    month_lists[month].append(i)


with open('similar_month_py.json', 'w') as f1:
    json.dump(month_lists, f1, indent=4)