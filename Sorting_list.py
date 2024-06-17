lst=[3,1,8,66,4,0,-1]
ln=len(lst)
var=0
for i in range(ln):
    j=i+1
    while(j<ln):
        if(lst[i]>lst[j]):
            var=lst[i]
            lst[i]=lst[j]
            lst[j]=var  
        j+=1
print("Sorted list is ",lst)