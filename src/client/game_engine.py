from src.client.user_input.user_input import UserInput
from src.const.colors import Colors
from src.data.board import Board, MoveInvalidException, PositionOutOfBoardException
from src.data.piece.bishop import Bishop
from src.data.piece.horse import Horse
from src.data.piece.king import King
from src.data.piece.pawn import Pawn
from src.data.piece.queen import Queen
from src.data.piece.tower import Tower
from src.data.position import Position, UnableToReadLetter
from copy import deepcopy

class GameEngine():
    def __init__(self, user_input: UserInput) -> None:
        self.player_color_turn = None
        self.board = None
        self.user_input = user_input
        self.piece_king_black = None
        self.piece_king_white = None

    def set_players_turn(self, color: str):
        self.player_color_turn = color

    def change_players_turn(self):
        if self.player_color_turn == Colors.WHITE:
            self.set_players_turn(color=Colors.BLACK)
        else:
            self.set_players_turn(color=Colors.WHITE)

    def generate_default_board(self) -> Board:
        board = Board()
        board_num_lines = len(board.squares)
        self.piece_king_white = King(color=Colors.WHITE)
        self.piece_king_black = King(color=Colors.BLACK)
        board.set_squares(
            pieces_and_positions=[
                [Tower(color=Colors.WHITE), Position(num_line=0, num_column=0)],
                [Horse(color=Colors.WHITE), Position(num_line=0, num_column=1)],
                [Bishop(color=Colors.WHITE), Position(num_line=0, num_column=2)],
                [Queen(color=Colors.WHITE), Position(num_line=0, num_column=3)],
                [self.piece_king_white, Position(num_line=0, num_column=4)],
                [Bishop(color=Colors.WHITE), Position(num_line=0, num_column=5)],
                [Horse(color=Colors.WHITE), Position(num_line=0, num_column=6)],
                [Tower(color=Colors.WHITE), Position(num_line=0, num_column=7)],
                [Pawn(color=Colors.WHITE), Position(num_line=1, num_column=0)],
                [Pawn(color=Colors.WHITE), Position(num_line=1, num_column=1)],
                [Pawn(color=Colors.WHITE), Position(num_line=1, num_column=2)],
                [Pawn(color=Colors.WHITE), Position(num_line=1, num_column=3)],
                [Pawn(color=Colors.WHITE), Position(num_line=1, num_column=4)],
                [Pawn(color=Colors.WHITE), Position(num_line=1, num_column=5)],
                [Pawn(color=Colors.WHITE), Position(num_line=1, num_column=6)],
                [Pawn(color=Colors.WHITE), Position(num_line=1, num_column=7)],

                [Pawn(color=Colors.BLACK), Position(num_line=board_num_lines-2, num_column=0)],
                [Pawn(color=Colors.BLACK), Position(num_line=board_num_lines-2, num_column=1)],
                [Pawn(color=Colors.BLACK), Position(num_line=board_num_lines-2, num_column=2)],
                [Pawn(color=Colors.BLACK), Position(num_line=board_num_lines-2, num_column=3)],
                [Pawn(color=Colors.BLACK), Position(num_line=board_num_lines-2, num_column=4)],
                [Pawn(color=Colors.BLACK), Position(num_line=board_num_lines-2, num_column=5)],
                [Pawn(color=Colors.BLACK), Position(num_line=board_num_lines-2, num_column=6)],
                [Pawn(color=Colors.BLACK), Position(num_line=board_num_lines-2, num_column=7)],
                [Tower(color=Colors.BLACK), Position(num_line=board_num_lines-1, num_column=0)],
                [Horse(color=Colors.BLACK), Position(num_line=board_num_lines-1, num_column=1)],
                [Bishop(color=Colors.BLACK), Position(num_line=board_num_lines-1, num_column=2)],
                [Queen(color=Colors.BLACK), Position(num_line=board_num_lines-1, num_column=3)],
                [self.piece_king_black, Position(num_line=board_num_lines-1, num_column=4)],
                [Bishop(color=Colors.BLACK), Position(num_line=board_num_lines-1, num_column=5)],
                [Horse(color=Colors.BLACK), Position(num_line=board_num_lines-1, num_column=6)],
                [Tower(color=Colors.BLACK), Position(num_line=board_num_lines-1, num_column=7)],
            ]
        )
        return board

    def get_piece_position_by_user_input(self):
        user_input = self.user_input.ask_for_choose_a_piece(self.player_color_turn)
        try:
            position = Position.init_by_letters(user_input)
        except UnableToReadLetter:
            return self.get_piece_position_by_user_input()
        try:
            piece = self.board.get_piece(position)
        except PositionOutOfBoardException:
            return self.get_piece_position_by_user_input()
        if (not piece) or (piece.color != self.player_color_turn):
            return self.get_piece_position_by_user_input()
        return position

    def get_piece_new_position_by_user_input(self):
        user_input = self.user_input.ask_for_move_the_piece(self.player_color_turn)
        try:
            position = Position.init_by_letters(user_input)
        except UnableToReadLetter:
            return self.get_piece_new_position_by_user_input()
        return position

    def player_action(self):
        position = self.get_piece_position_by_user_input()
        new_position = self.get_piece_new_position_by_user_input()
        future_board = deepcopy(self.board)
        try:
            future_board.move_piece(position=position, new_position=new_position)
        except MoveInvalidException:
            return self.player_action()
        if self.is_player_in_check(self.player_color_turn, future_board):
            return self.player_action()
        self.board.move_piece(position, new_position)


    def is_game_over(self):
        return self.is_player_in_checkmate(self.player_color_turn, self.board)

    def is_player_in_check(self, player_color: str, board: Board):
        opponent_color = self.get_opponent_color(player_color)
        player_turn_king = self.piece_king_white if player_color == Colors.WHITE else self.piece_king_black
        player_turn_king_position = board.get_position(piece=player_turn_king)
        opponent_pieces_positions = board.get_positions_from_pieces(color=opponent_color)
        for opponent_piece_position in opponent_pieces_positions:
            if board.get_piece(opponent_piece_position).can_move(board, opponent_piece_position, player_turn_king_position):
                return True
        return False

    def get_opponent_color(self, player_color):
        return Colors.BLACK if player_color == Colors.WHITE else Colors.WHITE

    def is_player_in_checkmate(self, player_color, board: Board):
        player_pieces_positions = board.get_positions_from_pieces(color=player_color)
        for player_piece_position in player_pieces_positions:
            for line, _ in enumerate(self.board.squares):
                for column, _ in enumerate(self.board.squares[line]):
                    new_position = Position(line,column)
                    future_board = deepcopy(self.board)
                    try:
                        future_board.move_piece(position=player_piece_position, new_position=new_position)
                    except MoveInvalidException:
                        continue
                    if not self.is_player_in_check(player_color=player_color, board=future_board):
                        return False
        return True
    
    def game_turns_loop(self):
        while(not self.is_game_over()):
            self.user_input.say_drawn_board(self.board)
            if self.is_player_in_check(player_color=self.player_color_turn, board=self.board):
                self.user_input.say_player_is_in_check(player_color=self.player_color_turn)
            self.user_input.say_is_player_turn(player_color=self.player_color_turn)
            self.player_action()
            self.change_players_turn()

    def execute(self):
        self.board = self.generate_default_board()
        self.set_players_turn(Colors.WHITE)
        self.game_turns_loop()
        self.user_input.say_color_wins(winner_color=self.get_opponent_color(self.player_color_turn))
        if self.user_input.ask_for_play_again():
            return self.execute()

