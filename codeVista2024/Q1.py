import sys


def minRemovals(S):
    # Write your code here
    SS = []
    for news in S:
        SS.append(news)

    N = len(SS)
    i = 0
    contChar = 0
    while i <= N-1:
        p = (i+N-2)%N
        if SS[i] != SS[p]:
            contChar = contChar+1
            SS.remove(SS[p])
        i = i+1
        N = len(SS)
    return contChar

def main():
    S = sys.stdin.readline().strip('\n')

    result = minRemovals(S)

    print(result)


if __name__ == "__main__":
    main()
