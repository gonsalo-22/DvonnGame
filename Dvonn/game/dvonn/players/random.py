from Dvonn.game.dvonn.player import DvonnPlayer
from Dvonn.game.state import State
from random import randint

import random
from Dvonn.game.dvonn.action import DvonnAction
from Dvonn.game.dvonn.state import DvonnState


def put_pieces(state: DvonnState) -> DvonnAction:
    return DvonnAction(randint(0, 20), randint(0, 4),
                       -1,
                       -1)


def move_play(state: DvonnState) -> DvonnAction:
    return DvonnAction(randint(0, 20), randint(0, 4), randint(0, 20), randint(0, 4)
                       )


class RandomDvonnPlayer(DvonnPlayer):

    def __init__(self, name):
        super().__init__(name)

    def get_action(self, state: DvonnState):
        state.display()
        if state.is_full():
            print("move")
            return move_play(state)
        else:
            print("put")
            return put_pieces(state)

    def event_action(self, pos: int, action, new_state: State):
        # ignore
        pass

    def event_end_game(self, final_state: State):
        # ignore
        pass
