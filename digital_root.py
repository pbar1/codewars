def digital_root(n):
    if n < 10: return n
    digits_str = list(str(n))
    digits = list(map(int, digits_str))
    return digital_root(sum(digits))

print(digital_root(16))
