class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        a = w = 0

        while a < len(abbr) and w < len(word):
            if abbr[a].isdigit():
                if abbr[a] == "0":
                    return False
                shift = 0
                while a < len(abbr) and abbr[a].isdigit():
                    shift = shift * 10 + int(abbr[a])
                    a += 1
                w += shift
            else:
                if word[w] != abbr[a]:
                    return False
                w += 1
                a += 1
        
        return w == len(word) and a == len(abbr)
            

