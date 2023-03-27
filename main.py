import os
import random
from art import logo, vs
from game_data import data

print("DAY 14")
flag = True


def get_random(d):
    l = random.choice(d)
    return l


def format_data(l1):
    name = l1["name"]
    profession = l1["description"]
    country = l1["country"]
    return f"{name}, a {profession}, from {country}"


def get_followers(l):
    for i in l:
        if i == 'follower_count':
            return l[i]


def compare(f1, f2):
    x = get_followers(f1)
    y = get_followers(f2)
    if x > y:
        if choice == 'A':
            return 1
        else:
            return 0
    elif x < y:
        if choice == 'B':
            return 1
        else:
            return 0


print(logo)
count = 0
data_list1 = get_random(data)
data_list2 = get_random(data)
while flag:
    os.system('cls')
    while data_list1 == data_list2:
        data_list2 = get_random(data)
    print(f"Compare A: {format_data(data_list1)}")
    print(vs)
    print(f"Against B: {format_data(data_list2)}")
    choice = input("Who has more followers? Type 'A' or 'B': ").upper()
    result = compare(data_list1, data_list2)
    if result == 1:
        count += 1
        print(f"You're right! Current score: {count}")
        if choice == 'A':
            data_list2 = get_random(data)
        else:
            data_list1 = get_random(data)
    else:
        print(f"Sorry, that's wrong. Final score: 1")
        c = input("Do you want to continue(y/n): ").upper()
        if c == 'N':
            flag = False
