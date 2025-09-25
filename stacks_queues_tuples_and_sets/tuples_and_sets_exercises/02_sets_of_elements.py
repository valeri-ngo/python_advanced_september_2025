nums = input().split()

set_a = set()
set_b = set()

num_n = int(nums[0])
num_m = int(nums[1])

for _ in range(num_n):
    set_n = int(input())
    set_a.add(set_n)

for _ in range(num_m):
    set_m = int(input())
    set_b.add(set_m)

if set_a & set_b:
    print(*set_a & set_b, sep='\n')