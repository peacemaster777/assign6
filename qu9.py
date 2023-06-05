# Ques 9
class ParenthesesValidator:
    def _init_(self):
        self.opening_brackets = "([{"
        self.closing_brackets = ")]}"
    
    def is_valid(self, string):
        stack = []
        for char in string:
            if char in self.opening_brackets:
                stack.append(char)
            elif char in self.closing_brackets:
                if not stack:
                    return False
                opening_bracket = stack.pop()
                if not self._is_matching(opening_bracket, char):
                    return False
        return len(stack) == 0
    
    def _is_matching(self, opening_bracket, closing_bracket):
        return self.opening_brackets.index(opening_bracket) == self.closing_brackets.index(closing_bracket)