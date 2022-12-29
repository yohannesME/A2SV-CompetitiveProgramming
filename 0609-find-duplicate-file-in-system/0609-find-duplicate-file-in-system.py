class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        #hash of all the paths that have the same file content
        filesHash = defaultdict(list)
        
        #answer that excludes the non duplicated elements
        answer = []
        
        for samedirpath in paths:
            #regular expression that extracts the content
            contents = re.findall('\((\w*)\)',samedirpath)
            #root directory and file name with content
            files = samedirpath.split(' ')
            root = files[0]
            for index,content in enumerate(contents):
                #while appending remove the content () and construct the path
                filesHash[content].append(root+'/'+files[index+1].split('(')[0])
        
        #remove the ones that are not duplicated
        for path in filesHash.values():
            if len(path) > 1:
                answer.append(path)
                
        
        return answer