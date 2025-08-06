def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

# Take input from the user
user_input = input("Enter numbers separated by spaces: ")

# Convert the input string to a list of integers
numbers = list(map(int, user_input.split()))

print("Original list:", numbers)

bubble_sort(numbers)

print("Sorted list:", numbers)
