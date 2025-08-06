#  Function to perform Bubble Sort
def bubble_sort(arr):
    n = len(arr)
    # Traverse through all elements in the list
    for i in range(n):
        # Last i elements are already in place, so reduce the range
        for j in range(0, n - i - 1):
            # Swap if the element is greater than the next
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

# Input: Taking numbers from the user
nums = list(map(int, input("Enter numbers separated by space: ").split()))

#  Sorting using Bubble Sort
bubble_sort(nums)

#  Output
print("Sorted array is:", nums)
