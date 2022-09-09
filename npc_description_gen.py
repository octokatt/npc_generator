import json
import random

with open("descriptors.json", "r") as read_file:
    descriptors = json.load(read_file)

def get_appearance():
    rand = random.randint(0,len(descriptors["appearance"])-1)
    return descriptors["appearance"][rand]

def get_interaction():
    rand = random.randint(0,len(descriptors["interaction traits"])-1)
    return descriptors["interaction traits"][rand]

def get_gender():
    rand = random.randint(0,len(descriptors["genders"])-1)
    return descriptors["genders"][rand]

def get_quirk():
    rand = random.randint(0,len(descriptors["talents"])-1)
    return descriptors["talents"][rand]    

def create_description():
 #   description = appearance() + personality() + interaction()
    description = "a "+ get_interaction() +" "+ get_gender()
    description += " who looks "+ get_appearance()
    description += " and is known for being " + get_quirk()
    return description

# current_description = create_description()
# print(current_description)
