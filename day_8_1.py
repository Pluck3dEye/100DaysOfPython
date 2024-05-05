import math


def calculate_paint(height, width, cover):
    painting = math.ceil((height * width) / cover)
    return painting


test_h = 2
test_w = 3
coverage = 5

print(calculate_paint(test_h, test_w, coverage))


def is_prime(num):
    if num < 2:
        return "not a prime number"

    for _ in range(2, round(math.sqrt(num)) + 1):
        if num % _ == 0:
            return "not a prime number"
    return "a prime number"


for i in range(1000000):
    print(f"{i} is {is_prime(i)}")
