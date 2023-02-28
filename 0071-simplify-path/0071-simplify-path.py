class Solution:
    def simplifyPath(self, path: str) -> str:
        pathStack = []
        N = len(path)
        
        #get the directorys and commands ., .. and also the // as ''
        path = path.split('/')
        output = ['/']
        
        #only add the directory and remove if ..
        for p in path:
            if p == '..':
                if len(output) > 1:
                    output.pop()
                    output.pop()
            elif p != '.' and p != '':
                output.append(p)
                output.append('/')
                
        #removing the trailing /
        if len(output) > 1:
            output. pop()
        
        return ''.join(output)