# Last updated: 4/7/2025, 6:57:11 PM
class Solution:
    def isValid(self, s: str) -> bool:

        stack = []
        d = {")":"(", "]":"[", "}":"{"}

        for i in range(len(s)):
            if s[i] in d.values():
                stack.append(s[i])
            elif s[i] in d.keys():
                if not stack or d[s[i]] != stack.pop():
                    return False

        return not stack