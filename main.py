from time import sleep
import random
import requests
from bs4 import BeautifulSoup
import json
import csv


with open("table.html") as file:
    src = file.read()
    soup = BeautifulSoup(src, 'lxml')
 
table_head = soup.find(class_='norm').find('tr').find_all('td')
#print(table_head)
product = table_head[0].text
proteins = table_head[2].text
fats = table_head[3].text
calories = table_head[1].text
carbohydrates = table_head[4].text

headtitle = table_head[0].text

with open('table.csv', 'w', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(
        (
        product,
        calories,
        proteins,
        fats,
        carbohydrates
        )
    )


products_data = soup.find_all(class_='norm')
#print(products_data)
product_info = [] #делаем json

for table in products_data:
    for item in table:
        product_tds = item.find_all('td')
        title = product_tds[0].text
        calories = product_tds[1].text
        proteins = product_tds[2].text
        fats = product_tds[3].text
        carbohydrates = product_tds[4].text.strip() 
        
        if title != headtitle:

            product_info.append(   #добавляем для json
                {
                'Title': title,
                'Calories': calories.strip(),
                'Proteins': proteins.strip(),
                'Fats': fats.strip(),
                'Carbohydrates': carbohydrates.strip()
                }
            )

            with open('table.csv', 'a', encoding='utf-8') as file:
                writer = csv.writer(file)
                writer.writerow(
                    (
                    title,
                    calories,
                    proteins,
                    fats,
                    carbohydrates
                    )
                )
with open(f'products.json', 'a', encoding='utf-8') as file:
            json.dump(product_info, file, indent=4, ensure_ascii=False)        