class Board:
    def __init__(self):
       
        self.points = [0] * 24
        self.bar = [0, 0]  
        self.home = [0, 0]  
        self.setup_initial_position()

    def setup_initial_position(self):
        # Configuración inicial estándar de backgammon
        self.points[0] = 2  
        self.points[5] = -5  
        self.points[7] = -3  
        self.points[11] = 5  
        self.points[12] = -5  
        self.points[16] = 3  
        self.points[18] = 5  
        self.points[23] = -2  

    def get_point(self, point_index):
        if point_index < 0 or point_index >= 24:
            raise ValueError("Posición fuera del tablero")
        return self.points[point_index]

    def get_pieces_on_bar(self, is_white):
        index = 0 if is_white else 1
        return self.bar[index]

    def get_pieces_at_home(self, is_white):
        index = 0 if is_white else 1
        return self.home[index]

    def move_piece(self, from_point, to_point, is_white):
        if from_point == -1:  # Moviendo desde la barra
            if self.bar[0 if is_white else 1] <= 0:
                return False
            self.bar[0 if is_white else 1] -= 1
        else:
            if from_point < 0 or from_point >= 24:
                return False
            if (is_white and self.points[from_point] <= 0) or (not is_white and self.points[from_point] >= 0):
                return False
            self.points[from_point] += -1 if is_white else 1

        if to_point == 24:  # Moviendo a casa
            self.home[0 if is_white else 1] += 1
            return True
            
        if to_point < 0 or to_point >= 24:
            return False
            
        # Verificar si el destino tiene una sola pieza del oponente
        if (is_white and self.points[to_point] == -1) or (not is_white and self.points[to_point] == 1):
            self.points[to_point] = 0
            self.bar[1 if is_white else 0] += 1
            
        # Añade la pieza al destino
        self.points[to_point] += 1 if is_white else -1
        return True

    def is_valid_move(self, from_point, to_point, is_white):
        # Valida movimientos desde la barra
        if from_point == -1:
            if self.bar[0 if is_white else 1] <= 0:
                return False
        elif from_point < 0 or from_point >= 24:
            return False
        # Verifica que haya piezas del jugador en el origen
        elif (is_white and self.points[from_point] <= 0) or (not is_white and self.points[from_point] >= 0):
            return False
            
        # Valida movimiento a casa
        if to_point == 24:
            return self.can_bear_off(is_white)
            
        if to_point < 0 or to_point >= 24:
            return False
            
        # Verifica si el destino permite el movimiento
        if (is_white and self.points[to_point] < -1) or (not is_white and self.points[to_point] > 1):
            return False
            
        return True
        
    def can_bear_off(self, is_white):
        # Verificar si el jugador puede sacar fichas (todas en el cuadrante final)
        home_quadrant_start = 18 if is_white else 0
        home_quadrant_end = 24 if is_white else 6
        
        # Si hay fichas en la barra, no puede sacar
        if self.bar[0 if is_white else 1] > 0:
            return False
            
        # Comprueba si todas las fichas están en el cuadrante final o en casa
        for i in range(24):
            if is_white:
                if i < home_quadrant_start and self.points[i] > 0:
                    return False
            else:
                if i >= home_quadrant_end and self.points[i] < 0:
                    return False
        
        return True 