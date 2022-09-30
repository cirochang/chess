from src.data.position import Position
from src.data.piece.piece import Piece
from typing import List

class BoardGenerationException(Exception):
    pass

class PositionOutOfBoardException(Exception):
    pass

class MoveInvalidException(Exception):
    pass

class PieceNotFoundException(Exception):
    pass

class Board():
    def __init__(self, num_lines: int=8, num_columns: int=8) -> None:
        self.squares = None
        self.generate_new_board(num_lines, num_columns)

    def generate_new_board(self, num_lines: int, num_columns: int) -> None:
        if num_lines < 2:
            raise BoardGenerationException("The board should contain 2 or more lines")
        if num_columns < 2:
            raise BoardGenerationException("The board should contain 2 or more columns")
        squares = []
        for i in range(0, num_lines):
            squares.append([])
            for _ in range(0, num_columns):
                squares[i].append(None)
        self.squares = squares

    def has_square(self, position: Position):
        if position.line < 0:
            return False
        if position.line >= len(self.squares):
            return False
        if position.column < 0:
            return False
        if position.column >= len(self.squares[position.line]):
            return False
        return True

    def get_piece(self, position: Position):
        if not self.has_square(position=position):
            raise PositionOutOfBoardException(f"The position line: {position.line} / column: {position.column} is out of the board.")
        return self.squares[position.line][position.column]

    def get_position(self, piece: Piece):
        for i, _ in enumerate(self.squares):
            for j, _ in enumerate(self.squares[i]):
                _piece = self.squares[i][j]
                if _piece and piece.uuid == _piece.uuid:
                    return Position(i, j)
        raise PieceNotFoundException(f"The {piece.color} {piece.name} was not found in the board.")

    def get_positions_from_pieces(self, color: str=None):
        positions = []
        for i, _ in enumerate(self.squares):
            for j, _ in enumerate(self.squares[i]):
                piece = self.squares[i][j]
                if not piece:
                    continue
                if not color or (color and color == piece.color):
                    positions.append(Position(i, j))
        return positions

    def clean_board(self):
        for i, _ in enumerate(self.squares):
            for j, _ in enumerate(self.squares[i]):
                self.squares[i][j] = None

    def set_square(self, piece: Piece, position: Position) -> None:
        self.squares[position.line][position.column] = piece

    def set_squares(self, pieces_and_positions):
        for piece_and_position in pieces_and_positions:
            self.set_square(piece=piece_and_position[0], position=piece_and_position[1])

    def move_piece(self, position: Position, new_position: Position) -> None:
        piece = self.get_piece(position)
        if not piece:
            raise MoveInvalidException(f"There is no piece on position line: {position.line} / column: {position.column}")
        if not piece.can_move(board=self, position=position, new_position=new_position):
            raise MoveInvalidException(f"The {piece.color} {piece.name} cant be moved to the position line: {new_position.line} / column: {new_position.column}")
        self.set_square(piece=None, position=position)
        self.set_square(piece=piece, position=new_position)
        piece.increase_moved_times(1)
