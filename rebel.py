from user import User


class Rebel(User):
    """
    The Rebel class represents a user whose parents are quite worried.
    """

    def __init__(self, name, age, budget_list, bank_account):
        super().__init__(name, age, budget_list, bank_account)

    def is_budget_locked(self, budget_type):
        amount_spent = self.get_amount_spent(budget_type)
        limit = self.get_limit(budget_type)
        if amount_spent > limit:
            return True

    def send_warning(self, budget_type):
        amount_spent = self.get_amount_spent(budget_type)
        limit = self.get_limit(budget_type)
        if amount_spent > 0.5 * float(limit):
            return "You have exceeded your 50% limit!\n" \
                   "You better spend responsibly! Seriously..."

    def is_account_locked(self):
        number_of_budgets_locked = 0
        for budget in self.get_budget_list():
            if self.is_budget_locked(budget.get_budget_type()):
                number_of_budgets_locked += 1
        if number_of_budgets_locked >= 2:
            return True
        else:
            return False

