
def gcd(a, b): return b and gcd(b, a%b) or a # greater common divisor
def lcm(a, b): return a*b / gcd(a,b)         # less common multiple

def solution():
    sol = 1
    for i in range(1, 21):
        sol = lcm(sol, i)
    return sol

if __name__ == "__main__":
    print "Solution:", solution()
