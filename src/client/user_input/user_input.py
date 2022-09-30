from abc import abstractmethod
from src.data.board import Board

from abc import ABC, abstractmethod

class UserInput():
    def __init__(self):
        pass

    @abstractmethod
    def say_drawn_board(self, board: Board) -> None:
        pass

    @abstractmethod
    def say_is_player_turn(self, player_color: str) -> None:
        pass

    @abstractmethod
    def say_color_wins(self, winner_color: str) -> None:
        pass

    @abstractmethod
    def say_player_is_in_check(self, player_color: str) -> None:
        pass

    @abstractmethod
    def ask_for_play_again(self) -> bool:
        return True

    @abstractmethod
    def ask_to_cancel_piece_chosen(self) -> bool:
        return False

    @abstractmethod
    def ask_for_choose_a_piece(self, player_color: str) -> str:
        return ""

    @abstractmethod
    def ask_for_move_the_piece(self, player_color: str) -> str:
        return ""


