class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def printList(self):
        pos = self.head
        res = []
        while pos is not None:
            res.append(pos.data)
            pos = pos.next
        print (res)

    def insertAtHead(self, data):
        node = Node(data)
        node.next = self.head
        self.head = node

    def insertAtTail(self, data):
        node = Node(data)
        pos = self.head
        current = pos
        ##traverse till end
        while pos is not None:
            current = pos
            pos = pos.next
        current.next = node

    def deleteNode(self, value):
        pos = self.head
        previous = pos
        ## check for head
        if pos.data == value:
            self.head = pos.next
        ##traverse till end
        while pos is not None:
            if pos.data == value:
                #print (previous, pos)
                #print(pos.data, value)
                previous.next = pos.next
                #print (previous, pos)
                break
            else:
                previous = pos
                pos = pos.next






# create 3 Nodes
first = Node(1)
second = Node(2)
third = Node(3)

Llist = LinkedList()
Llist.head = first
first.next = second
second.next = third

Llist.printList()
Llist.insertAtHead(0)
Llist.printList()
Llist.insertAtTail(4)
Llist.printList()
print("deleting 2")
Llist.deleteNode(2)
Llist.printList()

print("deleting 0")
Llist.deleteNode(0)
Llist.printList()

print("deleting 4")
Llist.deleteNode(2)
Llist.printList()