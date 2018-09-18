def sum_digits(numstr):
    return sum(list(map(int, list(numstr))))

def order_weight(strng):
    l = strng.split(' ')
    l.sort(key = lambda x: sum_digits(x))
    print(list(map(sum_digits, l)))
    return ' '.join(l)

print(order_weight("2000 10003 1234000 44444444 9999 11 11 22 123"))
