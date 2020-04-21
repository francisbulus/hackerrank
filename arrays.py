if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))
    a =  arr[::-1]
    print (" ".join(str(x) for x in a))