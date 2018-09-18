from time import time
inFilePath1 = r'C:\Users\sudheer\Documents\GitHub\Dynamic-Textbook\TagSet\33kTags.txt'
inFilePath2 = r'C:\Users\sudheer\Documents\GitHub\Dynamic-Textbook\TagSet\17kTags.txt'
d = {}
file1 = open(inFilePath1,'r')
d = set(file1.read().split('\n'))
file1.close()

file2 = open(inFilePath2,'r')
tests = file2.read().split('\n')
c = 0
start = time()
for i in tests:
    if i in d:
        c+=1
print(c)
c = 0
for i in tests:
    if i+'aiwjdiasj' in d:
        c+=1
file2.close()
print(c)
print(time()-start)
