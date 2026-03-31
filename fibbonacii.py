terms = int(input("Enter number of terms: "))

if terms <= 0:
    print("Please enter a positive number.")
else:
    a, b = 0, 1
    
    print("Fibonacci Series:")
    
    for i in range(terms):
        print(a, end=" ")
        a, b = b, a + b