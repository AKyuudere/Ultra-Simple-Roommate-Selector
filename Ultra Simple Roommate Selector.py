# Name: ultra Simple Roommate Selector
# By: J.Pak

import json

mem_data = {}

# Looking for Roommate or Registering as Potential Roommate
# Registering adds new user entry into "member_data.json"


def roommate_selection():
    status = 'true'
    print("Welcome to the roommate selection process!")
    print("If you are looking for a roommate, type 'look': ")
    print("If you are registering as an available roommate, type 'register': ")
    while status == 'true':
        a = input("Enter here: ")
        if a.lower() not in ('look', 'register'):
            print("Please enter 'look' or 'register'!")
        elif a == 'register':
            status = 'false'
            register_process()
        elif a == 'look':
            status = 'false'
            find_process()


# Questions that are asked to roommates
def register_process():
    gen_status = 'false'
    hyg_status = 'false'
    smo_status = 'false'
    pet_status = 'false'
    alc_status = 'false'
    gue_status = 'false'
    sha_status = 'false'
    a = input("Please enter your name: ")
    mem_data['name'] = a
    while gen_status == 'false':
        gen = input("What is your gender?: male, female, or other?: ")
        if gen.lower() not in ('male', 'female', 'other'):
            print("Enter 'male', 'female', or 'other'!")
        elif gen == 'female':
            gen_status = 'true'
            mem_data['gender'] = 'femal'
        elif gen == 'male':
            gen_status = 'true'
            mem_data['gender'] = 'male'
        elif gen == 'other':
            gen_status = 'true'
            mem_data['gender'] = 'other'
    while hyg_status == 'false':
        hyg = input("How much do you care about hygiene?: little, average, or lot?: ")
        if hyg.lower() not in ('little', 'average', 'lot'):
            print("Enter 'little', 'average', or 'lot'!")
        else:
            hyg_status = 'true'
            mem_data['hygiene'] = hyg
    while smo_status == 'false':
        smo = input("Your thoughts on smoking: yes or no: ")
        if smo.lower() not in ('yes', 'no'):
            print("Enter 'yes' or 'no'!")
        else:
            smo_status = 'true'
            mem_data['smoking'] = smo
    while pet_status == 'false':
        pet = input("Are pets allowed?: yes or no: ")
        if pet.lower() not in ('yes', 'no'):
            print("Enter 'yes' or 'no'!")
        else:
            pet_status = 'true'
            mem_data['pets'] = pet
    while gue_status == 'false':
        gue = input("Are Guests a yes or no?: ")
        if gue.lower() not in ('yes', 'no'):
            print("Enter 'yes' or 'no'!")
        else:
            gue_status = 'true'
            mem_data['guests'] = gue
    while sha_status == 'false':
        sha = input("How do you feel about sharing?: yes or no: ")
        if sha.lower() not in ('yes', 'no'):
            print("Enter 'yes' or 'no'!")
        else:
            sha_status = 'true'
            mem_data['sharing'] = sha
    while alc_status == 'false':
        alc = input("Thoughts on alcohol: yes or no: ")
        if alc.lower() not in ('yes', 'no'):
            print("Enter 'yes' or 'no'!")
        else:
            alc_status = 'true'
            mem_data['alcohol'] = alc
            print(f"Congratulations, Registrations for {a} has been completed!")
            with open("member_data.json") as f:
                lists = json.load(f)
                lists.append(mem_data)
            with open("member_data.json", 'w') as f:
                json.dump(lists, f, indent=4)
    ending()


# Registered users are searched for in database
def find_process():
    global z
    global data
    global look_name
    gi_status = 'false'
    status = 'false'
    with open('member_data.json', 'r') as read:
        data = json.load(read)
    while status == 'false':
        look_name = input("What is your registered name?(CASE SENSITIVE): ")
        try:
            z = list(filter(lambda data: data['name'] == look_name, data))
            if look_name in z[0]['name']:
                print("User Found")
                status = 'true'
                while gi_status == 'false':
                    a = input("Do you care which gender you are put in with?: Yes or No:  ")
                    if a.lower() not in ('yes', 'no'):
                        print("Yes or No!")
                    elif a.lower() == 'yes':
                        gi_status = 'true'
                        check_process()
                    elif a.lower() == 'no':
                        gi_status = 'true'
                        check_process_gi()
        except IndexError:
            print("User not found")


# Potential Roommates are looked for by gender
def check_process():
    temp_value = []
    potential_rm = []

    e = z[0]
    for key in e.keys():
        temp_value.append(e[key])
    temp_value.pop(0)
    for p in data:
        if temp_value[0] in p['gender'] and temp_value[1] in p['hygiene'] and temp_value[2] in p['smoking'] and temp_value[3] in p['pets'] and temp_value[4] in p['alcohol']:
            potential_rm.append(p['name'])
    plength = len(potential_rm)
    potential_rm.remove(f'{look_name}')
    print(f"You have {plength-1} potential roommates, they are: ")
    print(*potential_rm)
    ending()


# Potential Roommate Gender Inclusive
def check_process_gi():
    temp_value = []
    potential_rm = []

    e = z[0]
    for key in e.keys():
        temp_value.append(e[key])
    temp_value.pop(0)
    for p in data:
        if temp_value[1] in p['hygiene'] and temp_value[2] in p['smoking'] and temp_value[3] in p['pets'] and temp_value[4] in p['alcohol']:
            potential_rm.append(p['name'])
    plength = len(potential_rm)
    potential_rm.remove(f'{look_name}')
    print(f"You have {plength-1} potential roommates, they are: ")
    print(*potential_rm)
    ending()


def ending():
    print("Do you want to quit?")
    quits = input("'Yes' to exit or 'No' to go back: ")
    if quits.lower() not in ("yes", "no"):
        print("Type yes or no!")
        ending()
    elif quits.lower() == 'yes':
        return
    elif quits.lower() == 'no':
        roommate_selection()


roommate_selection()
