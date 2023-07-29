from CompositeDesignPattern.folder import Folder
from CompositeDesignPattern.file import File


file_a = File("File A")
file_b = File("File B")
file_c = File("File C")


folder_a = Folder("Folder A")
folder_b = Folder("Folder B")


folder_a.attach(file_a)
folder_a.attach(file_b)
folder_a.attach(file_c)
folder_b.attach(file_c)
folder_a.attach(folder_b)

folder_a.name()
