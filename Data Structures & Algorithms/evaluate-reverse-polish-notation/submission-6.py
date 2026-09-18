class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        numStack = []
        for c in tokens:
            if c == "+":
                res=numStack.pop()+numStack.pop()
                numStack.append(res)
            elif c == "-":
                a,b=numStack.pop(),numStack.pop()
                numStack.append(b-a)
            elif c == "/":
                a,b=numStack.pop(),numStack.pop()
                numStack.append(int(b/a))
            elif c == "*":
                res=numStack.pop()*numStack.pop()
                numStack.append(res)
            else:
                numStack.append(int(c))
        return numStack[0]

        