# Least Common Multiple
def lcm(a, b):
    return (a*b)//euclid(a,b)

def euclid(a, b):
    if b == 0:
        return a

    return euclid(b, a % b)

if __name__ == '__main__':
    a, b = map(int, input().split())
    print(lcm(a, b))