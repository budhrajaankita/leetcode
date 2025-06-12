# Last updated: 6/11/2025, 10:35:10 PM
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