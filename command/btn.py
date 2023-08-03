from command.btn_interface import IBtn


class Btn(IBtn):

    def __init__(self, command):
        self.command = command

    def invoke(self):
        self.command.execute()
