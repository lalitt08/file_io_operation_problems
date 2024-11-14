with open('input.txt', 'r') as f1:
    num = []
    for i in f1:
        num.append(int(i))

max_num = max(num)
min_num = min(num)

with open('output.txt', 'w') as f2:
    f2.write(f"Maximum: {max_num}\n")
    f2.write(f"Minimum: {min_num}\n")
