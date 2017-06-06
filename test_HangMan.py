import unittest
import HangMan

class TestHangManEngine(unittest.TestCase):

    def test_init(self):
        HangManEngine = HangMan.HangManEngine('TEST')
        self.assertEqual('TEST', HangManEngine.secret_message)

    def test_get_start_sting(self):
        HangManEngine = HangMan.HangManEngine('TEST')
        start_string = HangManEngine.get_message()
        self.assertEqual('This is a game of hangman. For an explanation, '\
                         'please search the web', start_string)

    def test_read_and_return_character(self):
        HangManEngine = HangMan.HangManEngine('TEST')
        self.assertEqual(HangManEngine.read_input('A'),
                         'You chose an "A"')
        self.assertEqual(HangManEngine.read_input('a'),
                         'You chose an "A"')

    def test_update_intermediate_string(self):
        HangManEngine = HangMan.HangManEngine('TEST')
        HangManEngine._update_intermediate_string('A')
        self.assertEqual(HangManEngine.intermediate_string, '____')
        HangManEngine._update_intermediate_string('T')
        self.assertEqual(HangManEngine.intermediate_string, 'T__T')
        HangManEngine._update_intermediate_string('A')
        self.assertEqual(HangManEngine.intermediate_string, 'T__T')
        
    def test_intermediate_string(self):
        HangManEngine = HangMan.HangManEngine('TEST')
        HangManEngine.get_message()
        HangManEngine.read_input('A')
        intermediate_string = HangManEngine.get_message()
        self.assertEqual(intermediate_string, '____')
        HangManEngine.read_input('T')
        intermediate_string = HangManEngine.get_message()
        self.assertEqual(intermediate_string, 'T__T')

if __name__=='__main__':
    unittest.main()
