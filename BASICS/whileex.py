bad_grades = int(input())
total_score = 0
num_problems = 0
last_problem = ""
num_bad_grades = 0
command = input()
too_many_bad_grades = False
while command != "Enough":
    last_problem = command
    current_grade = int(input())
    if current_grade <= 4:
        num_bad_grades += 1
        if num_bad_grades == bad_grades:
            too_many_bad_grades = True
            break
    num_problems += 1
    total_score += current_grade
    command = input()
if too_many_bad_grades:
    print(f"You need a break, {num_bad_grades} poor grades. ")
else:
    aver_score = total_score / num_problems
    print(f"Average score: {aver_score:.2f}")
    print(f"Number of problems: {num_problems}")
    print(f"Last problem: {last_problem}")