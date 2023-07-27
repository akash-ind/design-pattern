from abc import abstractmethod, ABCMeta


class IShape(metaclass=ABCMeta):

    @abstractmethod
    def draw(self):
        """Draws based on implementer class"""
