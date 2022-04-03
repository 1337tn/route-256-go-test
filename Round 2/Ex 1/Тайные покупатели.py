from math import factorial

m = int(input())
#results = []
for i in range(m+1):
    x = input().split(" ")
    #results.append(factorial(int(x[0])) % int(x[1]))
    print(factorial(int(x[0])) % int(x[1]))

"""for r in results:
    print(r)"""