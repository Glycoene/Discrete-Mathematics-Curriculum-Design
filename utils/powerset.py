def get_powerset(any_set: list):
    length = len(any_set)
    result = list()

    for i in range(2 ** length):
        subset = list()
        for j in range(length):
            if (i >> j) & 1:
                subset.append(any_set[j])
        result.append(subset)
    return result

if __name__ == '__main__':
    print(get_powerset([1, 2, 3]))
