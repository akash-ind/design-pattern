from observer.interface_event_manager import IEventManager


class EventManager(IEventManager):

    def __init__(self):
        self.subscriber_dict = dict()

    def add_subscriber(self, subscriber, event_type):
        if not self.subscriber_dict.get(event_type):
            self.subscriber_dict[event_type] = list()
        self.subscriber_dict[event_type].append(subscriber)

    def remove_subscriber(self, subscriber, event_type):
        if not self.subscriber_dict.get(event_type):
            return
        self.subscriber_dict[event_type].remove(subscriber)

    def send_notification(self, context, event_type):
        for subscriber in self.subscriber_dict[event_type]:
            subscriber.update(context)
