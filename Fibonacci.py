def firstnfib (n):
    fibseq = []
    a,b = 0,1
    for _ in range(n):
        fibseq.append(a)
        a,b = b,a+b
    print(fibseq)
    return()