# 🚨 Don't change the code below 👇
row1 = ["⬜️", "⬜️", "⬜️"]
row2 = ["⬜️", "⬜️", "⬜️"]
row3 = ["⬜️", "⬜️", "⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
# 🚨 Don't change the code above 👆

# Write your code below this row 👇
# Column-row conversion is used in this case
# First value is column number and give sthe horizontal position
# second value is row number and give the vertical position
horizontal_position = int(position[0])
vertical_position = int(position[1])

Selected_row = map[vertical_position - 1]
Selected_row[horizontal_position - 1] = "x"


# Write your code above this row 👆

# 🚨 Don't change the code below 👇
print(f"{row1}\n{row2}\n{row3}")
