# Greatest Common Divisor
def euclid(a, b):
    if b == 0:
        return a

    return euclid(b, a % b)


a, b = map(int, input().split())
print(euclid(a, b))
