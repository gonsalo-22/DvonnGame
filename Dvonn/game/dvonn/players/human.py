from Dvonn.game.dvonn.action import DvonnAction
from Dvonn.game.dvonn.player import DvonnPlayer
from Dvonn.game.dvonn.state import DvonnState


def put_pieces(state: DvonnState) -> DvonnAction:
    a = (int(input(f"Player {state.get_acting_player()} choose a column: ")))
    b = (int(input(f"Choose a line: ")))

    return DvonnAction(a, b, -1, -1)


def move_play(state: DvonnState) -> DvonnAction:

    print(f"Player {state.get_acting_player()} choose a piece to move")

    a = (int(input(f"Column: ")))
    b = (int(input(f"Line: ")))

    print(f"Choose a place to put chosen piece:")
    c = (int(input(f"Column: ")))
    d = (int(input(f"Line: ")))

    return DvonnAction(a, b, c, d)


class HumanDvonnPlayer(DvonnPlayer):

    def __init__(self, name):
        super().__init__(name)

    def get_action(self, state: DvonnState):
        state.display()
        if state.is_full():
            print("Move a piece")
            return move_play(state)
        else:
            print("Put a piece")
            return put_pieces(state)

    def event_action(self, pos: int, action, new_state: DvonnState):
        # ignore
        pass

    def event_end_game(self, final_state: DvonnState):
        # ignore
        pass
