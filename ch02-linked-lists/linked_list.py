from node import Node

class LinkedList(object):
    """docstring for LinkedList."""
    def __init__(self, head=None):
        """Initialize the list with no nodes and head set to None"""
        self.head = head

    def insert(self, data):
        """Method to insert a new node with the given data at the head of the
        list.  This implementation is constant O(1) because the insert method
        will always take the same amount of time: it can only take one data
        point, it can only ever create one node, and the new node doesn't need
        to interact with all the other nodes in the list, the inserted node
        will only ever interact with the head."""
        new_node = Node(data)
        new_node.set_next(self.head)
        self.head = new_node

    def size(self):
        """Method that counts nodes until it can't find anymore, and returns
        how any nodes it found."""
        current = self.head
        count = 0
        while current:
            # Until we get to None
            count += 1
            current = current.get_next()
        return count

    def search(self, data):
        """Traverse the nodes, stop at each one and check if the current node
        has the requested data.  If so, return the node holding the data. If
        the data is not found, raise a value error."""
        current = self.head
        found = False

        while current and not found:
            if current.get_data() == data:
                found = True
            else:
                current = current.get_next()

        if not current:
            # if current = None
            raise ValueError("Data not in list")

        return current

    def delete(self, data):
        current = self.head
        previous = None
        found = False

        while current and not found:
            if current.get_data() == data:
                found = True
            else:
                previous = current
                current = current.get_next()

        if not current:
            raise ValueError("Data not in list")
        if not previous:
            self.head = current.get_next()
        else:
            previous.set_next(current.get_next())
