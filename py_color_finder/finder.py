from typing import Any
from enum import Enum

from .utils import ColorType


def ColorDifferenceMethod(Enum):
    pass


def closest_color(hex: ColorType, palette: list[ColorType] | dict[str, Any], method) -> str:
    print(hex)
