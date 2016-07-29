#! python3

print('My name is')
for i in range(5):
    print('Jimmy Five Times (' + str(i) + ')')

print('My name is')
i = 0
while i < 5:
    print('Jimmy Five Times (' + str(i) +')')
    i = i  + 1


total = 0
for num in range(101):
    total = total + num
print(total)


for i in range(12, 16):
    print(i)

    for i in range(0, 10, 2):
        print(i)

for i in range(5, -1, -1):
    print(i)