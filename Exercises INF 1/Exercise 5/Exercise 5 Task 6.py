import os

def get_average_grade(path):
    if not os.path.exists(path):
        return None
    f = open(path, "r")
    grades = []
    grade = 0
    for line in f.readlines():
        words = line.split(":")
        if len(words) == 2:
            grades.append(float(words[1]))
    f.close()
    if len(grades) == 0:
        return 0.0
    for v in grades:
        grade += v
    avg = grade / len(grades)
    return avg


print(get_average_grade("my_grades.txt"))