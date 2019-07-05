from itertools import permutations
ab=[''.join(p) for p in permutations(input())]
print(*ab,sep=' ''\n')
