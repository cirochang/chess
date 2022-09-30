from src.data.piece.piece import Piece
from src.data.position import Position
from src.data.board import Board
import uuid

class Tower(Piece):

    def __init__(self, color: str):
        self.uuid = uuid.uuid4().hex
        self.color = color
        self.name = "tower"
        self.moved_times = 0

    def increase_moved_times(self, increase_num: int=1):
        self.moved_times += increase_num

    def can_move(self, board: Board, position: Position, new_position: Position) -> bool:
        if position.line == new_position.line and position.column == new_position.column:
            return False
        if position.line != new_position.line and position.column != new_position.column:
            return False
        if not board.has_square(new_position):
            return False
        piece = board.get_piece(new_position)
        if piece and piece.color == self.color:
            return False
        if position.line == new_position.line:
            for column in range(min(position.column, new_position.column) + 1, max(position.column, new_position.column)):
                if board.get_piece(Position(position.line, column)) != None:
                    return False
        if position.column == new_position.column:
            for line in range(min(position.line, new_position.line) + 1, max(position.line, new_position.line)):
                if board.get_piece(Position(line, position.column)) != None:
                    return False
        return True

