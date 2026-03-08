# implementing bubble sort in python
def bubbleSort(arr):
    n = len(arr)

    # Traverse through all elements in the array
    for i in range(n):
        swapped = False

        # Last i elements are already in place
        for j in range(0, n-i-1):
            # traverse the array from 0 to n-i-1
            # Swap if the element found is greater than the next Element
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        
        # Optimization: agar swap nahi hua to array already sorted hai
        if swapped == False:
            break

# Driver code to test above
if __name__ == "__main__":
    arr = [64, 34, 25, 12, 22, 11, 90]
    
    print(f"Original array: {arr}")
    
    bubbleSort(arr)
    
    print(f"Sorted array is: {arr}")
    
