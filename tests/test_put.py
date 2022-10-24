import http
import unittest

from battleship.controllers.shots import is_valid_shot
from battleship.models.board import Board


class TestPutRequest(unittest.TestCase):
    def test_is_valid_shot(self):
        # Valid shots
        shot = {
            'x': 0,
            'y': 0
        }
        self.assertTrue(is_valid_shot(shot), 'Should be True')

        shot = {
            'x': 9,
            'y': 5
        }
        self.assertTrue(is_valid_shot(shot), 'Should be True')

        # Invalid shots
        shot = {
            'x': 10,
            'y': 5
        }
        self.assertFalse(is_valid_shot(shot), 'Should be False')

        shot = {
            'x': 9,
            'y': 11
        }
        self.assertFalse(is_valid_shot(shot), 'Should be False')


    def test_shot_fired(self):
        board = Board()
        board.add_ship(x=2, y=1, size=4, direction='H')
        board.add_ship(x=7, y=4, size=3, direction='V')
        board.add_ship(x=3, y=5, size=2, direction='V')

        # Miss
        self.assertEqual(board.shot_fired(x=0, y=0), 'WATER')
        self.assertEqual(board.shot_fired(x=9, y=9), 'WATER')

        # Ship 1
        self.assertEqual(board.shot_fired(x=2, y=1), 'HIT')
        self.assertEqual(board.shot_fired(x=3, y=1), 'HIT')
        self.assertEqual(board.shot_fired(x=4, y=1), 'HIT')
        self.assertEqual(board.shot_fired(x=5, y=1), 'SINK')
        self.assertEqual(board.shot_fired(x=2, y=1), 'HIT')

        # Ship 2
        self.assertEqual(board.shot_fired(x=7, y=4), 'HIT')
        self.assertEqual(board.shot_fired(x=7, y=5), 'HIT')
        self.assertEqual(board.shot_fired(x=7, y=6), 'SINK')

        # Ship 3 / and last one
        self.assertEqual(board.shot_fired(x=3, y=5), 'HIT')
        self.assertEqual(board.shot_fired(x=3, y=6), 'SINK')
