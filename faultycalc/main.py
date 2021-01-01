inp = int(input("Enter a number"))
operator = input("Enter a operator")
se_inp = int(input("Enter a number"))
if(inp==2 and operator=="+" and se_inp==3):
    print(2*3)
else:
    if(operator=="+"):
        print(inp+se_inp)
    elif(operator=="-"):
        print(inp-se_inp)
    elif(operator=="*" or operator=="x"):
        print(inp*se_inp)
    elif(operator=="/"):
        print(inp / se_inp)
    else:
        print("something wrong")