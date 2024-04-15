class ListNode():
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next
    
    def __repr__(self):
        return f'<ListNode: {self.data}>'

class SinglyLinkedList():
    def __init__(self):
        self._head = None

    def __repr__(self):
        current_node = self._head
        values = ''
        while current_node:
            values += f', {current_node.data}'
            current_node = current_node.next
        return f'<SinglyLinkedList: [{values.lstrip(", ")}]>'
     
    def append(self, value):
        """
        Append a value to the end of the list

        Parameters:
        - 'value': The data to append

        Returns: None
        """
        # Create the node with the value
        node = ListNode(value)
        # If list is empty just point the header to the new node
        if not self._head:
            self._head = node
        else:
            # if list is not empty, search for the last element and point it to the new node
            current_node = self._head
            while current_node.next != None:
                current_node = current_node.next
            current_node.next = node
    
    def pop(self):
        """
        Remove the last element from the list

        Returns: The data of the removed element
        """
        val = None
        # If list is empty, return None
        if not self._head:
        # Search for last element and remove it
            val = None
        elif not self._head.next:
            val = self._head.data
            self._head = None
        else:
            curr_node = self._head
            while curr_node.next.next != None:
                curr_node = curr_node.next
            val = curr_node.next.data
            curr_node.next = None
        return val;

# Test

list = SinglyLinkedList()
for i in 'a':
    list.append(i)
val = list.pop()
print(val, list)