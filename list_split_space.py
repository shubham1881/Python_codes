# Taking input as a string using input function  
input_str = input("Enter elements of the list separated by spaces: ")  
  
# Converting input string to a list of integers  
my_list = input_str.split(' ')  
print(my_list)
my_list = [int(num) for num in my_list]  
  
# Printing the list  
print("List:", my_list)  
