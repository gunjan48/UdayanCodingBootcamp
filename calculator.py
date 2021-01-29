#My calculator
input1=int(input("Enetr first input: "))
input2=int(input("Enter second input: "))
print("  press 1 for adddition:\n  press 2 for sustraction:\n  press 3 for multiplication:\n  press 4 for division operation:\n  press 5 for performing remainder operation:\n")
operator=input(">")
if operator=="1":
    print("sum of two given inputs is: ",input1+input2)
elif operator=="2":
    print("substraction of two given inputs is: ",input1-input2)
elif operator=="3":
    print("multiplication of two given inputs is: ",input1*input2)
elif operator=="4":
    print("division of two given two given inputs is: ",input1/input2)
elif operator=="5":
    print("remainder is: ",input1%input2)
else:
    print("invalid operator choice")
