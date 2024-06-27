# Prompt User for Pattern Size
size = int(input("Enter the size of the pattern: "))  

# Draw the Pattern
if size <= 0:
   print("Please enter a positive integer for the size.")
else:
    row = 0
    while row < size:
          for _ in range(size):
              print("*", end="")
          print()
          row += 1


