from user import User


class Angel(User):
    """
    The Angel class represents a user whose parents are not worried at all.
    """

    def __init__(self, name, age, budget_list, bank_account):
        super().__init__(name, age, budget_list, bank_account)

    def send_warning(self, budget_type):
        """

        :param budget_type:
        :return:
        """
        amount_spent = self.get_amount_spent(budget_type)
        limit = self.get_limit(budget_type)
        if amount_spent > 0.9 * float(limit):
            return "Hi dear, you have exceeded your 90% limit.\n" \
                   "Please spend with caution."

    def is_budget_locked(self, budget_type):
        return False
