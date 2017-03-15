class Node(object):
    """docstring for Node."""
    def __init__(self, data=None, next=None):
        """Initialize with a single dataum and pointer set to None"""
        self.data = data
        self.next = next

    def get_data(self):
        """Convenience method to return the stored data"""
        return self.data

    def get_next(self):
        """Convenience method to return next node"""
        return self.next

    def set_next(self, new_next):
        """Method to reset the pointer to a new node"""
        self.next = new_next
