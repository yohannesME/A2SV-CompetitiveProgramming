# Enter your code here. Read input from STDIN. Print output to STDOUT
import collections

count = int(input())
strInput = []
for i in range(count):
    strInput.append(input())
    
wordCount = collections.Counter(strInput);

output = list(wordCount.values())
print(len(output))

for i in output:
    print(i,end=" ")

