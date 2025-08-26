class BackgammonGame:
    """Coordina el flujo general del juego."""
    def __init__(self, board, players, dice):
        self.__board__ = board
        self.__players__ = players
        self.__dice__ = dice
        self.__current_player_index__ = 0

    def current_player(self):
        return self.__players__[self.__current_player_index__]

    def roll(self):
        return self.__dice__.roll()
