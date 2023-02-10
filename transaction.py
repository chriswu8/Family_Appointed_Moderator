class Transaction:

    def __init__(self, timestamp, dollar_amount, budget_type, name):
        self._timestamp = timestamp
        self._dollar_amount = dollar_amount
        self._budget_type = budget_type
        self._shop_or_website_name = name

    def get_budget_type(self):
        return self._budget_type

    def get_timestamp(self):
        return self._timestamp

    def get_amount(self):
        return self._dollar_amount

    def get_shop_name(self):
        return self._shop_or_website_name
