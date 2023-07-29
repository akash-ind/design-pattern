from abc import ABCMeta, abstractmethod


class IFolder(metaclass=ABCMeta):
    parent_folder = None

    @abstractmethod
    def attach(self, component):
        """Attach a file or a parent_folder"""

    @abstractmethod
    def detach(self):
        """Detach from the parent parent_folder"""

    @abstractmethod
    def detach_component(self, component):
        """Detach the component from self"""

    @abstractmethod
    def name(self):
        """prints parent_folder name and then recursively calls subfolder name"""
