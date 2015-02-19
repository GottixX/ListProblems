num_count = input("Enter n: ")
num_count = int(num_count)

numbers = range(1, num_count + 1)
user_nums = []

for number in numbers:
    user_num = input("Number: ")
    user_num = int(user_num)
    user_nums = user_nums + [user_num]

avg = 0

for user_num in user_nums:
    avg += user_num
avg = avg / len(user_nums)
print(avg)
