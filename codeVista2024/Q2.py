import sys


def calcRegions(T, Arr):
    # Write your code here
    if Arr[-1]<=2:
        C=2*Arr[-1]
    else:
        C=2*Arr[-1]+1
    return C


def main():
    T = int(sys.stdin.readline().strip())
    
    Arr = []
    for _ in range(T):
        Arr.append(int(sys.stdin.readline().strip()))

    result = calcRegions(T, Arr)

    print(result)


if __name__ == "__main__":
    main()
