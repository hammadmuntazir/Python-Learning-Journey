def merge_sort(arr):
    if len(arr)>1:
        # divide array in two parts
        mid=len(arr)//2
        left_half=arr[:mid]
        right_half=arr[mid:]
        # recursive call on each half
        merge_sort(left_half)
        merge_sort(right_half)
        #merging the sorted halves
        i=j=k=0 # i for left_half, j for right_half, k for merged array
        #compare left and right half and merge them in sorted order
        while i<len(left_half) and j<len(right_half):
            if left_half[i]<right_half[j]:
                arr[k]=left_half[i]
                i+=1
            else:
                arr[k]=right_half[j]
                j+=1
            k+=1
        #checking if any element is left
        while i<len(left_half):
            arr[k]=left_half[i]
            i+=1
            k+=1
        #checking if any element is right
        while j<len(right_half):
            arr[k]=right_half[j]
            j+=1
            k+=1
# Driver code
if __name__ == "__main__":
    arr = [38, 27, 43, 3, 9, 82, 10]
    print(f"Original array: {arr}")
    merge_sort(arr)
    print(f"Sorted array: {arr}")
