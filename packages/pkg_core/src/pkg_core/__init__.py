"""pkg-core-zhuzhe-test - 核心包，提供基础功能。"""

__version__ = "0.1.0"


def greet(name: str) -> str:
    """返回问候语。

    Args:
        name: 被问候的名字。

    Returns:
        问候字符串。
    """
    return f"Hello, {name}!"
