# my_list = ['c','a','t']
# my_string ="cat"

# for item in my_list:
#     print(item)

# for char in my_string:
#     print(char)

# print(my_list[0], my_string[0])
# print(my_list[-1], my_string[-1])
# print(my_string[0:2])

# print(len(my_list)), len(my_string)
# print('a' in my_list, 'a' in my_string)


# def validate_username(username):

#     if len(username) >5 and len(username) <15:
#         print("False")
#         len_req=False
#     for character in username:
#         if not character.isalnum() and character != '_':
#             return False
#             char_num_under=False
#     if not username[0].isalpha():
#         return False
#         starts_letter=False
#     if username[-1] == "_":
#         return False
#         no_underscore=False
#     if not any(character.isdigit() for character in username):
#         return False

#     return True
# username = input("Enter a username: ")
# print(validate_username(username))

###########################################
passengers=["Lopez", "Chen", "Okafor", "Smith", "Patel"]
def print_boarding_list(passengers):
    for seat_number, passenger in enumerate(passengers, start=1):
        print(f"Seat {seat_number}: {passenger}")

print_boarding_list(passengers)