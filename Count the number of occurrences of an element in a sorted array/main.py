# Count the number of occurrences of an element in a sorted array.

# Brute Force approach (linear search)
def count(arr: [int], n: int, x: int) -> int:
    cnt = 0
    for i in range(n):
        if arr[i] == x:
            cnt += 1
    return cnt


# By Binary search
def firstOccurrence(arr: [int], n: int, x: int) -> int:
    low = 0
    hight = n - 1
    first = -1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == x:
            first = mid
            high = mid - 1  # look for smaller index on the left
        elif arr[mid] < x:
            low = mid + 1 # look on the right
        else:
            high = mid - 1  # look on the lef
    return first


def lastOccurrence(arr: [int], n: int, x: int) -> int:
    low = 0
    high = n - 1
    last = -1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == x:
            last = mid
            low = mid + 1 # look for larger index on the right
        elif arr[mid] < n:
            low = mid + 1 # look on the right
        else:
            high = mid - 1 # look on the left
    return last


def FirstLastOccurrence(arr, n, x):
    first = firstOccurrence(arr, n, x)
    if first == -1:
        return (-1, -1)
    last = lastOccurrence(arr, n, x)
    return (first, last)

def count2(arr: [int], n: int, x: int) -> int:
    first, last = firstOccurrence(arr, n, x)
    if first == -1:
        return 0
    return last - first + 1


if __name__ == "__main__":
    arr = [2, 2, 3, 3, 3, 3, 4, 4]
    n = 8
    x = 3
    # ans = count(arr, n, x)
    # print("The number of occurrences of an element is:", ans)

    ans = count(arr, n, x)
    print("The number of occurrence of an element is:", ans)
