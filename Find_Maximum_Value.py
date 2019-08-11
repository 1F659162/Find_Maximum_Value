# 6206021620159
# Kaittrakul Jaroenpong IT 1RA
# Python Chapter 5 Example 2

print(">> Program Find maximum value <<")
number = int(input("Enter number of value : "))
if number < 3 :
    number = 3
elif number > 10 :
    number = 10
Max = 0
Str = " "
print(f"\nProgram get value {number} numbers.")
for i in range(1,number+1) :
    value = int(input(f"Enter value #{i} : "))
    if Max < value :
        Max = value
    if Str == " " :
        Str = str(value)
    else :
        Str += ", " + str(value)
print(f"Your enter number : {Str}")
print(f"Maximum value number is {Max}")
print("Exit Program")
