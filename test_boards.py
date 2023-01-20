from boards import BigBoard
from errors import SizeError, ActiveError, RangeError, PlaceError
import pytest


def test_validate_size():
    a = BigBoard(5)
    assert a._size == 5
    with pytest.raises(SizeError):
        _ = BigBoard(1)
    with pytest.raises(SizeError):
        _ = BigBoard(4)


def test_make_move():
    a = BigBoard(3)
    a.make_move(1, 1, 1, 1, "X")
    a.make_move(1, 1, 2, 2, "O")
    a.make_move(2, 2, 0, 0, "X")

    assert a.get_small_value(1, 1, 1, 1) == "X"
    assert a.get_small_value(1, 1, 2, 2) == "O"
    assert a.get_small_value(2, 2, 0, 0) == "X"


def test_move_out_of_range():
    a = BigBoard(3)
    with pytest.raises(RangeError):
        a.make_move(2, 2, 3, 3, "X")


def test_move_place_taken():
    a = BigBoard(3)
    a.make_move(1, 1, 1, 1, "X")
    with pytest.raises(PlaceError):
        a.make_move(1, 1, 1, 1, "O")


def test_move_finished_board():
    a = BigBoard(3)
    a.make_move(0, 0, 2, 2, "X")
    a.make_move(2, 2, 0, 0, "O")
    a.make_move(0, 0, 1, 1, "X")
    a.make_move(1, 1, 0, 0, "O")
    a.make_move(0, 0, 0, 0, "X")
    with pytest.raises(PlaceError):
        a.make_move(0, 0, 2, 1, "O")


def test_move_not_active_board():
    a = BigBoard(3)
    a.make_move(1, 1, 1, 1, "X")
    with pytest.raises(ActiveError):
        a.make_move(0, 0, 0, 0, "O")


def test_active_boards():
    a = BigBoard(3)
    assert a.which_active() == "all"
    a.make_move(0, 0, 0, 0, "X")
    assert a.which_active() == (0, 0)
    a.make_move(0, 0, 1, 1, "O")
    assert a.which_active() == (1, 1)


def test_winner_none():
    a = BigBoard(3)
    assert a.check_winner() is None
    assert a.active is True


def test_winner():
    a = BigBoard(3)
    a.make_move(0, 0, 0, 0, "X")
    a.make_move(0, 0, 1, 1, "O")
    a.make_move(1, 1, 0, 0, "X")
    a.make_move(0, 0, 0, 1, "O")
    a.make_move(0, 1, 0, 0, "X")
    a.make_move(0, 0, 2, 1, "O")
    a.make_move(2, 1, 1, 1, "X")
    a.make_move(1, 1, 1, 1, "O")
    a.make_move(1, 1, 2, 2, "X")
    a.make_move(2, 2, 2, 2, "O")
    a.make_move(2, 2, 0, 0, "X")
    a.make_move(1, 1, 0, 1, "O")
    a.make_move(0, 1, 1, 1, "X")
    a.make_move(1, 1, 2, 1, "O")
    a.make_move(2, 1, 2, 2, "X")
    a.make_move(2, 2, 2, 1, "O")
    a.make_move(2, 1, 0, 0, "X")
    a.make_move(2, 2, 2, 0, "O")
    assert a.check_winner() == "O"
    assert a.active is False
