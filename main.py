
from _datetime import datetime
import random

print("/Welcome to health management system."
      "Here we record your daily food consumption, exercise you performed and your mental health."
      )

f2 = open("Users.txt", "r+")
users = f2.readlines()
f2.close()

def create_new_user():
    global user_id
    name= input("Enter your name: ")
    age= input("Enter your age: ")
    gender = input("Enter your gender: (M/F/prefer not to say)")
    user_id = input("Create your user id: ")

    if f"{user_id}\n" in users:
        print("User already Exists")
        exit()
    else:
        pass
    f = open(f"{user_id}.txt","w")
    f.write(f"Name:  {name}\n")
    f.write(f"Age: {age}\n")
    f.write(f"Gender: {gender}\n")
    f.write(f"User id: {user_id}\n")
    f.write(f"User id created at {datetime.now()}\n\n\n")
    f.write("Below is your entered data: \n\n\n")
    f.close()

    f1 = open("user_created_till.txt","a")
    f1.write(f"User id: {user_id} created at {datetime.now()}\n")
    f1.close()
    f2 = open("Users.txt","a")
    f2.write(f"{user_id}\n")
    f2.close()



def input_data():
    f1 = open(f"{user_id}.txt","a")
    while True:
        what_data= input("What data do you want to input? Food, exercise or mental health? (F/E/M): ")
        if what_data.upper() == "F":
            what_food = input("What did you eat? Write name of food and amount.:   ")
            f1.write(f"food : {what_food} at {datetime.now()}\n")
        elif what_data.upper() == "E":
            what_exercise = input("What exercise did you do?   ")
            f1.write(f"Exercise : {what_exercise} at {datetime.now()}\n")
        elif what_data.upper() == "M":
            how_are_ya = input("How are you feeling today? ")
            f1.write(f"Mental Health: Felt {how_are_ya} at {datetime.now()}\n")

        else:
            print(f"Invalid input \"{what_data}\"!!!")

        con = input("Do you want to continue ? (Y/N): ")
        if con.upper() == "Y":
            continue
        else:
            f1.close()
            exit()


def output_data():
    while True:
        user = input("Enter your username: ")
        if f"{user}\n" in users:
            f = open(f"{user}.txt")
            print("Your data is given below: \n\n")
            print(f.read())
            f.close()
            exit()
        else:
            print("Invalid user id!!! Retry")
            continue




def old_user():
    try:
        with open(f"{user_id}.txt") as f:
            pass
        task = input("Do you want to Input information or Access your data ? (I for input O for access data)")
        if task.upper() == "I":
            input_data()
        elif task.upper() == "O":
            output_data()


    except Exception as e:
        print("User not valid!!!")
        create = input("Do you want to create a new user id ?(Y/N)")
        if create.upper() == "Y":
            create_new_user()
            print("New User Created.")
            inn = input("Do you want to input data ? (Y/N)")
            if inn.upper() == "Y":
                input_data()
            else:
                exit()

        else:
            exit()



while True:
    is_new = input("Are you a new user ?(Y/N): ")
    if is_new.upper() == "Y":
        create= input("Do you want to create a new user id ?(Y/N): ")
        if create.upper() == "Y":
            create_new_user()
            print("New User Created.")
            inn = input("Do you want to input data ? (Y/N)")
            if inn.upper() == "Y":
                input_data()
            else:
                exit()
        else:
            exit()
    elif is_new.upper() =="N":
        user_id = input("Enter your user id: ")
        old_user()
        exit()

    else:
        print("not valid!!!")

    con = input("Do you want to continue ? (Y/N): ")

    if con.upper() == "Y":
        continue
    else:
        exit()