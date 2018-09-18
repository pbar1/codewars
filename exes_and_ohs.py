def xo(s):
    s_lower = s.lower()
    xs = s_lower.count('x')
    os = s_lower.count('o')
    return xs == os
