from fam import FamilyAppointedModeratorAccount


class Controller:
    fam_accounts = []
    active_user = None

    @classmethod
    def load_users(cls, user_list):

        for user in user_list:
            Controller.add_user_to_fam_account(user)

    @classmethod
    def add_user_to_fam_account(cls, user):
        # create a new FamilyAppointedModeratorAccount for each user
        bank_account = user.get_bank_account()
        bank_account_number = bank_account.get_bank_account_number()
        budget_list = user.get_budget_list()

        fam_account = FamilyAppointedModeratorAccount(user, bank_account_number, budget_list, [])

        Controller.fam_accounts.append(fam_account)

    @classmethod
    def set_active_user(cls, name):
        for fam_account in Controller.fam_accounts:
            user_name = fam_account.get_user().get_name()
            if user_name == name:
                Controller.active_user = fam_account.get_user()
                break

    @classmethod
    def append_the_transaction(cls, transaction):
        if Controller.active_user:
            Controller.active_user.append_transaction(transaction)

    @classmethod
    def view_the_transaction(cls, budget_type):
        if Controller.active_user:
            Controller.active_user.view_transaction_by_category(budget_type)

    @classmethod
    def reduce_budget_amount(cls, amount):
        if Controller.active_user:
            Controller.active_user.set_amount_spent(amount)
