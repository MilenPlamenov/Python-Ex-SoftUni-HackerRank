nums = [int(i) for i in input().split(", ")]
positive = [x for x in nums if x >= 0]
negative = [x for x in nums if x < 0]
evens = [x for x in nums if x % 2 == 0]
odds = [x for x in nums if x % 2 != 0]
print(f"Positive: {', '.join(str(x) for x in positive)}")
print(f"Negative: {', '.join(str(x) for x in negative)}")
print(f"Even: {', '.join(str(x) for x in evens)}")
print(f"Odd: {', '.join(str(x) for x in odds)}")