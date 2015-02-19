n = input("Enter n: ")
n = int(n)

namelist = []

lines = range(1, n + 1)

for line in lines:
    name = input("Enter name: ")
    namelist = namelist + [name]

namelist = sorted(namelist)

for name in namelist:
    print(name)
