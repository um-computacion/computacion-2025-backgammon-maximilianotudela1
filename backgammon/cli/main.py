from core.game import BackgammonGame
from core.board import Board
from core.player import Player
from core.dice import Dice

def main():
    board = Board()
    players = [Player("Jugador 1", "white"), Player("Jugador 2", "black")]
    game = BackgammonGame(board, players, Dice())
    print("Backgammon CLI - Bienvenido")
    print("Tirada inicial:", game.roll())

if __name__ == "__main__":
    main()
