from event_manager import EventManager


class Publisher:

    def __init__(self):
        self.event_manager = EventManager()

    def open(self):
        self.event_manager.send_notification("File opened", "open")

    def close(self):
        self.event_manager.send_notification("File closed", "close")