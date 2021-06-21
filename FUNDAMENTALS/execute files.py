limit = int(input())
num_cores = int(input())
times = 0
demo_list = []
a = sorted([int(c) for c in input().split()], reverse=True)
print(sum([c for c in [demo_list.append(int(a[c] / num_cores)) if a[c] % num_cores == 0 and c < limit else a[c] for c in range(len(a))] if c is not None]) + sum(demo_list))