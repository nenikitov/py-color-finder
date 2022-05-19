import webcolors

ColorType = str | tuple[int, int, int]

def get_rgb(col: ColorType) -> tuple[int, int, int]:
    if type(col) is str:
        return webcolors.hex_to_rgb(col)
    elif type(col) is tuple and len(col) == 3:
        return col
    else:
        raise TypeError(f'Input {col} is not a color')
