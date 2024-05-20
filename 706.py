# cook your dish here
for _ in range(int(input())):
    n,a,b = map(int, input().split())
    e = n//2
    o = n-e
    print((e*a)+(o*b))
# very intresting