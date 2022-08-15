""" New Password - Code Forces"""

import string
n, k = map(int, input().split())
alphas = list(chr(ord('a')+i) for i in range(26)) or list(string.ascii_lowercase)
for i in range(n):
    print(alphas[i % k], end='')
    

