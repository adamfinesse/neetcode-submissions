class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        s = []
        for t in tokens:
            if t == "+":
                n1,n2 = s.pop(),s.pop()
                s.append(n1+n2)
            elif t == "-":
                n1,n2 = s.pop(),s.pop()
                print(n1,n2,"-")
                s.append(n2-n1)
            elif t == "*":
                n1,n2 = s.pop(),s.pop()
                print(n1,n2,"*")
                s.append(n1*n2)
            elif t == "/":
                n1,n2 = s.pop(),s.pop()
                print(n2,n1,"/")
                s.append(int(n2/n1))
            else:
                s.append(int(t))
        return s.pop()