for _ in range(int(input())):
    n,k,m = map(int, input().split())
    c = k*m
    print((n+c-1)//c)
# my first solution to ceiling trick with integer division