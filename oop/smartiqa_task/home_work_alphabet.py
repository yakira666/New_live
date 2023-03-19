import string


class Alphabet:

    def __init__(self, lang, letters):
        self.lang = lang
        self.letters = list(letters)

    def print(self):
        print(f'{self.letters}')

    def letters_num(self):
        return len(self.letters)


class EngAlphabet(Alphabet):

    def __init__(self):
        letter = string.ascii_uppercase
        super().__init__("En", letter)
        self.__letter_num = len(letter)

    def is_en_letter(self, letter):
        self.letter = letter
        return self.letter.upper() in self.letters

    def letters_num(self):
        return self.__letter_num

    @staticmethod
    def example():
        print("Что-то")


if __name__ == '__main__':
    eng_alphabet = EngAlphabet()
    eng_alphabet.print()
    print(eng_alphabet.letters_num())
    print(eng_alphabet.is_en_letter('F'))
    print(eng_alphabet.is_en_letter('Щ'))
    EngAlphabet.example()
