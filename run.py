from database.models import User
from getpass import getpass
from core import run_game

<<<<<<< HEAD
# User.create('hamidr1212e', '6546')
=======
>>>>>>> ef065dc394459fd67fe530a1c61521c8a1b29870

username = input("username : ")
password = getpass("password : ")


if User.login(username, password):
    print("login is successfuly")

    def main():
        run_game()
<<<<<<< HEAD

    if __name__ == '__main__':
        main()

else:
    print("username or password is wrong")
=======
>>>>>>> ef065dc394459fd67fe530a1c61521c8a1b29870

    if __name__ == '__main__':
        main()

else:
    print("username or password is wrong")
