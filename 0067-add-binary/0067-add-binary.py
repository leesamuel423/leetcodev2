class Solution:
    def addBinary(self, a: str, b: str) -> str:
        output = ""
        p1 = len(a) - 1
        p2 = len(b) - 1
        carry_over = 0
        while p1 > -1 or p2 > -1:
            a_val = int(a[p1]) if p1 >= 0 else 0
            b_val = int(b[p2]) if p2 >= 0 else 0
    
            total = a_val + b_val + carry_over
    
            output = str(total % 2) + output
            carry_over = total // 2
            p1 -= 1
            p2 -= 1
    
        return "1" + output if carry_over else output
    
 