# Basic Algorithms

# Exercise 1

# What is the output of this block of code?


def mut_example(list1, list2, list3):
    if len(list1) > 2:
        list1 = list1[:2]
    list2[0] = "hi"
    list3 = "".join(list2)

a_list = [1, 2, 3]
b_list = ["a", "b", "c"]
a_str = "do-re-mi"
mut_example(a_list, b_list, a_str)
print(a_list)
print(b_list)
print(a_str)




# Exercise 2

# What's the difference between sort and sorted?

# Which one is a list method and which one is a function that works on lists?

# Please explain



# Exercise 3

# Write a function that doubles the elements in a list.
def double_list(mylist):
    newlist = []
    for i in mylist:
        newlist.append(i * 2)
    return newlist
newlist = double_list([1, 2, 3, 4, 5])
print(newlist)  
# Do you need to return anything here?



# Write a function that doubles the elements in a tuple.
def double_tuple(mytuple):
    newtuple = ()
    for i in mytuple:
        newtuple += (i * 2,)
    return newtuple
newtuple = double_tuple((1, 2, 3, 4, 5))


# Do you need to return anything here?



# Exercise 4

# Rewrite the pop, count, extend, reverse, and sort functions


# Return the results in a new list and do not modify the original list

# (do not use the function you are rewriting)


# Exercise 5

# Fractions can be reprsented by the tuple (numerator, denominator)

# Write a function that adds two fractions
fraction1 = (1, 2)
fraction2 = (1, 4)

numerator = (fraction1[0] * fraction2[1]) + (fraction2[0] * fraction1[1])
denominator = fraction1[1] * fraction2[1]

answer = (numerator, denominator)

print(answer)


# Write a function that multiplies two fractions
fraction1 = (1, 2)
fraction2 = (1, 4)

numerator = (fraction1[0] * fraction2[0])
denominator = (fraction1[1] * fraction2[1])

answer = (numerator, denominator)

print(answer)

# Write a function that simplifies a fraction


# Exercise 6

# write a function to calculate distance between two cartesian coordinates



# extension: make it work for more than two dimensions

