from itertools import permutations

for i in sorted([''.join(c) for c in list(permutations([char for char in input()]))]):
    print(i)