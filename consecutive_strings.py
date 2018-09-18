# k = 1: +
# k = 2: +-
# k = 2: -+
# k = 3: +-- => strarr[x-0:x+3]
# k = 3: -+- => strarr[x-1:x+2]
# k = 3: --+ => strarr[x-2:x+1]
# k = 4: +--- => strarr[x-0:x+4] (i = 0)
# k = 4: -+-- => strarr[x-1:x+3] (i = 1)
# k = 4: --+- => strarr[x-2:x+2] (i = 2)
# k = 4: ---+ => strarr[x-3:x+1] (1 = 3)
# ==> strarr[x-i:x+k]

# k = 4, e = 2, i = 1: ---x => [x-3:x+1]
# k = 4, e = 2, i = 2: --x+ => [x-2:x+2]
# k = 4, e = 2, i = 3: -x++ => [x-1:x+3]
# k = 4, e = 2, i = 4: x++- => [x-0:x+4]
# k = 4, e = 2, i = 5: ++-- => [x+1:x+5]
# k = 4, e = 2, i = 6: +--- => [x+2:x+6]

# ==> [x-(k-i):x+i], where i in range(1,k+e+1)

def longest_consec(strarr, k):
    n = len(strarr)
    if n == 0 or k > n or k <= 0: return ""
    strarr_sorted = sorted(strarr, key=lambda s: len(s), reverse=True)
    len_longest = len(strarr_sorted[0])
    e = 0
    for i in range(1, len(strarr_sorted)):
        if len(strarr_sorted[i]) == len_longest: e += 1
        else: break

    # this somehow causes more errors
    x = -1
    for i in range(0, len(strarr)):
        if len(strarr[i]) == len_longest:
            x = i
            break

    candidates = []
    for i in range(1, k+e+1):
        c = strarr[x-(k-i):x+i]
        candidates.append("".join(c))
    candidates.sort(key=lambda s: len(s), reverse=True)
    return candidates[0]
