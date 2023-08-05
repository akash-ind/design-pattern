from interface_subscriber import ISubscriber


class Subscriber(ISubscriber):
    def update(self, context):
        print(context)
