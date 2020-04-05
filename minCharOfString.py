from collections import Counter
string = "you are my favourite student"
#string1=string.replace(" ", "")
string1=''.join(string.split())
c=Counter(string1)
print(c)
val=min(c.values())
for i,j in c.items():
    if j==val:
        print(i)
        break
