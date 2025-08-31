class Checker:
    
    def __init__(self, player_id):
        self.__player_id__ = player_id
        self.__captured__ = False
        self.__bearing_off__ = False
    
    def get_player_id(self):
        return self.__player_id__
    
    def is_captured(self):
        return self.__captured__
    
    def set_captured(self, captured):
        self.__captured__ = captured
    
    def is_bearing_off(self):
        return self.__bearing_off__
    
    def set_bearing_off(self, bearing_off):
        self.__bearing_off__ = bearing_off 