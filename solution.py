
def sumOfSquares(numbers = 10):
    return sum(i*i for i in range(1, numbers+1))

def squareOfSums(numbers = 10):
    return sum(range(1, numbers+1))**2

def solution(numbers = 10):
    return squareOfSums(numbers) - sumOfSquares(numbers)

if __name__ == "__main__":
    print "Solution:", solution(100)
