mark = int(input("Enter mark: "))
while mark < 0 or mark > 100:
    print("Invalid mark")
    mark = int(input("Enter mark: "))
print("Accepted")