# operators - Arithmatic, logical, assignment...
print(3 + 4) # 3 and 4 are operands whereas + is called operator (addition operator) => Arithmatic
print(10 % 4) # 2
print(16 % 5) # 1
print(30 % 7) # 2
print(2 ** 3) # 2*2*2 = 8
print(5**2) # 5*5 = 25
print(10**3) # 10*10*10 = 1000
print(16 // 3) # 5
print(10 // 3) # 3

city = "Goa" # = is not an equal (assignment sign =)
num = 45
# equal to (==)
print(num == 45) # True
print(num == 40) # False

# > greater than
print(num > 30) # True

# < less than
print(num < 40) # False

# >= either greather than or equal to
print(num >= 45) # True

# <= either less than or equal to
print(num <= 50) # True
print(num <= 35) # False

# != not equal to
print(num != 45) # False
print(num != 40) # True

x = 5
x += 3 # x = 5 + 3

print(x)

x -= 2 # x = 8 - 2
print(x)

x *= 4 # x = 6 * 4
print(x)

x /= 3 # x = 24 / 3
print(x)

x **= 2 # x = 8 ** 2
print(x)

x //= 5 # x = 64.0//5
print(x)

x %= 5 # x = 12.0 % 5
print(x)

#Storingn values
tree1 = 98
tree2 = 94
tree3 = 41
tree4 = 95
tree5 = 11

#Finding the total of trees
sum = tree1+tree2+tree3+tree4+tree4+tree5
print("the sum of all the 5 trees is: ", sum)

#Finding the average of trees
average = sum/5
print("the average of all the trees is: ", average)