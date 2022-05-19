from .utils import ColorType, get_rgb

def euclidean(col1: ColorType, col2: ColorType) -> int:
    r1, g1, b1 = get_rgb(col1)
    r2, g2, b2 = get_rgb(col1)

    return (r2 - r1) ** 2 + (g2 - g1) ** 2 + (b2 - b1) ** 2

