# def feactorial(n):
#
#     if n < 1:
#         return  1
#     else:
#         return  n * feactorial(n-1)
#
#
# number=int(input("Input  factorial value :"))
# print(feactorial(number))

# def factorial(n):
# 	if n < 1 :
# 		return  1
# 	else:
# 		return  n * factorial(n -1)
#
# print(factorial(4))



def fib(n):
	a=0
	b=1
	print(a,b,end=" ")
	for i in range(n):
		c=a+b
		a=b
		b=c
		print(c,end=" ")
fib(8)

print("================")

# def fib(n):
# 	a = 0
# 	b = 1
# 	print(a, b, end=" ")
# 	for i in range(n):
# 		c = a + b
# 		a = b
# 		b = c
# 		print(c,end=" ")
#
# number = int(input("Enter your value :"))
# fib(number)

# def fibo(n):
# 	a = 0
# 	b = 1
# 	print(a,b,end=" ")
# 	for i in range(n):
# 		c = a + b
# 		a = b
# 		b = c
# 		print( c)
# 	print(c ,end=" ")
#
# fib(8)
#
# def factorial(n):
# 	fact = 1
# 	for i in range(n):
# 		fact = fact * (i+1)
# 	return  fact
# number=int(input("Enter the factorial number :"))
# print(factorial(number))


# factorial program using for loop
#iteratried function  program
# def factorial(n):
# 	fact=1
# 	for i in range(n):
# 		fact = fact * (i+1)
# 	return  fact
#
# number=int(input("Input afactorial number :"))
# print(factorial(number))

# Recursive function
#
# def factorial(n):
# 	if n==1:
# 		return 1
# 	else:
# 		return  n * factorial(n-1)
#
# number=int(input("Input factorial number :"))
# print(factorial(number))
#
# def fibo(n):
# 	a =0
# 	b =1
# 	print(a,b ,end=" ")
# 	for i in range(n):
# 		c = a + b
# 		a = b
# 		b = c
# 		print(c,end=" ")
#
# numbers=int(input("Input fibo number here : "))
# fib(numbers)

# fibonaccie program python different logica

# pattren program for pyython
#
# rows=int(input("Input rows value :"))
# new_bool=int(input('Input a bool value press key true = 1 and or false =0 :'))
#
# if new_bool == True:
# 	for i in  range(1,rows+1):
# 		for j in range(1,i+1):
# 			print("* ",end=" ")
# 		print(" ")
# else:
# 	for i in range(rows,0,-1):
# 		for j in range(1,i+1):
# 			print("* ",end=" ")
# 		print(" ")


