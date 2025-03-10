class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        # Stack stores elements in reverse order for efficient processing
        self.stack = []
        self._flatten(nestedList)

    def _flatten(self, nestedList):
        """Flatten the nested list and store elements in stack in reverse order."""
        for i in reversed(nestedList):
            self.stack.append(i)

    def next(self) -> int:
        """Return the next integer."""
        if self.hasNext():
            return self.stack.pop().getInteger()
        return None

    def hasNext(self) -> bool:
        """Check if there are any integers left to return."""
        while self.stack:
            top = self.stack[-1]
            if top.isInteger():
                return True  # Found an integer
            self.stack.pop()  # Remove the nested list
            self._flatten(top.getList())  # Expand it
        return False  # No integers left
