import sys
import os
import turtle

from figures.simple import Circle, Square
from figures.advance import Rectangle, Pie, RegularPoligon
from loaders.json_loader import JSONLoader
from loaders.yaml_loader import YAMLLoader

FIGURE_TYPES = {
    "circle": Circle,
    "square": Square,
    "rectangle": Rectangle,
    "pie": Pie,
    "regular poligon": RegularPoligon
}


def main():
    if len(sys.argv) < 2:
        print("Usage: {} input.json".format(sys.argv[0]))
        return 1

    try:
        input_data = load_input_data(sys.argv[1])
        figures = create_figures(input_data)
        draw_figures(figures)
    except Exception as e:
        print("Invalid input file provided! Error: " + str(e))
        return 2


def load_input_data(input_filename):
    # os.path.splitext връща tuple с 2 стойности - име и разширение на файла
    filename, extension = os.path.splitext(input_filename)
    loader = None
    if extension == '.json':
        loader = JSONLoader(input_filename)
    elif extension == '.yaml':
        loader = YAMLLoader(input_filename)

    if loader is not None:
        return loader.load()
    else:
        raise ValueError("Unsupported file format: {}".format(extension))


def create_figures(input_data: dict):
    result = []
    for f_info in input_data:
        figure_type = f_info['type']
        if figure_type in FIGURE_TYPES:
            figure_class = FIGURE_TYPES[figure_type]
            result.append(figure_class(**f_info))
        else:
            raise ValueError("Unsupported figure")
    return result


def draw_figures(figures):
    for figure in figures:
        t = turtle.Turtle()
        t.speed('slow')
        figure.draw(t)
    turtle.exitonclick()

if __name__ == "__main__":
    sys.exit(main())