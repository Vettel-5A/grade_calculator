import math

# Getting info (How many subgroups are working to determine your grade.)
subgroups = int(input('How many subgroups are affecting your grade? Just give a numerical value.\n'))

# Lists to store input from user
subgroup_weightage_list = []
subgroup_grade_list = []
grade_w_weightage = []

# The list_number variable is used to control what values the calculator uses to determine the projected grade
list_number = 0

# Loop to get and store input. The subgroup weightage, and the current subgroup grade is stored in their respective lists, subgroup_weightage_list and subgroup_grade_list
for x in range(0, subgroups):
    subgroup_weightage = int(input('How much is the subgroup worth as a percentage?\n'))*0.01
    subgroup_grade = float(input('What your current grade in that subgroup?\n'))*0.01
    
    # The info entered in by the user earlier is then stored in the lists in lines 7 and 8, and the subgrade with weightage is stored into the "grade_w_weightage" list.
    subgroup_weightage_list.append(float(subgroup_weightage))
    subgroup_grade_list.append(float(subgroup_grade))
    grade_w_weightage.append(subgroup_weightage_list[list_number]*subgroup_grade_list[list_number])
    
    # Once this whole process is finished, 1 is added to the value of the list number so that during the next run in the loop, the code stores as well as uses the next values in the lists on lines 7,8, and 9.
    list_number += 1

    # To inform the user that they must add new input concerning the next subgroup, the program will print the words, "Next subgroup description" in all caps.
    print('NEXT SUBGROUP DESCRIPTION')
subgroup_weightage_sum = sum(subgroup_weightage_list)

# This is the point where the total grade is calculated. It is calculated by taking the sum of the weighted grades of the subgroups, dividing that by the sum of the weightage of the subgroups, and multiplying that by 100 to get a percentage.
total_grade = (sum(grade_w_weightage)/subgroup_weightage_sum)*100

# The total grade is rounded and printed.
total_grade_rounded = round(total_grade, 2)
print(f"Your projected grade is: {total_grade_rounded}%")
