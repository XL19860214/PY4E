inputHours = input("Enter Hours:")
hours = float(inputHours)
inputRate = input("Enter Rate per Hour:")
rate = float(inputRate)

pay = 0
if hours <= 40 :
  pay = hours * rate
else :
  pay = 40 * rate
  pay += (hours - 40) * rate * 1.5

print(pay)
