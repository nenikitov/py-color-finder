from .utils import ColorType, get_rgb

def get_delta(col1: ColorType, col2: ColorType) -> tuple[int, int, int]:
    r1, g1, b1 = get_rgb(col1)
    r2, g2, b2 = get_rgb(col1)

    return r2 - r1, g2 - g1, b2 - b1

def euclidean(col1: ColorType, col2: ColorType) -> int:
    dr, dg, db = get_delta(col1, col2)

    return (
        dr * dr
        + dg * dg
        + db * db
    )

def euclidean(col1: ColorType, col2: ColorType) -> int:
    r1, g1, b1 = get_rgb(col1)
    r2, g2, b2 = get_rgb(col1)
    dr, dg, db = get_delta(col1, col2)

    blend = 0.5 * (r1 + r2)

    return (
        (2 + blend / 255) * dr * dr
        + 4 * dg * dg
        + (2 + (255 - blend) / 256) * db * db
    )

