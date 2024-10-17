#Making use of dictionaries.
#Simple program of converting dictionary key values from int to str via loop and ifs. And then assigning the new values to
#a different dictionary

#- Scores 91 - 100: Grade = "Outstanding" 
#- Scores 81 - 90: Grade = "Exceeds Expectations" 
#- Scores 71 - 80: Grade = "Acceptable" 
#- Scores 70 or lower: Grade = "Fail"

student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}
student_grade = {}
stat_score=""
for loop in student_scores:
    if student_scores[loop]>=91:
        stat_score = "Outstanding"
    elif student_scores[loop]>=81:
        stat_score = "Exceeds Expectations"
    elif student_scores[loop]>=71:
        stat_score = "Acceptable"
    else:
        stat_score = "Fail"
    student_grade[loop] = stat_score
    print(f"{loop}: {student_scores[loop]} - {stat_score}")
print(student_grade)