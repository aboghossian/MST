class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        string = ""
        current = self.head
        while current is not None:
            string += str(current) + " "
            current = current.next

        return string

    def add(self, vertex):
        vertex.next = self.head
        if self.head is not None:
            self.head.prev = vertex
        self.head = vertex

    def delete_min(self):
        current = self.head
        min_node = current

        while current.next is not None:
            current = current.next
            if current.weight < min_node.weight:
                min_node = current
        
        vertex = min_node.vertex
        min_node.delete(self)
        return vertex

    def is_empty(self):
        if self.head is None:
            return True
        else:
            return False

    def search(self, vertex):
        current = self.head
        while current is not None:
            if vertex == current.vertex:
                return current
            current = current.next
        return None


class Node:
    def __init__(self, vertex, weight):
        self.vertex = vertex
        self.weight = weight
        self.next = None
        self.prev = None

    def __str__(self):
        return str((self.vertex, self.weight))

    def delete(self, linked):
        if linked.head == self:
            linked.head = self.next
            self.next = None
        else:
            self.prev.next = self.next
            if self.next is not None:
                self.next.prev = self.prev
            self.next = None
