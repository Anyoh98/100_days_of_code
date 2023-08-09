# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


# Write your code below this row 👇
length = 0
for student in student_heights:
    length = length + 1

total = 0
for num in student_heights:
    total += num
average_height = int(total/length)
print(average_height)
