import numpy as np
for i in range(10):
    n = 10**i

    print(f'{n}')
    a = n * (len(str(n))**2)
    b = n**1.5
    c = n**100
    d = n**len(str(n))
    e = 4**n
    #f = 2**(n**2)
    #g = 2**(2**n)
    print(b>a)
    print(c>b)
    print(d>c)
    print(e>d)
    #print(f>e)
    #print(g>f)
