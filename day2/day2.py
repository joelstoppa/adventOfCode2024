with open('input','r') as file:
    data = []

    for line in file:
        lines = list(map(int, line.split()))
        data.append(lines)

safeReports = 0

for line in data:
    isSafe = True
    increasing = line[0] < line[1]
    for number in range(len(line) - 1):
        if (abs(line[number] - line[number + 1]) not in [1, 2, 3]):
            isSafe = False
            break
        if increasing and line[number] >= line[number+1]:
            isSafe = False
            break
        elif not increasing and line[number] <= line[number+1]:
            isSafe = False
            break
    if isSafe:
        safeReports += 1
print(safeReports)



