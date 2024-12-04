import re

with open('input','r') as file:
    data = file.read()


x = re.findall(r'mul\(\d{1,3}\,\d{1,3}\)',data)

def multiply(y):
    numbers = y.strip('mult()')
    a,b = numbers.split(',', 1)
    return int(a) * int(b)
total = 0

for y in x:
    total += multiply(y)

print('The total is: ',total)
