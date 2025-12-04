class VigenereCipher:
    offset = ord('A')

    def __init__(self, keyword: str):
        self.keyword = keyword.upper()

    def __shift_letter(self, letter: str, shift: int, forward: bool):
        # basic letter shift
        x = ord(letter) - self.offset
        if forward:
            y = (x + shift) % 26
        else:
            y = (x - shift) % 26
        return chr(y + self.offset)

    def __generate_shift_list(self, n: int):
        # repeat keyword and cut it
        key = (self.keyword * (n // len(self.keyword) + 1))[:n]
        return [ord(c) - self.offset for c in key]

    def encrypt(self, plaintext: str):
        # keep letters only
        s = "".join([c for c in plaintext.upper() if c.isalpha()])
        shifts = self.__generate_shift_list(len(s))

        res = []
        for i in range(len(s)):
            res.append(self.__shift_letter(s[i], shifts[i], True))
        return "".join(res)

    def decrypt(self, ciphertext: str):
        s = "".join([c for c in ciphertext.upper() if c.isalpha()])
        shifts = self.__generate_shift_list(len(s))

        res = []
        for i in range(len(s)):
            res.append(self.__shift_letter(s[i], shifts[i], False))
        return "".join(res)
