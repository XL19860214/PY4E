import re

inputFilename = input("Filename: ")
if len(inputFilename) < 1:
  inputFilename = "regex_sum_1362834.txt"

file = open(inputFilename)
fileContent = file.read()
numbers = re.findall('[0-9]+', fileContent)
sum = 0
for number in numbers:
  sum += int(number)

print(sum)
