# Activity 1

empty_list = []
print()

numbers = [1, 2, 3, 4, 5]
print(numbers)

triples = [(1, 2, 3) * 3]
print(triples)

aList = [100, 200, 300, 400, 500]
Alist = aList[::-1]
print(Alist)

# Activity 2

def match_words(words):
    ctr = 0
    lst = []
    for word in words:
        if len(word) > 1 and word[0] == word[-1]:
            ctr += 1
            lst.append(word)

    print("List of words with first and last character same\n", lst)
    return ctr

count = match_words(['abc','cfc', 'xyz', 'aba', '1221'])
print("Number of words with first and last character same: ", count)

# Activity 3

L = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("Original List: ", L)
count = 0
for i in L:
    count += i

avg = count / len(L)

print("The Total Sum of the List is: ", count)
print("The Average of the List is: ", avg)

L.sort()

print("The Smallest Element in the List is: ", L[0])

print("The Largest Element in the List is: ", L[-1])