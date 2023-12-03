def index(keys, values, match):
    """
    """
    return {key_i : [value_i for value_i in values if match(key_i, value_i)] for key_i in keys}


keys = [7, 9, 11]
values = range(30, 50)
a = {x: x * x for x in range(5) }

match = lambda x, y: y % x == 0

t = index(keys, values, match)