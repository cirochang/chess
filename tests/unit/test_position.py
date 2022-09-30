from src.data import position as position_module

def test_position_init_by_letters():
    assert position_module.Position.init_by_letters("A1") == position_module.Position(0, 0)
    assert position_module.Position.init_by_letters("BA9") == position_module.Position(8, 26+26+1-1)
    assert position_module.Position.init_by_letters("AZ234") == position_module.Position(233, 26+26-1)

def test_():
    assert position_module.Position.letters(position_module.Position(0,0)) == "A1"