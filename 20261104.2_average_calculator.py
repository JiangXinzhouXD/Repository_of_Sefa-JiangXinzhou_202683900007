total = 0
count = 0
while count < 5:
    mark = int(input("Enter mark: "))
    while mark < 0 or mark > 100:
        mark = int(input("Invalid. Try again: "))

    total += mark
    count += 1

average = total / count
print("Average:", average)