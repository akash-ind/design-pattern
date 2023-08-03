from abc import ABCMeta, abstractmethod


class ICommand(metaclass=ABCMeta):

    @abstractmethod
    def execute(self):
        """Calls the actual business logic"""
