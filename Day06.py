def get_letter_grade(score):
    if not 0 <= score <= 100:
        return "Invalid"
    if score >= 90:
        return "A"
    elif score >= 85:
        return "A-"
    elif score >= 80:
        return "B+"
    elif score >= 75:
        return "B"
    elif score >= 70:
        return "B-"
    elif score >= 65:
        return "C+"
    elif score >= 60:
        return "C"
    else:
        return "F"

def print_grade_summary(name, score):
    grade = get_letter_grade(score)
    if grade == "Invalid":
        print(f"Score {score} is out of range.")
    else:
        print(f"Student {name} scored {score} → Grade: {grade}")

# Example call using named parameters
print_grade_summary(name="Furqan", score=90)
