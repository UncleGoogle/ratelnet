from typing import TypeAlias, TypeVar


RegexStr: TypeAlias = str
T = TypeVar('T', bound=RegexStr)


def scan_content(content: bytes, regex_patterns: list[T]) -> dict[T, bool]:
    # dummy impl to always say ok
    return {k: True for k in regex_patterns}
