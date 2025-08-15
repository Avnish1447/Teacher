# def evenOdds():
#     n, k = list(map(int, input().split()))
#     odd = []
#     even = []
#     isValid = (1 <= k and k <= n and n <= 10**12)

#     if isValid:
#         for i in range(1,n+1):
#             if (i) % 2 !=0:
#                 odd.append(i)
#             else:
#                 even.append(i)
#         result = odd + even
#     else:
#         return
    
#     print(result[k-1])

# evenOdds()

def evenOdds():

    n, k = map(int, input().split())
    numOdds = (n + 1) // 2

    if k <= numOdds:
        result = 2 * k - 1
    else:
        kEvens = k - numOdds
        result = 2 * kEvens
        
    print(result)

evenOdds()