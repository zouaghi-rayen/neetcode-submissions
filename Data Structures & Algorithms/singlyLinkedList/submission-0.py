from typing import List

class Node:
    """A separate class to represent a single element in the list."""
    def __init__(self, value: int):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def get(self, index: int) -> int:
        """Retrieves the value at the given index."""
        if index < 0:
            return -1 
            
        current = self.head
        lookup_index = 0
        
        while current is not None:
            if lookup_index == index:
                return current.value
            
            current = current.next
            lookup_index += 1
            
        return -1

    def insertHead(self, val: int) -> None:
        new_node = Node(val)
        new_node.next = self.head
        self.head = new_node

    def insertTail(self, val: int) -> None:
        new_node = Node(val)
        
        if self.head is None:
            self.head = new_node
            return
            
        current = self.head
        while current.next is not None:
            current = current.next
            
        current.next = new_node

    def remove(self, index: int) -> bool:
        if index < 0 or self.head is None:
            return False
            
        if index == 0:
            self.head = self.head.next
            return True
            
        current = self.head
        lookup_index = 0
        
        while current is not None and lookup_index < index - 1:
            current = current.next
            lookup_index += 1
            
        if current is None or current.next is None:
            return False
            
        current.next = current.next.next
        return True

    def getValues(self) -> List[int]:
        values = []
        current = self.head
        
        while current is not None:
            values.append(current.value)
            current = current.next
            
        return values