from abc import ABCMeta, abstractmethod


class IShapeImplementer(metaclass=ABCMeta):

    @abstractmethod
    def draw_impl(self):
        """Drawing Implementation"""
