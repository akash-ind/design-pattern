from abc import ABC, abstractmethod


class IEventManager(ABC):

    @abstractmethod
    def add_subscriber(self, subscriber, event_type):
        """Adds subscriber to the list"""

    @abstractmethod
    def remove_subscriber(self, subscriber, event_type):
        """Removed subscriber from the list"""

    @abstractmethod
    def send_notification(self, context, event_type):
        """Send notification to all the subscriber"""
