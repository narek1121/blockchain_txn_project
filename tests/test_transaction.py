import unittest
from src.transaction import Transaction
from src.crypto_manager import CryptoManager

class TestTransaction(unittest.TestCase):
    def setUp(self):
        self.tx = Transaction()
        self.priv, self.pub = CryptoManager.generate_keypair()

    def test_add_io(self):
        ...

    def test_sign_and_verify(self):
        self.tx.add_input("abcd", 0)
        self.tx.add_output("bob", 5.0)
        self.tx.sign(self.priv)
        self.assertTrue(self.tx.verify(self.pub))
