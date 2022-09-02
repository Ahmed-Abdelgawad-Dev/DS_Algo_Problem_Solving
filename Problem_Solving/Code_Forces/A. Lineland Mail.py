
n=int(input());
x=list(map(int,input().split()))
for i in range(n):
    t=x[i];
    print(min(abs(t-x[i-1]),abs(x[i-n+1]-t)),max(t-x[0],x[n-1]-t))