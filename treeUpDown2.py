n=int(input("Enter maximum no. of stars: "))
#n=(l//2)+1
for i in range(0,n-1):
    print(" "*i,end='')
    for j in range(i,n):
        print("* ",end='')
    print("\r")    
for i in range(1,n+1):
    for j in range(i,n):
        print(" ",end='')
    print("* "*i)
 
