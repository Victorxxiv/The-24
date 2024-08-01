def linear_search(arr, element):
    for i in range(len(arr)):
        if arr[i] == element:
            return i
    return -1

# Searching for element 3
array = [1, 2, 3, 4, 5]
index = linear_search(array, 3)
print(index)

# Searching for element 24
index = linear_search(array, 24)
print(index)