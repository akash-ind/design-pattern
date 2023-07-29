from CompositeDesignPattern.interface_folder import IFolder


class Folder(IFolder):

    def __init__(self, folder_name):
        self.components = list()
        self.folder_name = folder_name

    def attach(self, component):
        component.detach()
        component.parent_folder = self
        self.components.append(component)

    def detach(self):
        if self.parent_folder:
            self.parent_folder.detach_component(self)
            self.parent_folder = None

    def detach_component(self, component):
        self.components.remove(component)

    def name(self):
        print(self.folder_name)

        for component in self.components:
            component.name()

