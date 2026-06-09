import csv
import random
import datetime
import re

line_count = 1
max_row = 221
x = datetime.datetime.now()
seed = x.day - x.month + x.year
random.seed(seed)
random_row = random.randint(1,max_row)

with open('animal_list.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        if line_count == random_row:
            print("The date today is ",x.month,"/",x.day,"/",x.year)
            animal = str(row)
            animal = animal.replace("[","")
            animal = animal.replace("]","")
            animal = animal.replace("'","")
            print("Your animal for today is",animal)
            break
        line_count += 1
