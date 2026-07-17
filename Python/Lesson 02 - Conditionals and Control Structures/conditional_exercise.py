###################################################################

###Exercise 1###
# number = float(input("Provide a number "))
# if number==0:
#       print("Your number is zero. ")
# elif number>=.1: 
#     print("Your number is positive. ")
# else:
#     print("Your number is negative. ")

# ##Exercise 2###
# num=int(input("Please provide an integer.  "))
# if num %2==1:
#     print("Your number is odd.")
# else:
#     print("Your number is even")

###################################################################

###Exercise 2###

# num=int(input("Please provide an integer number.  "))

# if num <0:
#     print("Your number is negative.")
# elif num == 0:
#     print("Your number is zero.")
# else:
#     print("Your number is positive.")

###################################################################

##Exercise 3###
# age= int(input("How old are you?   "))
# if age<13:
#     print("You are still a child   ")
# elif age <=19:
#     print("You are a teenager   ")
# elif age <65:
#     print("You are an adult   ")
# else:
#     print("You are ancient   ")

###################################################################

###Exercise 4###
# a=int(input("Provide a number:   "))
# b=int(input("Please provide a second number:   "))

# if a>b:
#     print("The first number is larger")
# elif b>a:
#     print("The second number is larger")
# else:
#     print("The numbers are the same.")

###################################################################

###Exercise 5###
# grade=float(input("What was your grade?   "))
# if grade >=90:
#     print("You got an A, good job!")
# elif grade >=80:
#     print("You got a B!")
# elif grade >=70:
#     print("Do better, you got a C!")
# elif grade >=60:
#     print("Big oof that's an D.")
# else:
#     print("Dangggg you failed!")

###################################################################

# ###Exercise 6### 
# user_string=(input("Please provde a string of characters or words    "))
# print(len(user_string))

# if len(user_string) >10:
#     print("Long String")
# else: 
#     print("Short String")
###################################################################

# ###Exercise 7###
# num=int(input("Please provide a number.   "))
# if num >=10 and num<=20:
#     print("Number is in range.")
# else:
#     print("Number is out of range.")

###################################################################

##Exercise 8###
# letter=input("Enter a lower case letter.    ")

# if letter=="a"or letter=="e" or letter=="i" or letter=="o" or letter=="u":
#     print("Vowel")
# else:
#     print("Consonant")

###################################################################

###Excercise 9### This one was hard... aka math is hard. 

# year=int(input("Please provide the year to determine if it is a leap year.   "))

# if (year%4==0 and year % 100!=0) or year%400==0:
#     print("It is a leap year") 
# else: 
#     print("It is not a leap year")

###################################################################

###Excercise 10### 

# height=float(input("How tall are you in meters?  "))
# weight=float(input("How much do you weigh in kilograms?   "))
# bmi=weight/height**2
# if bmi <18.5:
#     print("Underweight")
# elif bmi<=24.9:
#     print("Normal weight")
# elif bmi<=29.9:
#     print("Overweight")
# else:
#     print("Obese")

###################################################################

###Excercise 11### 

# colors=['red', 'blue', 'green', 'orange']
# for color in colors:
#     print(color)
    
###################################################################

###Excercise 12### 

# numbers=[5,10,15,20,25]
# print("The list has", len(numbers), "items.")

###################################################################

###Excercise 13### 

# my_list=[]
# my_list.append(1)
# my_list.append(2)
# my_list.append(3)
# my_list.append(4)
# my_list.append(5)
# print(my_list)

## A better way to do this would be, way easier

# my_list=[]
# my_list.extend([1,2,3,4,5])
# print(my_list)

###################################################################

###Excercise 14### 

# for number in range(1,11):
#     print(number)

###################################################################

###Excercise 15### 

# num_list= [4,7,2,9,12]
# total=0
# for number in num_list:
#     total=total+number
# print(total)

###################################################################

###Excercise 16### 

# ava_fruits=["apple", "banana", "orange", "mango"]
# fruit=input("What fruit are you looking for?  ")
# if fruit in ava_fruits:
#     print("This fruit is available")
# else: 
#     print("That fruit is not available")

###################################################################

###Excercise 17### 

# number=[1,2,3,4,5,6,7,8,9,10]
# even_count=0
# for num in number:
#     if num % 2 ==0:
#         even_count=even_count+1
# print("There are", even_count, "numbers.")

###################################################################

###Excercise 18### 

# count=10
# while count >0:
#     print(count)
#     count=count-1


# count=5
# while count<=25:
#     print(count)
#     count=count+5

###################################################################

###Excercise 19### 

# number=1
# while number <=100:
#     print(number)
#     number=number*2

###################################################################

###Excercise 20### 


# my_list=list(range(0, 21,2))
# print(my_list)

###################################################################

###Excercise 21### 

# my_list=[]
# for number in range(1,6):
#     my_list.append(number**2)
# print(my_list)

###################################################################

###Excercise 22### 

# text = "Hello World"
# vowels = "aeiouAEIOU"
# vowel_count = 0

# for character in text:
#     if character in vowels:
#         vowel_count = vowel_count + 1

# print(vowel_count)

###################################################################

###Excercise 23### 

# numbers = [23, 67, 12, 89, 45, 34]
# largest = numbers[0]
# for number in numbers:
#     if number > largest:
#         largest=number
# print(largest)

###################################################################

###Excercise 24### 

# numbers = [2, 5, 7, 10, 15]
# for number in numbers:
#     if number == 7:
#         break
#     print(number)

###################################################################

###Excercise 25### 

# for number in range(1, 11):
#     if number % 3 == 0:
#         continue

#     print(number)

###################################################################

###Excercise 26### 

# for row in range(1, 4):
#     for column in range(1, 4):
#         print(row, "x", column, "=", row * column)

###################################################################

###Excercise 27### 

# numbers = [5, 10, 8, 15, 12, 7]

# result = []
# total = 0
# i = 0

# while total <= 50 and i < len(numbers):
#     result.append(numbers[i])
#     total = total + numbers[i]
#     i= i + 1

# print(f"Final list: {result}")
# print(f"Total sum: {total}")

###################################################################

###Excercise 28### 

# fruits = ["apple", "banana", "cherry", "date"]
# target = "cherry"
# index = 0

# for fruit in fruits:
#     if fruit == target:
#         print(target, "is at index", index)
#         break
#     index += 1

###################################################################

###Excercise 29### 

# original = [10, 20, 30, 40, 50]
# reversed_list = []

# for number in original:
#     reversed_list.insert(0, number)

# print(reversed_list)

###################################################################

###Excercise 30### 

# max_asterisks = 10
# total_printed = 0
# row = 1
# finished = False

# while not finished:
#     for position in range(row):
#         if total_printed >= max_asterisks:
#             finished = True
#             break

#         print("*", end="")
#         total_printed += 1

#     print()

#     if finished:
#         break

#     row += 1

###################################################################

###Instructor led exercise###
# magic_number=22
# guess=int(input("Guess an integer number.  "))
# count=1
# while guess != magic_number and count <3:
#     if guess < magic_number:
#         print("Higher!")
#     else:
#         print("Too high, try again")

#     guess=int(input("Guess an integer number.  "))
#     count+=1
# if guess==magic_number:
#     print(f"Congrats! Thats right!")
#     print(f"It took you {count} guesses.")
# else:
#     print("Better luck next time")
########################################################

# def personalized_card(name: str, number: int, symbol: str) -> None:
#     name_sentence = "Hello, " + name
#     number_sentence = "Your favorite number is " + str(number)

#     sent1 = len(name_sentence)
#     sent2 = len(number_sentence)

#     if sent1 >= sent2:
#         max_len = sent1
#     else:
#         max_len = sent2

#     print(symbol * (max_len + 4))
#     print(symbol + " " + name_sentence.ljust(max_len) + " " + symbol)
#     print(symbol + " " + number_sentence.ljust(max_len) + " " + symbol)
#     print(symbol * (max_len + 4))


# name = input("What is your name? ")
# number = int(input("What is your favorite number? "))

# personalized_card(name, number, "*")
##################################


for i in range(1,16):
    print(i, sep=" ", end=" ")
print() 
for j in range(2,31,2):
    print(j, sep=" ",end=" ")
print() 
for k in range(20,-1,-2):
    print(k,sep=" ",end=" ")
print()

def print_range(start:int, stop:int,step:int)-> None:
    for number in range(start, stop, step):
        print(number,sep=" ", end=" ")
print_range(20,-1,-2)