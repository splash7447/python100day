# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇
total_value = 0
for value in student_heights:
  total_value += value
#print(total_value)

denominator_value = 0
for value in student_heights:
  denominator_value += 1
#print(denominator_value)

average_value = round(total_value / denominator_value)
print(average_value)