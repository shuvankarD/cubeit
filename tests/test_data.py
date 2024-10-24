import pytest
from root import root


@pytest.mark.parametrize(
        ("num","num_root"),
        (
            (100,10),
            (36,16),
            (25,4),
            (9,3),

        )
)

def test_root(num, num_root):
    assert root(25) == 5