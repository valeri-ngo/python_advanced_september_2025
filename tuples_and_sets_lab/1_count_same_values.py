nums = tuple([float(x) for x in input().split()])

data = {}

for ele in nums:
    data[ele] = nums.count(ele)

for key, value in data.items():
    print(f"{key:.1f} - {value} times")