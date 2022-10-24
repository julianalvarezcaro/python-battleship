import http
import unittest

from battleship.controllers.placement import create_game, is_valid_payload, is_valid_ship_positioning
from battleship.models.board import Board


class TestPostRequest(unittest.TestCase):

    def test_is_valid_payload(self):
        # Invalid payloads
        payload = {
            'zhips': [
                {
                    "x": 2,
                    "y": 1,
                    "size": 4,
                    "direction": "H"
                },
                {
                    "x": 7,
                    "y": 4,
                    "size": 3,
                    "direction": "V"
                }
            ]
        }
        self.assertFalse(is_valid_payload(payload), 'Should return False')

        payload = {
            'ships': [
                {
                    "p": 2,
                    "y": 1,
                    "size": 4,
                    "direction": "H"
                },
                {
                    "x": 7,
                    "y": 4,
                    "size": 3,
                    "direction": "V"
                }
            ]
        }
        self.assertFalse(is_valid_payload(payload), 'Should return False')

        # Valid payload
        payload = {
            'ships': [
                {
                    "x": 2,
                    "y": 1,
                    "size": 4,
                    "direction": "H"
                },
                {
                    "x": 7,
                    "y": 4,
                    "size": 3,
                    "direction": "V"
                }
            ]
        }
        self.assertTrue(is_valid_payload(payload), 'Should return True')


    def test_is_valid_ship_positioning(self):
        # Out of board cases
        args = {
            'x': 8,
            'y': 7,
            'size': 5,
            'direction': 'H'
        }
        self.assertFalse(is_valid_ship_positioning(**args))

        args = {
            'x': 2,
            'y': 7,
            'size': 5,
            'direction': 'V'
        }
        self.assertFalse(is_valid_ship_positioning(**args))

        # Valid positioning
        args = {
            'x': 2,
            'y': 7,
            'size': 5,
            'direction': 'H'
        }
        self.assertTrue(is_valid_ship_positioning(**args))

    def test_add_ship(self):
        board = Board()
        expected_board = [
            [0, 0, 0, 1, 1, 1, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        ]
        board.add_ship(x=3, y=0, size=3, direction='H')
        self.assertEqual(board.board_matrix, expected_board)

        expected_board = [
            [0, 0, 0, 1, 1, 1, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 2, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 2, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 2, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 2, 0]
        ]
        board.add_ship(x=8, y=6, size=4, direction='V')
        self.assertEqual(board.board_matrix, expected_board)

        expected_board = [
            [0, 0, 0, 1, 1, 1, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 2, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 2, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 2, 0],
            [0, 0, 0, 0, 0, 3, 3, 3, 2, 0]
        ]
        board.add_ship(x=5, y=9, size=4, direction='H')
        self.assertEqual(board.board_matrix, expected_board,)

        # Overlapping error
        self.assertEqual(
            board.add_ship(x=6, y=8, size=4, direction='H'), http.HTTPStatus.BAD_REQUEST)


if __name__=="__main__":
    unittest.main()
