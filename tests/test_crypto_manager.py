import unittest
from src.crypto_manager import CryptoManager

class TestCryptoManager(unittest.TestCase):
    def test_keypair_generation(self):
        priv, pub = CryptoManager.generate_keypair()
        self.assertIsNotNone(priv)
        self.assertIsNotNone(pub)

    def test_sign_and_verify_valid(self):
        data = b"test data for signature"
        priv, pub = CryptoManager.generate_keypair()
        signature = CryptoManager.sign_data(priv, data)
        self.assertTrue(CryptoManager.verify_signature(pub, data, signature))

    def test_verify_fails_on_tampering(self):
        data = b"original data"
        priv, pub = CryptoManager.generate_keypair()
        signature = CryptoManager.sign_data(priv, data)
        self.assertFalse(CryptoManager.verify_signature(pub, data + b"x", signature))

if __name__ == "__main__":
    unittest.main()
