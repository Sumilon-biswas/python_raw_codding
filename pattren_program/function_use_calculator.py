
def calculator_fun(operator,a,b):

    if operator == '+':
        print("Total Result :",a+b)
    elif operator == '-':
        print("Toral Result :",a-b)
    elif operator == '*':
        print("Total Resukt :",a *b)
    elif operator == '/':
        print("Total Result :".a /b)
    elif operator == '//':
        print("Total Result :",a//b)
    elif operator == '%':
        print("Total result",a%b)
    else:
        print("Please ! selected any opeator ....")

calculator_fun('+',20,30)