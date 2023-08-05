from chain_of_responsiblity.base_handler import BaseHandler


class MonkeyHandler(BaseHandler):

    def handle(self, request):
        if request == "banana":
            return "Monkey Ate bananas"
        else:
            return super().handle(request)
