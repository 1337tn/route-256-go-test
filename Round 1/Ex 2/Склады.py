n = int(input())
prices = list(input().split(' '))

#prices_dict = {i : prices[i] for i in range(0, len(prices))}

s = 1
income = []
for i in range(1, len(prices)+1):
    income.append(s * int(prices[i-1]))
    s += 1

print(max(income))
