numbers = input("enter numbers: ")
numbers_list = numbers.split()

numbers_list = [float(num) for num in numbers_list]

average = sum(numbers_list)/len(numbers_list)

print(f"the average is: {average}")
