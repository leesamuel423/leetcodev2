class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        s = list(s)
        dictionary= {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7, 'i': 8, 'j': 9, 'k': 10, 'l': 11, 'm': 12, 'n': 13, 'o': 14, 'p': 15, 'q': 16, 'r': 17, 's': 18, 't': 19, 'u': 20, 'v': 21, 'w': 22, 'x': 23, 'y': 24, 'z': 25}
        letters = 'abcdefghijklmnopqrstuvwxyz'

        total = sum(shifts)

        for idx, letter in enumerate(s):
            curr_letter_idx = dictionary[letter]
            new_idx = curr_letter_idx + total
            new_letter = letters[new_idx % 26]

            s[idx]  = new_letter
            total -= shifts[idx]
        
        return "".join(s)




        

            
        