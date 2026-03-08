def quick_sort(arr,low,high):
    if low<high:
        # pi is partitioning index, arr[p] is now at right place
        pi=partition(arr,low,high)
        # Separately sort elements before partition and after partition
        quick_sort(arr,low,pi-1)
        quick_sort(arr,pi+1,high)
def partition(arr,low,high):
    i=(low-1) # index of smaller element
    pivot=arr[high] # pivot
    for j in range(low,high):
        # If current element is smaller than or equal to pivot
        if arr[j]<=pivot:
            i+=1 # increment index of smaller element
            arr[i],arr[j]=arr[j],arr[i]
    arr[i+1],arr[high]=arr[high],arr[i+1]
    return (i+1)
# Driver code to test above
if __name__ == "__main__":
    arr = [10, 7, 8, 9, 1, 5]
    n = len(arr)
    print(f"Original array: {arr}")
    quick_sort(arr,0,n-1)
    print(f"Sorted array: {arr}")
