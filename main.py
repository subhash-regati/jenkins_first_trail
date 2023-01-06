def addition(a,b):
    return a+b
input_var=int(input("please enter \n1- for addition\n2 - for subtraction\n3 - for division \n4 - for multiplication\t"))
a=int(input("enter 1st variable"))
b=int(input("enter 2nd variable"))
ans=0
if(input_var==1):
    ans=addition(a,b)
else:
    ans="None"
    print("pls enter properly")
print(ans)