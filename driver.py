# Name: Chris Wu
# Student number: A01256284

# Name: Sarvenaz Mohammadi
# Student number: A01158179

# Set: D

from main_menu import MainMenu
from controller import Controller


def main():
    Controller.load_users(MainMenu.user_list)
    MainMenu.welcome()


if __name__ == '__main__':
    main()
