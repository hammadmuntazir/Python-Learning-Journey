def binary_search(arr, low, high, target):
    # check base case
    if high >= low:
        mid = low + (high - low) // 2
        
        # if element is present at middle itself
        if arr[mid] == target:
            return mid
        # if element is smaller than mid, then it can only be present in left subarray
        elif arr[mid] > target:
            return binary_search(arr, low, mid - 1, target)
        # else the element can only be present in right subarray
        else:
            return binary_search(arr, mid + 1, high, target)
    else:
        # element is not present in array
        return -1
    
if __name__ == "__main__":
    arr=[1,2,3,4,5,6,7,8,9,10]
    target=5
    result=binary_search(arr, 0, len(arr)-1, target)
    if(result==-1):
        print("Element not found in array")
    else:
        print("Element is present at index",result)
