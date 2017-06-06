import logging

class HangManEngine(object):
    def __init__(self, secret_message):
        self.secret_message = secret_message
        self.start_string = 'This is a game of hangman. For an explanation, '\
                         'please search the web'
        self.intermediate_string_list = ['_' for _  in
                                            range(len(secret_message))]
        self.intermediate_string = ''.join(self.intermediate_string_list)
        self.final_message = 'You won!'
        self._round_count = 0
        
    def get_message(self):
        if self._round_count == 0:
            print(self.start_string)
            print(self.intermediate_string)
            return self.start_string
        elif self.intermediate_string == self.secret_message:
            print(self.final_message)
            return 0
        else:
            print(self.intermediate_string)
            return self.intermediate_string

    def read_input(self, test_char=None):
        if test_char:
            guess_char = test_char
        else:
            guess_char = input('Choose a character: ')
        guess_char = guess_char.upper()
        self._update_intermediate_string(guess_char)
        self._round_count += 1
        return 'You chose an "{}"'.format(guess_char)

    def _update_intermediate_string(self, guess_char):
        new_intermediate_string = list(self.intermediate_string)
        for pos, char in enumerate(self.secret_message):
            if guess_char == char:
                new_intermediate_string[pos] = guess_char
            else:
                continue
        self.intermediate_string = ''.join(new_intermediate_string)

        
def main():
    HME = HangManEngine('TEST')
    while HME.get_message():
        HME.read_input()

if __name__== '__main__':
    main()
