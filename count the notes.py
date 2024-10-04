#taking total amount by user
amount=int(input("please enter amount to withdraw"))
#calculating the number of notes of different denomintions
n1=amount//100
n2=(amount%100)//50
n3=((amount%100)%50)//10
print("number of 100 rupee notes=",n1)
print("number of 50 rupee notes=",n2)
print("number of 10 rupee notes=",n3)