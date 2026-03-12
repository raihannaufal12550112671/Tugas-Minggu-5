# Nama      : Raihan Naufal
# NIM       : 12550112671
# Kelas     : H
# Dosen     : Muhammad Affandes, S.T., M.T.

class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return self.balance
        else:
            raise ValueError("Deposit amount must be greater than zero")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            return self.balance
        else:
            raise ValueError("Insufficient funds or invalid withdrawal amount")

    def get_balance(self):
        return self.balance


import unittest

class TestBankAccount(unittest.TestCase):

    def setUp(self):
        self.account = BankAccount("Raihan", 500)

    def test_deposit(self):
        result = self.account.deposit(50)
        self.assertEqual(result, 550)

    def test_deposit_invalid(self):
        with self.assertRaises(ValueError):
            self.account.deposit(-10)

    def test_withdraw(self):
        result = self.account.withdraw(30)
        self.assertEqual(result, 470)

    def test_withdraw_insufficient(self):
        with self.assertRaises(ValueError):
            self.account.withdraw(600)

    def test_get_balance(self):
        self.assertEqual(self.account.get_balance(), 500)


if __name__ == "__main__":
    unittest.main(argv=[''], exit=False)