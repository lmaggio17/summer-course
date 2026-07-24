import random

with open("random_numbers.txt", "w") as file:
    for i in range(100):
        random_number = random.randint(1, 1000)
        file.write(str(random_number) + "\n")

print("100 random numbers were written to random_numbers.txt")

with open("random_numbers.txt", "r") as file:
    numbers = []

    for line in file:
        number = int(line.strip())
        numbers.append(number)

highest_number = max(numbers)
lowest_number = min(numbers)
average = sum(numbers) / len(numbers)

print(f"Highest number: {highest_number}")
print(f"Lowest number: {lowest_number}")
print(f"Average: {average:.2f}")