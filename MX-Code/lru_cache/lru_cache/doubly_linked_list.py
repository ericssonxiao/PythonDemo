#from doubly_linked_list import Node

class DoublyLinkedList:
    """ This is Doubly Linked List.
    """

    def __init__(self, start=None, last=None, len=0):
        self.start = start
        self.last = last
        self.len = len

    def get_node(self, index):
        current = self.first
        for i in range(index):
            if current is None:
                return None
            current = current.next
        return current
 
    def insert_after(self, ref_node, new_node):
        new_node.prev = ref_node
        if ref_node.next is None:
            self.last = new_node
        else:
            new_node.next = ref_node.next
            new_node.next.prev = new_node
        ref_node.next = new_node
        self.len += 1

    def insert_before(self, ref_node, new_node):
        new_node.next = ref_node
        if ref_node.prev is None:
            self.first = new_node
        else:
            new_node.prev = ref_node.prev
            new_node.prev.next = new_node
        ref_node.prev = new_node
        self.len += 1

    def insert_at_begin(self, new_node):
        if self.first is None:
            self.first = new_node
            self.last = new_node
        else:
            self.insert_before(self.first, new_node)
        self.len += 1

    def insert_at_end(self, new_node):
        if self.last is None:
            self.last = new_node
            self.first = new_node
        else:
            self.insert_after(self.last, new_node)
        self.len += 1
 
    def remove(self, node):
        if node.prev is None:
            self.first = node.next
        else:
            node.prev.next = node.next
 
        if node.next is None:
            self.last = node.prev
        else:
            node.next.prev = node.prev
        self.len -=1
        
    def display(self):
        current = self.first
        while current:
            print(current.data, end = ' ')
            current = current.next

    def to_list(self): # return a python list with the elements of the doubly-linked list
        res = []
        curr = self.first
        while curr != None:
            res.append(curr.val)
            curr = curr.next
        return res

    def is_empty(self): # check whether the list is empty
        return self.len == 0

class Node:
    def __init__(self, next=None, prev=None, data=None):
        self.next = next # reference to next node in DLL 
        self.prev = prev # reference to previous node in DLL 
        self.data = data

    def __hash__(self, data):
        pass

    def __str__(self, data):
        pass