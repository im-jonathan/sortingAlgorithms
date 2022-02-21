"""Bubble sort implementation."""

def bubble_sort(data: list, reverse: bool = False) -> list:
    """Bubble sorting function.
    Args:
        data (list): list to be ordered.
        reverse (bool, optional): ascending(False) or descending(True) order. Defaults to False.
    Returns:
        list: ordered list.
    """
    n = len(data)
    # 1st loop goes through the list as many times as there are elements
    for i in range(n):
        for j in range(n-i-1):
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[ j + 1], data[j]
    if reverse:
        data = data[::-1]
    return data


a = [43, 46, 8, 7, 6, 18, 9, 33, 41, 4, 39, 20, 19, 10, 25, 1]
print(bubble_sort(a))
