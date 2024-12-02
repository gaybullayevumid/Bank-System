from os import write

username = input("Create username: ")
password = input("Create password: ")

def create_user(user, pas):
    with open("user_register.txt", "w") as file:
        user_info = file.write(f"Username: {username}\n")
        user_password = file.write(f"Password: {password}")

create_user(username, password)