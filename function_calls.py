x_global = 100


def sum_number(*args):
    total_sum = sum(args)
    return total_sum


def print_dictionary(**kwargs):
    for key, value in kwargs.items():
        print("The value of {}: {}".format(key, value))


def calculate_double(x):
    global x_local
    x_local = x * 2
    return x_local
