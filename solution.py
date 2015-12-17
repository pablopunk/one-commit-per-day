
def solution():
    largest = 0
    for i in range(100, 1000): # 3 digits 100-999
        for j in range(i, 1000):
            prod = i * j
            s = str(prod)
            if s == s[::-1]: # palindrome
                if prod > largest:
                    largest = prod # update if it's greater
    return largest

if __name__ == "__main__":
    print "The largest prime factor is", solution()
