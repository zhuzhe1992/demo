"""pkg_utils 的单元测试。"""

from pkg_utils import add


def test_add():
    assert add(1, 2) == 3
    assert add(-1, 1) == 0
    assert add(0, 0) == 0
