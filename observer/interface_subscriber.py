from abc import ABC, abstractmethod


class ISubscriber(ABC):

    @abstractmethod
    def update(self, context):
        """Updates the subscriber about the info"""
