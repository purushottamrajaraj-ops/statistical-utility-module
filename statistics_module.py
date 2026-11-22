# Custom Statistical Utility Module

def calculate_mean(data):
    return sum(data) / len(data)


def calculate_median(data):
    sorted_data = sorted(data)
    n = len(sorted_data)

    if n % 2 == 0:
        return (sorted_data[n//2 - 1] +
                sorted_data[n//2]) / 2
    else:
        return sorted_data[n//2]


def calculate_mode(data):
    frequency = {}

    for num in data:
        frequency[num] = frequency.get(num, 0) + 1

    max_frequency = max(frequency.values())

    if max_frequency == 1:
        return "No mode"

    return [num for num, count in frequency.items()
            if count == max_frequency]


def calculate_variance(data):
    mean = calculate_mean(data)

    return sum((x - mean) ** 2 for x in data) / len(data)


def calculate_std(data):
    return calculate_variance(data) ** 0.5


def find_maximum(data):
    return max(data)


def find_minimum(data):
    return min(data)
def calculate_sum(data):
    return sum(data)


def count_values(data):
    return len(data)


def calculate_range(data):
    return max(data) - min(data)


def count_unique(data):
    return len(set(data))


def sort_ascending(data):
    return sorted(data)


def sort_descending(data):
    return sorted(data, reverse=True)
def calculate_quartiles(data):

    sorted_data = sorted(data)

    n = len(sorted_data)

    q2 = calculate_median(sorted_data)

    middle = n // 2

    if n % 2 == 0:

        lower = sorted_data[:middle]
        upper = sorted_data[middle:]

    else:

        lower = sorted_data[:middle]
        upper = sorted_data[middle + 1:]

    q1 = calculate_median(lower) if lower else None

    q3 = calculate_median(upper) if upper else None

    return q1, q2, q3
def calculate_iqr(data):

    q1, q2, q3 = calculate_quartiles(data)

    if q1 is None or q3 is None:
        return None

    return q3 - q1