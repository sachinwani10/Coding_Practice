Leetcode: 67
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        if len(a) == 0:
            return b
        if len(b) == 0:
            return a
        if a[-1] == '1' and b[-1] == '1':
            return self.addBinary(self.addBinary(a[:-1], b[:-1]), '1') + '0'
        if a[-1] == '0' and b[-1] == '0':
            return self.addBinary(a[:-1], b[:-1]) + '0'
        else:
            return self.addBinary(a[:-1], b[:-1]) + '1'
        
# why i am writing either (+ '0') or (+ '1') after each call?
# Ans: if we do binary addition of 0 & 0 result is 0
#      ------------||------------- 0 & 1 result is 1
#      ------------||------------- 1 & 1 result is 0 (with carry 1, therefore extra inner call which adds the carry and the result)
