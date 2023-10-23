class Solution:
    def isValid(s: str) -> bool:
        stack = []
        mapping = {")": "(", "}": "{", "]": "["}
        for char in s:
            print(f"char at starting {char}")
            if char in mapping:
                print(f"char in mappng {char}")
                print(f"stack is {stack}")
                top_element = stack.pop() if stack else '#'
                print(f"top element is {top_element}")
                print(f"after pop stack is {stack}")
                if mapping[char] != top_element:
                    return False
            else:
                stack.append(char)
            print(f"at the end stack is {stack}")    
        return not stack
    

s='([(({}))])'
print(Solution.isValid(s)) 

   