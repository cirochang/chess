from src.data.piece import tower as tower_module
from src.data.piece import horse as horse_module
from src.data import board as board_module
from src.data.position import Position
from src.const.colors import Colors

def test_can_move_tower():
    tower = tower_module.Tower(color=Colors.BLACK)
    board = board_module.Board(num_lines=8, num_columns=8)
    tower_position = Position(3, 3)
    board.set_square(
        piece=tower, position=tower_position
    )
    board.set_square(
        piece=horse_module.Horse(color=Colors.WHITE), position=Position(3, 6)
    )
    board.set_square(
        piece=horse_module.Horse(color=Colors.BLACK), position=Position(3, 1)
    )
    board.set_square(
        piece=horse_module.Horse(color=Colors.BLACK), position=Position(1, 3)
    )
    assert tower.can_move(board=board, position=tower_position, new_position=Position(3, 6)) == True
    assert tower.can_move(board=board, position=tower_position, new_position=Position(2, 3)) == True
    assert tower.can_move(board=board, position=tower_position, new_position=Position(3, 2)) == True
    assert tower.can_move(board=board, position=tower_position, new_position=Position(3, 7)) == False
    assert tower.can_move(board=board, position=tower_position, new_position=Position(1, 3)) == False
    assert tower.can_move(board=board, position=tower_position, new_position=Position(3, 1)) == False
    assert tower.can_move(board=board, position=tower_position, new_position=Position(2, 2)) == False
    assert tower.can_move(board=board, position=tower_position, new_position=Position(3, 3)) == False
