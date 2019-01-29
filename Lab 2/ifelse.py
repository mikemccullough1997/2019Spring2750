def grade(score):
    if score >= 90:
        gradepoint = 4
    elif score >= 80 and score <= 89:
        gradepoint = 3
    elif score >= 70 and score <= 79:
        gradepoint = 2
    elif score >= 60 and score <=69:
        gradepoint = 1 
    elif score > 60:
        gradepoint = 0
    return gradepoint
