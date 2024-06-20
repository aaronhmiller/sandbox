import sys
sys.setrecursionlimit(1500)
entry = input("Enter a positive integer: ")

def factorial(n):
    # Base case: if n is 0 or 1
    if n == 0 or n == 1:
        return 1
    # Recursive case: n! = n * (n-1)!
    else:
        return n * factorial(n-1)

# Example usage
if int(entry) >= 0:
  print(entry + "! is:")
  print(factorial(int(entry)))
else:
  print("Kindly enter a value greater than or equal to zero.")
