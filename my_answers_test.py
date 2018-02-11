import unittest
import numpy as np
import my_answers

class MyAnswersTest(unittest.TestCase):
        
    def setUp(self):
    	pass

    def test_window_transform_series(self):
        window_size = 2
        odd_nums = np.array([1, 3, 5, 7, 9, 11, 13])

        X = []
        X.append(odd_nums[0:2])
        X.append(odd_nums[1:3])
        X.append(odd_nums[2:4])
        X.append(odd_nums[3:5])
        X.append(odd_nums[4:6])

        y = odd_nums[2:]

        X = np.asarray(X)
        y = np.asarray(y)
        y = np.reshape(y, (len(y), 1))  # optional

        assert (type(X).__name__ == 'ndarray')
        assert (type(y).__name__ == 'ndarray')
        assert (X.shape == (5, 2))
        assert (y.shape in [(5, 1), (5,)])

        print('X:\n{}\ny:\n{}'.format(X, y))

        my_X, my_y = my_answers.window_transform_series(odd_nums, window_size)

        print('my_X:\n{}\nmy_y:\n{}'.format(my_X, my_y))

        self.assertTrue(np.array_equal(X, my_X))
        self.assertTrue(np.array_equal(y, my_y))

    def test_cleaned_text(self):
        text = "Shall%& I compare| th9ee to a ´summer's da°y?"

        self.assertEquals("Shall   I compare  th ee to a  summer s da y?", my_answers.cleaned_text(text))

    def test_window_transform_text(self):
        text = "Shall I compare thee to a summers day?"
        inputs, outputs = my_answers.window_transform_text(text, 3, 2)

        print(inputs)
        print(outputs)

        self.assertEqual(len(inputs), len(outputs))
        self.assertEqual('Sha', inputs[0])
        self.assertEqual('l', outputs[0])
        self.assertEqual('day', inputs[-1])
        self.assertEqual('?', outputs[-1])

        while len(text) > 15:
            text = text[:-1]
            inputs, outputs = my_answers.window_transform_text(text, 10, 5)

            print(inputs)
            print(outputs)

        # self.assertEqual(len(inputs), len(outputs))
        # self.assertEqual('Sha', inputs[0])
        # self.assertEqual('l', outputs[0])
        # self.assertEqual('da', inputs[-1])
        # self.assertEqual('y', outputs[-1])
