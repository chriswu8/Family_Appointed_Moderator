from budget_type import BudgetType


class User:
    """
    The User class represents a user.
    """

    def __init__(self, name, age, budget_list, bank_account):
        self._name = name
        self._age = age
        self._budget_list = budget_list
        self._bank_account = bank_account
        self._transaction_dict = {BudgetType.GAMES: [],
                                  BudgetType.CLOTHING: [],
                                  BudgetType.FOOD: [],
                                  BudgetType.MISC: []}

    def get_name(self):
        """
        Returns the user's name.

        :return: the user's name
        """
        return self._name

    def get_age(self):
        """
        Returns the user's age.

        :return: the user's age
        """
        return self._age

    def is_budget_locked(self, budget_type):
        """
        Returns True if the user is locked, else False.

        :return: True if the user is locked, else False
        """
        return False

    def send_warning(self, budget_type):
        pass

    def get_budget_list(self):
        """
        Returns the user's budget list.

        :return: the user's budget list
        """
        return self._budget_list

    def get_bank_account(self):
        """
        Returns the user's bank (account).

        :return: the user's bank (account)
        """
        return self._bank_account

    def append_transaction(self, transaction):
        self._transaction_dict[transaction.get_budget_type()].append(transaction)

    def view_transaction_by_category(self, budget_type):
        print(f"All transactions of category {budget_type.value}:\n")
        for tr in self._transaction_dict[budget_type]:
            print("Date: \t", tr.get_timestamp())
            print("Amount:  $" + str(tr.get_amount()))
            print("Vendor:\t", tr.get_shop_name(), "\n")

    def get_amount_spent(self, budget_type):
        sum_for_budget = 0
        for tr in self._transaction_dict[budget_type]:
            sum_for_budget += tr.get_amount()
        return sum_for_budget

    def get_amount_left(self, budget_type):
        return self.get_limit(budget_type) - self.get_amount_spent(budget_type)

    def get_limit(self, budget_type):
        for budget in self._budget_list:
            if budget.get_budget_type() == budget_type:
                return budget.get_limit()
        raise Exception("Budget type not found")

    def is_account_locked(self):
        return False

    def has_2_or_more_budget_categories_locked(self):
        running_sum = 0

        # for each budget category
        for budget_type, transactions in self._transaction_dict.items():
            # calculate the total amount of money spent
            total_spent = sum(transaction.get_amount() for transaction in transactions)

            if total_spent >= self.get_limit(budget_type):
                running_sum += 1

            if running_sum >= 2:
                return True

        return False

    def will_induce_negative_balance(self, transaction_amount):
        """
        Returns True if the transaction amount will render the bank balance to a negative value, else False.

        :return: True if the transaction amount will render the bank balance to a negative value, else False
        """
        if self._bank_account.get_balance() - transaction_amount < 0:
            return True
        else:
            return False
