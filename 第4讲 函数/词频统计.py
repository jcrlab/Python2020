A=input()
a=A.split(' ')
WordCount={}
for i in a:
    if i in WordCount:
        WordCount[i]+=1
    else:
        WordCount[i]=1
b=max(WordCount.values())
for k,v in WordCount.items():
    if v==b:
        print(k,end=' ')