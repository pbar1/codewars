__trib_cache = {}

def trib_memo(signature, n):
    if n in __trib_cache: return __trib_cache[n]
    if n <= len(signature): __trib_cache[n] = signature[n-1]
    else: __trib_cache[n] = trib_memo(signature, n-1) + trib_memo(signature, n-2) + trib_memo(signature, n-3)
    return __trib_cache[n]

def tribonacci(signature, n):
    arr = []
    if n == 0: return arr
    for i in range(1,n+1): arr.append(trib_memo(signature, i))
    __trib_cache.clear()
    return arr
