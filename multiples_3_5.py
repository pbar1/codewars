def multiples(n, limit):
    multiplesarr = []
    i = 1
    while True:
        multiple = n * i
        if multiple >= limit: break
        multiplesarr.append(multiple)
        i += 1
    return multiplesarr

def solution(number):
    threes = set(multiples(3, number))
    fives = set(multiples(5, number))
    threes_or_fives = threes.union(fives)
    return sum(threes_or_fives)
