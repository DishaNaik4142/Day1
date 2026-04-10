# Recursion

# def powerOfTwo(n):
#     if n == 0:
#         return 1
#     else:
#         power = powerOfTwo(n-1)
#         return power * 2


#Example 1:Fdactorial solution

# def factorial(num):
#     if num <= 1:
#         return 1
#     return num * factorial(num-1)

# print(factorial(4))

#op:24



#ex.2:
# def isPalindrome(strng):
#     if len(strng) == 0:
#         return True
#     if strng[0] != strng[len(strng)-1]:
#         return False
#     return(isPalindrome(strng[1:-1]))

# # print (isPalindrome('awesome'))#False
# print(isPalindrome('tacocat'))#True
    


# #ex3:
# def power (base, exponent):
#     if exponent ==0:
#         return 1
#     return base * power(base, exponent-1)

# print(power(2,0))#1
# print(power(2,2))#4
# print(power(2,4))#16



#capita;izefirst Solution using recursion:

# def capitalizeFirst(arr):
#     result =[]
#     if len(arr) ==0:
#         return result
    
#     result.append(arr[0][0].upper() + arr[0][1:])
#     return result + capitalizeFirst(arr[1:])

# print(capitalizeFirst(['car','taco','banana']))




#productOf Array Solution:

# def productOfArray(arr):
#     if len(arr) == 0:
#         return 1
#     return arr[0] * productOfArray(arr[1:])

# print(productOfArray([1,2,3]))
# print(productOfArray([1,2,3,10]))



#fib Solution:

# def fib(num):
#     if (num < 2):
#         return num
#     return fib (num - 1) + fib(num - 2)
# print(fib(4))#3
# print(fib(10))#55
# print(fib(28))#317811
# print(fib(35))#9227465



class Tree: