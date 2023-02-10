from user import User


class TroubleMaker(User):
    """
    The TroubleMaker class represents a user whose parents are concerned but not worried.
    """

    def __init__(self, name, age, budget_list, bank_account):
        super().__init__(name, age, budget_list, bank_account)

    def is_budget_locked(self, budget_type):
        amount_spent = self.get_amount_spent(budget_type)
        limit = self.get_limit(budget_type)
        if amount_spent > 1.2 * float(limit):
            return True

    def send_warning(self, budget_type):
        amount_spent = self.get_amount_spent(budget_type)
        limit = self.get_limit(budget_type)
        if amount_spent > 0.75 * float(limit):
            return "You have exceeded your 75% limit!\n" \
                   "Please spend cautiously."
