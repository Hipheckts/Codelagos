
GTB = 1
AccessBank = 2
FirstBank = 3
ZenithBank = 4

print("________________________________________________")
print("*****************Select your Bank*****************")
print("________________________________________________")
print("1 - GTB", "2 - Access Bank", "3 - First Bank", "4 - Zenith Bank")

Bankname = int(input("Select Bank: "))

if Bankname == 1:
    print("Selected Bank is Guarantee Trust Bank")

elif Bankname == 2:
    print("Selected Bank is Access Bank")

elif Bankname == 3:
    print("Selected Bank is First Bank")

elif Bankname == 4:
    print("Selected Bank is Zenith Bank")

Pin = int(input("Enter Pin: "))

if Pin == 0000:
    print("________________________________________________")
    print("*****************Welcome*****************")
    print("________________________________________________")
else:
    print("________________________________________________")
    print("*****************incorrect pin*****************")
    print("________________________________________________")
    
Withdraw = 5
Inquiry = 6
Transfer = 7
ChangePin = 8
print ("5 - Withdraw", "6 - Inquiry", "7 - Transfer", "8 - Change Pin")
    
Transaction = int(input("Select Transaction: "))

if Transaction == 5:
        amount = int(input ("Enter Amount: "))
        print ("....processing")
        print ("Take Your cash")
elif Transaction == 6:
    print ("Your account balance is One million, two hundred and twenty thousand naira only")
    print ("")
    print ("Thank you for banking with us")
    print ("")
    print ("Take your card")
elif Transaction == 7:
    receiver = int(input("Enter receiver's NUBAN: "))
elif Transaction == 8:
    old = int(input("Enter Old pin: "))
    new = int(input ("Enter New pin: "))
    print("Pin changed successfully!!!")
    print("")
    print ("Thank you for banking with us")
    print ("")
    print ("Take your card")
    
for num in range (1,amount):
    print (amount)
    print ("Thank you for banking with us")
    print("")
    print ("Take your card")

