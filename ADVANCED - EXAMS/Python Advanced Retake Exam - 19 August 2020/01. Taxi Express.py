from collections import deque

time_customers = deque([int(i) for i in input().split(", ")])
time_of_taxis = [int(i) for i in input().split(", ")]

total_time = 0

while time_of_taxis:
    current_customer = time_customers[0]
    current_taxi = time_of_taxis[-1]
    if current_taxi >= current_customer:
        total_time += current_customer
        time_customers.popleft()
        time_of_taxis.pop()
    else:
        time_of_taxis.pop()

if not time_customers:
    print("All customers were driven to their destinations")
    print(f"Total time: {total_time} minutes")
else:
    print("Not all customers were driven to their destinations")
    print(f"Customers left: {', '.join([str(customer) for customer in time_customers])}")