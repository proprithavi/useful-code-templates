'''def function(n:int,k:int) -> int:
    studlist = [i for i in range(1, n + 1)]
    l=[]
    if n==1 and k==1:
        return 1
    elif n==2 and k==1:
        return studlist[-1]
    elif n==2 and k==2:
        return studlist[0]
    
    else:
        idx=1
        while len(studlist)!=0:
            l.append(studlist.pop(idx))

               
            if idx==len(studlist)-1:
                idx=1
            elif idx==len(studlist)-2:
                idx=0
            idx+=1
           
    return l


print(function(5, 2))  # Example usage'''

l=[1,1,2,3,4,5,6]
l.pop(2)
print(l)