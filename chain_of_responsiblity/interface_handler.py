from abc import ABC, abstractmethod


class IHandler(ABC):

    @abstractmethod
    def set_next(self, handler):
        """Sets the next handler"""

    @abstractmethod
    def handle(self, request):
        """Process the req and if not invokes the next handler"""
