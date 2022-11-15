
# def outer_fun():
#     x=6
#     def inner_fun():
#         print("x =",x)
#
#     inner_fun()
#
# outer_fun()

def outer_fun():
    x=8
    def inner_fun():
        y=9
        return x+y
    return inner_fun

a=outer_fun()
# print(a())
