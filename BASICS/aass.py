student_name = input()
fails = 0
current_class = 1
total_grade = 0
is_rej = False
while True:
    current_grade = float(input())
    if current_grade < 4:
        fails += 1
        if fails == 2:
            is_rej = True
            break
    else:
        total_grade += current_grade
        if current_class == 12:
            break
        current_class += 1

if is_rej:
    print(f"{student_name} has been excluded at {current_class} grade")
else:
    print(f"{student_name} graduated. Average grade: {total_grade / current_class:.2f}")
