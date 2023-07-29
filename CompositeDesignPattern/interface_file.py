from abc import ABCMeta, abstractmethod


class IFile(metaclass=ABCMeta):
    parent_folder = None

    @abstractmethod
    def detach(self):
        """Detach from the current parent_folder"""

    @abstractmethod
    def name(self):
        """Print current file name"""
