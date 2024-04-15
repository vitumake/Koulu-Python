from one import Stack

class StackBasedQueue():
    def __init__(self):
        self._size = 0
        self._InboundStack = Stack()
        self._OutboundStack = Stack()
        
    def __repr__(self):
        plural = '' if self._size == 1 else 's'
        values = [c for c in self._InboundStack]
        values.extend([c for c in self._OutboundStack][::-1])
        return f'<StackBasedQueue ({self._size} element{plural}): [{", ".join(values)}]>'

    def enqueue(self, data):
        self._InboundStack.push(data)
        self._size += 1

    def dequeue(self):
        if len(self._OutboundStack) == 0:
            for n in self._InboundStack:
                node = self._InboundStack.pop()
                self._OutboundStack.push(node)
        self._size -= 1 if self._size > 0 else 0
        return self._OutboundStack.pop()