n = input()

if len(n)%2 == 0:
    p = n[:len(n)//2:]+n[len(n)//2-1::-1]
    if int(p) < int(n):
        p = list(p)
        p[len(p)//2] = str(int(p[len(p)//2])+1)
        p[len(p)//2-1] = str(int(p[len(p)//2-1])+1)
        p = ''.join(p)
    print(int(p) - int(n))
else:
    p = n[:len(n)//2:]+n[len(n)//2::-1]
    if int(p) < int(n):
        p = list(p)
        p[len(p)//2] = str(int(p[len(p)//2])+1)
        p = ''.join(p)
    print(int(p) - int(n))