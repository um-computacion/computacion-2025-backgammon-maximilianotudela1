from backgammon.core.board import Board
from backgammon.core.player import Player
from backgammon.core.dice import Dice

class Game:
    def __init__(self):
        self.board = Board()
        self.players = [Player(0), Player(1)]
        self.dice = Dice()
        self.current_player_index = 0
        self.game_over = False
        self.winner = None
    
    def get_current_player(self):
        return self.players[self.current_player_index]
    
    def switch_turn(self):
        self.current_player_index = 1 - self.current_player_index
    
    def roll_dice(self):
        return self.dice.roll()
    
    def make_move(self, from_position, steps):
        current_player = self.get_current_player()
        
        if steps not in self.dice.get_available_moves():
            return False
        
        move_result = self.board.move_checker(from_position, steps, current_player.id)
        
        if move_result:
            self.dice.use_value(steps)
            self.check_victory_conditions()
            
            if len(self.dice.get_available_moves()) == 0:
                self.switch_turn()
                
            return True
        
        return False
    
    def check_victory_conditions(self):
        for player_id in range(2):
            if self.board.home[player_id] == 15:
                self.game_over = True
                self.winner = self.players[player_id]
                break
    
    def get_available_moves(self):
        current_player = self.get_current_player()
        available_moves = []
        
        for pos in range(24):
            if self.board.can_move_from(pos, current_player.id):
                for step in self.dice.get_available_moves():
                    if self.board.is_valid_move(pos, step, current_player.id):
                        available_moves.append((pos, step))
        
        return available_moves
    
    def restart_game(self):
        self.board = Board()
        self.dice = Dice()
        self.current_player_index = 0
        self.game_over = False
        self.winner = None 