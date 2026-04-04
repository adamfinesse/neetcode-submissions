class TimeMap:

    def __init__(self):
        self.map = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.map[key].append((value,timestamp))

    def get(self, key: str, timestamp: int) -> str:
        if self.map[key] and self.map[key][-1][1] == timestamp:
            return self.map[key][-1][0]

        res = ""
        l,r=0,len(self.map[key])-1
        while l<=r:
            m=(l+r)//2

            if self.map[key][m][1] == timestamp:
                return self.map[key][m][0]
            
            if self.map[key][m][1] > timestamp:
                r = m-1
            else:
                res = self.map[key][m][0]
                l = m+1

        return res

