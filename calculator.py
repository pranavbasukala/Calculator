a=float(input("enter first number")) #DECLARED AS FLOAT
b=float(input("etner second number"))
print("choose the arithmetic operation")
L=input("1=addition,2=substraction,3=multiplication,4=division")
sum=0
def cal(): #FUNCTION
    if L=='1': #IF STATEMENT FOR COMPARISION
        final=a+b
        print("addition=",final)
        return final
    elif L=='2':
        final=a-b
        print("substraction=",final)
        return final
    elif L=='3':
        final=a*b
        print("multiplication",final)
        return final
    elif L=='4':
        if b!=0:
            final=a/b
            print("division=",final)
            return final
        else:

            print("NOT VALID")
        return None
cal()
