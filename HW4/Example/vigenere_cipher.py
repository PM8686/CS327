from os import stat


class VigenereCipher:
    def __init__(self, keyword):
        self.keyword = keyword

    def encode(self, plaintext):
        return self._code(plaintext, 1)

    def decode(self, ciphertext):
        return self._code(ciphertext, -1)

    def _code(self, text, direction):
        text = text.replace(" ", "").upper()
        combined = []
        keyword = self._extend_keyword(len(text))
        for p, k in zip(text, keyword):
            combined.append(self._rotate(p, k, direction))
        return "".join(combined)

    def _extend_keyword(self, number):
        repeats = number // len(self.keyword) + 1
        return (self.keyword * repeats)[:number]

    @staticmethod
    def _rotate(plainChar, keyChar, direction):
        plainChar = plainChar.upper()
        keyChar = keyChar.upper()
        plain_num = ord(plainChar) - ord("A") # bring into the range of 0-25
        keyword_num = ord(keyChar) - ord("A")
        return chr(ord("A") + (plain_num + keyword_num * direction) % 26)
