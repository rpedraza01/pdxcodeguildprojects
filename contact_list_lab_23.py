#contact_list_lab_23.py
import csv, os


with open('contacts_list.csv', 'r') as file:
    lines = file.read().split('\n')
    print(lines)
    # print(file)

def new_user(lines):
    user = ""
    name = input("What's your name? > ")
    user += name + ','
    fav_fruit = input("What's your favorite fruit? > ")
    user += fav_fruit + ','
    fav_color = input("What's your favorite color? > ")
    user += fav_color
    lines.append(user)
    print(lines)

# new_user(lines)

def retrieve_user(lines):
    name = input("Who're you trying to find? > ")
    for each in lines:
        each = each.split(',')
        if each[0] == name:
            print(each)


# retrieve_user(lines)

def update_record(lines):
    name = input("Which user are you looking for? > ")
    attribute = input("Which attribute would you like to change? > ")
    record = 0
    for each in lines:
        each = each.split(',')
        if each[0] == name:
            if attribute == "favorite color":
                change_to = input("What should the new favorite color be? > ")
                each[2] = change_to
                each = ",".join(each)
                lines[record] = each
                print(lines)
                return
            elif attribute == "favorite fruit":
                change_to = input("What should the new favorite fruit be? > ")
                each[1] = change_to
                each = ",".join(each)
                lines[record] = each
                print(lines)
                return
        record += 1

# update_record(lines)

def delete_record(lines):
    name = input("Which user are you looking to delete? > ")
    for each in lines:
        each = each.remove()
        if each[0] == name:
            print("User deleted.")

delete_record(lines)