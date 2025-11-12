import pytest
from app.main import get_coin_combination


@pytest.mark.parametrize(
    "cents, expected",
    [
        (0, [0, 0, 0, 0]),
        (1, [1, 0, 0, 0]),
        (5, [0, 1, 0, 0]),
        (10, [0, 0, 1, 0]),
        (25, [0, 0, 0, 1]),
        (6, [1, 1, 0, 0]),
        (17, [2, 1, 1, 0]),
        (50, [0, 0, 0, 2]),
        (99, [4, 0, 2, 3]),
    ],
)
def test_should_return_correct_coin_combination(
        cents: int,
        expected: list
) -> None:
    assert get_coin_combination(cents) == expected


@pytest.mark.parametrize("cents", [-1, -50, -999])
def test_should_raise_error_for_negative_values(cents: int) -> None:
    with pytest.raises(ValueError):
        get_coin_combination(cents)


@pytest.mark.parametrize("cents", [1.5, "10", None, [10]])
def test_should_raise_type_error_for_invalid_input_types(cents: int) -> None:
    with pytest.raises((TypeError, ValueError)):
        get_coin_combination(cents)
