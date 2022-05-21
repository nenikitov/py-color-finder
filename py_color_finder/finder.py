from typing import Any
from enum import Enum

from . import utils
from . import difference


class ColorDifferenceMethod(Enum):
    EUCLIDEAN          = difference.euclidean
    EUCLIDEAN_WEIGHTED = difference.euclidean_weighted


def closest_color(hex: utils.ColorType, palette: list[utils.ColorType] | dict[str, Any], method: difference.DifferenceFunction=ColorDifferenceMethod.EUCLIDEAN_WEIGHTED) -> str:
    print(hex)
