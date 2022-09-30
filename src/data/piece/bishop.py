from src.data.piece.piece import Piece
from src.data.position import Position
from src.data.board import Board
import math
import uuid

class Bishop(Piece):

    def __init__(self, color: str):
        self.uuid = uuid.uuid4().hex
        self.color = color
        self.name = "bishop"
        self.moved_times = 0

    def increase_moved_times(self, increase_num: int=1):
        self.moved_times += increase_num

    def can_move(self, board: Board, position: Position, new_position: Position) -> bool:
        diff_line = new_position.line - position.line
        diff_mod_line = int(math.sqrt((diff_line)**2))
        diff_column = new_position.column - position.column
        diff_mod_column = int(math.sqrt((diff_column)**2))
        if diff_mod_line != diff_mod_column:
            return False
        if not board.has_square(new_position):
            return False
        piece = board.get_piece(new_position)
        if piece and piece.color == self.color:
            return False
        for distance_line in range(1, diff_mod_line):
            line = position.line + distance_line if diff_line > 0 else position.line - distance_line
            column = position.column + distance_line if diff_column > 0 else position.column - distance_line
            if board.get_piece(Position(line, column)) != None:
                return False
        return True

