class LetterIterator:
    def __init__(self, a, b, c):
        self.letter_count = {'a': a, 'b': b, 'c': c}
        self.count = 0
        self.last = None

    def __iter__(self):
        return self

    def __next__(self):
        mx = {l: self.letter_count[l] if self.last != l or self.count < 2 else 0 for l in 'abc'}

        max_letter = max(mx, key=mx.get)
        if mx[max_letter] == 0:
            raise StopIteration
        if self.last != max_letter:
            self.count = 0
            self.last = max_letter
        self.count += 1
        self.letter_count[max_letter] -= 1
        return max_letter


class Solution:

    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        return "".join(LetterIterator(a, b, c))
