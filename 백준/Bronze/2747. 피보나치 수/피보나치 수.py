n = int(input())

def fibo(n):
    dp = [0,1]
    
    for i in range(2,n+1):
        dp.append(dp[i-1]+dp[i-2])

    return dp[-1]

print(fibo(n))