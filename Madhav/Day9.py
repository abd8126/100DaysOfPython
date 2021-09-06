#Program that converts their scores to grades. By the end of your program, you should have a new dictionary called student_grades that should contain student names for keys and their grades for values. The final version of the student_grades dictionary will be checked
student_scores ={"Harry": 81,"Ron": 78,"Hermione": 99, "Draco": 74,"Neville": 62}
for i in student_scores.keys():
    if student_scores[i]>90:
        student_scores[i]="Outstanding"
    elif student_scores[i]>80:
        student_scores[i]="Exceeds Expectations"
    elif student_scores[i]>70:
        student_scores[i]="Acceptable"
    else:
        student_scores[i]="Fail"
print(student_scores)