nums = range(1, 10000000)
has_divisible = any(n % 99 == 0 for n in nums)
print("Found a number divisible by 99:", has_divisible)
