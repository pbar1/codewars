from decimal import *
getcontext().prec = 50

def doubles(maxk, maxn):
    agg = Decimal(0)
    for k in range(1, maxk+1):
        for n in range(1, maxn+1):
            agg += Decimal(1) / Decimal(k*(n + 1)**(2*k))
    return float(agg)

print(doubles(1, 10))
