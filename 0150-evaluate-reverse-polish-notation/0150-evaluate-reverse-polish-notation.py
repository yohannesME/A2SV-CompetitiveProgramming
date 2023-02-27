class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        val1=0
        val2=0
        
        for i in range(len(tokens)):
            if tokens[i]=='+':
                stack.append(stack.pop()+stack.pop())
            elif tokens[i]=='-':
                val2=stack.pop()
                val1=stack.pop()
                stack.append(val1-val2)
            elif tokens[i]=='*':
                stack.append(stack.pop()*stack.pop())
                
            elif tokens[i]=='/':
                val2=stack.pop()
                val1=stack.pop()
                stack.append(int(val1/val2))
            else:
                stack.append(int(tokens[i])) 
                        
                    
        return stack.pop()