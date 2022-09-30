from src.client.user_input.user_input import UserInput
from src.data.board import Board
from src.data.position import Position
from colorama import Fore, Back, Style
from src.data.piece.piece import Piece
from src.const.colors import Colors

class Terminal(UserInput):
    board_lines_bcolor = Fore.YELLOW
    board_background_color = Back.GREEN
    white_piece_color = Fore.WHITE
    black_piece_color = Fore.BLACK

    def __init__(self):
        pass       

    def _get_piece_bcolor(self, piece: Piece):
        if not piece:
            return ""
        return {
            Colors.WHITE: self.white_piece_color,
            Colors.BLACK: self.black_piece_color
        }.get(piece.color, "")

    def _print_board_line(self, string: str):
        print(f"{self.board_background_color}{self.board_lines_bcolor}{string}{Style.RESET_ALL}")

    def say_drawn_board(self, board: Board):
        square_size = len(board.squares)
        self._print_board_line(f"-------------------")
        for index_line, _ in enumerate(board.squares):
            line = square_size - index_line - 1
            print_line = (f"{Position.line_letters(line)} |")
            for piece in board.squares[line]:
                piece_char = piece.name[0] if piece else " "
                piece_bcolor = self._get_piece_bcolor(piece)
                print_line += (f"{piece_bcolor}")
                print_line += (f"{piece_char}")
                print_line += (f"{self.board_lines_bcolor}|")
            self._print_board_line(print_line)
            if index_line + 1 == square_size:
                self._print_board_line("-------------------")
                print_line = ("  |")
                for index_column, piece in enumerate(board.squares[line]):
                    column = index_column
                    print_line += (f"{Position.column_letters(column)}|")
                self._print_board_line(print_line)

    def say_is_player_turn(self, player_color: str) -> None:
        print(f"It is {player_color.value} turns!")

    def say_color_wins(self, winner_color: str) -> None:
        print(f"Player {winner_color.value} wins!")

    def say_player_is_in_check(self, player_color: str) -> None:
        print(f"Player {player_color.value} is in Check!")
    
    def ask_for_play_again(self) -> bool:
        print(f"Do you want play again? [Y/N]: ")
        user_input = input()
        if user_input.lower() == "y":
            return True
        elif user_input.lower() == "n":
            return False
        return self.ask_for_play_again()

    def ask_for_choose_a_piece(self, player_color: str) -> str:
        print(f"Choose a piece: ")
        user_input = input()
        return user_input

    def ask_to_cancel_piece_chosen(self) -> str:
        return False

    def ask_for_move_the_piece(self, player_color: str) -> str:
        print("Move the piece to: ")
        user_input = input()
        return user_input
