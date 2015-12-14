
def solution(iterations = 10):
    sum = 0
    for i in range(iterations):
        if i % 3 == 0: sum += i
        elif i % 5 == 0: sum += i

    return sum

if __name__ == "__main__":
    print "The final sum is", solution(1000)
