from abc import ABC, abstractmethod

class CantMovePieceException(Exception):
    pass

class Piece(ABC):

    @abstractmethod
    def __init__(self, color: str):
        self.color = color
