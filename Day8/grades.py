# Given is a list of student names and their corresponding grades
# 1. Create a dictionary from the given lists
# 2. calcualate the average grade for each student
# 3. Find the student with the highest average grade
# 4. Find the student with the lowest average grade
# 5 print all students have a an average grade above 85
import statistics

def grade_stats(students, grades):

    highavg=0
    lowavg=1000
    avg85={}

    for x in range(len(students)):
        avg_grade=statistics.fmean(grades[x])
        if avg_grade > 85:
            avg85[students[x]]=avg_grade
        if avg_grade > highavg:
            highstudent=students[x]
            highavg=avg_grade
        if avg_grade < lowavg:
            lowstudent=students[x]
            lowavg=avg_grade

    print(f"Student: {highstudent} has the highest average of {round(highavg,2)}.")
    print(f"Student: {lowstudent} has the lowest average of {round(lowavg,2)}.")

    return avg85

students = ['Alice', 'Bob', 'Charlie', 'David', 'Eve']
grades = [
    [85, 92, 78],
    [79, 85, 88],
    [91, 89, 95],
    [70, 65, 80],
    [88, 90, 92]
]

avg85=grade_stats(students,grades)

for key,value in avg85.items():
    print(f"Student: {key} has an average of {round(value,2)} which is over 85.")

# ## Brad's solution

# student_grades = dict(zip(students, grades))

# for student, grades in student_grades.items():
#     average_grade = sum(grades) / len(grades)
#     student_grades[student] = {
#         'grades': grades,
#         'average': average_grade
#     }

# student_highest_avg = max(student_grades, key=lambda student: student_grades[student]['average'])
# student_lowest_avg = min(student_grades, key=lambda student: student_grades[student]['average'])

# print("Highest average = " + student_highest_avg)
# print("Lowest average = " + student_lowest_avg)

# for student, grades in student_grades.items():
#     if grades['average'] > 85:
#         print(student)

# ## Greg's solution

# students = ['Alice', 'Bob', 'Charlie', 'David', 'Eve']
# grades = [
#     [85, 92, 78],
#     [79, 85, 88],
#     [91, 89, 95],
#     [70, 65, 80],
#     [88, 90, 92]
# ]

# student_scores = {}
# avg_grades = {}
# for i in range(0, len(students)):
#     student_scores[students[i]] = grades[i]
#     avg_grades[students[i]] = (lambda score_list: sum(score_list)/float(len(score_list)))(grades[i])

# print("Student Scores --> ", student_scores)
# print("Average Grades --> ", avg_grades)

# top_student = max(avg_grades, key = avg_grades.get)
# bot_student = min(avg_grades, key = avg_grades.get)
# eight_five_club = {k:v for (k,v) in avg_grades.items() if v > 85}

# print("Highest Grade --> ", top_student)
# print("Lowest Grade --> ", bot_student)
# print("Students with a grade above 85% --> ", eight_five_club.keys())