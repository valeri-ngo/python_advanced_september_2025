from collections import deque

robots_info = input().split(';')
robots = []
products = deque()

h, m, s = map(int, input().split(':'))
start_time = h * 3600 + m * 60 + s
current_time = start_time

for info in robots_info:
    robot_name, processing_time = info.split('-')
    robots.append([robot_name, int(processing_time), 0])

while True:
    line = input()
    if line == 'End':
        break
    products.append(line)

while products:
    current_time += 1
    product = products.popleft()

    assigned = False

    for i in range(len(robots)):
        robot_name, processing_time, busy_until = robots[i]
        if current_time >= busy_until:
            print(f"{robot_name} - {product} [{(current_time // 3600) % 24:02d}:{(current_time % 3600) // 60:02d}:{current_time % 60:02d}]")
            robots[i][2] = current_time + processing_time
            assigned = True
            break
    if not assigned:
        products.append(product)
