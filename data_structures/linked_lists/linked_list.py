"""Linked lists"""

# Operations involved
# Removing or adding at the end, beginning or middle
# Lookup

# * Under the hood we can think of linked lists as a set of nested dictionaries
head = {
    "value": 4,
    "next": {
        "value": 8,
        "next": {
            "value": 1,
            "next": {
                "value": 3,
                "next": None
            }
        }
    }
}

# print(head["next"]["next"]["next"]["value"])
# my_linked_list.head.next.next.next.value


class Node:
    """Node class for creating new nodes for the LinkedList class
    """

    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    """Linked list implementation
    """

    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        """Printing out the elements of the list
        """
        temp = self.head
        # The linked list is not empty
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def append(self, value):
        """Adding an element at the end of the linked list
        """
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True


my_linked_list = LinkedList(5)
my_linked_list.append(43)
my_linked_list.append(4)
my_linked_list.append(14)
my_linked_list.print_list()
