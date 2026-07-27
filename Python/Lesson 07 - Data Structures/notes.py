# # # with open("preclass_problem1_data.txt", "r") as file:
# # #     lines = file.readlines()

# # # signal_values = []

# # # for line in lines:
# # #     cleaned_line = line.strip()

# # #     if cleaned_line != "":
# # #         number = int(cleaned_line)
# # #         signal_values.append(number)

# # # signal_values.sort(reverse=True)

# # # highest_five = signal_values[:5]

# # # total = sum(highest_five)

# # # coordinate = total / 10

# # # print("Highest five:", highest_five)
# # # print("Coordinate:", coordinate)

# # mylist = [1, 2, 3, 4, 5]
# # mylist.remove(3)
# # print(mylist)  # Output: [1, 2, 4, 5]
# # del mylist
# # print(mylist)  # This will raise a TypeError because remove() requires an argument

# import copy
# copy.deepcopy(mylist)

# #This creates an actual copy of the list, so that if you modify the copy, 
# # the original list remains unchanged.

# #tuples do not change, they are immutable. 
# # You cannot change the values of a tuple after it has been created.

mydict = {"Smith": ("SGT", 3), "Jones": ("CPL", 2), "Brown": ("PVT", 1), "Johnson": ("PFC", 4), "Davis": ("SGT", 5)}
unit= [(rank, years_of_service) for rank, years_of_service in mydict.values()]
for rank, years_of_service in unit:
    print(f"Rank: {rank}, Years of Service: {years_of_service}")

def lookup_soldier(soldiers, name):
    if name not in soldiers:
        return None

    return soldiers[name]


name = input("Enter the soldier's last name: ")

result = lookup_soldier(mydict, name)

if result is None:
    print("Soldier not found.")
else:
    rank, years_of_service = result
    print(f"Rank: {rank}, Years of Service: {years_of_service}")