def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        # Check if the target is present at mid
        if arr[mid] == target:
            return mid
        
        # If target is greater, ignore left half
        elif arr[mid] < target:
            left = mid + 1
        
        # If target is smaller, ignore right half
        else:
            right = mid - 1
    
    # Element is not present in array
    return -1

# Example usage:
arr = [2, 3, 5, 7, 11, 13, 17, 19, 23]
target = 13

result = binary_search(arr, target)

if result != -1:
    print(f"Element {target} is present at index {result}")
else:
    print(f"Element {target} is not present in array")

# Checking: Element not found