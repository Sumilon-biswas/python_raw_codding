# import frist_function
# import second_function
# from  frist_function import  function
# from  second_function import  function
#
# frist_function.function()
# second_function.function()

# gobal varibel,local variable,
#
# y=20
# def myfunction():
#      x=10
#      global y
#      y =y+1
#      print("x :",x)
#      print("Y inserted the function :",y)
#
# print("Printed golbal y :",y)
# myfunction()


# y=20
# def myfun():
#       x=10
#       global  y
#       y=y+1
#       print("local function x ",x)
#       print("local function print use gobal variable ",y)
#
# myfun()


#nested function

# y=10
#
# def outer_fun():
#      z=4
#      def inner_fun():
#           x=4
#           print("x  :",x)
#           print("outer function insert z",z)
#      inner_fun()
#      print("outer function print ",z)
# outer_fun()

# y=10
#
# def outer_fun():
#      z=4
#      def inner_fun():
#           x=4
#           nonlocal z
#           z=z+1
#           print("x  :",x)
#           print("outer function insert z",z)
#      inner_fun()
#      print("outer function print ",z)
# outer_fun()


# y=10
# def outer_fun():
#      z=6
#      def inner_fun():
#           k=10
#           nonlocal z
#           z=z+8
#           print("inner variable k:",k)
#           print(" outer variable z updates ",z)
#
#      inner_fun()
#
# outer_fun()

#
# x=10
# def outer_fun():
#      # x=7
#      def inner_fun():
#           # x=20
#           print("display x:",x)
#      inner_fun()
#
# outer_fun()

name="sumilon bisws"
def outer_fun():
     # name="anik"
     def inner_fun():
          # name="Ronie"
          print("print name ",name)
     inner_fun()

outer_fun()