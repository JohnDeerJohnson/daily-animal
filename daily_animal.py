import random
import os
import datetime
import wikipedia

file_path = 'animal_list.txt'
shuffled_file = 'shuffled.txt'
lines = []

def file_write(arr):
    with open(shuffled_file, "w") as file:
        file.writelines(arr) 

def read_file(f):
    with open(f,'r') as file:
        a = file.readlines()
    return a

def shuffled (arr):
    shuffled = []
    while len(arr) > 0:
        rand_index = random.randrange(0,len(arr))
        shuffled.append(arr[rand_index])
        arr.pop(rand_index)
    return shuffled

def remove_animal (arr):
    date_file = 'date.txt'
    d = str(read_file(date_file))
    n = str(datetime.datetime.now().day) + str(datetime.datetime.now().month)
    d = d.replace("[","")
    d = d.replace("]","")
    d = d.replace("'","")
    d = d.replace('n','')
    d = d.replace('/','')
    if(n != d):
        arr.pop(0)
        with open(date_file,'w') as file:
            file.write(n)
        file_write(arr)

def wiki(arr):
    result = wikipedia.summary(str(arr[0]),sentences = 8) 
    print("Here is a small section of the animals wiki!")
    print(result)

if os.path.isfile(shuffled_file):
    lines = read_file(shuffled_file)
else:
    lines = read_file(file_path)
    lines = shuffled(lines)
    file_write(lines)

try: 
    print('The animal of the day is', lines[0])
    remove_animal(lines)
    wiki(lines)
except IndexError:
    print('You have exhausted all listed animals. You are now the animal master!')

