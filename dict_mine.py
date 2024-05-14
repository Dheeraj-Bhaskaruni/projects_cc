# cook your dish here
for _ in range(int(input())):
    n = int(input())
    s = input()
    d = {"A":'T', 'T':"A", "C":'G', 'G':'C'}
    s = list(s)
    for i in range(0, n):
        s[i] = d[s[i]]
    print(''.join(s))
