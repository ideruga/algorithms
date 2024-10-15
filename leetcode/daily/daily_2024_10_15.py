class Solution:
    def minimumSteps(self, s: str) -> int:
        white_count = sum([1 for character in s if character == "0"])
        steps = 0
        for i in range(0, white_count):
            if s[i] == "1":
                steps += white_count - i
        for i in range(white_count, len(s)):
            if s[i] == "0":
                steps += i - white_count
        return steps
