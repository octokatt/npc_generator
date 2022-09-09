import json
import random

with open("descriptors.json", "r") as read_file:
    descriptors = json.load(read_file)

def appearance():
    return "funny"

def personality():
    return "nervous"

def interaction():
    rand = random.randint(0,len(descriptors["interaction traits"])-1)
    return descriptors["interaction traits"][rand]

def gender():
    genders = ["male", "female", "non-binary"]
    rand = random.randint(0,2)
    if rand == 0:
        return "man"
    elif rand == 1:
        return "woman"
    else:
        return "enby"

def create_description():
 #   description = appearance() + personality() + interaction()
    description = interaction() +" "+ gender()
    return description

current_description = create_description()
print(current_description)
