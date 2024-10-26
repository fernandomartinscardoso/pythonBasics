import sys


def calcNum(N, M, dec, K, Arr):
    # Write your code here
    i=0
    while i<K:
        for j in range(N):
            for k in range(M):
                Arr[j,k] = Arr[j,k]-dec
        i=i+1



def main():
    N = int(sys.stdin.readline().strip())
    
    M = int(sys.stdin.readline().strip())
    
    dec = int(sys.stdin.readline().strip())
    
    K = int(sys.stdin.readline().strip())
    
    Arr = []
    for _ in range(N):
        Arr.append(list(map(lambda x: int(x), sys.stdin.readline().strip().split(" "))))

    result = calcNum(N, M, dec, K, Arr)

    print(result)


if __name__ == "__main__":
    main()
