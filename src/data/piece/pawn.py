from src.data.piece.piece import Piece
from src.data.position import Position
from src.data.board import Board
from src.const.colors import Colors
import uuid

class Pawn(Piece):

    def __init__(self, color: str):
        self.uuid = uuid.uuid4().hex
        self.color = color
        self.name = "pawn"
        self.moved_times = 0

    def increase_moved_times(self, increase_num: int=1):
        self.moved_times += increase_num

    def can_move(self, board: Board, position: Position, new_position: Position) -> bool:
        if not board.has_square(new_position):
            return False
        piece = board.get_piece(new_position)
        # for whites
        if (
            self.color == Colors.WHITE and 
            Position(num_line=position.line+1, num_column=position.column) == new_position and 
            piece == None
        ):
            return True
        if (
            self.color == Colors.WHITE and
            Position(num_line=position.line+2, num_column=position.column) == new_position and
            piece == None and
            position.line == 1
        ):
            return True
        if (
            (self.color == Colors.WHITE) and
            (
                (Position(num_line=position.line+1, num_column=position.column+1) == new_position) or
                (Position(num_line=position.line+1, num_column=position.column-1) == new_position)
            ) and
            piece and
            (piece.color == Colors.BLACK)
        ):
            return True

        # for blacks
        if (
            self.color == Colors.BLACK and 
            Position(num_line=position.line-1, num_column=position.column) == new_position and 
            piece == None
        ):
            return True
        if (
            self.color == Colors.BLACK and
            Position(num_line=position.line-2, num_column=position.column) == new_position and
            piece == None and
            position.line == len(board.squares) - 2
        ):
            return True
        if (
            (self.color == Colors.BLACK) and
            (
                (Position(num_line=position.line-1, num_column=position.column+1) == new_position) or
                (Position(num_line=position.line-1, num_column=position.column-1) == new_position)
            ) and
            piece and 
            (piece.color == Colors.WHITE)
        ):
            return True
        return False
