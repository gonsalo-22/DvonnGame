from game.dvonn.players.random import RandomDvonnPlayer
from game.dvonn.players.human import HumanDvonnPlayer
from game.dvonn.simulator import DvonnSimulator
from game.game_simulator import GameSimulator


def run_simulation(desc: str, simulator: GameSimulator, iterations: int):
    print(f"----- {desc} -----")

    for i in range(0, iterations):
        simulator.change_player_positions()
        simulator.run_simulation()

    print("Results for the game:")
    simulator.print_stats()


def main():
    print("---ESTG IA Games Simulator---")

    choice = 0

    num_iterations = 1

    print('Hello, welcome to Dvonn')
    print('Let´s begin :)')
    print('-Chose 1 to play 1v1')
    print('-Chose 2 to play against Computer with random actions')
    print('-Chose 3 to generate automatic plays between 2 random players')
    choice = int(input('Take a choice:'))

    if choice == 1:
        c4_simulations = [
            # uncomment to play as human
            {
                "name": "Dvonn - Human VS Human",
                "player1": HumanDvonnPlayer("Human"),
                "player2": HumanDvonnPlayer("Random")
            }]

        for sim in c4_simulations:
            run_simulation(sim["name"], DvonnSimulator(sim["player1"], sim["player2"]), num_iterations)

    if choice == 2:
        c4_simulations = [
            {
                "name": "Dvonn - Human VS Random",
                "player1": HumanDvonnPlayer("Human"),
                "player2": RandomDvonnPlayer("Random")
            }]
        for sim in c4_simulations:
            run_simulation(sim["name"], DvonnSimulator(sim["player1"], sim["player2"]), num_iterations)

    if choice == 3:
        c4_simulations = [
            {
                "name": "Dvonn - Random VS Random",
                "player1": RandomDvonnPlayer("Human"),
                "player2": RandomDvonnPlayer("Random")
            }]
        for sim in c4_simulations:
            run_simulation(sim["name"], DvonnSimulator(sim["player1"], sim["player2"]), num_iterations)


if __name__ == "__main__":
    main()
