from src.data import board as board_module

def test_init_board_without_args():
    board = board_module.Board()
    assert board.squares == [
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None]
    ]

def test_init_board_with_args():
    board = board_module.Board(num_lines=2, num_columns=11)
    assert board.squares == [
        [None, None, None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None, None, None],
    ]

    