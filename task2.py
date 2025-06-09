def binary_search_with_upper_bound(arr, x):
    low = 0
    high = len(arr) - 1
    iterations = 0
    upper_bound = None

    while low <= high:
        iterations += 1
        mid = (low + high) // 2

        if arr[mid] < x:
            low = mid + 1
        else:
            # Це може бути верхня межа
            upper_bound = arr[mid]
            high = mid - 1

    return (iterations, upper_bound)


arr = [1.1, 2.5, 3.3, 4.4, 5.8, 7.2, 9.9]
x = 6.0
result = binary_search_with_upper_bound(arr, x)
print(f"Iterations: {result[0]}, Upper Bound: {result[1]}")
