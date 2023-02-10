class FamilyAppointedModeratorAccount:

    def __init__(self, user, account_number, budget_list, transactions_list):
        self._user = user
        self._bank_account = account_number
        self._budget_list = budget_list
        self._transactions_list = transactions_list

    def get_user(self):
        return self._user

    def get_account_number(self):
        return self._account_number

    def get_budget_list(self):
        return self._budget_list

    def get_transactions_list(self):
        return self._transactions_list

    def append_transaction(self, transaction):
        self._transactions_list.append(transaction)
