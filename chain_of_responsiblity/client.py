from cat_handler import CatHandler
from monkey_handler import MonkeyHandler


c_handler = CatHandler()
m_handler = MonkeyHandler()
c_handler.set_next(m_handler)


requests = ["banana", "milk", "nuts"]
for request in requests:
    res = c_handler.handle(request)
    if res:
        print(res)
    else:
        print("No handler found")
