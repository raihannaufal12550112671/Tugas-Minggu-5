import unittest
#from bank_account import BankAccount

class TestBankAccount(unittest.TestCase):

    def setUp(self):
        # Membuat objek sebelum setiap test dijalankan
        self.account = BankAccount("Raihan", 100)

    def test_deposit(self):
        result = self.account.deposit(50)
        self.assertEqual(result, 150)

    def test_deposit_invalid(self):
        with self.assertRaises(ValueError):
            self.account.deposit(-10)

    def test_withdraw(self):
        result = self.account.withdraw(30)
        self.assertEqual(result, 70)

    def test_withdraw_insufficient(self):
        with self.assertRaises(ValueError):
            self.account.withdraw(200)

    def test_get_balance(self):
        self.assertEqual(self.account.get_balance(), 100)


if __name__ == "__main__":
    unittest.main()