#using break and continue in a loop
import numbers

for i in range(10):
    if i == 5:
        break
    print(i)

for num in range(10):
    if num % 2 == 0:
        continue
    print(num)