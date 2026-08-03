# def palindrome(input_string):
#     # Base case: if the string is empty or has one character, it's a palindrome
#     if len(input_string) <= 1:
#         return True
#     # Check if the first and last characters are the same
#     if input_string[0] != input_string[-1]:
#         return False
#     # Recursive case: check the substring without the first and last characters
#     return palindrome(input_string[1:-1])

#     print(f"computing {input_string[1:-1]}")  
#     result = palindrome(input_string[1:-1])
#     print(f"result for {input_string[1:-1]}: {result}")
#     return result

### Calculate the sum of a list of numbers using recursion
def recursive_sum(numbers):
    if not numbers:
        print("Empty list reached. Returning 0.")
        return 0

    print(f"Adding {numbers[0]}, then {numbers[1:]}")
    result = numbers[0] + recursive_sum(numbers[1:])
    print(f"Sum for {numbers}: {result}")

    return result


print("Final result:", recursive_sum([1, 2, 3, 4, 5, 6, 7]))