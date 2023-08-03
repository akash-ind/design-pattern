from abc import ABCMeta, abstractmethod


class IBtn(metaclass=ABCMeta):
    @abstractmethod
    def __int__(self, command):
        """Initialised with a command"""

    @abstractmethod
    def invoke(self):
        """Invokes the command"""
