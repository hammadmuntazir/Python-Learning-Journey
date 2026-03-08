def insertion_sort(arr):
    for i in range(1,len(arr)):
        #starting from 1
        key=arr[i]
        j=i-1
        # Move elements of arr[0..i-1], that are greater than key, to one position ahead of their current position
        while j>=0 and key<arr[j]:
            arr[j+1]=arr[j]
            j-=1
        arr[j+1]=key
# Driver code
if __name__ == "__main__":
    arr=[12,11,13,5,6]
    print(f"Original array: {arr}")
    insertion_sort(arr)
    print(f"Sorted array: {arr}")
