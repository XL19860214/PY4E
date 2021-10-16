inputScore = input("Enter Score: ")
score = float(inputScore)

grade = ""
if score >= 0.9 :
  grade = "A"
elif score >= 0.8 :
  grade = "B"
elif score >= 0.7 :
  grade = "C"
elif score >= 0.6 :
  grade = "D"
elif score < 0.6 and score >= 0.0 :
  grade = "E"
else :
  grade = "Error"
    
print(grade)
