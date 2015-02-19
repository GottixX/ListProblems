n = input("Enter number of lines: ")
n = int(n)

numbers = range(1, n + 1)

user_nums = []

for number in numbers:
    user_num = input("Enter number: ")
    user_nums = user_nums + [user_num]

curent_min = user_nums[0]

for number in user_nums:
    if number < curent_min:
        number = curent_min

print("The smallest of them is " + str(current_min))
