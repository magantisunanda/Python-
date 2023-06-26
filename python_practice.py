#1) Given a string s, return the longest palindromic substring in s.  Example 1:Input: s = "babad" Output: "bab"


def check(myStr):
    open_list = ["[","{","("]
    close_list = ["]","}",")"]
    stack = []
    for i in myStr:
        if i in open_list:
            stack.append(i)
        elif i in close_list:
            pos = close_list.index(i)

            if ( (open_list[pos] == stack[len(stack)-1])):
                stack.pop()
            else:
                return "Not Valid"
    if len(stack) == 0:
        return "Valid"
    else:
        return "Not Valid"
print( "input is: ", check( "[()]" ) )

#2) Fibonacci Sequence:Take length as input and give fib seq till that length  Example 1:  Input: 5  Output:  0,1,1,2,3

def fibonacci(n):

 a  = 0
 b = 1
 next_number = 0
 count = 1

 while (count <= n):
   print(next_number,end=" ")
   count += 1
   a = b
   b = next_number
   next_number = a + b
 return (next_number)


print(fibonacci(8))

 #3) Remove Duplicates from given Array  Example 1:  Input: 1,2,3,2,5,4,1,4,5   Output: 1,2,3,5,4


def remove_duplicates(arr):
    return list(set(arr))

arr = [1, 2, 3, 4, 5, 5, 4, 3, 2, 1]
print(remove_duplicates(arr))


 # 4) Concatenate any 2 strings to give smallest string from given array of srings  Example:  Input: S=[“aab”,”bcddbc”,”aa”,”aazef”]  Output: “aabaa”

def str_concat(S):
    min_len = float('inf')

    for i in range(len(S)):
        print("i:",i)
        for j in range(i+1, len(S)):
            print("J:",j)
            concat_str = S[i] + S[j]
            if len(concat_str) < min_len:
                min_len = len(concat_str)
                result = (S[i], S[j])
    return ''.join(result)

S = ["aab","bcddbc","aa","aazef"]
print(str_concat(S))

 # 5) Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid. An input string is valid if:Open brackets must be closed by the same type of brackets.Open brackets must be closed in the correct order.Every close bracket has corresponding open bracket of the same type.  Example 1: Input: s = "()"Output: true



def check(myStr):
    open_list = ["[","{","("]
    close_list = ["]","}",")"]
    stack = []
    for i in myStr:
        if i in open_list:
            stack.append(i)
        elif i in close_list:
            pos = close_list.index(i)

            if ( (open_list[pos] == stack[len(stack)-1])):
                stack.pop()
            else:
                return "Not Valid"
    if len(stack) == 0:
        return "Valid"
    else:
        return "Not Valid"
print( "input is: ", check( "[()]" ) )
