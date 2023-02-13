class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = []
        popped = list(reversed(popped))
        for i in pushed:
            if i != popped[-1]:
                stack.append(i)
            else:
                popped.pop()
                while len(stack) and  stack[-1] == popped[-1]:
                    stack.pop()
                    popped.pop()

        return len(stack) == 0
