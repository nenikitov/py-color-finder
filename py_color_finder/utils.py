import webcolors

TupleColor = tuple[int, int, int]
ColorType = str | TupleColor

def get_rgb(col: ColorType) -> TupleColor:
    if type(col) is str:
        return webcolors.hex_to_rgb(col)
    elif type(col) is tuple and len(col) == 3:
        return col
    else:
        raise TypeError(f'Input {col} is not a color')
