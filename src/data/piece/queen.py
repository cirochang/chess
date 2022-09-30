from src.data.piece.piece import Piece
from src.data.position import Position
from src.data.board import Board
from src.data.piece.tower import Tower
from src.data.piece.bishop import Bishop

import uuid

class Queen(Piece):

    def __init__(self, color: str):
        self.uuid = uuid.uuid4().hex
        self.color = color
        self.name = "queen"
        self.moved_times = 0

    def increase_moved_times(self, increase_num: int=1):
        self.moved_times += increase_num

    def can_move(self, board: Board, position: Position, new_position: Position) -> bool:
        return (
            Tower(self.color).can_move(board=board, position=position, new_position=new_position)
            or Bishop(self.color).can_move(board=board, position=position, new_position=new_position)
        )


