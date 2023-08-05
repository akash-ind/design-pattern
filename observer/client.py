from observer.subscriber import Subscriber
from observer.publisher import Publisher


publisher = Publisher()

sub1 = Subscriber()
sub2 = Subscriber()

publisher.event_manager.add_subscriber(sub1, "open")
publisher.event_manager.add_subscriber(sub2, "close")

publisher.open()
publisher.close()