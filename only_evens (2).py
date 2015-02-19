n = input("Enter Number Of Lines: ")
n = int(n)

numbers = range(1, n + 1)
evens = []
for number in numbers:
    user_number = input("Enter Number: ")

    if number % 2 == 0:
        
        evens = evens + [number]

print(len(evens))
for even in evens:
    print(even)
        


    
