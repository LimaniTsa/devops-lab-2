numbers = input("Enter numbers: ")
numbers_list = numbers.split()

numbers_list = [float(num) for num in numbers_list]

average = sum(numbers_list) / len(numbers_list)

# Using built in python functions to get min and max of numbers_list
smallest = min(numbers_list)
largest = max(numbers_list)

# Print average / smallest & largest num
print(f"The average is: {average}")
print(f"The smallest number is: {smallest}")
print(f"The largest number is: {largest}")
