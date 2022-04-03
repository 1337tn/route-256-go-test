from re import M


n = int(input())

b = n // 384
n -= 384 * b

p = n // 24
if p > 14:
    p = 0
    b += 1
    n -= 384
else:
    n -= 24 * p

m = n
if m > 19:
    m = 0
    p += 1

print(m, p, b)
