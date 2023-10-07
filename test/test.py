from stories_generator.customization import Customization
from stories_generator.story_automaton import StoryAutomaton

import unittest



class TestInteractiveStory(unittest.TestCase):
    def setUp(self):
        self.input_name = "John"
        self.output_name = "Doe"
        self.fragment1 = "This is a test"

    def test_customizeName_no_match(self):
        c = Customization()
        result = c.customizeName(self.fragment1, self.input_name, self.output_name)
        self.assertEqual(result, self.fragment1)
#####        
    

class Name_match(unittest.TestCase):
    def setUp(self):
        self.input_name = "John"
        self.output_name = "Doe"
        self.fragment2 = "Hello Doe, how are you?"
        self.fragment3 = "John likes John and John likes pizza."

    def test_customizeName_match(self):
        c = Customization()
        result = c.customizeName(self.fragment2, self.input_name, self.output_name)

        expected_result = "Hello Doe, how are you?"
        self.assertEqual(result, expected_result)

    def test_customizeName_multiple_matches(self):
        c = Customization()
        result = c.customizeName(self.fragment3, self.input_name, self.output_name)

        expected_result = "Doe likes Doe and Doe likes pizza."
        self.assertEqual(result, expected_result)
    

class Test_Accepting(unittest.TestCase):
    def setUp(self):
        self.accepting_strings = ["111111111", "11111112", "21111", "22111111", "12111"]

    def test_accepting_string(self):
        s = StoryAutomaton()
        for string in self.accepting_strings:
            with self.subTest(msg=f'Testing accepting string: {string}'):
                self.assertTrue(s.dfa.accepts(string))

class Test_Non(unittest.TestCase):
    def setUp(self):
        self.non_accepting_strings = ["123", "1111", "1222", "333", "2222"]

    def test_non_accepting_string(self):
        s = StoryAutomaton()
        for string in self.non_accepting_strings:
            with self.subTest(msg=f'Testing non-accepting string: {string}'):
                self.assertFalse(s.dfa.accepts(string))

if __name__ == '__main__':
    unittest.main()
"""""
 ###########
    def test_decide_choice_1(self, mock_input, mock_stdout):
        point = 0
        exclude = []
        decide(point, exclude)
        expected_output = "Es momento de decidir...\n1. Option 1\n2. Option 2\n3. Descipción detallada\n4. Hablar con un personaje\n"
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    def test_decide_choice_2(self, mock_input, mock_stdout):
        point = 1
        exclude = []
        decide(point, exclude)
        expected_output = "Es momento de decidir...\n1. Option 1\n2. Option 2\n3. Descipción detallada\n4. Hablar con un personaje\n"
        self.assertEqual(mock_stdout.getvalue(), expected_output)


    def test_decide_choice_3(self, mock_input, mock_stdout):
        point = 2
        exclude = []
        decide(point, exclude)
        expected_output = "Es momento de decidir...\n1. Option 1\n2. Option 2\n3. Descipción detallada\n4. Hablar con un personaje\nNo encuentras pistas en este momento\nEs momento de decidir...\n1. Option 1\n2. Option 2\n4. Hablar con un personaje\n"
        self.assertEqual(mock_stdout.getvalue(), expected_output)


    def test_decide_choice_4(self, mock_input, mock_stdout):
        point = 3
        exclude = []
        decide(point, exclude)
        expected_output = "Es momento de decidir...\n1. Option 1\n2. Option 2\n3. Descipción detallada\n4. Hablar con un personaje\nNadie está de humor para hablar ahora mismo\nEs momento de decidir...\n1. Option 1\n2. Option 2\n3. Descipción detallada\n"
        self.assertEqual(mock_stdout.getvalue(), expected_output)


    def test_decide_invalid_choice(self, mock_input, mock_stdout):
        point = 4
        exclude = []
        decide(point, exclude)
        expected_output = "Es momento de decidir...\n1. Option 1\n2. Option 2\n3. Descipción detallada\n4. Hablar con un personaje\nEs momento de decidir...\n1. Option 1\n2. Option 2\n3. Descipción detallada\n4. Hablar con un personaje\n"
        self.assertEqual(mock_stdout.getvalue(), expected_output)
######

    def test_storyPoint_non_q0(self, mock_stdout):
        point = 'p1'
        storyPoint(point)
        expected_output = "\nStory content for point p1\nEs momento de decidir...\n1. Option 1\n2. Option 2\n3. Descipción detallada\n4. Hablar con un personaje\n"
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    def test_storyPoint_q0(self):
        point = 'q0'
        storyPoint(point)
        expected_output = ""
        self.assertEqual("", expected_output)

    def test_storyPoint_final_state(self):
        point = 'final_state'
        storyPoint(point)
        expected_output = "\nFinal state content\n"
        self.assertEqual("", expected_output)"""
