# Maximum Pairwise Product

n = int(input())
a = [int(x) for x in input().split()]
assert(len(a) == n)

a.sort(reverse=True)
print(a[0] * a[1])