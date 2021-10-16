largest = None
smallest = None
while True:
    inputNum = input("Enter a number: ")
    if inputNum == "done":
        break
    else:
        try:
            num = int(inputNum)
            if largest == None or largest < num:
                largest = num
            elif smallest == None or smallest > num:
                smallest = num
        except:
            print("Invalid input")

print("Maximum is", largest)
print("Minimum is", smallest)
