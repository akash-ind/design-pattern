from Bridge.interface_shape_implementer import IShapeImplementer


class CircleImplementer(IShapeImplementer):

    def draw_impl(self):
        print("Circle")


class SquareImplementer(IShapeImplementer):

    def draw_impl(self):
        print("Square")