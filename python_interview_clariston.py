## Given a list of numbers and output a list sorted  based on frequency of these numbers. If the frequency is same then higher number will get priority

ab = [7, 2, 6, 6, 5, 3, 5, 5, 3, 3]
output = [5, 5, 5, 3, 3, 3, 6, 6, 7, 2]
ab.sort()



a=ab[0]
global var
var=1
dict_1={}

for i in ab:
    if(a == i):
        if(len(dict_1)==0):
            dict_1[i]=1
            continue
        var=var+1
        dict_1[i]=var
    else:
       var=1
       dict_1[i]=var
       a=i

print("dict_1ionary created is : ", dict_1)

maxi=1

for val in dict_1.values():
    if(val > maxi):
        maxi=val 


sorted_dict_1=dict(sorted(dict_1.items(), key=lambda item: item[1], reverse=True))  
sorted_dict_1=dict(sorted(dict_1.items(), key=lambda item: item[0], reverse=True))
print("here i am " ,sorted_dict_1)

sorted_list = []  
    # Iterate over the keys in the sorted dict_1ionary  
for key in sorted_dict_1:  
        # Append the key to the sorted list as many times  
        # as specified by its frequency count  
    for i in range(sorted_dict_1[key]):  
        sorted_list.append(key)  

print(sorted_list)
