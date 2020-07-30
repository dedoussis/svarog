from dataclasses import dataclass
from typing import Optional


def test_can_build_primitive_str(build):
    assert build(str, "the-string") == "the-string"


def test_can_build_primitive_int(build):
    assert build(int, "3") == 3


def test_can_build_none(build):
    assert build(None, None) is None


def test_can_build_dataclass(build):
    @dataclass
    class A:
        foo: str

    assert build(A, {"foo": "bar"}) == A(foo="bar")


def test_can_build_optional(build):
    assert build(Optional[str], None) is None
    assert build(Optional[str], "str") == "str"
