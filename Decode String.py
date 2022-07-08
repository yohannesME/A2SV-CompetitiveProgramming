class Solution:
    def decodeString(self, s: str) -> str:
        def decode(s):
            if '[' not in s:
                return s
            for i in range(len(s)):
                if s[i].isdigit():
                    num = ''
                    for j in range(i, len(s)):
                        if s[j]=='[':
                            i = j-1
                            break
                        num += s[j]
                    num = int(num)
                    stack = []
                    for j in range(i+1,len(s)):
                        if s[j] == '[':
                            stack.append('[')
                        elif s[j] == ']':
                            stack.pop(-1)
                        if len(stack)==0:
                            s = s[0:i]+(s[i+2:j])*num+s[j+1:]
                            return decode(re.sub('(?!\d*[\[])\d', '',s))

        s = decode(s)
        return re.sub('\d', '',s)
