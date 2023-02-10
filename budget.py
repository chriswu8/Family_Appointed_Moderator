class Budget:
    """
    The Budget class represents the budget for a particular type of expense.
    """

    def __init__(self, budget_type, limit):
        self._budget_type = budget_type
        self._limit = limit

    def get_budget_type(self):
        """
        Returns the budget type (Games and Entertainment, Clothing
        and Accessories, Eating Out, Miscellaneous).

        :return: Returns the budget type.
        """
        return self._budget_type

    def get_limit(self):
        """
        Returns the user's budget limit.

        :return: Returns the user's budget limit
        """
        return self._limit
