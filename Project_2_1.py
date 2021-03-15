# Task 1

# Printing Fibonacci numbers by taking input from user as till what they want series

n = int(input("How many terms of series you need : "))

 # For first and second term of series and one variable for our loop and condition 
i1, i2, count = 0, 1, 0 

if n <= 0:
    print("Enter valid input as greater than 0.")
elif n == 1:
    print("Fibonacci Series : ")
    print(i1) 
else:
    print("Fibonacci Series : ")
    while count < n:
        print(i1) # For placing 0 at starting point of series as it needed 
        i3 = i1 + i2
        # Now just we passing values 1 step forward like 1->2 & 2->3
        i1 = i2
        i2 = i3
        count += 1