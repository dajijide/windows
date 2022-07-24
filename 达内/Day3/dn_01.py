class Node():
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


node = Node(1)
node1 = Node(2, node)
node2 = Node(3, node1)



