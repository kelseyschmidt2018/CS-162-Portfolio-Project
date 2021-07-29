# Author: Kelsey Schmidt
# Date: 7-28-21
# Description:  # Creates a class named QuoridorGame for playing a board game called Quoridor.
                # This class plays the two-player version of the game.


class QuoridorGame:
    """
    Creates a game of Quoridor, to be played by two players.
    The board is formed by a 9k9 grid, upon which the two players will each have a pawn,
    and each player's pawn will move on the cells. Each player will have 10 fences.
    The fences can be placed on the edges of the cells, to obstruct the other player's pawn's movement.

    The board spaces are numbered 0-8 from left to right, and top to bottom.
    The four edges are labeled as fences, and the rows of the cells where the pawns
    are positioned at the start of the game (rows 0 and 8) are called base lines.

    The pawn position (k,y) is defined by the coordinate of the top left corner of the cell
    that the pawn is on. k is the number from the vertical line
    and y is the number from the horizontal line, making the top left corner of the cell.
    The board positions start with (0,0) and end at (8,8).
    At the beginning of the game, player 1 places pawn 1 (P1) on the top center of the board, (4,0),
    and player 2 places pawn 2 (P2) on the bottom center of the board, (4,8).

    When a player tries to place a fence on the board, the position of the fence is defined
    by a letter and coordinates; “v” for vertical fences, and “h” for horizontal fences,
    and a tuple of the coordinates. So, for ekample, “h”,(6,5) would be a horizontal fence
    starting at the (6,5) coordinate, and drawn one space to the right, whereas  “v”,(6,5)
    would be a vertical fence starting at the (6,5) coordinate, and drawn one space down.
    Fences only block one square, and cannot be moved once placed, nor can they be re-used.
    On each turn, players can move one space or place a fence.
    Fences cannot be arranged in such a way that makes it impossible for the other player to win,
    such as blocking a player in, or blocking the target side of the board entirely.
    (This is the fair play rule)

    A valid move for a player to make would be moving one space horizontally or vertically,
    unless blocked by a fence, with no diagonal movement allowed EkCEPT for a special condition.
    If facing the other player's piece directly, you are allowed to jump over the other piece,
    assuming no fence is behind the other player's piece that would stop that movement.
    It is in this case ONLY, when one could otherwise jump over an opponent's piece, but is blocked
    by a fence directly behind that piece, that the player can move one space *diagonally* to either
    of the spaces to the side of the opponent's piece, in lieu of going over.
    In this same scenario, if there is a fence to the *side* of the opponent's piece,
    in the intended move direction, that move is blocked by the fence, and cannot be completed.

    Player 1 will start the game. Each player takes turn playing.
    On a player’s turn they will make one move.
    They can either move the pawn (move_pawn) or place a fence (place_fence).
    The first player whose pawn reaches any of the cells of the opposite player's base line wins the game.
    No turn can be played after a player has won.

    This class contains methods:
        init
            - initializes the board with the fences (four edges) and pawns (P1 and P2) placed in the correct positions.
        move_pawn
            - takes the following two parameters in order:
                an integer that represents which player (1 or 2) is making the move,
                and a tuple with the coordinates of where the pawn is going to be moved to.
                    (ek. move_pawn(2, (4,7))
            - if the game has been already won, returns False
            - if the move is forbidden by the fair play rule or blocked by a fence, returns False
            - if the move was successful or if the move makes the player win, returns True
        place_fence
            - takes the following parameters in order:
                an integer that represents which player (1 or 2) is making the move,
                a letter indicating whether it is a vertical (v) or horizontal (h) fence,
                and a tuple of integers that represents the position on which the fence is to be placed.
            - if the game has been already won, returns False
            - if player has no fences left, returns False
            - if the intended fence position is out of the boundaries of the board, returns False
            - if there is already a fence at the intended position, returns False
            - if the intended position breaks the "fair play rule", returns the string "breaks the fair play rule"
            - if the fence can be placed successfully, returns True
        is_winner
            - takes a single integer representing the player number (1 or 2) as a parameter,
            - returns True if that player has won and False if that player has not won.
        print_board
            - takes no parameters
            - prints the board in a pretty manner.
    """

    def __init__(self):
        """
        Initializes the board with the fences (four edges) and pawns (P1 and P2) placed in the correct positions.
        All data members are private. Get and set methods are named in the usual fashion.
        """

        # all of these empty lists/dictionaries will get filled within the init function body

        self._board = []    # creates an empty list to hold the game board

        self._coords_dict = dict()  # creates an empty dictionary to hold the coordinates (". ", for visual clarity)
                                    # keys of the coords_dict are a tuple of the position

        self._spaces_dict = dict()  # creates an empty dictionary to hold the spaces ("  " unless filled with a pawn)
                                    # keys of the spaces_dict are a tuple of the position

        self._horiz_edges_dict = dict() # creates an empty dictionary to hold the  horiz edges
                                        # keys of the horiz_edges_dict are a tuple of the position
                                        # ("  " until filled with a fence, which looks like "--")

        self._vert_edges_dict = dict() # creates an empty dictionary to hold the
                                        # keys of the vert_edges_dict are a tuple of the position
                                        # ("  " until filled with a fence, which looks like "| ")

        self._game_won = False      # the game has not been won yet

        self._winner = None         # there is no winner yet

        self._player_1_turn = True  # the game starts on player 1's turn

        self._player_2_turn = False # the game starts on player 1's turn

        for i in range(0, 10):
            for j in range(0, 10):
                self._coords_dict[(j, i)] = ". "    # fill the coords_dict

        for i in range(0, 9):
            for j in range(0, 9):
                self._spaces_dict[(j, i)] = "  "    # fill the spaces_dict with un-occupied spaces
        self._spaces_dict[(4, 0)] = "P1"  # fill in player 1's default position
        self._spaces_dict[(4, 8)] = "P2"  # fill in player 2's default position


        for i in range(0, 10):
            for j in range(0, 9):
                if i == 0 or i ==9 :
                    self._horiz_edges_dict[(j, i)] = "--"
                else:
                    self._horiz_edges_dict[(j, i)] = "  "   # fill the horiz_edges_dict
                                                            # (outlines the outer edges with fences)


        for i in range(0, 9):
            for j in range(0, 10):
                if j == 0 or j == 9:
                    self._vert_edges_dict[(j, i)] = "| "
                else:
                    self._vert_edges_dict[(j, i)] = "  "    # fill the vert_edges_dict
                                                            #(outlines the outer edges with fences)

        for k in range(0, 10):
            horiz_row = []
            vert_row = []
            for i in range(k, k + 1):
                for j in range(0, 10):
                    if j != 9:
                        horiz_row.append(self._coords_dict[(j, i)])
                        horiz_row.append(self._horiz_edges_dict[(j, i)])
                    else:
                        horiz_row.append(self._coords_dict[(j, i)])
            self._board.append(horiz_row)
            if k == 9:
                break

            for i in range(k, k + 1):
                for j in range(0, 10):
                    if j != 9:
                        vert_row.append(self._vert_edges_dict[(j, i)])
                        vert_row.append(self._spaces_dict[(j, i)])
                    else:
                        vert_row.append(self._vert_edges_dict[(j, i)])
            self._board.append(vert_row)                                # fills up the game board with a default
                                                                        # board with the edges lined and 2 pawns
                                                                        # in starting position




    def print_board(self):
        """
        Takes no parameters
        Prints the board in a pretty manner.
        """



        #print(board)
        for line in self._board:
            print(*line[:])



def main():
    """
    A main function to run the program as a script or a module.
    """
    q = QuoridorGame()
    q.print_board()
    pass

if __name__ == '__main__':  # if running as a script, runs the main function
  main()