class Solution:
    def validAnagram(self, s: str, t: str) -> bool:
        d1 = {}
        for char in s:
            if d1.get(char):
                d1[char] += 1
            else:
                d1[char] = 1
        
        d2 = {}
        for char in t:
            if d2.get(char):
                d2[char] += 1
            else:
                d2[char] = 1
        
        return d1 == d2

s = "racecar"
t = "carrace"
print(Solution().validAnagram(s, t))