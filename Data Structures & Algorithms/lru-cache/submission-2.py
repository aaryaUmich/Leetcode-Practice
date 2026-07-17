class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        else:
            val = self.cache[key]
            del self.cache[key]
            self.cache[key] = val
            return self.cache[key]

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            del self.cache[key]
       
        if len(self.cache)< self.capacity:
            self.cache[key] = value
        else:
            first_key = next(iter(self.cache))
            del self.cache[first_key]
            self.cache[key] = value


