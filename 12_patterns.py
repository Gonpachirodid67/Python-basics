# Half Pyramid of stars
print("Half Pyramid Patterns of Stars (*): ")
n = int(input("Enter the number of rows: "))
# outer loop to handle number of columns
for i in range(n):
    # inner loop to handle numbers of columns
    for j in range(i+1):
        #display result
        print("* ", end="")
    print()

# Floyd's Triangle
print("Floyd's Triangle")
rows = int(input("Enter the number of rows: "))
number = 1 # initialize by 1

for i in range(1, rows + 1):
    for j in range(1, i + 1):
        print(number, end="")
    print()

# Half of Diamond
print("Half of Diamond")
rowSize = int(input("Enter the number of rows: "))
if rowSize%2==0:
    halfDiamRow = int(rowSize/2)
else:
    halfDiamRow = int(rowSize/2)+1
space = halfDiamRow - 1

for i in range(1, halfDiamRow + 1):
    for j in range(1, space + 1):
        print(end="")
    space = space + 1
    num = 1
    for j in range(1, 2*(halfDiamRow - i)):
        print(end=str(num))
        num = num + 1
    print()