class VigenereCipher:
    """
       VigenereCipher class (TO BE COMPLETED).

       Attributes:
           keyword (str): The word to be used as the key
           offset (int): The ASCII value of the letter 'A'. A static utility attribute to help you calculate
                a letter's position in the alphabet from 0 (A) to 25 (Z).
    """
    offset = ord('A')

    def __init__(self, keyword: str):
        self.keyword = keyword.upper()

    def __shift_letter(self, letter: str, shift: int, forward: bool):
        """
        Simple helper that shifts one letter forward or backward.
        """
        pos = ord(letter) - self.offset
        if forward:
            new_pos = (pos + shift) % 26
        else:
            new_pos = (pos - shift) % 26
        return chr(new_pos + self.offset)

    def __generate_shift_list(self, plaintext_length: int):
        """
        Build the shift list by repeating the keyword and turning letters into numbers.
        """
        # repeat keyword until reaching required length
        repeated = (self.keyword * ((plaintext_length // len(self.keyword)) + 1))[:plaintext_length]

        shifts = []
        for ch in repeated:
            shifts.append(ord(ch) - self.offset)
        return shifts

    def encrypt(self, plaintext: str):
        """
        Encrypt a plaintext using Vigenere cipher.
        """
        # convert to upper and remove non-letters
        cleaned = "".join([c for c in plaintext.upper() if c.isalpha()])

        shifts = self.__generate_shift_list(len(cleaned))

        result = []
        for i, ch in enumerate(cleaned):
            result.append(self.__shift_letter(ch, shifts[i], True))

        return "".join(result)

    def decrypt(self, ciphertext: str):
        """
        Decrypt a ciphertext using Vigenere cipher.
        """
        cleaned = "".join([c for c in ciphertext.upper() if c.isalpha()])
        shifts = self.__generate_shift_list(len(cleaned))

        result = []
        for i, ch in enumerate(cleaned):
            result.append(self.__shift_letter(ch, shifts[i], False))

        return "".join(result)


def main():
    vig_cipher = VigenereCipher('smarties')
    ciphertext = vig_cipher.encrypt("The quick brown fox jumps over the lazy dog")
    plaintext = vig_cipher.decrypt(ciphertext)
    assert plaintext == 'THEQUICKBROWNFOXJUMPSOVERTHELAZYDOG'


if __name__ == "__main__":
    main()
