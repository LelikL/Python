import sys


def nums_gen(n):
    for num in range(1, n + 1, 2):
        yield num


for i in nums_gen(11):
    print(i)
