def calculate_gpa(grades, total_courses=5):
    if not grades or total_courses == 0:
        return 0
    gpa = sum(grades) / total_courses
    return round(gpa,2)

grades_list = [3.5, 3.7, 3.2, 4.0, 3.8]

gpa_result = calculate_gpa(grades=grades_list, total_courses=5)

print(f"GPA: {gpa_result}")
