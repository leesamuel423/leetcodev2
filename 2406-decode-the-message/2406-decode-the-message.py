class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        alphabet = list(string.ascii_lowercase)
        decode = {" ": " "}

        alpha_pointer = 0
        for idx, i in enumerate(key):
            if i not in decode:
                decode[i] = alphabet[alpha_pointer]
                alpha_pointer += 1
        
        final = ""
        for idx, j in enumerate(message):
            final += decode[j]
        
        return final
        