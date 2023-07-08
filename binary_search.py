def binary_search(list, min, max, value):
    mid = (min + max) // 2
    while max - min > 1:
        if value > list[mid]:
            min = mid
            mid = (min + max + 1) // 2
        elif value < list[mid]:
            max = mid
            mid = (min + max) // 2
        else:
            return mid
    return mid
