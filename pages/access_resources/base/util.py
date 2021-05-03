from PIL import ImageColor


def qt_color(hex_color: str):
    color_tuple = ImageColor.getcolor(f"#{hex_color}", "RGB")
    stylized_qt_color_string = f"rgb{color_tuple}"
    return stylized_qt_color_string
