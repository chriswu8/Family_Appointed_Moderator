class InvalidBudgetException(Exception):
    def __init__(self, my_msg):
        super().__init__(my_msg)