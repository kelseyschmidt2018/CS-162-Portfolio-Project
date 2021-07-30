# Author: Kelsey Schmidt
# Date: 7-29-21
# Description:  # Testing file for QuoridorGame.py, containing unit tests.

import unittest
from Quoridor import QuoridorGame

class TestQuoridorGame(unittest.TestCase):

    """
    Contains unit tests for the Quoridor file.
    """

    def test_QuoridorGame_get_board(self):
        """
        Tests QuoridorGame get_board.
        """
        q = QuoridorGame()
        result = q.get_board()
        # this is only hard coded here for the purpose of the test
        self.assertEqual(result, [
            ['. ', '__', '. ', '__', '. ', '__', '. ', '__', '. ', '__', '. ', '__', '. ', '__', '. ', '__', '. ', '__', '. '],
            ['| ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', 'P1', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '| '],
            ['. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. '],
            ['| ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '| '],
            ['. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. '],
            ['| ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '| '],
            ['. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. '],
            ['| ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '| '],
            ['. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. '],
            ['| ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '| '],
            ['. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. '],
            ['| ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '| '],
            ['. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. '],
            ['| ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '| '],
            ['. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. '],
            ['| ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '| '],
            ['. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. '],
            ['| ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', 'P2', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '| '],
            ['. ', '__', '. ', '__', '. ', '__', '. ', '__', '. ', '__', '. ', '__', '. ', '__', '. ', '__', '. ', '__', '. ']
        ])

    def test_QuoridorGame_set_board(self):
        """
        Tests QuoridorGame set_board.
        """
        q = QuoridorGame()
        board = [0, 1, 2, 3]
        q.set_board(board)
        result = q.get_board()
        self.assertEqual(result, [0, 1, 2, 3])

    def test_QuoridorGame_get_coords_dict(self):
        """
        Tests QuoridorGame get_coords_dict.
        """
        q = QuoridorGame()
        result = q.get_coords_dict()
        # this is only hard coded here for the purpose of the test
        self.assertEqual(result, {(0, 0): '. ', (1, 0): '. ', (2, 0): '. ', (3, 0): '. ', (4, 0): '. ', (5, 0): '. ',
                                  (6, 0): '. ', (7, 0): '. ', (8, 0): '. ', (9, 0): '. ', (0, 1): '. ', (1, 1): '. ',
                                  (2, 1): '. ', (3, 1): '. ', (4, 1): '. ', (5, 1): '. ', (6, 1): '. ', (7, 1): '. ',
                                  (8, 1): '. ', (9, 1): '. ', (0, 2): '. ', (1, 2): '. ', (2, 2): '. ', (3, 2): '. ',
                                  (4, 2): '. ', (5, 2): '. ', (6, 2): '. ', (7, 2): '. ', (8, 2): '. ', (9, 2): '. ',
                                  (0, 3): '. ', (1, 3): '. ', (2, 3): '. ', (3, 3): '. ', (4, 3): '. ', (5, 3): '. ',
                                  (6, 3): '. ', (7, 3): '. ', (8, 3): '. ', (9, 3): '. ', (0, 4): '. ', (1, 4): '. ',
                                  (2, 4): '. ', (3, 4): '. ', (4, 4): '. ', (5, 4): '. ', (6, 4): '. ', (7, 4): '. ',
                                  (8, 4): '. ', (9, 4): '. ', (0, 5): '. ', (1, 5): '. ', (2, 5): '. ', (3, 5): '. ',
                                  (4, 5): '. ', (5, 5): '. ', (6, 5): '. ', (7, 5): '. ', (8, 5): '. ', (9, 5): '. ',
                                  (0, 6): '. ', (1, 6): '. ', (2, 6): '. ', (3, 6): '. ', (4, 6): '. ', (5, 6): '. ',
                                  (6, 6): '. ', (7, 6): '. ', (8, 6): '. ', (9, 6): '. ', (0, 7): '. ', (1, 7): '. ',
                                  (2, 7): '. ', (3, 7): '. ', (4, 7): '. ', (5, 7): '. ', (6, 7): '. ', (7, 7): '. ',
                                  (8, 7): '. ', (9, 7): '. ', (0, 8): '. ', (1, 8): '. ', (2, 8): '. ', (3, 8): '. ',
                                  (4, 8): '. ', (5, 8): '. ', (6, 8): '. ', (7, 8): '. ', (8, 8): '. ', (9, 8): '. ',
                                  (0, 9): '. ', (1, 9): '. ', (2, 9): '. ', (3, 9): '. ', (4, 9): '. ', (5, 9): '. ',
                                  (6, 9): '. ', (7, 9): '. ', (8, 9): '. ', (9, 9): '. '})

    def test_QuoridorGame_get_horiz_edges_dict(self):
        """
        Tests QuoridorGame get_horiz_edges_dict.
        """
        q = QuoridorGame()
        result = q.get_horiz_edges_dict()
        # this is only hard coded here for the purpose of the test
        self.assertEqual(result, {(0, 0): '__', (1, 0): '__', (2, 0): '__', (3, 0): '__', (4, 0): '__', (5, 0): '__',
                                  (6, 0): '__', (7, 0): '__', (8, 0): '__', (0, 1): '  ', (1, 1): '  ', (2, 1): '  ',
                                  (3, 1): '  ', (4, 1): '  ', (5, 1): '  ', (6, 1): '  ', (7, 1): '  ', (8, 1): '  ',
                                  (0, 2): '  ', (1, 2): '  ', (2, 2): '  ', (3, 2): '  ', (4, 2): '  ', (5, 2): '  ',
                                  (6, 2): '  ', (7, 2): '  ', (8, 2): '  ', (0, 3): '  ', (1, 3): '  ', (2, 3): '  ',
                                  (3, 3): '  ', (4, 3): '  ', (5, 3): '  ', (6, 3): '  ', (7, 3): '  ', (8, 3): '  ',
                                  (0, 4): '  ', (1, 4): '  ', (2, 4): '  ', (3, 4): '  ', (4, 4): '  ', (5, 4): '  ',
                                  (6, 4): '  ', (7, 4): '  ', (8, 4): '  ', (0, 5): '  ', (1, 5): '  ', (2, 5): '  ',
                                  (3, 5): '  ', (4, 5): '  ', (5, 5): '  ', (6, 5): '  ', (7, 5): '  ', (8, 5): '  ',
                                  (0, 6): '  ', (1, 6): '  ', (2, 6): '  ', (3, 6): '  ', (4, 6): '  ', (5, 6): '  ',
                                  (6, 6): '  ', (7, 6): '  ', (8, 6): '  ', (0, 7): '  ', (1, 7): '  ', (2, 7): '  ',
                                  (3, 7): '  ', (4, 7): '  ', (5, 7): '  ', (6, 7): '  ', (7, 7): '  ', (8, 7): '  ',
                                  (0, 8): '  ', (1, 8): '  ', (2, 8): '  ', (3, 8): '  ', (4, 8): '  ', (5, 8): '  ',
                                  (6, 8): '  ', (7, 8): '  ', (8, 8): '  ', (0, 9): '__', (1, 9): '__', (2, 9): '__',
                                  (3, 9): '__', (4, 9): '__', (5, 9): '__', (6, 9): '__', (7, 9): '__', (8, 9): '__'})

    def test_QuoridorGame_set_horiz_edges_dict(self):
        """
        Tests QuoridorGame set_horiz_edges_dict.
        """
        q = QuoridorGame()
        q.set_horiz_edges_dict({"a":1})
        result = q.get_horiz_edges_dict()
        self.assertEqual(result, {"a":1})

    def test_QuoridorGame_get_vert_edges_dict(self):
        """
        Tests QuoridorGame get_vert_edges_dict.
        """
        q = QuoridorGame()
        result = q.get_vert_edges_dict()
        # this is only hard coded here for the purpose of the test
        self.assertEqual(result, {(0, 0): '| ', (1, 0): '  ', (2, 0): '  ', (3, 0): '  ', (4, 0): '  ', (5, 0): '  ',
                                  (6, 0): '  ', (7, 0): '  ', (8, 0): '  ', (9, 0): '| ', (0, 1): '| ', (1, 1): '  ',
                                  (2, 1): '  ', (3, 1): '  ', (4, 1): '  ', (5, 1): '  ', (6, 1): '  ', (7, 1): '  ',
                                  (8, 1): '  ', (9, 1): '| ', (0, 2): '| ', (1, 2): '  ', (2, 2): '  ', (3, 2): '  ',
                                  (4, 2): '  ', (5, 2): '  ', (6, 2): '  ', (7, 2): '  ', (8, 2): '  ', (9, 2): '| ',
                                  (0, 3): '| ', (1, 3): '  ', (2, 3): '  ', (3, 3): '  ', (4, 3): '  ', (5, 3): '  ',
                                  (6, 3): '  ', (7, 3): '  ', (8, 3): '  ', (9, 3): '| ', (0, 4): '| ', (1, 4): '  ',
                                  (2, 4): '  ', (3, 4): '  ', (4, 4): '  ', (5, 4): '  ', (6, 4): '  ', (7, 4): '  ',
                                  (8, 4): '  ', (9, 4): '| ', (0, 5): '| ', (1, 5): '  ', (2, 5): '  ', (3, 5): '  ',
                                  (4, 5): '  ', (5, 5): '  ', (6, 5): '  ', (7, 5): '  ', (8, 5): '  ', (9, 5): '| ',
                                  (0, 6): '| ', (1, 6): '  ', (2, 6): '  ', (3, 6): '  ', (4, 6): '  ', (5, 6): '  ',
                                  (6, 6): '  ', (7, 6): '  ', (8, 6): '  ', (9, 6): '| ', (0, 7): '| ', (1, 7): '  ',
                                  (2, 7): '  ', (3, 7): '  ', (4, 7): '  ', (5, 7): '  ', (6, 7): '  ', (7, 7): '  ',
                                  (8, 7): '  ', (9, 7): '| ', (0, 8): '| ', (1, 8): '  ', (2, 8): '  ', (3, 8): '  ',
                                  (4, 8): '  ', (5, 8): '  ', (6, 8): '  ', (7, 8): '  ', (8, 8): '  ', (9, 8): '| '})

    def test_QuoridorGame_set_vert_edges_dict(self):
        """
        Tests QuoridorGame set_vert_edges_dict.
        """
        q = QuoridorGame()
        q.set_vert_edges_dict({"a":1})
        result = q.get_vert_edges_dict()
        self.assertEqual(result, {"a":1})

    def test_QuoridorGame_get_spaces_dict(self):
        """
        Tests QuoridorGame get_spaces_dict.
        """
        q = QuoridorGame()
        result = q.get_spaces_dict()
        # this is only hard coded here for the purpose of the test
        self.assertEqual(result, {(0, 0): '  ', (1, 0): '  ', (2, 0): '  ', (3, 0): '  ', (4, 0): 'P1', (5, 0): '  ',
                                  (6, 0): '  ', (7, 0): '  ', (8, 0): '  ', (0, 1): '  ', (1, 1): '  ', (2, 1): '  ',
                                  (3, 1): '  ', (4, 1): '  ', (5, 1): '  ', (6, 1): '  ', (7, 1): '  ', (8, 1): '  ',
                                  (0, 2): '  ', (1, 2): '  ', (2, 2): '  ', (3, 2): '  ', (4, 2): '  ', (5, 2): '  ',
                                  (6, 2): '  ', (7, 2): '  ', (8, 2): '  ', (0, 3): '  ', (1, 3): '  ', (2, 3): '  ',
                                  (3, 3): '  ', (4, 3): '  ', (5, 3): '  ', (6, 3): '  ', (7, 3): '  ', (8, 3): '  ',
                                  (0, 4): '  ', (1, 4): '  ', (2, 4): '  ', (3, 4): '  ', (4, 4): '  ', (5, 4): '  ',
                                  (6, 4): '  ', (7, 4): '  ', (8, 4): '  ', (0, 5): '  ', (1, 5): '  ', (2, 5): '  ',
                                  (3, 5): '  ', (4, 5): '  ', (5, 5): '  ', (6, 5): '  ', (7, 5): '  ', (8, 5): '  ',
                                  (0, 6): '  ', (1, 6): '  ', (2, 6): '  ', (3, 6): '  ', (4, 6): '  ', (5, 6): '  ',
                                  (6, 6): '  ', (7, 6): '  ', (8, 6): '  ', (0, 7): '  ', (1, 7): '  ', (2, 7): '  ',
                                  (3, 7): '  ', (4, 7): '  ', (5, 7): '  ', (6, 7): '  ', (7, 7): '  ', (8, 7): '  ',
                                  (0, 8): '  ', (1, 8): '  ', (2, 8): '  ', (3, 8): '  ', (4, 8): 'P2', (5, 8): '  ',
                                  (6, 8): '  ', (7, 8): '  ', (8, 8): '  '})

    def test_QuoridorGame_set_spaces_dict(self):
        """
        Tests QuoridorGame set_spaces_dict.
        """
        q = QuoridorGame()
        q.set_spaces_dict({"a":1})
        result = q.get_spaces_dict()
        self.assertEqual(result, {"a":1})

    def test_QuoridorGame_get_game_won(self):
        """
        Tests QuoridorGame get_game_won.
        """
        q = QuoridorGame()
        result = q.get_game_won()
        self.assertFalse(result)

    def test_QuoridorGame_set_game_won(self):
        """
        Tests QuoridorGame set_game_won.
        """
        q = QuoridorGame()
        q.set_game_won(True)
        result = q.get_game_won()
        self.assertTrue(result)

    def test_QuoridorGame_get_winner(self):
        """
        Tests QuoridorGame get_winner.
        """
        q = QuoridorGame()
        result = q.get_winner()
        self.assertEqual(result, None)

    def test_QuoridorGame_set_winner(self):
        """
        Tests QuoridorGame set_winner.
        """
        q = QuoridorGame()
        q.set_winner(1)
        result = q.get_winner()
        self.assertEqual(result, 1)

    def test_QuoridorGame_get_player_1_turn(self):
        """
        Tests QuoridorGame get_player_1_turn.
        """
        q = QuoridorGame()
        result = q.get_player_1_turn()
        self.assertTrue(result)

    def test_QuoridorGame_set_player_1_turn(self):
        """
        Tests QuoridorGame set_player_1_turn.
        """
        q = QuoridorGame()
        q.set_player_1_turn(False)
        result = q.get_player_1_turn()
        self.assertFalse(result)

    def test_QuoridorGame_get_player_2_turn(self):
        """
        Tests QuoridorGame get_player_2_turn.
        """
        q = QuoridorGame()
        result = q.get_player_2_turn()
        self.assertFalse(result)

    def test_QuoridorGame_set_player_2_turn(self):
        """
        Tests QuoridorGame set_player_2_turn.
        """
        q = QuoridorGame()
        q.set_player_2_turn(True)
        result = q.get_player_1_turn()
        self.assertTrue(result)

    def test_QuoridorGame_amend_board(self):
        """
        Tests QuoridorGame amend_board.
        """
        q = QuoridorGame()
        horiz_edges_dict = {(0, 0): '**', (1, 0): '**', (2, 0): '**', (3, 0): '**', (4, 0): '**', (5, 0): '**',
                                  (6, 0): '**', (7, 0): '**', (8, 0): '**', (0, 1): '  ', (1, 1): '  ', (2, 1): '  ',
                                  (3, 1): '  ', (4, 1): '  ', (5, 1): '  ', (6, 1): '  ', (7, 1): '  ', (8, 1): '  ',
                                  (0, 2): '  ', (1, 2): '  ', (2, 2): '  ', (3, 2): '  ', (4, 2): '  ', (5, 2): '  ',
                                  (6, 2): '  ', (7, 2): '  ', (8, 2): '  ', (0, 3): '  ', (1, 3): '  ', (2, 3): '  ',
                                  (3, 3): '  ', (4, 3): '  ', (5, 3): '  ', (6, 3): '  ', (7, 3): '  ', (8, 3): '  ',
                                  (0, 4): '  ', (1, 4): '  ', (2, 4): '  ', (3, 4): '  ', (4, 4): '  ', (5, 4): '  ',
                                  (6, 4): '  ', (7, 4): '  ', (8, 4): '  ', (0, 5): '  ', (1, 5): '  ', (2, 5): '  ',
                                  (3, 5): '  ', (4, 5): '  ', (5, 5): '  ', (6, 5): '  ', (7, 5): '  ', (8, 5): '  ',
                                  (0, 6): '  ', (1, 6): '  ', (2, 6): '  ', (3, 6): '  ', (4, 6): '  ', (5, 6): '  ',
                                  (6, 6): '  ', (7, 6): '  ', (8, 6): '  ', (0, 7): '  ', (1, 7): '  ', (2, 7): '  ',
                                  (3, 7): '  ', (4, 7): '  ', (5, 7): '  ', (6, 7): '  ', (7, 7): '  ', (8, 7): '  ',
                                  (0, 8): '  ', (1, 8): '  ', (2, 8): '  ', (3, 8): '  ', (4, 8): '  ', (5, 8): '  ',
                                  (6, 8): '  ', (7, 8): '  ', (8, 8): '  ', (0, 9): '**', (1, 9): '**', (2, 9): '**',
                                  (3, 9): '**', (4, 9): '**', (5, 9): '**', (6, 9): '**', (7, 9): '**', (8, 9): '**'}
        vert_edges_dict = {(0, 0): '@ ', (1, 0): '  ', (2, 0): '  ', (3, 0): '  ', (4, 0): '  ', (5, 0): '  ',
                                  (6, 0): '  ', (7, 0): '  ', (8, 0): '  ', (9, 0): '@ ', (0, 1): '@ ', (1, 1): '  ',
                                  (2, 1): '  ', (3, 1): '  ', (4, 1): '  ', (5, 1): '  ', (6, 1): '  ', (7, 1): '  ',
                                  (8, 1): '  ', (9, 1): '@ ', (0, 2): '@ ', (1, 2): '  ', (2, 2): '  ', (3, 2): '  ',
                                  (4, 2): '  ', (5, 2): '  ', (6, 2): '  ', (7, 2): '  ', (8, 2): '  ', (9, 2): '@ ',
                                  (0, 3): '@ ', (1, 3): '  ', (2, 3): '  ', (3, 3): '  ', (4, 3): '  ', (5, 3): '  ',
                                  (6, 3): '  ', (7, 3): '  ', (8, 3): '  ', (9, 3): '@ ', (0, 4): '@ ', (1, 4): '  ',
                                  (2, 4): '  ', (3, 4): '  ', (4, 4): '  ', (5, 4): '  ', (6, 4): '  ', (7, 4): '  ',
                                  (8, 4): '  ', (9, 4): '@ ', (0, 5): '@ ', (1, 5): '  ', (2, 5): '  ', (3, 5): '  ',
                                  (4, 5): '  ', (5, 5): '  ', (6, 5): '  ', (7, 5): '  ', (8, 5): '  ', (9, 5): '@ ',
                                  (0, 6): '@ ', (1, 6): '  ', (2, 6): '  ', (3, 6): '  ', (4, 6): '  ', (5, 6): '  ',
                                  (6, 6): '  ', (7, 6): '  ', (8, 6): '  ', (9, 6): '@ ', (0, 7): '@ ', (1, 7): '  ',
                                  (2, 7): '  ', (3, 7): '  ', (4, 7): '  ', (5, 7): '  ', (6, 7): '  ', (7, 7): '  ',
                                  (8, 7): '  ', (9, 7): '@ ', (0, 8): '@ ', (1, 8): '  ', (2, 8): '  ', (3, 8): '  ',
                                  (4, 8): '  ', (5, 8): '  ', (6, 8): '  ', (7, 8): '  ', (8, 8): '  ', (9, 8): '@ '}
        spaces_dict = {(0, 0): 'b ', (1, 0): 'b ', (2, 0): 'b ', (3, 0): 'b ', (4, 0): 'P1', (5, 0): 'b ',
                                  (6, 0): 'b ', (7, 0): 'b ', (8, 0): 'b ', (0, 1): 'b ', (1, 1): 'b ', (2, 1): 'b ',
                                  (3, 1): 'b ', (4, 1): 'b ', (5, 1): 'b ', (6, 1): 'b ', (7, 1): 'b ', (8, 1): 'b ',
                                  (0, 2): 'b ', (1, 2): 'b ', (2, 2): 'b ', (3, 2): 'b ', (4, 2): 'b ', (5, 2): 'b ',
                                  (6, 2): 'b ', (7, 2): 'b ', (8, 2): 'b ', (0, 3): 'b ', (1, 3): 'b ', (2, 3): 'b ',
                                  (3, 3): 'b ', (4, 3): 'b ', (5, 3): 'b ', (6, 3): 'b ', (7, 3): 'b ', (8, 3): 'b ',
                                  (0, 4): 'b ', (1, 4): 'b ', (2, 4): 'b ', (3, 4): 'b ', (4, 4): 'b ', (5, 4): 'b ',
                                  (6, 4): 'b ', (7, 4): 'b ', (8, 4): 'b ', (0, 5): 'b ', (1, 5): 'b ', (2, 5): 'b ',
                                  (3, 5): 'b ', (4, 5): 'b ', (5, 5): 'b ', (6, 5): 'b ', (7, 5): 'b ', (8, 5): 'b ',
                                  (0, 6): 'b ', (1, 6): 'b ', (2, 6): 'b ', (3, 6): 'b ', (4, 6): 'b ', (5, 6): 'b ',
                                  (6, 6): 'b ', (7, 6): 'b ', (8, 6): 'b ', (0, 7): 'b ', (1, 7): 'b ', (2, 7): 'b ',
                                  (3, 7): 'b ', (4, 7): 'b ', (5, 7): 'b ', (6, 7): 'b ', (7, 7): 'b ', (8, 7): 'b ',
                                  (0, 8): 'b ', (1, 8): 'b ', (2, 8): 'b ', (3, 8): 'b ', (4, 8): 'P2', (5, 8): 'b ',
                                  (6, 8): 'b ', (7, 8): 'b ', (8, 8): 'b '}
        q.set_horiz_edges_dict(horiz_edges_dict)
        q.set_vert_edges_dict(vert_edges_dict)
        q.set_spaces_dict(spaces_dict)
        q.amend_board()
        result = q.get_board()
        self.assertEqual(result, [
            ['. ', '**', '. ', '**', '. ', '**', '. ', '**', '. ', '**', '. ', '**', '. ', '**', '. ', '**', '. ', '**', '. '],
            ['@ ', 'b ', '  ', 'b ', '  ', 'b ', '  ', 'b ', '  ', 'P1', '  ', 'b ', '  ', 'b ', '  ', 'b ', '  ', 'b ', '@ '],
            ['. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. '],
            ['@ ', 'b ', '  ', 'b ', '  ', 'b ', '  ', 'b ', '  ', 'b ', '  ', 'b ', '  ', 'b ', '  ', 'b ', '  ', 'b ', '@ '],
            ['. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. '],
            ['@ ', 'b ', '  ', 'b ', '  ', 'b ', '  ', 'b ', '  ', 'b ', '  ', 'b ', '  ', 'b ', '  ', 'b ', '  ', 'b ', '@ '],
            ['. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. '],
            ['@ ', 'b ', '  ', 'b ', '  ', 'b ', '  ', 'b ', '  ', 'b ', '  ', 'b ', '  ', 'b ', '  ', 'b ', '  ', 'b ', '@ '],
            ['. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. '],
            ['@ ', 'b ', '  ', 'b ', '  ', 'b ', '  ', 'b ', '  ', 'b ', '  ', 'b ', '  ', 'b ', '  ', 'b ', '  ', 'b ', '@ '],
            ['. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. '],
            ['@ ', 'b ', '  ', 'b ', '  ', 'b ', '  ', 'b ', '  ', 'b ', '  ', 'b ', '  ', 'b ', '  ', 'b ', '  ', 'b ', '@ '],
            ['. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. '],
            ['@ ', 'b ', '  ', 'b ', '  ', 'b ', '  ', 'b ', '  ', 'b ', '  ', 'b ', '  ', 'b ', '  ', 'b ', '  ', 'b ', '@ '],
            ['. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. '],
            ['@ ', 'b ', '  ', 'b ', '  ', 'b ', '  ', 'b ', '  ', 'b ', '  ', 'b ', '  ', 'b ', '  ', 'b ', '  ', 'b ', '@ '],
            ['. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. '],
            ['@ ', 'b ', '  ', 'b ', '  ', 'b ', '  ', 'b ', '  ', 'P2', '  ', 'b ', '  ', 'b ', '  ', 'b ', '  ', 'b ', '@ '],
            ['. ', '**', '. ', '**', '. ', '**', '. ', '**', '. ', '**', '. ', '**', '. ', '**', '. ', '**', '. ', '**', '. ']
        ])

    def test_QuoridorGame_amend_horiz_edges_dict(self):
        """
        Tests QuoridorGame amend_horiz_edges_dict.
        """
        q = QuoridorGame()
        q.amend_horiz_edges_dict((0,0), "**")
        q.amend_board()
        result = q.get_board()
        self.assertEqual(result, [
            ['. ', '**', '. ', '__', '. ', '__', '. ', '__', '. ', '__', '. ', '__', '. ', '__', '. ', '__', '. ', '__', '. '],
            ['| ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', 'P1', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '| '],
            ['. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. '],
            ['| ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '| '],
            ['. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. '],
            ['| ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '| '],
            ['. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. '],
            ['| ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '| '],
            ['. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. '],
            ['| ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '| '],
            ['. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. '],
            ['| ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '| '],
            ['. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. '],
            ['| ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '| '],
            ['. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. '],
            ['| ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '| '],
            ['. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. '],
            ['| ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', 'P2', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '| '],
            ['. ', '__', '. ', '__', '. ', '__', '. ', '__', '. ', '__', '. ', '__', '. ', '__', '. ', '__', '. ', '__', '. ']
        ])

    def test_QuoridorGame_amend_vert_edges_dict(self):
        """
        Tests QuoridorGame amend_vert_edges_dict.
        """
        q = QuoridorGame()
        q.amend_vert_edges_dict((0,0), "f ")
        q.amend_board()
        result = q.get_board()
        self.assertEqual(result, [
            ['. ', '__', '. ', '__', '. ', '__', '. ', '__', '. ', '__', '. ', '__', '. ', '__', '. ', '__', '. ', '__', '. '],
            ['f ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', 'P1', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '| '],
            ['. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. '],
            ['| ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '| '],
            ['. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. '],
            ['| ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '| '],
            ['. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. '],
            ['| ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '| '],
            ['. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. '],
            ['| ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '| '],
            ['. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. '],
            ['| ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '| '],
            ['. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. '],
            ['| ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '| '],
            ['. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. '],
            ['| ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '| '],
            ['. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. '],
            ['| ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', 'P2', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '| '],
            ['. ', '__', '. ', '__', '. ', '__', '. ', '__', '. ', '__', '. ', '__', '. ', '__', '. ', '__', '. ', '__', '. ']
        ])

    def test_QuoridorGame_amend_spaces_dict(self):
        """
        Tests QuoridorGame amend_spaces_dict.
        """
        q = QuoridorGame()
        q.amend_spaces_dict((0,0), "P3")
        q.amend_board()
        result = q.get_board()
        self.assertEqual(result, [
            ['. ', '__', '. ', '__', '. ', '__', '. ', '__', '. ', '__', '. ', '__', '. ', '__', '. ', '__', '. ', '__', '. '],
            ['| ', 'P3', '  ', '  ', '  ', '  ', '  ', '  ', '  ', 'P1', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '| '],
            ['. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. '],
            ['| ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '| '],
            ['. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. '],
            ['| ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '| '],
            ['. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. '],
            ['| ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '| '],
            ['. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. '],
            ['| ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '| '],
            ['. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. '],
            ['| ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '| '],
            ['. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. '],
            ['| ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '| '],
            ['. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. '],
            ['| ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '| '],
            ['. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. '],
            ['| ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', 'P2', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '| '],
            ['. ', '__', '. ', '__', '. ', '__', '. ', '__', '. ', '__', '. ', '__', '. ', '__', '. ', '__', '. ', '__', '. ']
        ])

    def test_QuoridorGame_is_winner(self):
        """
        Tests QuoridorGame is_winner.
        """
        q = QuoridorGame()
        result = q.is_winner(1)
        self.assertFalse(result)

    def test_QuoridorGame_pawn_position(self):
        """
        Tests QuoridorGame is_winner.
        """
        q = QuoridorGame()
        result = q.pawn_position(1)
        self.assertEqual(result, (4,0))



if __name__ == '__main__':      # #runs the unit tests
    unittest.main()