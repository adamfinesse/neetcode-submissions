class Solution:
    def calPoints(self, operations: List[str]) -> int:
        record=[]
        res =0
        for i in range(len(operations)):
            if operations[i] == "C":
                res -= record.pop(-1)
            elif operations[i] == "+":
                a = record[-1] + record[-2]
                record.append(a)
                res += a
            elif operations[i] == "D":
                d = record[-1] * 2
                record.append(d)
                res+= d
            else:
                num = int(operations[i])
                record.append(num)
                res+=num
        return res