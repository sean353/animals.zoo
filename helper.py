import json
from icecream import ic


def delete_Animal(animals):
    
    search_id = input("Enter Animal number: ")
    for animal in animals:
        if animal.get("Animal number") == search_id:
            animals.remove(animal)
            print(f"Animal with number {search_id} has been deleted.")
            return
        
    print("Cannot find your Animal...")


def exitanimal(animals,my_data_file):
    json_string = json.dumps(animals)
    # save the list in a file
    with open(my_data_file, 'w') as file:
        file.write(json_string)
    
    ic("see ya")
    exit()


   


   

