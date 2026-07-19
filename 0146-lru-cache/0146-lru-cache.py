class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}

        self.left, self.right = Node(0,0), Node(0,0)
        self.left.next = self.right
        self.right.prev = self.left

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        else:
            
            node = self.cache[key]

            node.prev.next = node.next
            node.next.prev = node.prev
            
            last_newest = self.right.prev
            last_newest.next = node
            node.next = self.right
            self.right.prev = node
            node.prev = last_newest
            return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.val = value  # Update the value
            
            # Disconnect from its current position
            node.prev.next = node.next
            node.next.prev = node.prev
            
            # Move to the right side (MRU)
            old_newest = self.right.prev
            old_newest.next = node
            node.prev = old_newest
            node.next = self.right
            self.right.prev = node
            return

        # Case 2: New key requires eviction because we are at capacity
        if len(self.cache) >= self.capacity:
            node_deleted = self.left.next
            node_deleted_next = node_deleted.next
            self.left.next = node_deleted_next
            node_deleted_next.prev = self.left

            # FIX 1: Delete from the actual map using its key
            del self.cache[node_deleted.key]

        # Case 3: Insert the brand new node (whether we evicted or not)
        node = Node(key, value)
        self.cache[key] = node  # Save to hash map
        
        old_newest = self.right.prev
        old_newest.next = node
        node.prev = old_newest
        node.next = self.right
        self.right.prev = node