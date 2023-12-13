from enum import Enum
import json
import os
from helper import delete_Animal, exitanimal
from icecream import ic


class Actions (Enum):
    PRINT = 1
    ADD = 2
    SEARCH = 3
    DELETE = 4
    EXIT = 5

   
animals=[]
my_data_file = 'animals.json'

def menu():
    for x in Actions:
        ic(f'{x.value} - {x.name}')

    return Actions(int(input("Enter your selection:")))
    
def load_data(my_data_file):# load a list from a file
    global animals
    try:
        with open(my_data_file, 'r') as file:
            json_string = file.read()
            animals = json.loads(json_string)
    except: pass
    
    
def main():
    os.system('cls' if os.name == 'nt' else 'clear')# clear screen
    load_data(my_data_file) #load data from a file


    while(True):
        userselection= menu () #display a menu and get user selection and  implements menu
        if userselection == Actions.EXIT:exitanimal(animals,my_data_file)
        if userselection == Actions.PRINT:ic(animals)
        if userselection == Actions.ADD:add_animal()
        if userselection == Actions.SEARCH: search_animal()
        if userselection == Actions.DELETE: delete_Animal(animals)
       

def add_animal():
    animals.append({"Name":input("Enter your name:"),"Type":input("Enter your Type:"), "Age":input("Enter your Age:"),"Animal number":input("Enter your Animal number:")})


def search_animal():
    global animals
    
    search_id = input("Enter your Animal number:")
    for animal in animals:

        if animal.get("Animal number")== search_id:
            ic(animals)
            return 
    ic("Cannot find your Animal :)")
    return






   
















    
    
    
   
if __name__ == "__main__":
    main() 