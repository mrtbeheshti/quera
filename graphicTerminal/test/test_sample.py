import unittest, pygame, subprocess, os
from subprocess import PIPE, run
import time


class TestPygame(unittest.TestCase):

    def send_input(self, inputs):
        with open('test/input.txt', 'w') as f:
            f.write(inputs)
        os.system('python terminal.py < test/input.txt')
        time.sleep(2)

    def __test_drawing(self):
        with open('sample_media/myDraw.png', 'rb') as f:
            quera_drawing = f.read()
        with open('draw.png', 'rb') as f:
            user_drawing = f.read()
        self.assertEqual(user_drawing, quera_drawing)

    def test_draw_line(self):
        commands = [
            'change size 10',
            'change color 25 25 25',
            'draw line 0 0 100 100',
            'draw line 10 0 100 100',
            'end drawing'
        ]
        self.send_input('\n'.join(commands))
        self.__test_drawing()
