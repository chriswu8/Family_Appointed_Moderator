import calendar
import sys

from budget_type import BudgetType
from generator import UserGenerator
from controller import Controller
from invalid_budget_type import InvalidBudgetException
from rebel import Rebel
from transaction import Transaction
from datetime import datetime


class MainMenu:
    user_list = UserGenerator.generate_users()

    def __init__(self):
        pass

    @staticmethod
    def login():
        MainMenu._login_as()
        MainMenu._acquire_active_user()
        MainMenu.display_options()

    @staticmethod
    def _acquire_active_user():
        number_of_users = len(MainMenu.user_list)
        invalid_user_selection = True

        while True:
            # selects the user
            option = MainMenu._acquire_valid_user_selection(invalid_user_selection, number_of_users)

            try:
                selected_user = MainMenu.user_list[option - 1]

            except ValueError:
                print("Enter a valid number.")

            except IndexError:
                print("Enter a valid number within the given range of users.")

            if isinstance(selected_user, Rebel) and selected_user.has_2_or_more_budget_categories_locked():
                print("\n" + selected_user.get_name() + "\'s account is LOCKED. Cannot login.\n")
                continue

            Controller.set_active_user(selected_user.get_name())
            break

    @staticmethod
    def _acquire_valid_user_selection(invalid_user_selection, number_of_users):
        while invalid_user_selection:
            try:
                option = input(f"\nEnter a number between 1 and {number_of_users}: ")
                option = int(option)
                if option <= 0:
                    continue
                if option > number_of_users:
                    continue
                invalid_user_selection = False
            except ValueError:
                print("\nOnly numbers inputs are accepted.")
        return option

    @staticmethod
    def _login_as():
        print("\nLogin as:")

        # number of letters in the name of the user with the longest name
        max_length = max([len(user.get_name()) for user in MainMenu.user_list])

        for i in range(len(MainMenu.user_list)):
            user = MainMenu.user_list[i]
            user_type = "(" + user.__class__.__name__ + ")"

            print(f"{i + 1}. {user.get_name()}"
                  # a string w/ spaces just enough to align the user types
                  f"{' ' * (max_length - len(user.get_name()))}"
                  f"\t{user_type}")

    @staticmethod
    def register_user():
        new_user = UserGenerator.generate_user()
        Controller.add_user_to_fam_account(new_user)
        return new_user

    @staticmethod
    def welcome():
        while True:
            print("\nWelcome to FAM!\n1) Register new user\n2) Login\n3) Exit program")

            option = input()

            if option == "1":
                MainMenu.user_list.append(MainMenu.register_user())
                MainMenu.welcome()

            elif option == "2":
                MainMenu.login()

            elif option == "3":
                sys.exit()

            else:
                print("Invalid option. Please select options 1, 2 or 3.")
                MainMenu.welcome()

    @staticmethod
    def display_options():
        while True:
            option = MainMenu._acquire_display_option_selection()

            invalid_display_option = True

            option = MainMenu.validate_user_input(invalid_display_option, option, 5)

            if option == 1:
                """
                Selecting this option should show the user the current status of their budgets (locked or not),
                the amount spent, amount left, and the total amount allocated to the budget.
                """
                MainMenu._view_budgets()

            elif option == 2:
                """
                Takes the user to where they are prompted to enter 
                the transaction details, if they are not locked.
                """
                if Controller.active_user.is_account_locked():
                    print("\nYou are locked out of your account.")
                else:
                    MainMenu.record_transaction()

            elif option == 3:
                """
                Takes the user to a sub-menu where they select their budget category and 
                view all the transactions to date in that category.
                """
                MainMenu.view_transaction()
                MainMenu.display_options()

            elif option == 4:
                """
                Prints out the bank account details of the user and 
                all transactions conducted to date alongside the closing balance.
                """
                print("\nBank: \t\t\t\t " + str(Controller.active_user.get_bank_account().get_bank_name()))
                print("Account Number: \t " + str(Controller.active_user.get_bank_account().get_bank_account_number()))
                print("Initial Balance:\t $" + str(Controller.active_user.get_bank_account().get_balance()))
                print("Remaining Balance:   $" + str(Controller.active_user.get_bank_account().get_balance()
                                                     - Controller.active_user.get_amount_spent(BudgetType.GAMES)
                                                     - Controller.active_user.get_amount_spent(BudgetType.CLOTHING)
                                                     - Controller.active_user.get_amount_spent(BudgetType.FOOD)
                                                     - Controller.active_user.get_amount_spent(BudgetType.MISC)))


            elif option == 5:
                # MainMenu.welcome()
                break

    @staticmethod
    def _acquire_display_option_selection():
        option = 0
        while option < 1 or option > 5:
            try:
                option = int(input("\n1. View Budgets"
                                   + "\n2. Record a Transaction"
                                   + "\n3. View Transactions by Budget"
                                   + "\n4. View Bank Account Details"
                                   + "\n5. Logout"
                                   + "\n\nEnter your choice: "))
            except ValueError:
                print("Please enter a valid number between 1 and 5.")
        return option

    @staticmethod
    def _view_budgets():
        for budget_type in BudgetType:
            print(f"\nBudget information for \"{budget_type.value}\"")
            print(f"Status:          {MainMenu.determine_lock_status(budget_type)}")
            print(f"Amount spent:    ${str(Controller.active_user.get_amount_spent(budget_type))}")
            print(f"Amount left:     ${str(Controller.active_user.get_amount_left(budget_type))}")
            print(f"Total allocated: ${str(Controller.active_user.get_limit(budget_type))}")

    @staticmethod
    def record_transaction():
        # present menu for recording transaction
        MainMenu._prompt_budget_category()

        budget_type = MainMenu._acquire_budget_type()

        if Controller.active_user.is_budget_locked(budget_type):
            print("You are locked out of this budget category!\n"
                  "Money is a finite resource. Please learn to spend wisely.")
            return

        time_stamp_object = MainMenu._acquire_transaction_time()

        trans_amount = MainMenu._acquire_cost()

        if Controller.active_user.will_induce_negative_balance(trans_amount):
            print("\n2You should not spend this amount, as it would induce a negative bank balance.")
            return

        print("Enter the name of shop:")
        shop_name = input()

        # Transaction trans = new Transaction(use input gathered from user)
        new_transaction = Transaction(time_stamp_object, trans_amount, budget_type, shop_name)

        Controller.append_the_transaction(new_transaction)

        warning = Controller.active_user.send_warning(budget_type)

        if warning is not None:
            print(warning)

    @staticmethod
    def _acquire_budget_type():
        while True:
            try:
                budget_type_input = int(input())
                if 0 < budget_type_input <= 4:
                    break
                else:
                    print("\nPlease enter a number between 1 and 4.\n")
            except ValueError:
                print("\nPlease enter a number.\n")

        budget_type = MainMenu.get_budget_type_for_number(budget_type_input)

        return budget_type

    @staticmethod
    def _acquire_cost():
        print("Enter the cost: ")
        while True:
            try:
                cost = float(input())
                if cost < 0:
                    raise ValueError
                break
            except ValueError:
                print("Cost must be a positive numeric value.")
        return cost

    @staticmethod
    def _prompt_budget_category():
        print("\nEnter the category of purchase:\n")
        print(f"1. {BudgetType.GAMES.value}")
        print(f"2. {BudgetType.CLOTHING.value}")
        print(f"3. {BudgetType.FOOD.value}")
        print(f"4. {BudgetType.MISC.value}")

    @staticmethod
    def _acquire_transaction_time():
        year = MainMenu._acquire_year()
        month = MainMenu._acquire_month()
        day = MainMenu._acquire_day(month, year)

        time_stamp_object = datetime(year, month, day).date()

        return time_stamp_object

    @staticmethod
    def _acquire_day(month, year):
        print("Enter the day of the transaction:")
        while True:
            try:
                day = int(input())
                if day < 1 or day > calendar.monthrange(year, month)[1]:
                    raise ValueError
                break
            except ValueError:
                print("Invalid input. Please enter a numeric day between 1 and {}.".format(
                    calendar.monthrange(year, month)[1]))
        return day

    @staticmethod
    def _acquire_month():
        print("Enter the month of the transaction:")
        while True:
            try:
                month = int(input())
                if month < 1 or month > 12:
                    raise ValueError
                break
            except ValueError:
                print("Invalid input. Please enter a numeric month between 1 and 12.")
        return month

    @staticmethod
    def _acquire_year():
        print("Enter the year of the transaction:")
        while True:
            try:
                year = int(input())
                if year < 1:
                    raise ValueError
                break
            except ValueError:
                print("Invalid input. Please enter a valid numeric year.")
        return year

    @staticmethod
    def view_transaction():
        while True:
            try:
                option = int(
                    input(f"\nChoose the category you want to see transactions of:\n1. {BudgetType.GAMES.value}"
                          + f"\n2. {BudgetType.CLOTHING.value}"
                          + f"\n3. {BudgetType.FOOD.value}"
                          + f"\n4. {BudgetType.MISC.value}\n"))
                if 0 < option <= 4:
                    break
                else:
                    print("\nPlease enter a number between 1 and 4!\n")
            except ValueError:
                print("\nPlease enter a valid number!\n")

        Controller.view_the_transaction(MainMenu.get_budget_type_for_number(option))

    @staticmethod
    def validate_user_input(invalid_display_option, option, max_value):
        if 0 < option <= max_value:
            return option

        while invalid_display_option:
            try:
                option = input(f"\nChoose between options 1 and {max_value}: ")
                option = int(option)
                if option <= 0:
                    continue
                if option > max_value:
                    continue
                invalid_display_option = False
            except ValueError:
                print("Enter a valid number as displayed: ")
            except TypeError:
                print("Only NUMBERS allowed. Please try again.")
        return option

    @staticmethod
    def determine_lock_status(budget_type):
        if Controller.active_user.is_budget_locked(budget_type):
            return "Locked"
        else:
            return "Unlocked"

    @classmethod
    def get_budget_type_for_number(cls, budget_type_number):
        try:
            match budget_type_number:
                case 1:
                    return BudgetType.GAMES
                case 2:
                    return BudgetType.CLOTHING
                case 3:
                    return BudgetType.FOOD
                case 4:
                    return BudgetType.MISC
                case _:
                    raise InvalidBudgetException("Invalid Budget Type")
        except InvalidBudgetException as e:
            print(e.args[0])
