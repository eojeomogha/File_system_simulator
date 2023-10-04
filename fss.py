class Node:
    def __init__(self, name, is_file=False):
        self.name = name
        self.is_file = is_file
        self.children = LinkedList()
        self.parent = None

    def add_child(self, child):
        self.children.append(child)
        child.parent = self

    def remove_child(self, child):
        self.children.remove(child)

    def get_child(self, name):
        for child in self.children:
            if child.name == name:
                return child
        return None

    def get_parent(self):
        return self.parent


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, node):
        if not self.head:
            self.head = node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = node

    def remove(self, node):
        if self.head == node:
            self.head = node.next
        else:
            current = self.head
            while current.next and current.next != node:
                current = current.next
            if current.next:
                current.next = current.next.next


class FileSystem:
    def __init__(self):
        self.root = Node("/")
        self.current_dir = self.root

    def ls(self):
        if not self.current_dir.children.head:
            print("Empty directory")
            return
        for child in self.current_dir.children:
            print(child.name, end=" ")
        print()

    def mkdir(self, name):
        new_dir = Node(name)
        self.current_dir.add_child(new_dir)

    def cd(self, name):
        if name == "..":
            if self.current_dir != self.root:
                self.current_dir = self.current_dir.get_parent()
        else:
            new_dir = self.current_dir.get_child(name)
            if new_dir is not None and not new_dir.is_file:
                self.current_dir = new_dir

    def touch(self, name):
        new_file = Node(name, True)
        self.current_dir.add_child(new_file)


# Example usage
fs = FileSystem()
fs.ls()  # Output: Empty directory
fs.mkdir("documents")
fs.cd("documents")
fs.touch("file1.txt")
fs.touch("file2.txt")
fs.ls()  # Output: file1.txt file2.txt
fs.cd("..")
fs.ls()  # Output: documents
