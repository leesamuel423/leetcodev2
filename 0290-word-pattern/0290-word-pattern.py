class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        pattern_to_word = {}
        word_to_pattern = {}
        words = s.split(" ")

        if len(pattern) != len(words):
            return False

        for letter, word in zip(pattern, words):
            if letter in pattern_to_word and word != pattern_to_word[letter]:
                return False
            if word in word_to_pattern and letter != word_to_pattern[word]:
                return False
                
            pattern_to_word[letter] = word
            word_to_pattern[word] = letter
        print(pattern_to_word)
        print(word_to_pattern)
        return True