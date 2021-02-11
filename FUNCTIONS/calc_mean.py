# * allows to get more input than we know we will pass as argument
def calculate_mean(first, *remainder):
    mean = (first + sum(remainder)) / (1 + len(remainder))
    # print(first)
    # print(sum(remainder))
    # print(len(remainder))

    return mean

print(calculate_mean(21, 34, 45, 89, 45, 90))

