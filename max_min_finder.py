numbers = []
count = int(input("How many numbers do you want to enter?"))
for i in range (count):
    num=int(input(f"Enter Number {i+1}: "))
    numbers.append(num) #adding the value to that list 

print("Maximum Number is ",max(numbers))
print("Minimum Number is " , min(numbers))