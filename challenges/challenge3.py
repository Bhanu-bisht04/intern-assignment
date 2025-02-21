target = int(input("Enter the target element: "))
array = sorted(map(int, input("The array: ").split()))
left, right = 0, len(array) - 1

#algorithm used for searching
while left <= right:
    mid = (left + right) // 2
    if array[mid] == target:
        print("Target", target, "found at index", mid)
        break
    elif array[mid] < target:
        left = mid + 1
    else:
        right = mid - 1
else:
    print("Target", target, "not found.")