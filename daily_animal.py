import os
import wikipedia
import numpy as np

file_path = os.path.join(os.path.dirname(__file__), 'animal_list.txt')
lines = []

def read_file(f):
    with open(f,'r') as file:
        a = file.readlines()
    return a

def shuffled(arr):
    np.random.shuffle(arr)
    return arr

def wiki(arr):
    try:
        result = wikipedia.summary(str(arr[0]),sentences = 8) 
        print("Here is a small section of the animals wiki!")
        print(result)
    except Exception:
        print("An error occurred while fetching the Wikipedia summary")

lines = read_file(file_path)
lines = shuffled(lines)

print('The animal of the day is', lines[0])
wiki(lines)
