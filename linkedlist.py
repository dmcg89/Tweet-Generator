#!python


class Node(object):

    def __init__(self, data):
        """Initialize this node with the given data."""
        self.data = data
        self.next = None

    def __repr__(self):
        """Return a string representation of this node."""
        return 'Node({!r})'.format(self.data)


class LinkedList(object):

    def __init__(self, items=None):
        """Initialize this linked list and append the given items, if any."""
        self.head = None  # First node
        self.tail = None  # Last node
        self.size = 0   # Length
        # Append given items
        if items is not None:
            for item in items:
                self.append(item)

    def __str__(self):
        """Return a formatted string representation of this linked list."""
        items = ['({!r})'.format(item) for item in self.items()]
        return '[{}]'.format(' -> '.join(items))

    def __repr__(self):
        """Return a string representation of this linked list."""
        return 'LinkedList({!r})'.format(self.items())

    def items(self):
        """Return a list (dynamic array) of all items in this linked list.
        Best and worst case running time: O(n) for n items in the list (length)
        because we always need to loop through all n nodes to get each item."""
        items = []  # O(1) time to create empty list
        # Start at head node
        node = self.head  # O(1) time to assign new variable
        # Loop until node is None, which is one node too far past tail
        while node is not None:  # Always n iterations because no early return
            items.append(node.data)  # O(1) time (on average) to append to list
            # Skip to next node to advance forward in linked list
            node = node.next  # O(1) time to reassign variable
        # Now list contains items from all nodes
        return items  # O(1) time to return list

    def is_empty(self):
        """Return a boolean indicating whether this linked list is empty."""
        return self.head is None

    def length(self):
        """Return the length of this linked list by traversing its nodes.
        TODO: Running time: O(???) Why and under what conditions?"""
        # TODO: Loop through all nodes and count one for each
        # count = 0
        # current_node = self.head
        # while current_node is not None:
        #     count += 1
        #     current_node = current_node.next
        # return count
        return self.size

    def append(self, item):
        """Insert the given item at the tail of this linked list.
        TODO: Running time: O(???) Why and under what conditions?"""
        # TODO: Create new node to hold given item
        new_node = Node(item)
        # TODO: Append node after tail, if it exists
        if self.size > 0:
            (self.tail).next = new_node
            self.tail = new_node
            self.size += 1
        else:
            self.tail = new_node
            self.head = new_node
            self.size += 1


    def prepend(self, item):
        """Insert the given item at the head of this linked list.
        TODO: Running time: O(1) Why and under what conditions?"""
        # Create new node to hold given item
        new_node = Node(item)
        # Prepend node before head, if it exists
        if self.size == 0:
            self.head = new_node
            self.tail = new_node
            self.size += 1

        else:
            new_node.next = self.head
            self.head = new_node
            self.size += 1

        # new_node.next = self.head
        # self.head = new_node
        # if self.size == 1:
        #     self.tail = new_node
        # self.size += 1

    def find(self, quality):
        """Return an item from this linked list satisfying the given quality.
        Best case running time: O(1) Why and under what conditions? item in First part of list
        Worst case running time: O(n) Why and under what conditions? item in end of list"""
        # Loop through all nodes to find item where quality(item) is True
        node = self.head
        while node is not None:
            # Check if node's data satisfies given quality function
            if quality(node.data) is True:
                return node.data
            else:
                node = node.next

        # value wasnt in list, return nothing
        return None



    def delete(self, item):
        """Delete the given item from this linked list, or raise ValueError.
        TODO: Best case running time: O(1) Why and under what conditions?
        TODO: Worst case running time: O(n) Why and under what conditions?"""
        # TODO: Loop through all nodes to find one whose data matches given item
        if self.is_empty():
            raise ValueError("LinkedList is Empty")

        if self.size == 1:
            self.head = None
            self.tail = None
            self.size -= 1
            return True

        current_node = self.head
        prev_node = None

        while current_node:
            if current_node.data == item:
                if current_node == self.tail:
                    prev_node.next = None
                    self.tail = prev_node
                    self.size -= 1
                    return
                if prev_node:
                    prev_node.next = current_node.next
                    self.size -= 1
                else:
                    self.head = current_node.next
                    self.size -= 1
                return

            else:
                prev_node = current_node
                current_node = current_node.next

        raise ValueError('Item not found: {}'.format(item))
        # target = self.find(item)
        # if target == None:
        #         print('delete item not found')
        #         raise ValueError('item not found: {}'.format(item))
        #
        # print(target)
        # node = self.head
        # prev_node = self.head
        # while node is not None:
        #     if target == node:
        #         prev_node.next = node.next
        #         break
        #         # print(node)
        #         # print(prev_node)
        #     else:
        #         prev_node = node
        #         node = node.next

        # TODO: Update previous node to skip around node with matching data
        # TODO: Otherwise raise error to tell user that delete has failed
        # Hint: raise ValueError('Item not found: {}'.format(item))

# ll = LinkedList()
# node1 = Node('A')
# node2 = Node('B')
# node1.next = node2
# # # print((node1.next).data)
#     # # ll.items(node1)
# ll.head = node1
# ll.tail = node2
# ll.append('d')
# ll.append('e')
# print(ll.find('A'))
# print(ll)
# ll.delete('d')
# print(ll)
# ll.delete('z')

def test_linked_list():
    ll = LinkedList()
    print('list: {}'.format(ll))

    print('\nTesting append:')
    for item in ['A', 'B', 'C']:
        print('append({!r})'.format(item))
        ll.append(item)
        print('list: {}'.format(ll))

    print('head: {}'.format(ll.head))
    print('tail: {}'.format(ll.tail))
    print('length: {}'.format(ll.length()))

    # Enable this after implementing delete method
    delete_implemented = False
    if delete_implemented:
        print('\nTesting delete:')
        for item in ['B', 'C', 'A']:
            print('delete({!r})'.format(item))
            ll.delete(item)
            print('list: {}'.format(ll))

        print('head: {}'.format(ll.head))
        print('tail: {}'.format(ll.tail))
        print('length: {}'.format(ll.length()))


if __name__ == '__main__':
    test_linked_list()
