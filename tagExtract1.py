inFilePath = r'C:\Users\sudheer\Documents\GitHub\Dynamic-Textbook\TagSet\33kTags.csv'
outFilePath = r'C:\Users\sudheer\Documents\GitHub\Dynamic-Textbook\TagSet\33kTags.txt'
file1 = open(inFilePath,'r')
t = file1.read().split('\n')
t1 = filter(lambda x : x if '-' not in x else None, list(map(lambda y : y.strip('"'),t[1:])))
file1.close()

file2 = open(outFilePath,'w')
file2.write('\n'.join(t1))
file2.close()
