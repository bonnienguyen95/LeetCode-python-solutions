##Question link: https://leetcode.com/problems/roman-to-integer/

class Solution:
    def romanToInt(self, s: str) -> int:
        roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        special_dict = {'I': ['V', 'X'], 'X': ['L', 'C'], 'C': ['D', 'M']}
        i = 0
        result = 0

        while i < len(s):
            if s[i] in special_dict:
                if (i + 1) < len(s) and s[i + 1] in special_dict[s[i]]:
                    result += roman_dict[s[i + 1]] - roman_dict[s[i]]
                    i += 2
                else:
                    result += roman_dict[s[i]]
                    i += 1
            else:
                result += roman_dict[s[i]]
                i += 1

        return result

#Reflection:
#When running a while loop / for loop, need to make sure that your index will not go out of range.
#This will cause error and prevent your solution from running.