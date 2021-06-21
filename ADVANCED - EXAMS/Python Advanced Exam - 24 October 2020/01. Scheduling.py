jobs = [int(i) for i in input().split(", ")]
index_of_needed_job = int(input())
counter = 0
needed_value = jobs.pop(index_of_needed_job)
for index in range(len(jobs)):
    if jobs[index] <= needed_value:
        counter += jobs[index]
    else:
        continue

print(counter + needed_value)