def myround(x, base = 5):
    return base * math.ceil(x / base)

def gradingStudents(grades):
    # Write your code here
    rounded_grades = []
    for grade in grades:
        if grade < 38:
            rounded_grades.append(grade)
        elif abs(myround(grade) - grade) < 3:
            rounded_grades.append(myround(grade))
        else:
            rounded_grades.append(grade)
    return rounded_grades