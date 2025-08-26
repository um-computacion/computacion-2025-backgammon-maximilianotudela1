class Board:
    """Representa el tablero y los puntos."""
    def __init__(self):
        self.__points__ = [[] for _ in range(24)]
        self.__bar__ = { 'white': [], 'black': [] }
        self.__borne_off__ = { 'white': [], 'black': [] }
