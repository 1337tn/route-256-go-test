N = int(input())
results = []
for i in range(N):
    n = int(input())
    s = input()
    t = input()
    if str(sorted(s)) < str(sorted(t, reverse=True)):
        results.append("Yes")
    else:
        results.append("No")
for i in range(N):
    print(results[i])