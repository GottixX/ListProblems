n = input("Enter number of lines: ")
n = int(n)

numbers = range(1, n + 1)

user_nums = []

for number in numbers:
    user_num = input("Enter number: ")
    user_nums = user_nums + [user_num]

curent_max = user_nums[0]

for num in user_nums:
    if num > curent_max:
        curent_max = num 

print("The biggest of them is " + str(curent_max))
