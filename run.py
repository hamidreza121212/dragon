from database.models import User
from getpass import getpass
from core import run_game

username = input("username : ")
password = getpass("password : ")

print(User.login(username, password))


# if User.login(username, password):
#     print("login is successfuly")

#     def main():
#         run_game()

#     if __name__ == '__main__':
#         main()

# else:
#     print("username or password is wrong")


