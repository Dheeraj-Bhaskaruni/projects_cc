import sys
input = sys.stdin.read

def main():
    data = input().split()
    T = int(data[0])
    index = 1
    results = []
    for _ in range(T):
        a = int(data[index])
        b = int(data[index + 1])
        if a > b:
            results.append('>')
        elif a < b:
            results.append('<')
        else:
            results.append('=')
        index += 2
    print('\n'.join(results))

if __name__ == "__main__":
    main()