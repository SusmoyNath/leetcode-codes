# Wrapper class for the given iterator
class PeekingIterator:
    def __init__(self, iterator):
        self.iterator = iterator  # Store original iterator
        self._next = self.iterator.next() if self.iterator.hasNext() else None  # Pre-fetch next element

    def peek(self):
        return self._next  # Return pre-fetched value

    def next(self):
        current_value = self._next  # Store current value to return
        self._next = self.iterator.next() if self.iterator.hasNext() else None  # Pre-fetch next
        return current_value  # Return the stored value

    def hasNext(self):
        return self._next is not None  # Check if we have a pre-fetched value
