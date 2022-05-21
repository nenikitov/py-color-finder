from typing import Callable

from . import utils


DifferenceFunction = Callable[[utils.ColorType, utils.ColorType], float]


def get_delta(col1: utils.ColorType, col2: utils.ColorType) -> tuple[int, int, int]:
    r1, g1, b1 = utils.get_rgb(col1)
    r2, g2, b2 = utils.get_rgb(col2)

    return r2 - r1, g2 - g1, b2 - b1



def euclidean(col1: utils.ColorType, col2: utils.ColorType) -> float:
    dr, dg, db = get_delta(col1, col2)

    return (
        dr * dr
        + dg * dg
        + db * db
    )

def euclidean_weighted(col1: utils.ColorType, col2: utils.ColorType) -> float:
    r1, g1, b1 = utils.get_rgb(col1)
    r2, g2, b2 = utils.get_rgb(col1)
    dr, dg, db = get_delta(col1, col2)

    blend = 0.5 * (r1 + r2)

    return (
        (2 + blend / 255) * dr * dr
        + 4 * dg * dg
        + (2 + (255 - blend) / 256) * db * db
    )

