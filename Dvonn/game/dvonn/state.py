import random
from typing import Optional
from collections import Counter
from Dvonn.game.dvonn.action import DvonnAction
from Dvonn.game.dvonn.result import DvonnResult
from Dvonn.game.state import State

E = -1
_ = -2
W = 0
B = 1
R = 2
Q = 3


class DvonnState(State):

    def __init__(self):
        super().__init__()

        """
        the grid
        """

        self.__grid = [[_, _, E, _, E, _, E, _, E, _, E, _, E, _, E, _, E, _, E, _, _],
                       [_, E, _, E, _, E, _, E, _, E, _, E, _, E, _, E, _, E, _, E, _],
                       [E, _, E, _, E, _, E, _, E, _, E, _, E, _, E, _, E, _, E, _, E],
                       [_, E, _, E, _, E, _, E, _, E, _, E, _, E, _, E, _, E, _, E, _],
                       [_, _, E, _, E, _, E, _, E, _, E, _, E, _, E, _, E, _, E, _, _]
                       ]

        empty_places = []

        for row in range(0, len(self.__grid)):
            for col in range(0, len(self.__grid[0])):
                if self.__grid[row][col] == E:
                    empty_places.append([row, col])

        random.shuffle(empty_places)
        for i in range(0, 3):
            row = empty_places[i][0]
            col = empty_places[i][1]
            self.__grid[row][col] = R

        """
        counts the number of turns in the current game
        """
        self.__turns_count = 1

        """
        the index of the current acting player
        """
        self.__acting_player = 0

        """
        determine if a winner was found already 
        """
        self.__has_winner = False

    def __check_winner(self, player):
        pass

    def get_grid(self):
        return self.__grid

    def get_num_players(self):
        return 2

    def validate_action(self, action: DvonnAction) -> bool:

        org_col = action.get_org_col()
        org_row = action.get_org_row()
        dst_col = action.get_dst_col()
        dst_row = action.get_dst_row()

        if dst_col == -1 and dst_row == -1:
            # valid column
            if org_col < 0 or org_col > 20:
                return False
            if org_row < 0 or org_row > 4:
                return False
            if dst_col < -1 or dst_col > 20:
                return False
            if dst_row < -1 or dst_row > 4:
                return False

            if self.__grid[org_row][org_col] == _ or self.__grid[org_row][org_col] == W or self.__grid[org_row][
                org_col] == B or self.__grid[org_row][org_col] == R:
                return False

        elif dst_col != -1 and dst_row != -1:
            # valid column
            if self.__acting_player == 0 and self.__grid[org_row][org_col] == 1 or self.__grid[org_row][org_col] == 2 or \
                    self.__grid[org_row][org_col] == 3 or self.__grid[org_row][org_col] == -2:
                return False
            if self.__acting_player == 1 and self.__grid[org_row][org_col] == 0 or self.__grid[org_row][org_col] == 2 or \
                    self.__grid[org_row][org_col] == 3 or self.__grid[org_row][org_col] == -2:
                return False
            if org_col < 0 or org_col > 20:
                return False
            if org_row < 0 or org_row > 4:
                return False
            if dst_col < 0 or dst_col > 20:
                return False
            if dst_row < 0 or dst_row > 4:
                return False
            if self.__grid[dst_row][dst_col] == _:
                return False

            if self.__grid[org_row - 1][org_col - 1] != -2 and self.__grid[org_row][org_col - 2] != -2 and \
                    self.__grid[org_row][org_col + 2] != -2 and self.__grid[org_row - 1][org_col + 1] != -2 and \
                    self.__grid[org_row + 1][org_col + 1] != -2 and self.__grid[org_row + 1][
                org_col + -1] != -2 and \
                    self.__grid[org_row - 1][org_col - 1] != 3 and self.__grid[org_row][org_col - 2] != 3 and \
                    self.__grid[org_row][org_col + 2] != 3 and self.__grid[org_row - 1][org_col + 1] != 3 and \
                    self.__grid[org_row + 1][org_col + 1] != 3 and self.__grid[org_row + 1][org_col + -1] != 3:
                return False

            if self.__grid[dst_row][dst_col] == 3:
                return False

            if self.__grid[org_col] == self.__grid[dst_col]:
                return False

        return True

    def update(self, action: DvonnAction):

        # if not self.is_full():
        org_col = action.get_org_col()
        org_row = action.get_org_row()
        dst_col = action.get_dst_col()
        dst_row = action.get_dst_row()

        if dst_col == -1 and dst_row == -1:

            self.__grid[org_row][org_col] = self.__acting_player

            # determine if there is a winner
            self.__check_winner(self.__acting_player)

            # switch to next player
            self.__acting_player = 1 if self.__acting_player == 0 else 0

            self.__turns_count += 1


        elif dst_col != -1 and dst_row != -1:

            self.__grid[org_row][org_col] = 3

            self.__grid[dst_row][dst_col] = self.__acting_player

            # determine if there is a winner
            self.__check_winner(self.__acting_player)

            # switch to next player
            self.__acting_player = 1 if self.__acting_player == 0 else 0

            self.__turns_count += 1

        # if self.neighborsRemove():

        #   return

    #    def neighborsRemove(self) -> bool:
    #        result = []
    #        c = 0
    #        row = self.get_num_rows()
    #        col = self.get_num_cols()
    #        # verificar os das pontas
    #        for r in range(0,5):
    #            for c in range(0,21):
    #
    #                if (r - 2) >= 0:
    #                    c += 1
    #                    if self.__grid[r - 2][c] == Q:
    #                        result.append(self.__grid[r - 2][c])
    #                if (r + 2) <= row:
    #                    c += 1
    #                    if self.__grid[r + 2][c] == Q:
    #                        result.append(self.__grid[r + 2][c])
    #
    #                # verificar os da diagonal
    #                if (r - 1) >= 0 and (c - 1) >= 0:
    #                    c += 1
    #                    if self.__grid[r - 1][c - 1] == Q:
    #                        result.append(self.__grid[r - 1][c - 1])
    #
    #                if (r - 1) >= 0 and (c + 1) <= col:
    #                    c += 1
    #                    if self.__grid[r - 1][c + 1] == Q:
    #                        result.append(self.__grid[r - 1][c + 1])
    #
    #                if (r + 1) <= row and (c - 1) <= col:
    #                    c += 1
    #                    if self.__grid[r + 1][c - 1] == Q:
    #                        result.append(self.__grid[r + 1][c - 1])
    #
    #                if (r + 1) <= row and (c + 1) >= 0:
    #                    c += 1
    #                    if self.__grid[r + 1][c + 1] == Q:
    #                        result.append(self.__grid[r + 1][c + 1])
    #
    #        return c == len(result)

    def __display_cell(self, row, col):
        print({
                  W: 'W',
                  B: 'B',
                  R: 'R',
                  E: 'o',
                  _: ' ',
                  Q: 'x'
              }[self.__grid[row][col]], end="")

    def __display_numbers(self):
        print(' ', end="")
        for col in range(0, len(self.__grid[0])):
            if col <= 20:
                print('  ', end="")
            print(col, end="")
        print("")

    def __display_separator(self):
        print(' ', end="")
        for col in range(0, len(self.__grid[0])):
            print("--", end="")
        print("-")

    def display(self):
        self.__display_numbers()

        for row in range(0, 5):
            if row < len(self.__grid):
                print(row, ' ', end="")
            else:
                print(row, ' ', end="")
            for col in range(0, 21):
                if col >= 10:
                    print(" ", end="")
                self.__display_cell(row, col)
                print('  ', end="")
            print("")

        self.__display_numbers()
        print("")

    def is_full(self) -> bool:

        for i in range(0, 4):
            for j in range(0, 20):
                if self.__grid[i][j] == -1:
                    return False
        return True

    def is_finished(self) -> bool:
        return self.__has_winner  # or self.is_full()

    def get_acting_player(self) -> int:
        return self.__acting_player

    def clone(self):
        cloned_state = DvonnState()
        cloned_state.__turns_count = self.__turns_count
        cloned_state.__acting_player = self.__acting_player
        cloned_state.__has_winner = self.__has_winner
        for row in range(0, len(self.__grid)):
            for col in range(0, len(self.__grid[0])):
                cloned_state.__grid[row][col] = self.__grid[row][col]
        return cloned_state

    def get_result(self, pos) -> Optional[DvonnResult]:
        if self.__has_winner:
            return DvonnResult.LOOSE if pos == self.__acting_player else DvonnResult.WIN
        return None

    def get_num_rows(self):
        return len(self.__grid)

    def get_num_cols(self):
        return len(self.__grid[0])

    def before_results(self):
        pass
