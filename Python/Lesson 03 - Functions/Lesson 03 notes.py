# start=int(input("Enter starting value"  ))
# stop=int(input("Enter end value"   ))

# def count_fizzbuzz(beginning: int, end:int): 
#     fizzbuzzes = 0 
#     for num in range(beginning,end+1):
#         if num % 3==0 and num % 5==0:
#             print("Fizzbuzz")
#             fizzbuzzes+=1
#         elif num % 3==0:
#             print("Fizz")
#         elif num % 5==0:
#             print("Buzz")
#         else:
#             print(num)
#     return fizzbuzzes

# amount = count_fizzbuzz(start,stop)
# print("There are", amount, "fizzbuzzes")
# ##########################################################################

# digitlist=['1','2','3','4','5','6','7','8','9']
# def check_password(password: str)->str:
#     hasdigit=False
#     passwordlen=len(password)
#     if passwordlen<8:
#         return("Weak Password. ")
#     else:
#         for letter in password:
#             for digit in digitlist:
#                 if letter == digit:
#                     hasdigit=True
#                     return "Strong Password"
                
#         return "Medium Password"
# user_password=str(input("Enter a password: "))
# password_strength=check_password(user_password)

# while password_strength != "Strong Password":
#     #print(f"The password strength is {password_strength}")
#     user_password=input("Enter a password: ")
#     password_strength=check_password(user_password)
# print("Your password strength is", password_strength)

##########################
def letter_grade(letters:float)-> str:
    if grade >=90:
        return "A"
    elif grade >=85:
        return "B"
    elif grade >=75:
        return "C"
    elif grade >=65:
        return"D"
    return"F"

students=int(input("How many grades are there to enter?  "))
for student in range(1,students+1):
    grade= float(input("Enter student's score"))
    total_scores =+ grade
    print(f"Student number{student} got aletter grade {letter_grade(grade)}")
print("The class average was", {total_scores/students})