n = int(input())
students_data = {}
for i in range(n):
    student_name = input()
    student_grade = float(input())
    if student_name not in students_data:
        students_data[student_name] = []
    students_data[student_name].append(student_grade)

filtered_data = {}
for student, grade in students_data.items():
    average_grade = sum(grade) / len(grade)
    if average_grade >= 4.50:
        filtered_data[student] = average_grade

for student, av_gr in sorted(filtered_data.items(), key=lambda x: x[1], reverse=True):
    print(f"{student} -> {av_gr:.2f}")
