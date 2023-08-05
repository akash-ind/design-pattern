from base_handler import BaseHandler

class CatHandler(BaseHandler):

    def handle(self, request):
        if request == "milk":
            return "Cat drank all the milk"
        else:
            return super().handle(request)