from chain_of_responsiblity.interface_handler import IHandler


class BaseHandler(IHandler):

    def __init__(self):
        self._next_handler = None

    def set_next(self, handler):

        self._next_handler = handler

    def handle(self, request):
        if self._next_handler:
            return self._next_handler.handle(request)
        else:
            return None
