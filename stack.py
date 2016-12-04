class Stack:
    """creates a basic stack setup"""
    def __init__(self):
        self._items = []
        self._max_size = None
        self._stack_pointer = None

    def is_empty(self):
        if len(self.items) == 0:
            return True
        else:
            return False

    def push(self, item_to_add):
        if len(self._items) < self._max_size:
            self._items.append(item_to_add)
            if len(self._items) == 1:
                self._stack_pointer = 0
            else:
                self._stack_pointer += 1

    def pop(self):
        if len(self._items) > 0:
            item = self._items[self._stack_pointer]
            self._items.pop(self._stack_pointer)
            if self._stack_pointer > 0:
                self._stack_pointer -= 1
            else:
                self._stack_pointer = None
            return item

    def peek(self):
        if len(self._items) >= 1:
            return self._items[self._stack_pointer]
        else:
            return None

    def set_max_size(self, max_size):
        self._max_size = max_size

    def clear(self):
        items = self._items.copy()
        self._items.clear()
        return items
