n = input("Number of numbers:")
n = int(n)

numbers = range(1, n + 1)
total_sum = 0

for number in numbers:
    a = input("Enter Number: ")
    a = int(a)
    total_sum += a

print("The total sum is " + str(total_sum))
