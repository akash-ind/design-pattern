from Bridge.shape import Shape
from Bridge.shape_implementer import CircleImplementer, SquareImplementer


circle_shape = Shape(CircleImplementer)
square_shape = Shape(SquareImplementer)

circle_shape.draw()
square_shape.draw()
