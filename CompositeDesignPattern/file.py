from CompositeDesignPattern.interface_file import IFile


class File(IFile):

    def __init__(self, file_name):
        self.file_name = file_name

    def detach(self):
        if self.parent_folder:
            self.parent_folder.detach_component(self)
            self.parent_folder = None

    def name(self):
        print(self.file_name)
