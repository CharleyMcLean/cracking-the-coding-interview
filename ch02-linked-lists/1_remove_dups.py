from node import Node
from linked_list import LinkedList


def remove_dups(ll):
    """Function to remove duplicates from an unsorted linked list"""

    if ll.head is None or ll.size() == 1:
        # If the linked list is empty or has only one Node, we know
        # there won't be any duplicates, so just return the linked list.
        return ll

    current = ll.head

    # Create a set of seen node values
    seen = set([current.data])

    while current.next:
        # The last node will point to None, at which point the loop will
        # terminate
        if current.next.data not in seen:
            # If we haven't seen this node's value yet, add to seen and
            # move on to check the next node.
            seen.add(current.next.data)
            current = current.next
        else:
            # If the node's value has been seen, reassign the next node
            current.next = current.next.next

    return ll


##########################################################################
# testing...
ll = LinkedList()
print "Testing a linked list with no nodes.  Expecting True, got >>>",
print ll == remove_dups(ll)

ll2 = LinkedList()
ll2.insert(1)
print "Testing a linked list with one node.  Expecting True, got >>>",
print ll2 == remove_dups(ll2)

ll3 = LinkedList()
ll3.insert(2)
ll3.insert(1)
ll3.insert(2)
ll3.insert(1)
remove_dups(ll3)
print "Testing a linked list two node values dup'd.  Expecting True, got >>>",
print ll3.size() == 2

ll4 = LinkedList()
ll4.insert(1)
ll4.insert(2)
print "Testing a linked list with nodes of diff vals. Expecting True, got >>>",
print ll4 == remove_dups(ll4)
