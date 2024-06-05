from operator import xor
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        # Convert binary strings to integers
        x, y = int(a, 2), int(b, 2)
        
        # While there's a carry
        while y:
            # XOR gives the sum without carrying
            answer = x ^ y
            # AND and shift left gives the carry
            carry = (x & y) << 1
            # Prepare for the next iteration
            x, y = answer, carry
        
        # Convert the result back to a binary string
        return bin(x)[2:] 