from src.data.piece.piece import Piece
from src.data.position import Position
from src.data.board import Board
import uuid

class King(Piece):

    def __init__(self, color: str):
        self.uuid = uuid.uuid4().hex
        self.color = color
        self.name = "king"
        self.moved_times = 0

    def increase_moved_times(self, increase_num: int=1):
        self.moved_times += increase_num

    def can_move(self, board: Board, position: Position, new_position: Position) -> bool:
        possible_positions = [
            Position(num_line=position.line+1, num_column=position.column-1),
            Position(num_line=position.line+1, num_column=position.column),
            Position(num_line=position.line+1, num_column=position.column+1),
            Position(num_line=position.line, num_column=position.column-1),
            Position(num_line=position.line, num_column=position.column+1),
            Position(num_line=position.line-1, num_column=position.column-1),
            Position(num_line=position.line-1, num_column=position.column),
            Position(num_line=position.line-1, num_column=position.column+1),
        ]
        if not (new_position in possible_positions):
            return False
        if not board.has_square(new_position):
            return False
        piece = board.get_piece(new_position)
        if piece and piece.color == self.color:
            return False

        return True


