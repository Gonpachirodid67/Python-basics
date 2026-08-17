def full_name(fname, lname):
    fullName = f"{fname} {lname}"
    return fullName # function exists here
    print(fullName)

full_name("Frank", "Williams")

for i in range(1, 11, 1):
    # if i is 5, skip it
    # if i == 5:
    #   continue  # skip
    # print(i)

# even numbers 
    # if i % 2 != 0:
    #   continue  # skipping all the odd numbers
    # print(i)

    if i % 2 == 0:
        continue
    print(i)

# break statement breaks the loop
for i in range(1, 11, 1):
    if i == 5:
        break;  # breaks or stops the loop
    print(i)

num = 8
if num > 5:
    pass

age = 24
print(age)