import random

import pytest


class Account(object):
    def __init__(self, user_id, currency='USD'):
        self.user_id = user_id
        self.currency = currency
        self.current_balance = self.__read_balance_from_database()
        print("Current balance is ".format(self.current_balance))

    def withdraw(self, amount):
        self.current_balance = self.current_balance - float(amount)
        print(f"New Balance after Withdrawal:{self.current_balance}")

    def deposit(self, amount):
        self.current_balance = self.current_balance + float(amount)
        print(f"New Balance after Deposit:{self.current_balance}")

    def generate_statement(self, start_date, end_date):
        pass

    # private method cannot be called outside class
    def __read_balance_from_database(self):
        print("Getting balance from db for:".format(self.user_id))
        return random.randint(100, 1000)


myaccount1 = Account(8765)
import pdb; pdb.set_trace()

