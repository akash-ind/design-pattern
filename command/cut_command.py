from command_interface import ICommand


class CutCommand(ICommand):

    def __init__(self, editor, client):
        self.editor = editor
        self.client = client

    def execute(self):
        text = self.editor.get_selection()
        self.editor.delete_selection()
        self.client.add_to_cliboard(text)
