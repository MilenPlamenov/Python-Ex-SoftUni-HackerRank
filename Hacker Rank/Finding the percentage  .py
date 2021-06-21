#The provided code stub will read in a dictionary containing key/value pairs of name:[marks] for a list of students.
# Print the average of the marks array for the student name provided, showing 2 places after the decimal.
#The first line contains the integer n , the number of students' records.
# The next  lines contain the names and marks obtained by a student, each value separated by a space.
# The final line contains query_name, the name of a student to query.
n = int(input())

dect = {}

for i in range(n):
    name, *marks = input().split()
    if name not in dect:
        dect[name] = marks

name_to_be_found = input()

for name, marks in dect.items():
    if name == name_to_be_found:
        print(f"{sum([float(i) for i in marks]) / len(marks):.2f}")
