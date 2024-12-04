with open('input','r') as file:
    col1 = []
    col2 = []

    for line in file:
        num1, num2 = line.split()

        col1.append(int(num1))
        col2.append(int(num2))
col1.sort()
col2.sort()

result = 0

for x in range(len(col1)):
    result += abs(col1[x]-col2[x])

# for x in range(len(col1)):
#     if col1[x] > col2[x]:
#         result += col1[x] - col2[x]
#     elif col1[x] < col2[x]:
#         result += col2[x] - col1[x]
#     else:
#         continue

print('Risultato = ', result)


