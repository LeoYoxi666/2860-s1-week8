import random
import string
import unittest
import exercise3

class TestVigenereCipher(unittest.TestCase):
    def test_encryption(self):
        vig_cipher = exercise3.VigenereCipher('cornflakes')
        ciphertext = vig_cipher.encrypt("The quick brown fox jumps over the lazy dog")
        self.assertEqual(ciphertext, 'VVVDZTCUFJQKESTIJEQHUCMRWEHOPSBMUBL')

    def test_decryption(self):
        vig_cipher = exercise3.VigenereCipher('marmite')
        plaintext = vig_cipher.decrypt("FHVCCBGWBIAEGJAXAGUIWAVVDBAIXAQKLHK")
        self.assertEqual(plaintext, 'THEQUICKBROWNFOXJUMPSOVERTHELAZYDOG')

    def test_consistency(self):
        keyword = ''.join(random.sample(string.ascii_uppercase, 6))
        vig_cipher = exercise3.VigenereCipher(keyword)
        ciphertext = vig_cipher.encrypt("The quick brown fox jumps over the lazy dog")
        plaintext = vig_cipher.decrypt(ciphertext)
        self.assertEqual(plaintext,'THEQUICKBROWNFOXJUMPSOVERTHELAZYDOG')


if __name__ == '__main__':
    unittest.main()
