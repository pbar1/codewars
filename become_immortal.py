# https://www.codewars.com/kata/become-immortal/train/python

def list_map(fn, l):
    return list(map(fn, l))


def digits(integer):
    import math
    return math.floor(math.log10(integer)) + 1


def print_rectange(cols, rows):
    rectangle_sum = 0
    for i in range(0, rows):
        row_ints = []
        for j in range(0, cols):
            row_ints.append(j ^ i)
        row_sum = sum(row_ints)
        rectangle_sum += row_sum
        row_strs = list_map(str, row_ints)
        row_strs_rjust = list_map(lambda x: x.rjust(digits(cols), ' '),
                                  row_strs)
        print(" ".join(row_strs_rjust))  # + "\t\t" + str(row_sum))
    print("rectangle total: " + str(rectangle_sum))
    print()


# analagous to an additive factorial
def T(n):
    if n <= 0: return 0
    return n * (n + 1) >> 1

# greatest power of 2 less than n
def power2under(n):
    if n == 0: return 0
    return 1 << (n.bit_length() - 1)

# assuming columns always >= rows
def sum_rectangle(cols, rows, loss, gain):
    # return rows * (T(cols - 1) + (gain - loss) * cols)
    row_sum = T(cols - 1 - loss) + cols * gain
    return rows * row_sum

# def calc_excess_line(low, high):


def elder_age_rec(cols, rows, loss, gain):
    if rows > cols:
        cols ^= rows
        rows ^= cols
        cols ^= rows

    print_rectange(cols, rows)

    # BASE CASE: just a 0
    if cols == 1 and rows == 1:
        if gain < gain:
            return 0
        net = gain - loss
        return net

    p2under = power2under(cols)

    # CASE A: perfect columns (.: rows don't matter)
    if cols == p2under:
        rectangle = sum_rectangle(cols, rows, loss, gain)
        return rectangle

    # CASE B: extra columns, not enough rows
    elif rows < p2under:
        excess_cols = cols - p2under
        rec = elder_age_rec(excess_cols, rows, loss, gain + p2under)
        rectangle = sum_rectangle(p2under, rows, loss, gain)
        to_return = rec + rectangle
        return to_return

    elif rows == p2under:
        excess_cols = cols - p2under
        excess_line_sum = T((p2under << 1) - 1 - loss) - T(p2under - 1 - loss) + gain # include LOSS and gain
        excess = excess_cols * excess_line_sum
        rectangle = sum_rectangle(p2under, p2under, loss, gain)
        to_return = excess + rectangle
        return to_return

    # CASE C: extra columns, extra rows
    elif rows > p2under:
        excess_cols = cols - p2under
        excess_rows = rows - p2under
        new_rows = rows if excess_rows == 0 else excess_rows
        excess_line_sum = T((p2under << 1) - 1 - loss) - T(p2under - 1 - loss) + gain
        excess = (excess_cols + excess_rows) * excess_line_sum
        rec = elder_age_rec(excess_cols, new_rows, loss, gain)
        rectangle = sum_rectangle(p2under, p2under, loss, gain)
        to_return = excess + rec + rectangle
        return to_return

# We can't apply loss twice

def elder_age(m, n, l, t):
    print('-' * 100)
    age_total = elder_age_rec(m, n, l, 0)
    age = age_total % t
    print("total age: " + str(age_total))
    print("wrapped age: " + str(age))
    print('-' * 100)


# elder_age(8, 5, 1, 100)  #  5
# elder_age(8, 8, 0, 100007)  #   224
# elder_age(25, 31, 0, 100007)  # 11925
elder_age(5,45,3,1000007) # 4323
# elder_age(36,39,7,2345) #   1586
# elder_age(545,435,342,1000007) #    808451
# elder_age(28827050410, 35165045587, 7109602, 13719506) #    5456283
