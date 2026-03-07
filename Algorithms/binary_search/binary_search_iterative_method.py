# # it can be done by two ways: iterative and recursive
# # iterative way

def binary_search(arr,target):
    left=0
    right=len(arr)-1
    while(left<=right):
        mid=left+(right-left)//2
        if(arr[mid]==target):
            return mid
        elif(arr[mid]<target):
            left=mid+1
        else:
            right=mid-1
    return -1

if __name__ == "__main__":
    arr=[1,2,3,4,5,6,7,8,9,10]
    target=5
    result=binary_search(arr,target)
    if(result==-1):
        print("Element not found in array")
    else:
        print("Element is present at index",result)
    
