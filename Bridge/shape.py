from Bridge.interface_shape import IShape


class Shape(IShape):

    def __init__(self, implementer):
        self.implementer = implementer()

    def draw(self):
        self.implementer.draw_impl()

