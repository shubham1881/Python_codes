# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.

lst=[1,2-3,-4,9,-7,2,5,8,9,1,0,9]
ln=len(lst)-1
ls=0
a=0
while(ls<ln):
    if(lst[ls]>0 and lst[ln]<0):
        a=lst[ls]
        lst[ls]=lst[ln]
        lst[ln]=a
        ln-=1
        ls+=1
        continue
    if(lst[ls]>0):
        if(lst[ln]>0):
            ln-=1
            continue
    if(lst[ln]<0):
        if(lst[ls]<0):
            ln+=1
            continue
    else:
        ln-=1
        ls+=1
        continue

print(lst)
lst.sort()
print(lst)
        
        
