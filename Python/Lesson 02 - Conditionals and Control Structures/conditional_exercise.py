# age= int(input("How old are you?   "))
# if age<13:
#     print("You are still a child   ")
# elif age <=19:
#     print("You are a teenager   ")
# elif age <65:
#     print("You are an adult   ")
# else:
#     print("You are ancient   ")
######################################
# a=int(input("Provide a number:   "))
# b=int(input("Please provide a second number:   "))

# if a>b:
#     print("The first number is larger")
# elif b>a:
#     print("The second number is larger")
# else:
#     print("The numbers are the same.")
######################################
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
##########################################
###Made it to exercise 6, do these at home...

magic_number=22
guess=int(input("Guess an integer number.  "))
count=1
while guess != magic_number and count <3:
    if guess < magic_number:
        print("Higher!")
    else:
        print("Too high, try again")

    guess=int(input("Guess an integer number.  "))
    count+=1
if guess==magic_number:
    print(f"Congrats! Thats right!")
    print(f"It took you {count} guesses.")
else:
    print("Better luck next time")
