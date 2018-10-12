def get_indices_of_item_weights(weights, limit):
    result = ()
    d = {}
    i = 0
    for item in weights:
        d[item] = i
        i = i + 1

    if len(weights) is 1:
        return result

    for k,v in d.items():
        if (limit - k) in d.keys():
            result = (d[limit - k], d[k])
            return result


if __name__ == '__main__':
    # You can write code here to test your implementation using the Python repl
    pass
