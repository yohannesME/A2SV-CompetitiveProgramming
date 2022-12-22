class Solution:
    def freqAlphabets(self, s: str) -> str:
        alphabet = {}
        N = len(s)
        output = ''
        stack = []
        
        #create a hashmap containing lower case letters of the alphabet for o(1) access
        i = 1
        for c in string.ascii_lowercase:
            alphabet[str(i)] = c
            i += 1
        #remove all the # from the input string by evaluating them first
        for digit in s:
            if digit == '#':
                stack[-2] = alphabet[''.join(stack[-2:])]
                stack.pop()
            else:
                stack.append(digit)
        #convert what is left
        for i in range(len(stack)):
            if stack[i].isdigit():
                stack[i] = alphabet[stack[i]]
        return ''.join(stack)