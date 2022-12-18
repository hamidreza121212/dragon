from database.models import User


# User.create('hamidreza121212', '1234')

user = User.read('hamidreza121212')
print(user[0].username)


# from core import run_game


# def main():
#     run_game()


# if __name__ == '__main__':
#     main()


