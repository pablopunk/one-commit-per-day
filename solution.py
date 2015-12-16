
def solution(num = 13195):
    i = 2
    while i * i < num:
        while num % i == 0:
            num /= i # we factor 'num' as long as it keeps being divided by 'i'
        i += 1
    return num # now it's gonna be the largest prime we reached (it couldn't be divided any more)

if __name__ == "__main__":
    print "The largest prime factor is", solution(600851475143)
