from angel import Angel
from bank_account import BankAccount
from budget_type import BudgetType
from troublemaker import TroubleMaker
from rebel import Rebel
from budget import Budget
from enum import Enum


class UserType(Enum):
    ANGEL = "Angel"
    TROUBLE_MAKER = "Trouble Maker"
    REBEL = "Rebel"


class UserGenerator:
    """
    The UserGenerator generates a list of test users.
    """

    def __init__(self):
        pass

    @staticmethod
    def generate_users():
        """
        Return a list of users with dummy data.

        :return: a list of users
        """
        user_list = [

            Angel("Jeff", 20, [Budget(BudgetType.GAMES, 100),
                               Budget(BudgetType.CLOTHING, 100),
                               Budget(BudgetType.FOOD, 100),
                               Budget(BudgetType.MISC, 100)], BankAccount(1000, "CIBC", "1111")),

            TroubleMaker("Lawrence", 20, [Budget(BudgetType.GAMES, 100),
                                          Budget(BudgetType.CLOTHING, 100),
                                          Budget(BudgetType.FOOD, 100),
                                          Budget(BudgetType.MISC, 100)],
                         BankAccount(1000, "CIBC", "2222")),

            Rebel("Chrissy", 20, [Budget(BudgetType.GAMES, 100),
                                  Budget(BudgetType.CLOTHING, 100),
                                  Budget(BudgetType.FOOD, 100),
                                  Budget(BudgetType.MISC, 100)], BankAccount(1000, "CIBC", "3333")),

        ]
        return user_list

    @staticmethod
    def generate_user():
        """
        Generates a user based on user input.

        :return:  a user based on user input
        """
        while True:
            option = input(
                "\nEnter the type of user you would like to generate.\n1. Angel\n2. Trouble Maker\n3. Rebel\n")

            if option == "1":
                return UserGenerator._create_user(UserType.ANGEL)
            elif option == "2":
                return UserGenerator._create_user(UserType.TROUBLE_MAKER)
            elif option == "3":
                return UserGenerator._create_user(UserType.REBEL)
            else:
                print("\nInvalid item type. Enter either 1, 2 or 3")

    @staticmethod
    def _create_user(user_type):

        name = UserGenerator._acquire_name()
        age = UserGenerator._acquire_age()
        budget_list = UserGenerator._acquire_budgets()
        balance = UserGenerator._acquire_balance()
        bank_name = UserGenerator._acquire_bank_name()
        bank_number = UserGenerator._acquire_bank_number()
        bank_account = BankAccount(balance, bank_name, bank_number)

        match user_type:
            case UserType.ANGEL:
                return Angel(name, age, budget_list, bank_account)
            case UserType.TROUBLE_MAKER:
                return TroubleMaker(name, age, budget_list, bank_account)
            case UserType.REBEL:
                return Rebel(name, age, budget_list, bank_account)
            case _:
                raise Exception("Invalid User Type")

    @staticmethod
    def _acquire_bank_number():
        while True:
            bank_number = input("Enter the user's bank number: ")
            if bank_number.isdigit():
                break
            else:
                print("A valid bank number must contain only digits.")
        bank_number = int(bank_number)
        return bank_number

    @staticmethod
    def _acquire_bank_name():
        while True:
            bank_name = input("Enter the user's bank name: ")
            if not bank_name.isnumeric():
                break
            print("Bank name should not contain numbers.")
        return bank_name

    @staticmethod
    def _acquire_name():
        while True:
            name = input("Enter the user's name: ")
            if name.isalpha():
                break
            else:
                print("Name cannot be empty or consist of numbers. Please try again.")
        return name

    @staticmethod
    def _acquire_budgets():
        while True:
            try:
                budget_list = [
                    Budget(BudgetType.GAMES, int(input("Enter budget for Games and Entertainment: "))),
                    Budget(BudgetType.CLOTHING, int(input("Enter budget for Clothing and Accessories: "))),
                    Budget(BudgetType.FOOD, int(input("Enter budget for Eating Out: "))),
                    Budget(BudgetType.MISC, int(input("Enter budget for Miscellaneous: ")))
                ]
                break
            except ValueError:
                print("Budget must be a numeric value.")
        return budget_list

    @staticmethod
    def _acquire_balance():
        while True:
            try:
                balance = float(input("Enter the user's balance: "))
                if balance <= 0:
                    print("Invalid balance. Enter a positive quantity.")
                else:
                    break
            except ValueError:
                print("Balance must be a numeric value.")
        return balance

    @staticmethod
    def _acquire_age():
        while True:
            try:
                age = int(input("Enter the user's age: "))
                if age < 0 or age > 120:
                    print("Invalid age. Enter a number between 0 and 120")
                else:
                    break
            except ValueError:
                print("Enter a valid numeric value for the user's age.")
        return age
