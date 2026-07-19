class TimeMap:

    def __init__(self):
        self.store = {}
    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = [[value, timestamp]]
        
        else:
            self.store[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store:
            return ""
        
        res = ""
        pair = self.store[key]

        l,r = 0, len(pair)-1

        while l<=r:
            mid = (l+r)//2

            if pair[mid][1]<=timestamp:
                res = pair[mid][0]
                l = mid+1
            elif pair[mid][1]>timestamp:
                r = mid-1
            
            elif pair[mid][1] == timestamp:
                return pair[mid][0]
        return res 

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)