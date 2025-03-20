#Find the second Most Frequent Element.If there is a tie, return any one of the most frequent elements.
l=[1,2,1,3,4,5,7,5,4,4]
max=0
mf=-1
for i in l:
    count=l.count(i)
    if count>max:
        max=count
        mf=i
print(max)