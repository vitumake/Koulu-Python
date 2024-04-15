class Queue():
    def __init__(self):
        self._size = 0
        self._head = None
        
    def __repr__(self):
        current_node = self._head
        values = ''
        while current_node:
            values += f', {current_node.data}'
            current_node = current_node.next
        plural = '' if self._size == 1 else 's'
        return f'<Queue ({self._size} element{plural}): [{values.lstrip(", ")}]>'
    
    def enqueue(self, data):
        node = ListNode(data, self._head)
        self._head = node