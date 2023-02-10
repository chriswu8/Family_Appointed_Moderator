class BankAccount:
    def __init__(self, balance, bank_name, bank_account_number):
        self._balance = balance
        self._bank_name = bank_name
        self._bank_account_number = bank_account_number

    def get_balance(self):
        """
        Returns the bank account balance.

        :return: the bank account balance
        """
        return self._balance

    def get_bank_name(self):
        """
        Returns the name of the bank.

        :return: the name of the bank
        """
        return self._bank_name

    def get_bank_account_number(self):
        """
        Returns the bank account number.

        :return: the bank account number
        """
        return self._bank_account_number
