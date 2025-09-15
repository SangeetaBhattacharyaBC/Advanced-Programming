# Sample Python Program: Simple Interest Calculator

# Ask user for principal, rate, and time
principal = float(input("Enter principal amount (£): "))
rate = float(input("Enter annual interest rate (%): "))
time = float(input("Enter time in years: "))

# Calculate simple interest
interest = (principal * rate * time) / 100

# Print result
print(f"The simple interest for £{principal} at {rate}% for {time} years is £{interest:.2f}")
