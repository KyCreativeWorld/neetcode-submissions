class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        letter_dict = {}
        for letter in s:
            if letter_dict.get(letter):
                letter_dict[letter] += 1
            else:  
                letter_dict[letter] = 1
        
        for letter in t:
            if letter_dict.get(letter):
                letter_dict[letter] -= 1
                if letter_dict[letter] == 0:
                    letter_dict.pop(letter)
            else:
                letter_dict[letter] = 1


        return len(letter_dict) == 0
